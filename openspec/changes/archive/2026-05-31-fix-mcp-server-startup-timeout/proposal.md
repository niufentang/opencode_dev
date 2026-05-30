## Why

MCP Knowledge Server 在 `main()` 中同步调用 `store.load()` 加载全部 2129 个知识条目（~41MB），包含 jieba 全文分词和倒排索引构建，首次加载耗时远超 30 秒。OpenCode MCP 客户端在 30s 内收不到 `initialize` 响应即判定超时，导致 `knowledge-base` 服务始终处于 `failed` 状态。

## What Changes

- 将 `store.load()` 从同步阻塞改为后台线程（`daemon=True`）执行，`server.run()` 立即启动监听 stdin
- 新增 `ArticleStore.wait_ready()` 方法，数据未就绪时工具调用主动等待（默认最长 60s）
- 在 `_handle_tools_call` 入口处调用 `wait_ready()`，确保搜索/读取等操作在数据加载完成后执行

## Capabilities

### New Capabilities
- `mcp-server-startup`: MCP 知识库服务启动流程，包含异步数据加载、就绪等待机制

### Modified Capabilities
- *(无修改，本次仅涉及实现层面的启动流程调整，不改变已有能力的行为契约)*

## Impact

- **Affected code**: `mcp_knowledge_server.py` — `main()` 函数、`ArticleStore` 类、`MCPServer._handle_tools_call`
- **Dependencies**: 新增 `threading` 标准库模块
- **启动行为**: 服务会在数据加载完成前即响应 `initialize`，工具调用会透明等待数据就绪
