## Why

MCP Knowledge Server 每次启动时需重新扫描 `knowledge/articles/{sse,szse,chinaclear}/entries/` 下所有 JSON 文件，重新执行 jieba 分词构建倒排索引。当前约 230 条目启动耗时约 0.3s，随着条目增长到 500+，启动耗时将超过 2s，且每次重启都重复相同的计算工作。

此外，MCP stdio 协议早期实现存在以下问题：
- `sys.stdin` / `sys.stdout` 文本模式在 Windows 下可能触发编码转换问题
- 响应未 flush 导致 MCP 客户端偶发超时
- 搜索无结果时返回空结果，缺乏调试信息让开发者判断是搜索词问题还是索引问题
- 因未捕获的启动异常导致进程静默退出，难以排查

## What Changes

- **索引缓存机制**：首次构建倒排索引后序列化为 `.index_cache.pkl`，后续启动时校验文件 mtime 决定是否使用缓存
- **stdio 协议层优化**：`sys.stdin.buffer` 读取 bytes + `sys.stdout.buffer` 写入 bytes，避免 Windows 编码转换异常
- **统一响应写入**：抽取 `_write_response()` 方法，确保每次写入后 flush
- **搜索调试信息**：`search_articles` 调用时输出 jieba 分词结果和每个词的倒排索引命中数，无结果时展示调试信息
- **启动异常防护**：`main()` 包裹 try/except，异常时 `sys.exit(1)` 并输出错误日志
- **信号注册兼容**：SIGINT 在 Windows 上不可用时优雅降级
- **倒排索引统计**：`knowledge_stats` 增加倒排索引词条数

## Capabilities

### New Capabilities
- 索引缓存加速：二次启动速度提升 10–50x（视条目数而定），跳过 jieba 重分词

### Modified Capabilities
- `search_articles`：无结果时返回 jieba 分词调试信息，帮助定位问题
- `knowledge_stats`：新增倒排索引词条数统计字段
- stdio 通信层：从文本模式改为二进制模式，提升 Windows 兼容性
- 启动/关闭：优雅处理 Windows 信号限制 + 启动异常兜底 exit(1)

## Impact

- **修改文件**：`mcp_knowledge_server.py`（已修改，无新增文件）
- **新增依赖**：`pickle`（Python 内置，无需额外安装）
- **缓存文件**：首次启动后生成 `knowledge/articles/.index_cache.pkl`，建议加入 `.gitignore`
- **风险**：极低 — 纯性能优化与健壮性提升，不改变外部行为
