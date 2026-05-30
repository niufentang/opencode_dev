## Context

MCP Knowledge Server (`mcp_knowledge_server.py`) 启动时全量加载知识条目到内存并构建倒排索引。启动过程中最耗时的环节是 jieba 分词（每篇全量 Markdown 内容分词），每次重启均需重复该操作。

当前实现使用 `sys.stdin` / `sys.stdout` 文本模式进行 JSON-RPC 通信。Windows 下 Python 的文本模式会自动处理换行符转换，而 MCP 协议对字节流的完整性要求严格，二进制模式更可靠。

## Goals / Non-Goals

**Goals:**
- 引入 gzip + JSON 缓存倒排索引，启动速度提升 10x+（跳过重分词）
- 缓存自动失效：当 `entries/*.json` 文件 mtime 新于缓存文件时自动重建
- stdio 协议层迁移至二进制模式（`sys.stdin.buffer` / `sys.stdout.buffer`），消除编码转换隐患
- 搜索无结果时展示调试信息（分词结果 + 各词命中数）
- 启动异常时显式 exit(1) 并输出错误日志
- SIGBREAK (Ctrl+Break) 在 Windows 上提供可靠中断

**Non-Goals:**
- 不做内存索引的增量更新（仍需重启）
- 不做缓存文件内容校验（仅靠 mtime 判断）
- 不改变外部 API（MCP 工具签名保持不变）

## Decisions

- **gzip + JSON 序列化**：使用 `gzip.open("wt")` + `json.dump`，Python 内置无额外依赖。序列化整个 `ArticleStore` 状态（`_entries`、`_inverted_index`、`_synonym_map`、`manifest`）。
  - 相比 pickle 的优势：跨 Python 版本兼容、`gunzip` 即得明文可读、CI 中可 diff 索引差异
  - 代价：体积略大约 2x（~1–2MB），gzip 压缩开销约 5–10ms，相对重分词的 10–30s 可忽略
- **缓存位置**：存放在 `knowledge/.cache/`，与只读原始数据 `knowledge/articles/` 隔离。通过 `knowledge/.gitignore` 中 `/.cache/` 规则防止误提交
- **单次遍历 + 合并校验**：`_load_cache` 中仅调用一次 `_build_manifest`，用其结果同时做集合比对（检测删除/重命名）和 mtime 上限校验（检测修改）。去掉了独立的 `_cache_is_fresh` 方法，缓存命中的启动路径仅做一次全量 stat 遍历
- **二进制 stdio**：`sys.stdin.buffer.readline()` 读取原始 bytes 后 decode 为 str，`sys.stdout.buffer.write()` 写入 bytes + flush。日志仍输出到 stderr 不变
- **延迟调试 + 条件输出**：jieba 分词和命中统计仅在搜索无结果且 `LOG_LEVEL=DEBUG` 时执行，不污染正常请求路径。INFO 级别下无结果时仅输出一行 `logger.debug` 日志，结果文本不变

## Deployment

无部署变更 — 现有 `opencode.json` 中的 `mcpServers.knowledge-base` 配置无需修改。

**原子写入策略：** `_save_cache` 先写入 `.tmp` 临时文件，再 `os.replace()` 原子覆盖。写入中断时原缓存文件保留完好，下次启动可复用。读取失败时自动删除残骸缓存文件，下次启动重建。

**版本标记：** 缓存 data 顶层包含 `cache_version` 整数（当前 `CACHE_VERSION = 1`），`_load_cache` 校验版本号匹配，不匹配时主动重建。格式变迁时只需递增 `CACHE_VERSION`，旧缓存自动降级。

**新增文件（自动生成）：**
- `knowledge/.cache/.index_cache.json.gz` — 索引缓存文件（gzip + JSON）
- `knowledge/.gitignore` — 忽略 `.cache/` 目录

## Risks / Trade-offs

- **序列化版本兼容**：gzip + JSON 天然跨版本兼容，不存在 pickle 的 Python 版本间协议不兼容问题。若需要减小体积，将来可考虑 msgpack 替代 JSON
- **mtime 精度**：在 NTFS 上 mtime 精度为 100ns，够用。若将来条目文件从网络文件系统加载，需评估 mtime 一致性
- **缓存膨胀**：当前缓存 ~5MB。条目增长到 5000 时预计 ~50MB，仍在可接受范围
