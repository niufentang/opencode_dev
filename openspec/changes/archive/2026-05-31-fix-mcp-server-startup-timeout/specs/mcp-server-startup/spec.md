## ADDED Requirements

### Requirement: MCP server SHALL respond to initialize immediately on startup

The MCP knowledge server SHALL start listening on stdin for JSON-RPC messages before data loading completes, so that the OpenCode MCP client receives an `initialize` response within the 30-second timeout window.

#### Scenario: Server responds to initialize before data loading completes
- **WHEN** the server process starts
- **THEN** the server SHALL immediately begin reading stdin for MCP messages
- **AND** the server SHALL respond to an `initialize` request even if data loading has not yet finished

### Requirement: Tool calls SHALL wait for data loading to complete

When a tool call (search, get_article, get_article_content, knowledge_stats) is received before `ArticleStore` finishes loading, the server SHALL wait for loading to complete before processing the request.

#### Scenario: Tool call arrives during data loading
- **WHEN** a tool call request is received
- **AND** data loading is still in progress
- **THEN** the handler SHALL wait (up to 60 seconds) for loading to finish
- **THEN** the handler SHALL process the request normally
#### Scenario: Tool call arrives after data loading completed
- **WHEN** a tool call request is received
- **AND** data loading has already finished
- **THEN** the handler SHALL process the request immediately without waiting

### Requirement: wait_ready SHALL return boolean indicating load status

The `ArticleStore.wait_ready(timeout)` method SHALL block until `_loaded` is True or timeout expires, returning True if loading completed or False on timeout.

#### Scenario: Loading completes before timeout
- **WHEN** `wait_ready(60)` is called
- **AND** loading completes within 60 seconds
- **THEN** the method SHALL return True
#### Scenario: Timeout expires before loading completes
- **WHEN** `wait_ready(5)` is called
- **AND** loading does not complete within 5 seconds
- **THEN** the method SHALL return False
