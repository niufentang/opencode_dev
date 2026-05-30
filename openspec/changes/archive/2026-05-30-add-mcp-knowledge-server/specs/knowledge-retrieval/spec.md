## ADDED Requirements

### Requirement: get_article tool

The system SHALL provide a `get_article` MCP tool that retrieves article metadata by article ID.

- **Tool name**: `get_article`
- **Description**: 按文章 ID 获取文章元数据（不含全文），返回字符数信息
- **Input parameters**:
  - `article_id: string` (required) — 文章 ID，如 sse-tech-20250428-001
- **Lookup**: O(1) from in-memory dict by article ID
- **Return**: article metadata (all JSON fields except content_markdown), with total character count annotation
- **Not found**: return "未找到文章: {article_id}"

#### Scenario: Get existing article metadata
- **WHEN** user calls `get_article` with valid article_id
- **THEN** system returns metadata with title, source, type, tags, version, and total char count (no full text)

#### Scenario: Get non-existent article
- **WHEN** user calls `get_article` with article_id="nonexistent-id"
- **THEN** system returns "未找到文章: nonexistent-id"

### Requirement: get_article_content tool

The system SHALL provide a `get_article_content` MCP tool that retrieves article full text in paginated chunks.

- **Tool name**: `get_article_content`
- **Description**: 分页获取文章全文 Markdown 内容（配合 get_article 使用）
- **Input parameters**:
  - `article_id: string` (required) — 文章 ID
  - `offset: number` (optional, default 0) — 字符偏移量
  - `limit: number` (optional, default 3000, max 10000) — 返回字符数
- **Lookup**: O(1) from in-memory content dict by article ID
- **Return**: content_markdown slice `[offset:offset+limit]`, append "[全文共 N 字符，已返回第 offset-offset+len 字符]"
- **Not found**: return "未找到文章: {article_id}"
- **Edge cases**: offset < 0 auto-set to 0; limit exceeding remaining length auto-truncated

#### Scenario: Get first page of article content
- **WHEN** user calls `get_article_content` with article_id and default offset=0, limit=3000
- **THEN** system returns first 3000 characters with char count annotation

#### Scenario: Get next page of article content
- **WHEN** user calls `get_article_content` with article_id, offset=3000, limit=3000
- **THEN** system returns characters 3000-5999 with char count annotation

#### Scenario: Get content with offset exceeding length
- **WHEN** user calls `get_article_content` with offset beyond total character count
- **THEN** system returns empty text with full char count annotation
