# pipeline/pipeline.py — 知识库自动化流水线设计方案

## 一、概述

五步知识库自动化流水线编排器。**不修改任何已有文件**，仅新增 `pipeline/pipeline.py` 一个文件。

```
Collect → Parse → Analyze (规则+LLM混合) → Organize → Save (质量门禁)
```

## 二、架构关系

```
pipeline/pipeline.py                ← 编排器（新增）
pipeline/model_client.py            ← LLM 统一客户端（已有，零改动）

# 下游调用（只导入函数，不修改原文件）:
utils/*_doc_api.py                  ← Step 1 爬虫
utils/parse_all.py                  ← Step 2
utils/analyze_all.py                ← Step 3（规则分析）
utils/organize_all.py               ← Step 4
hooks/validate_json.py              ┐
hooks/check_quality.py              ┴ Step 5 质量门禁
```

## 三、数据类设计

```python
@dataclass
class PipelineConfig:
    sources: list[str]              # ["sse", "szse", "chinaclear"]
    steps: list[Step]               # 执行的步骤序列（由 --from/--to/--step 推算）
    limit: int | None               # 每步处理上限
    incremental: bool                # 增量模式
    use_llm: bool                    # Analyze 启用 LLM 增强
    llm_provider: str                # deepseek / qwen / kimi
    llm_threshold: float             # 置信度阈值，低于此值触发 LLM
    fail_fast: bool                  # 遇错即停
    skip_quality: bool               # 跳过质量门禁
    dry_run: bool                    # 试运行

@dataclass
class StepResult:
    step: Step
    status: str                      # success / partial / skipped / failed
    total: int
    success: int
    failed: int
    duration: float
    error: str | None

@dataclass
class PipelineReport:
    status: str                      # success / partial / failed
    total_duration: float
    per_step: dict[str, StepResult]
```

## 四、五步详细设计

### Step 1: Collect — 采集

| 项目 | 内容 |
|------|------|
| 入口 | `SSECrawler` / `SZSECrawler` / `CSDCCrawler`（from `utils/`） |
| 调用方式 | `crawler.crawl_all(dry_run=self.config.dry_run)` |
| 增量判断 | `crawl_metadata.json` 已存在且 `mtime` 未变 → 跳过 |
| 产出 | `knowledge/raw/{source}/{category}/*` + `crawl_metadata.json` 更新 |
| 错误处理 | 某源不可达 → 标记该源为 `skipped`，继续其他源 |

### Step 2: Parse — 解析

| 项目 | 内容 |
|------|------|
| 入口 | `collect_raw_files()` / `parse_file()` / `save_output()`（from `parse_all.py`） |
| 扫描 | `collect_raw_files(source, limit)` → `[(source, category, sub_category, Path)]` |
| 匹配元数据 | `match_crawl_meta(path, crawl_items)` → 回填发布日期、URL |
| 增量判断 | `pipeline_state.json` 中该文件 `sha256` 未变且 `parse` 步骤已完成 → 跳过 |
| 产出 | `articles/{source}/markdown/{category}/*.md` + `metadata/{category}/*_meta.json` |

### Step 3: Analyze — 分析（混合模式）

**核心创新：规则 + LLM 双通道**

#### 3.1 规则通道（必走）

100% 文件先走规则通道 `analyze_all.analyze_document()`：

- 精确检出 `<span style="color:...">` 格式标注的变更
- 正则提取版本号、发布日期、文档类型
- 确定性、零幻觉、~0.3s/篇

#### 3.2 LLM 通道（条件触发）

规则通道完成后，根据结果质量和配置决定是否触发 LLM：

```
                      ┌──────────────────┐
                      │  规则通道分析完成   │
                      └────────┬─────────┘
                               │
                               ▼
          ┌──── changes 数量 > 200? ────┐
          │  (疑似颜色标注误报)           │
          │  yes                  no     │
          ▼                              ▼
    ┌───────────┐               ┌──────────────────┐
    │ 否掉规则   │               │ confidence ≥ 阈值 │
    │ changes,   │               │ 且 changes ≤ 50?  │
    │ 交给 LLM   │               └────────┬─────────┘
    │ 全量重做   │                  yes           no
    └───────────┘                    ▼             ▼
                              ┌──────────┐   ┌──────────┐
                              │ 跳过 LLM │   │ 触发 LLM │
                              │ 规则结果  │   │ 语义增强  │
                              │ 直接输出  │   └────┬─────┘
                              └──────────┘         │
                                                   ▼
                                            ┌──────────┐
                                            │  合并器   │
                                            │ 规则+LLM  │
                                            └──────────┘
```

触发决策树解读：

| 条件 | 动作 | 原因 |
|------|------|------|
| `changes > 200` | 否掉规则 changes，LLM 全量重做 | 颜色标注误报过高，规则结果不可信 |
| `confidence ≥ 阈值` 且 `changes ≤ 50` | 跳过 LLM，直接输出 | 规则结果已可信，无需 LLM 开销 |
| 以上皆否 | 触发 LLM 语义增强 | 规则结果质量不够，需要 LLM 补盲 |

#### 3.3 合并器算法（Merge Strategy）

双通道不是覆盖关系，是叠加关系。各字段归属：

| 字段 | 规则通道（所有权） | LLM 通道（补充权） | 合并策略 |
|------|-------------------|-------------------|----------|
| `doc_id` / `version` / `file_hash` | ✅ 规则负责 | ❌ 不参与 | 以规则为准 |
| `changes[].color` | ✅ `<span>` 颜色检测 | ❌ LLM 不看颜色 | 保留规则字段 |
| `changes[].type` | ⚠️ 关键词推断，常误判 | ✅ 语义判断 | LLM 的 `type` 覆盖规则的 |
| `changes[].summary` | ⚠️ 原始截取 | ✅ 精简摘要 | LLM 的 `summary` 替换规则的 |
| `changes[].severity` | ✅ 关键词命中 | ✅ 语义判断 | 取最高严重度 |
| 变更遗漏（无 `<span>`） | ❌ 0 检出 | ✅ 语义分析发现 | LLM 发现的直接追加 |
| `summary`（文档级） | ❌ 模板填空 | ✅ 语义摘要 | 完全由 LLM 提供 |
| `tags` | ✅ 正则匹配 | ✅ 语义标签 | Union，去重 |
| `related_ids` | ❌ 始终为空 | ✅ 跨文档关联 | 完全由 LLM 提供 |
| `confidence` | 二值化（0.75/0.95） | 连续值 0-1 | `max(规则版, LLM版)` |

```python
def merge_analysis(rule_result: dict, llm_result: dict) -> dict:
    merged = rule_result.copy()

    # --- changes: Union + type 覆盖 + 去重 ---
    rule_changes = rule_result.get("changes", [])
    llm_changes = llm_result.get("changes", [])

    type_overrides = {c["summary"][:40]: c for c in llm_changes}
    merged_changes = []
    seen = set()

    for c in rule_changes:
        key = c["summary"][:40]
        if key in type_overrides:
            llm_c = type_overrides[key]
            c["type"] = llm_c["type"]
            c["summary"] = llm_c["summary"]
            c["severity"] = max_severity(c["severity"], llm_c["severity"])
        merged_changes.append(c)
        seen.add(key)

    for c in llm_changes:
        if c["summary"][:40] not in seen:
            merged_changes.append(c)
            seen.add(c["summary"][:40])

    merged["changes"] = merged_changes

    # --- summary: LLM 语义摘要替换模板 ---
    llm_summary = llm_result.get("summary", "")
    if llm_summary and len(llm_summary) > 5:
        merged["summary"] = llm_summary

    # --- tags: Union ---
    merged["tags"] = list(set(
        rule_result.get("tags", []) + llm_result.get("tags", [])
    ))

    # --- related_ids: 完全由 LLM 提供 ---
    if llm_result.get("related_ids"):
        merged["related_ids"] = llm_result["related_ids"]

    # --- confidence: 取最大值 ---
    merged["confidence"] = round(max(
        rule_result.get("confidence", 0.75),
        llm_result.get("confidence", 0.75)
    ), 2)

    return merged
```

#### 3.4 接入 pipeline.py 的位置

```python
class PipelineRunner:
    def _execute_analyze(self) -> StepResult:
        md_files = collect_markdown_files(...)
        llm_provider = None
        if self.config.use_llm:
            llm_provider = OpenAICompatibleProvider(
                provider_name=self.config.llm_provider
            )

        for i, md_file in enumerate(md_files, 1):
            if self._incremental_skip(md_file, "analyze"):
                continue

            rule_result = analyze_document(md_file, i)  # 规则通道

            if self._should_use_llm(rule_result, llm_provider):
                llm_result = self._llm_analyze(
                    llm_provider, md_file, rule_result
                )
                final = merge_analysis(rule_result, llm_result)
            else:
                final = rule_result

            save_analysis(md_file, final)
            self._update_state(md_file, "analyze")
```

| 项目 | 内容 |
|------|------|
| 规则入口 | `collect_markdown_files()` / `analyze_document()` / `save_analysis()` |
| LLM 入口 | `OpenAICompatibleProvider` + `chat_with_retry()` |
| 输出 | `articles/{source}/analyzed/{category}/*_analysis.json` |

### Step 4: Organize — 整理

| 项目 | 内容 |
|------|------|
| 入口 | `scan_analysis_files()` / `process_analysis_file()` / `build_index()` |
| 过滤 | 空标题、置信度 < 0.3 的条目自动跳过 |
| 产出 | `articles/{source}/entries/{doc_id}.json` + `entries.json` 索引 |

### Step 5: Save — 质量门禁 + 最终化

| 项目 | 内容 |
|------|------|
| 质量校验 | 调用 `hooks/validate_json.py` 的 `validate_entry()` → 记录不合格 |
| 质量评分 | 调用 `hooks/check_quality.py` 的 `score_entry()` → 可选附加分数 |
| 版本追溯 | 调用 `organize_all.perform_version_traceability(source)` |
| 索引重建 | 重新生成 `entries.json` |
| 报告输出 | 汇总统计 → `log/pipeline_report.json` + stdout 表格 |
| 通知占位 | `_trigger_notifications()` 留空函数，待后续实现 |

## 五、增量模式

状态文件：`knowledge/.pipeline_state.json`

```json
{
  "version": 1,
  "last_run": "2026-05-11T10:00:00+00:00",
  "files": {
    "knowledge/raw/sse/技术通知/xxx.pdf": {
      "sha256": "abc123...",
      "mtime": "2026-05-11T09:00:00",
      "steps": {
        "parse":   {"done": true, "timestamp": "2026-05-11T10:01:00"},
        "analyze": {"done": true, "timestamp": "2026-05-11T10:02:00"}
      }
    }
  }
}
```

判断规则（逐文件逐步骤）：

| 条件 | 动作 |
|------|------|
| 文件不在 state 中 | 新增文件 → 从 Parse 全量处理 |
| `sha256` 或 `mtime` 变化 | 已变更 → 从 Parse 重新处理 |
| 状态未变但某步骤未 `done` | 断点续跑 → 从该步骤继续 |
| 状态未变且步骤已 `done` | 跳过该文件该步骤 |

`--reset` 选项：删除整个 state 文件，强制全量。

## 六、CLI 接口

```bash
python pipeline/pipeline.py [选项]

# 运行控制
--sources LIST         SSE,SZSE,CHINACLEAR 逗号分隔
--from STEP            起始步骤
--to STEP              终止步骤
--step STEP            只跑单步
--limit N              每步文件上限

# 增量
--incremental          增量模式（按 hash 跳过）
--reset                重置增量状态

# LLM
--use-llm              Analyze 启用 LLM 增强通道
--llm-provider NAME    模型名（deepseek/qwen/kimi）
--llm-threshold F      置信度阈值（默认 0.7）

# 质量与错误
--skip-quality         跳过质量门禁
--fail-fast            遇错即停
--dry-run              试运行

# 日志
--verbose              详细日志
```

## 七、LLM Prompt 设计

核心原则：**规则通道已检出的结构化信息注入 LLM 上下文，让 LLM 专注补盲而非重复劳动。**

```python
ANALYZE_SYSTEM_PROMPT = """你是一个证券行业技术文档变更分析专家。
请分析以下文档内容，识别其中的技术变更或规则变更。

输出严格的 JSON 格式（不要包含 markdown 代码块标记）：
{
  "changes": [
    {
      "type": "新增|修改|删除|废止",
      "summary": "20字以内的变更摘要",
      "detail": "50字以内的详细描述",
      "severity": "major|minor|cosmetic"
    }
  ],
  "tags": ["标签1", "标签2"],
  "summary": "30字以内的文档摘要",
  "confidence": 0.95,
  "related_ids": []
}

注意事项：
- type 只能取 "新增"、"修改"、"删除"、"废止" 之一
- severity: major=影响现有系统/流程, minor=新增功能/补充说明, cosmetic=格式/勘误
- 无变更时 changes 返回空数组 []
- tags 包括：数据源(sse/szse/chinaclear)、文档类型、涉及系统(如IS105)、技术主题
- confidence 范围 0.0-1.0
- related_ids：如果本文档明确引用或替代了其他已知文档，填入其 ID，否则留空
"""

ANALYZE_USER_PROMPT = """文档信息：
- 标题: {title}
- 文档类型: {doc_type}
- 版本: {version}
- 规则通道已检出 {rule_change_count} 条格式标注变更（来自红色/蓝色文本标注）

请分析以下文档全文，重点关注：
1. 规则通道可能遗漏的变更（无颜色标注的正文变更描述）
2. 对规则通道已检出的变更做 type 纠偏
3. 提取语义标签（不限于预定义关键词库）

文档内容：
{markdown_content}
"""
```

## 八、错误处理策略

| 场景 | 默认（skip-and-continue） | --fail-fast |
|------|--------------------------|-------------|
| 单文件解析失败 | 记录错误，继续下一个 | 立即停止 |
| 单步整体失败 | 标记 failed，继续后续 | 立即停止 |
| LLM 调用超时/失败 | 降级到纯规则结果 | 立即停止 |
| 目标源无数据 | Warning + 跳过该源 | 同左 |
| 质量门禁不合格 | Warning，继续 | 同左 |

## 九、执行报告输出

```
╔══════════════════════════════════════════════════╗
║         知识库自动化流水线 — 执行报告              ║
╠══════════════════════════════════════════════════╣
║ 状态: 部分成功                                   ║
║ 总耗时: 187.3s                                   ║
╠══════════════════════════════════════════════════╣
║ Step 1: Collect    ✅  3/3 源            45.2s   ║
║ Step 2: Parse      ✅  171/171           62.1s   ║
║ Step 3: Analyze    ⚠️  169/171           58.4s   ║
║   ├─ 规则通道: 159/159  ✅                        ║
║   ├─ LLM 增强:  12   触发 (置信度<0.7)           ║
║   └─ 合并后:  新增 23 条变更, 78 篇摘要已语义化   ║
║ Step 4: Organize   ✅  169/169           12.3s    ║
║ Step 5: Save       ✅  通过率 98.2%      9.3s     ║
║   ├─ 校验通过: 166                               ║
║   ├─ needs_review: 3                             ║
║   └─ 版本追溯: 8 条链路已建立                     ║
╚══════════════════════════════════════════════════╝
```

## 十、不包含在此次实现中的内容

| 项目 | 说明 |
|------|------|
| 通知分发 | 邮件/飞书推送 — 只留 `_trigger_notifications()` 占位函数 |
| LangGraph 工作流 | 后续迭代 |
| OpenClaw 部署 | 后续迭代 |
| 修改已有文件 | 所有 `utils/*.py`、`hooks/*.py`、`pipeline/model_client.py` **零改动** |

## 十一、风险评估与缓解措施

| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|---------|
| LLM 幻觉出不存在变更 | 中 | 高 | 仅追加不删除，规则变更永远保留；LLM 变更置信度 < 0.6 的不采纳 |
| LLM 结果不一致 | 高 | 中 | 规则结果作为锚定不变；LLM 仅做增强，不改变 `doc_id`/`version`/`hash` 等确定性字段 |
| LLM 调用超时/失败 | 低 | 低 | 捕获异常后降级到纯规则结果，不影响流水线 |
| LLM 遗漏规则已有的变更 | 中 | 低 | 合并器做 Union，规则变更永远保留 |
| Token 超限（文档过大） | 低 | 低 | 截断到 8000 tokens，prompt 中说明"已截断，请基于已有内容分析" |

## 十二、文件规模预估

| 模块 | 行数 |
|------|------|
| 数据类 + 枚举 | 50 |
| CLI 参数解析 | 60 |
| PipelineRunner 类 + `run()` 主流程 | 80 |
| `_execute_collect` | 30 |
| `_execute_parse` | 30 |
| `_execute_analyze`（含 LLM 混合 + 合并器） | 100 |
| `_execute_organize` | 30 |
| `_execute_save`（质量门禁 + 报告） | 60 |
| 增量状态管理 | 40 |
| `main()` + 报告输出 | 40 |
| **合计** | **~520 行** |
