---
name: ls_analyzer
description: "Use this skill when the task involves semantic analysis of parsed Markdown documents for change detection, version diffing, deprecation detection, cross-source correlation, or tag classification. Triggers include: @analyzer, mentions of analysis/分析/变更检测/版本比对/跨站关联, references to knowledge/articles/analyzed, requests to identify what changed between document versions, detect deprecated/obsolete rules, find related documents across SSE/SZSE/ChinaClear, or auto-generate tags/keywords. Also use when generating doc_id, classifying changes (interface field / business process / rule clause / technical architecture), or assigning confidence scores. Do NOT use for parsing raw files (use parser skill), for crawling (use collector skill), or for final entry formatting (use organizer skill)."
allowed-tools: [Read, Grep, Glob, WebFetch]
---

# 分析技能 (Analyzer Skill)

## 使用场景

对解析后的 Markdown 文档进行语义分析，执行技术变更/规则变更检测、版本差异比对、废止替代检测、跨站关联发现与标签自动分类，产出结构化分析结果。

## 输入

- `knowledge/articles/{source}/markdown/{category}/{file}.md` — 解析后的 Markdown
- `knowledge/articles/{source}/metadata/{category}/{file}_meta.json` — 元数据
- `knowledge/articles/{source}/analyzed/{category}/` — 历史分析记录（用于版本 diff）

## 执行步骤

### Step 1: 变更检测

**策略（二选一，优先 1）：**

1. **解析 span 标注** — 扫描 Markdown 中的 `<span style="color:...">` 标签，提取变更位置和语义前缀
2. **全文 diff 兜底** — 无 span 标注时，与历史版本 Markdown 逐段比对

**过滤规则：**
- 长度 < 4 字符的文本跳过
- 纯标点/数字的文本跳过
- 页眉/页码/版权声明等页面级工件跳过
- 去重：相同 color + text[:80] 只保留一次

### Step 2: 变更分类

| 类别 | 说明 | 示例 |
|------|------|------|
| `接口字段变更` | 字段名/类型/长度变化 | "字段长度由32改为64" |
| `业务流程变更` | 流程步骤变化 | "取消线下申请环节" |
| `规则条款变更` | 规则新增/修改/废止 | "第X条新增科创板适用" |
| `技术架构变更` | 系统通信方式变化 | "FTP切换为SFTP" |
| `版本升级` | 版本号变更 | "V3.1 → V3.2" |
| `时效变更` | 生效/过渡期变化 | "过渡期延长至6个月" |
| `废止` | 文档或接口被完全废止 | "该接口自2025-06-01废止" |

### Step 3: 严重程度

- `critical`：安全/风险/数据丢失相关
- `major`：新增/删除/废止/替换/迁移
- `minor`：优化/说明/补充/扩容
- `cosmetic`：格式/排版/文案/更正

蓝色 span 的 major 降级为 minor。

### Step 4: 废止/替代检测

扫描文档内容中的关键词："废止"、"替代"、"停止使用"、"不再支持"、"下线"
- 如发现 → status = `deprecated`，记录 `deprecated_date` 和 `superseded_by`

### Step 5: 文档标识生成

格式：`doc_id = {source}-{short_type}-{YYYYMMDD}-{seq:03d}`

short_type 映射：technical_notice→tech, interface_spec→iface, business_rule→rule, guide→guide, software→soft, test_doc→test, magazine→mag

日期优先从元数据 `public_date` 获取，其次从文件名正则提取。

### Step 6: 标签自动分类

- 来源标签：sse / szse / chinaclear
- 类型标签：technical_notice / interface_spec / ...
- 主题标签：IS\d{3} / STEP / BINARY / ETF / 期权 / 债券 / 科创板 等（最多 8 个）
- 变更标签：has_changes / deprecated / superseded

### Step 7: 跨站关联

使用 Grep 在 `knowledge/articles/` 中搜索关键词发现：
- 同主题关联（相同时间发布的同类内容）
- 交叉引用（文档引用其他机构标准）
- 配套文档（同一业务的不同环节）

## 输出

```
knowledge/articles/{source}/analyzed/{category}/{filename}_analysis.json
```

```json
{
  "doc_id": "sse-tech-20250428-001",
  "title": "关于xx接口规范V3.2发布的通知",
  "source": "sse",
  "source_url": "https://...",
  "analysis_date": "2025-04-28T12:00:00+00:00",
  "status": "active",
  "version": "3.2",
  "previous_version": "3.1",
  "changes": [
    {
      "type": "接口字段变更",
      "summary": "字段XXX长度限制由32位调整为64位",
      "detail": "原：长度32 → 新：长度64",
      "severity": "minor",
      "source": "parser_span"
    }
  ],
  "tags": ["sse", "technical_notice", "IS124", "has_changes"],
  "related_ids": ["csdc-rule-20250420-015"],
  "deprecated_date": null,
  "superseded_by": null,
  "summary": "本次涉及1项变更。接口字段变更: 1项。",
  "confidence": 0.95
}
```

## 注意事项

- 变更分类不将排版差异误判为内容变更
- 废止/替代检测基于文档内明确声明，不推测
- related_ids 仅包含证实有关联的条目
- confidence 如实反映：0.95（span 标注）/ 0.85（diff 检测）/ 0.75（初始版本）
- 低置信度（< 0.3）需过滤，0.3-0.7 标记 needs_review

## 质量检查

- [ ] 每个 Markdown 文档生成了对应的 _analysis.json
- [ ] 变更检测优先利用了 span 标注
- [ ] 变更分类准确
- [ ] tags 无冗余/无空字符串
- [ ] summary 不超过 200 字

## 参考脚本

- `utils/analyze_all.py` — 批量分析脚本
