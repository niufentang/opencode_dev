## ADDED Requirements

> **错误处理约定**：所有 MCP tools/call 的业务错误（未找到、参数不合法等）统一以格式化文本形式返回在 result 中，不走 JSON-RPC error 响应。JSON-RPC error 仅用于协议层错误（无效 JSON = -32700，未知 method = -32601，无效参数结构 = -32602，内部异常 = -32603）。

### Requirement: search_articles tool

The system SHALL provide a `search_articles` MCP tool that searches the knowledge base by keyword with jieba word segmentation and inverted index.

- **Tool name**: `search_articles`
- **Description**: 按关键词搜索知识库文章（基于 jieba 分词 + 倒排索引，支持中英文混合搜索）
- **Input parameters**:
  - `keyword: string` (required) — 搜索关键词
  - `limit: number` (optional, default 5, max 50) — 最大返回条数
  - `source: string` (optional, values: "sse" / "szse" / "chinaclear") — 限定数据源，不传则搜索全部
- **Search scope**: title + summary + tags + content_markdown, based on inverted index
- **Matching logic**: jieba tokenize keyword → look up in inverted index → score by field-weighted hits (title=5, summary=3, tags=2, content=1) → sort descending by score
- **Return**: formatted text with sequence number, ID, title, source, type, tags, summary (truncated to 120 chars)
- **Empty result**: return "未找到匹配文章"
- **Error handling**: empty keyword returns "keyword 不能为空"; keyword < 2 chars only searches title + summary
- **Synonym expansion**: keyword hits SYNONYM_MAP auto-expands search terms before query
- **Synonym source**: auto-discovered from entries' tags + 中文名（English）patterns in summary at startup; ~20 hardcoded high-frequency mappings; supports overrides via `SYNONYM_FILE` env var

#### Scenario: Basic keyword search
- **WHEN** user calls `search_articles` with keyword "ETF", limit=3
- **THEN** system returns up to 3 matching articles with formatted metadata

#### Scenario: Search filtered by source
- **WHEN** user calls `search_articles` with keyword="接口", source="sse"
- **THEN** system only returns results from SSE (上交所) articles

#### Scenario: Search with synonym expansion
- **WHEN** user calls `search_articles` with keyword="交易型开放式指数基金"
- **THEN** system also matches articles containing "ETF" via synonym map

#### Scenario: Empty search returns no-match message
- **WHEN** user calls `search_articles` with keyword="zzz_not_exist_12345"
- **THEN** system returns "未找到匹配文章"

#### Scenario: Empty keyword validation
- **WHEN** user calls `search_articles` with keyword=""
- **THEN** system returns "keyword 不能为空"

#### Scenario: Short keyword limited search
- **WHEN** user calls `search_articles` with keyword="a" (single character)
- **THEN** system only searches title + summary fields, not full inverted index
