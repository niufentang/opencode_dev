## ADDED Requirements

### Requirement: resources/list

The system SHALL implement the MCP `resources/list` method to expose knowledge entries as browsable resources.

- **Method**: `resources/list`
- **Resource URI scheme**: `knowledge://{source}/entries/{doc_id}`
- **Examples**: `knowledge://sse/entries/sse-tech-20250428-001`, `knowledge://szse/entries/szse-iface-20250512-103`
- **Pagination**: support optional cursor-based pagination via `params.cursor`
- **Cursor format**: last returned entry's doc_id (e.g., `sse-tech-20250428-001`); empty/null = start from first entry
- **Page size**: 50 entries per page (fixed)
- **Return**: list of resource URIs with metadata (name, description, mimeType = "text/markdown"), plus `nextCursor` if more pages exist

#### Scenario: List all resources
- **WHEN** client sends `resources/list` request
- **THEN** system returns list of all available knowledge entry URIs with pagination cursor

#### Scenario: List resources with pagination
- **WHEN** client sends `resources/list` with cursor parameter
- **THEN** system returns next page of resource URIs

### Requirement: resources/read

The system SHALL implement the MCP `resources/read` method to retrieve the full content of a knowledge entry by its resource URI.

- **Method**: `resources/read`
- **Input**: `params.uri` — the resource URI (e.g., `knowledge://sse/entries/sse-tech-20250428-001`)
- **Return**: full entry content including all fields and content_markdown
- **Not found**: return formatted text "未找到资源: {uri}" in result（遵循 tools/call 业务错误约定，不走 JSON-RPC error）

#### Scenario: Read existing resource
- **WHEN** client sends `resources/read` with valid `knowledge://{source}/entries/{doc_id}` URI
- **THEN** system returns the full entry content with mimeType "text/markdown"

#### Scenario: Read non-existent resource
- **WHEN** client sends `resources/read` with invalid URI
- **THEN** system returns MCP error indicating resource not found
