## Context

MCP Knowledge Server 通过 stdio 与 OpenCode 通信，启动时序为：`main()` → `store.load()` → `server.run()`。`store.load()` 读取所有 JSON 条目后用 jieba 分词构建倒排索引，首次加载（无缓存）耗时 >30s，在新机器或缓存失效时同样会出现长加载。OpenCode 的 MCP 客户端默认 30s 超时，导致服务注册失败。

当前 `ArticleStore` 采用同步单线程加载，无就绪通知机制。

## Goals / Non-Goals

**Goals:**
- 服务进程启动后立即响应 MCP `initialize` 请求
- 工具调用（search / get_article 等）在数据加载完成前自动等待，不报错、不返回空结果
- 保持加载逻辑不变，不改动 `ArticleStore.load` 内部实现

**Non-Goals:**
- 不改变缓存策略或索引结构
- 不引入异步 IO 框架
- 不修改 MCP 协议消息处理流程

## Decisions

| 决定 | 选择 | 备选方案 | 理由 |
|------|------|----------|------|
| 加载线程 | `threading.Thread(daemon=True)` | `asyncio` / `concurrent.futures` | stdio 同步模型最简单，无需引入事件循环改造 |
| 就绪等待 | 轮询 `_loaded` 标志 + `time.sleep(0.1)` | `threading.Event` / `Condition` | `_loaded` 已是同步标志位，轮询足够可靠且代码侵入最小 |
| 等待时机 | 工具调用入口统一调用 `wait_ready()` | 每个 handler 自行检查 | 单点控制，避免遗漏；`_handle_tools_call` 是工具调用的唯一入口 |
| 默认超时 | 60s | 30s | 与 OpenCode 超时一致不够安全，60s 给加载留足余量 |

## Risks / Trade-offs

- **加载中调用返回延迟**: 若工具在加载期间被调用，`wait_ready()` 会最多阻塞 60s。正常情况下首次加载在缓存命中时 <5s，全量加载约 30-50s，风险可控。
- **部分加载时被调用**: 若 `load()` 中有异常导致 `_loaded` 从未置 True，`wait_ready()` 会超时返回 False，工具调用继续执行但可能操作不完整的索引。已由 `ArticleStore.load` 的 try/except 兜底（日志 + sys.exit）。
