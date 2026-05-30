## 1. 项目初始化

- [x] 1.1 创建 `mcp_knowledge_server.py`，搭建模块结构
- [x] 1.2 创建 `requirements-mcp.txt`，声明 jieba 依赖
- [x] 1.3 创建 `tests/test_mcp_server.py` 测试文件
- [x] 1.4 创建 `tests/fixtures/entries/` 放入 5–10 个控制好的样本 JSON 条目，供集成测试使用

## 2. 数据层实现

- [x] 2.1 实现启动时数据加载器：扫描 `knowledge/articles/{sse,szse,chinaclear}/entries/` 加载所有 *.json
- [x] 2.2 实现基于 jieba 分词的倒排索引构建器
- [x] 2.3 实现同义词扩展映射：启动时从已有条目 tags 和摘要中自动挖掘中英文映射（如"交易型开放式指数基金（ETF）"） + 硬编码 ~20 组高频术语 + 支持 SYNONYM_FILE 外部覆盖
- [x] 2.4 实现内存文章存储 (dict[doc_id, entry])，可访问 content_markdown

## 3. MCP 协议处理器

- [x] 3.1 实现 stdio 传输层（从 stdin readline，写入 stdout，日志到 stderr）
- [x] 3.2 实现 JSON-RPC 2.0 消息解析与分发器
- [x] 3.3 实现 `initialize` 方法，声明 server capabilities
- [x] 3.4 实现 `ping` 方法用于健康检查
- [x] 3.5 实现优雅关闭（SIGTERM/SIGINT 处理器）

## 4. MCP 工具实现

- [x] 4.1 实现 `tools/list`，返回 4 个工具定义
- [x] 4.2 实现 `search_articles` 工具（jieba 分词 → 倒排索引查找 → 同义词扩展 → 字段加权排序(title=5, summary=3, tags=2, content=1) → 格式化结果）
- [x] 4.3 实现 `get_article` 工具（O(1) 元数据查找，排除 content_markdown）
- [x] 4.4 实现 `get_article_content` 工具（分页返回 content_markdown，支持 offset/limit）
- [x] 4.5 实现 `knowledge_stats` 工具（按 source/type/status 聚合统计，Top 10 标签，最近 5 条更新）
- [x] 4.6 实现 `resources/list` 方法，支持分页
- [x] 4.7 实现 `resources/read` 方法，通过 URI 返回条目

## 5. 可观测性

- [x] 5.1 添加结构化日志输出到 stderr，支持 LOG_LEVEL 配置
- [x] 5.2 添加启动校验与统计日志：加载条目数、来源分布、内存估算；若加载 0 条输出 WARNING 及排查提示；解析失败逐文件输出 ERROR 并跳过
- [x] 5.3 添加请求追踪，每条消息带 request_id
- [x] 5.4 添加所有 JSON-RPC 错误码处理（-32700 解析错误, -32601 方法未找到, -32602 无效参数, -32603 内部错误），工具业务错误不触发 JSON-RPC error

## 6. 测试

- [x] 6.1 编写数据加载器单元测试（模拟文件系统）
- [x] 6.2 编写基于 jieba 的倒排索引构建器单元测试
- [x] 6.3 编写同义词扩展单元测试
- [x] 6.4 编写 initialize + tools/list 集成测试
- [x] 6.5 编写 search_articles 集成测试（使用真实条目）
- [x] 6.6 编写 get_article + get_article_content 分页集成测试
- [x] 6.7 编写 knowledge_stats 集成测试
- [x] 6.8 编写 resources/list + resources/read 集成测试
- [x] 6.9 编写异常场景集成测试（无效 JSON、未知工具、未找到）
- [x] 6.10 编写优雅关闭集成测试（SIGTERM）
