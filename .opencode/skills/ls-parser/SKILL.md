---
name: ls-parser
description: "Use this skill when the task involves converting raw downloaded documents (PDF, Word, Excel, HTML, ZIP) into structured Markdown and metadata. Triggers include: @parser, mentions of parsing/解析/格式转换, references to knowledge/articles/markdown or knowledge/articles/metadata, requests to extract text or tables from PDFs/Word/Excel files, or converting HTML to clean Markdown. Also use when extracting document metadata (title, version, date, doc_type), detecting change annotations (red/blue text), or generating SHA256 file hashes. Do NOT use for crawling/downloading files (use collector skill), for semantic analysis of content (use analyzer skill), or for final entry formatting (use organizer skill)."
allowed-tools: [Read, Grep, Glob, WebFetch]
---

# 解析技能 (Parser Skill)

## 使用场景

将采集到的原始异构文件（PDF/Word/ZIP/HTML）解析为结构化 Markdown 文本和元数据，标注技术变更与规则变更，为下游分析提供标准化输入。

## 输入

- `knowledge/raw/{source}/{category}/{files}` — 待解析的原始文件
- `knowledge/raw/crawl_metadata.json` — 采集元数据（用于继承 source_url 等）

## 执行步骤

### Step 1: 格式识别

根据文件扩展名选择解析策略：

| 格式 | 解析策略 | 依赖库 |
|------|----------|--------|
| PDF | 提取文本 + 表格，扫描件需 OCR | PyMuPDF (fitz) |
| DOC/DOCX | 提取正文 + 样式，保留标题层级 | python-docx |
| XLS/XLSX | 提取表格内容，转为 Markdown 表格 | openpyxl |
| ZIP | 标记为压缩包，暂不递归解压（返回占位内容） | zipfile |
| HTML/SHTML | 清理标签，提取正文（BeautifulSoup） | beautifulsoup4 + lxml |

### Step 2: 元数据抽取

从文档内容和文件名中提取：

- **标题** — 文档首部/元信息
- **发布日期** — 文档标注日期或文件名正则提取
- **生效日期** — 规则中明确标注的生效时间
- **版本号** — 文件名或标题中提取（`V3.2` / `Ver1.40` 等）
- **文档类型** — 自动推断：`technical_notice` / `interface_spec` / `business_rule` / `guide` / `software` / `test_doc` / `magazine`
- **源文件哈希** — SHA256
- **原文 URL** — 从 `crawl_metadata.json` 继承

### Step 3: 全文转 Markdown

- 保留原文标题层级（H1 → H2 → H3）
- 表格转为 Markdown 表格格式
- 列表、代码块、引文保持原结构
- 图片占位保留 `![描述](路径)`
- 在 Markdown 末尾附上 `<metadata>` 代码块

### Step 4: 变更标注（颜色检测）

**决策树：**

1. 原文有颜色标注（红/蓝）→ 保留颜色，转 `<span style="color:xxx">`
2. 原文无颜色 + 存在历史版本 → 执行版本 diff 兜底
3. 原文无颜色 + 首次采集 → 标注"初始版本，无历史变更"

**语义前缀：**
- `<span style="color:red">[新增] ...</span>`
- `<span style="color:red">[修改] 旧 → 新</span>`
- `<span style="color:red">[删除] ...</span>`
- `<span style="color:red">[废止] 自YYYY-MM-DD起废止</span>`

**颜色映射：** 上交所/深交所 PDF 中红色=变更、蓝色=重要说明。

## 输出

```
knowledge/articles/
├── {source}/
│   ├── markdown/{category}/{safe_name}.md              ← 全文 Markdown（含 metadata 块），文件名取自原始文件 stem 去日期前缀后截取 60 字符
│   └── metadata/{category}/{safe_name}_meta.json       ← 元数据 JSON
```

### _meta.json 格式

```json
{
  "title": "文档标题",
  "source_url": "https://...",
  "raw_path": "knowledge/raw/sse/.../file.pdf",
  "markdown_path": "knowledge/articles/sse/markdown/.../file.md",
  "file_hash": "sha256:abc123...",
  "file_format": "pdf",
  "page_count": 12,
  "doc_type": "technical_notice",
  "version": "3.2",
  "public_date": "2025-04-28",
  "has_changes": true,
  "parse_status": "success",
  "parse_date": "2025-04-28T11:00:00+00:00"
}
```

## 注意事项

- 所有编码保持 UTF-8，禁止出现乱码
- 不编造任何原文中不存在的内容
- 表格必须转为 Markdown 表格格式，不丢失数据
- HTML 解析需清除导航/广告等无关内容
- 扫描件 PDF 需 OCR，标注 parse_status = "ocr_required"

## 质量检查

- [ ] 每个原始文件生成了对应的 `.md` 和 `_meta.json`
- [ ] Markdown 保留了原文标题层级和表格结构
- [ ] 变更标注按三段决策处理
- [ ] source_hash 与原始文件 SHA256 一致
- [ ] parse_status 为 success / failed

## 参考脚本

- `utils/parse_all.py` — 批量解析脚本

依赖库：`PyMuPDF`, `python-docx`, `openpyxl`, `beautifulsoup4`, `lxml`
