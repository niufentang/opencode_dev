---
name: ls_organizer
description: "Use this skill when the task involves finalizing knowledge entries from analyzed data: deduplication, filtering, formatting into standard knowledge entry JSON, maintaining version traceability, and creating index files. Triggers include: @organizer, mentions of organizing/整理/条目生成/去重/格式化, references to knowledge/articles/entries, requests to produce final consumable knowledge entries, create version chains (previous_version / superseded_by), or generate entries.json index. Also use when cleaning up redundant entries, filtering low-confidence results, or validating JSON output quality. Do NOT use for crawling (use collector skill), parsing (use parser skill), or analysis (use analyzer skill)."
allowed-tools: [Read, Grep, Glob, Write, Edit]
---

# 整理技能 (Organizer Skill)

## 使用场景

对分析后的原始数据进行去重、过滤、格式化，输出为标准知识条目 JSON，是流水线的最后一环，产出供下游检索和分发的最终数据。

## 输入

- `knowledge/articles/{source}/analyzed/{category}/{file}_analysis.json` — 分析结果
- `knowledge/articles/{source}/markdown/{category}/{file}.md` — 全文 Markdown（嵌入 content_markdown）
- `knowledge/articles/{source}/entries/entries.json` — 已有索引（用于去重）

## 执行步骤

### Step 1: 数据过滤

**丢弃规则：**
- title 为空或仅有占位符的条目
- 解析失败（parse_status = failed）且无有效内容的条目
- 分析置信度 < 0.3 的条目（标记需人工复核）
- 内容重复度 > 95% 的近似条目（保留一份）

**保留规则：**
- status = deprecated 的条目保留（用于版本追溯）
- 置信度 0.3-0.7 的条目标记为 `needs_review` 并入

### Step 2: 去重

以 `doc_id` 作为唯一键。读取已有 `entries.json` 与新条目比对：
- 完全重复（content_markdown 哈希一致）→ 跳过
- 内容有更新的重复 → 旧条目标记为 superseded，新增当前条目
- 标识重复但内容相同 → 跳过

### Step 3: 格式化

组装为标准知识条目 JSON（字段映射）：

| 目标字段 | 来源 |
|----------|------|
| id | analysis.doc_id |
| type | analysis.doc_id 推断（tech/iface/guide/...） |
| title | analysis.title（清理 YYYYMMDD_ 前缀） |
| source | analysis.source |
| source_url | analysis.source_url |
| summary | analysis.summary |
| tags | analysis.tags |
| status | analysis.status |
| version | analysis.version |
| previous_version | analysis.previous_version |
| public_date | analysis.doc_id 中的日期部分（YYYY-MM-DD） |
| file_format | 原始文件扩展名 |
| file_hash | meta.file_hash |
| content_markdown | 从对应 .md 文件读取全文 |

```json
{
  "id": "sse-tech-20250428-001",
  "type": "technical_notice",
  "title": "关于xx接口规范V3.2发布的通知",
  "source": "sse",
  "source_url": "https://www.sse.com.cn/...",
  "summary": "本次更新主要调整了xx字段的长度限制。",
  "tags": ["sse", "technical_notice", "接口规范", "V3.2", "has_changes"],
  "status": "active",
  "version": "3.2",
  "previous_version": "3.1",
  "public_date": "2025-04-28",
  "crawl_date": null,
  "effective_date": null,
  "deprecated_date": null,
  "superseded_by": null,
  "related_ids": [],
  "file_format": "pdf",
  "file_hash": "sha256:abc123...",
  "content_markdown": "# ...全文Markdown..."
}
```

### Step 4: 版本追溯

对同一接口规范的不同版本建立版本链：

1. 按接口编号分组（如 IS105, IS124, IS122）
2. 按版本号排序
3. 连续版本配对：
   - 新条目：`previous_version` = 旧版本号
   - 旧条目：`superseded_by` = 新条目的 id
   - 旧条目：`status` = `superseded`

**示例版本链：** IS124 V2.42 → V2.43 → V2.44 → V2.45 → V2.46 → V2.47 → V2.50 → V2.60 → V2.70 → V3.10 → V3.20 → V3.30

### Step 5: 索引维护

每个数据源维护 `entries.json`：

```json
{
  "source": "sse",
  "last_updated": "2025-04-28T13:00:00+00:00",
  "total_entries": 171,
  "entries": [
    {
      "id": "sse-tech-20250428-001",
      "title": "文档标题",
      "type": "technical_notice",
      "status": "active",
      "public_date": "2025-04-28",
      "tags": ["接口规范", "V3.2"]
    }
  ]
}
```

## 输出

```
knowledge/articles/{source}/entries/
├── entries.json                   ← 索引文件
├── {doc_id}.json                  ← 单条知识条目（含 content_markdown）
└── ...
```

## 注意事项

- 所有 JSON 文件使用 `ensure_ascii=False, indent=2` 格式
- content_markdown 必须非空且为合法 Markdown
- file_hash 为合法 SHA256 值
- entries.json 中的 total_entries 必须与实际条目数一致
- 版本链需要双向追溯（previous_version + superseded_by）

## 质量检查

- [ ] 每个条目有合法 id（`{source}-{type}-{date}-{seq}`）
- [ ] title / source / source_url / public_date 非空
- [ ] 无重复条目入库
- [ ] 废弃条目标记了 deprecated_date
- [ ] tags 无重复、无空字符串
- [ ] content_markdown 非空
- [ ] JSON 可通过 JSON.parse() 校验
- [ ] 不编造任何数据

## 参考脚本

- `utils/organize_all.py` — 批量整理脚本
