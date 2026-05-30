## 1. Background Data Loading

- [x] 1.1 Add `import threading` to `mcp_knowledge_server.py`
- [x] 1.2 Move `store.load(KNOWLEDGE_DIR)` call from `main()` into a `daemon=True` background thread, starting before `server.run()`

## 2. Readiness Guard

- [x] 2.1 Add `wait_ready(timeout=60)` method to `ArticleStore` that polls `_loaded` flag
- [x] 2.2 Call `self._store.wait_ready()` at the beginning of `MCPServer._handle_tools_call` before dispatching to any tool handler
