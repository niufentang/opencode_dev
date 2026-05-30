## Why

当前知识库的检索能力局限在项目内部：AI Agent 只能通过预配置的 Skill + Bash（grep）方式查询知识条目，搜索能力仅支持子串匹配，不支持中文分词、同义词扩展、分页拉取全文等功能。其他 MCP 客户端（Cursor、Copilot 等）完全无法访问本知识库。

构建一个 MCP Knowledge Server，通过标准 MCP 协议（JSON-RPC 2.0 over stdio）将本地知识库暴露给任何兼容 MCP 的 AI 工具，同时引入 jieba 分词 + 倒排索引提升中文搜索精度。

## What Changes

- 新增 `mcp_knowledge_server.py` — MCP Server 主文件，实现 MCP 协议（initialize / tools/list / tools/call / ping）
- 实现 4 个 MCP 工具：`search_articles`、`get_article`、`get_article_content`、`knowledge_stats`
- 引入 jieba 分词 + 倒排索引 + 同义词表，替代现有 grep 子串匹配
- 新增 `requirements-mcp.txt` — 声明 jieba 依赖
- 新增 `tests/test_mcp_server.py` — 单元测试 + 集成测试
- 支持资源浏览（MCP resources/list + resources/read），以 `knowledge://{source}/entries/{doc_id}` URI 格式暴露条目
- 数据加载策略：启动时全量加载到内存（当前 ~230 条目 / ~5MB），后续 Tier 1/2/3 可平滑升级
- 支持 graceful shutdown（SIGTERM/SIGINT）
- 可观测性：标准 logging 输出到 stderr，LOG_LEVEL 控制日志级别，请求追踪

## Capabilities

### New Capabilities
- `knowledge-search`: 按关键词搜索知识库文章，支持 jieba 分词 + 倒排索引 + 同义词扩展，可限定数据源和返回条数
- `knowledge-retrieval`: 按文章 ID 获取元数据或分页拉取全文 Markdown 内容
- `knowledge-stats`: 获取知识库统计信息（总数、来源分布、类型分布、热门标签、最近更新）
- `knowledge-resources`: 通过 MCP Resource URI 浏览知识条目（knowledge://{source}/entries/{doc_id}）

### Modified Capabilities
- 无（新增能力，不修改已有功能）

## Impact

- **新增文件**：`mcp_knowledge_server.py`（~400 行）、`tests/test_mcp_server.py`、`requirements-mcp.txt`
- **新增依赖**：`jieba`（纯 Python，~15MB）
- **目录变更**：`knowledge/articles/` 为只读数据源，MCP Server 不做任何写入
- **配置变更**：无（无需修改现有 pipeline、workflows、opencode.json）
- **部署变更**：需在 opencode.json 或 MCP 客户端配置中注册该 MCP Server
- **风险**：低 — 纯新增模块，不修改现有系统
