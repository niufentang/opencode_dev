## 新增需求

### 需求: 并行源分发

系统必须支持使用 LangGraph 的 `Send()` API 在多个数据源（SSE、SZSE、ChinaClear）之间并行执行 `collect → parse` 流水线。

主图在入口点之后扇出，为每个配置的源创建一个子图调用。

#### 场景: 三个源并行分发
- **WHEN** 图以 `state.sources = ["sse", "szse", "chinaclear"]` 调用
- **THEN** 三个子图实例并发执行，各自独立处理一个源

#### 场景: 单个源分发
- **WHEN** 图以 `state.sources = ["sse"]` 调用
- **THEN** 只为 SSE 分发一个子图实例

---

### 需求: 子图组合

每个数据源必须定义为独立的 LangGraph `StateGraph` 子图，包含两个串行节点：`collect_source` → `parse_source`。

子图必须使用作用域限定的 state 键模式——只写入 `state.sources[source]` 和 `state.source_status[source]`，以避免多个子图结果合并时的 reducer 冲突。

#### 场景: 子图顺序执行 collect 然后 parse
- **WHEN** 调用源子图
- **THEN** `collect_source` 先执行，然后是 `parse_source`，collect 的输出对 parse 可用

#### 场景: 子图结果键隔离
- **WHEN** "sse" 和 "szse" 的两个子图完成并合并结果
- **THEN** `state.sources["sse"]` 和 `state.sources["szse"]` 独立存储，无字段冲突

---

### 需求: 源子图工厂

系统必须提供 `build_source_subgraph(source: str) -> StateGraph` 函数，为给定源名称构建子图。

#### 场景: 子图工厂返回配置好的图
- **WHEN** 调用 `build_source_subgraph("szse")`
- **THEN** 返回一个包含绑定到 "szse" 键的 `collect_source` 和 `parse_source` 节点的 `StateGraph`

---

### 需求: 通过 Checkpointer 增量爬取

系统必须在 `KBState` 中存储 `last_crawl_dates[source]`，由 LangGraph 的 `MemorySaver` 或 `SqliteSaver` checkpointer 持久化。

`collect_source` 运行时：
- 若 `last_crawl_dates.get(source)` 为 `None` → 执行全量爬取
- 若存在日期字符串 → 将其作为 `since_date` 传给爬虫 API，进行按日期过滤的分页

默认行为是增量的，无需 `--incremental` 标志。`SqliteSaver` checkpointer 文件在提供 `--checkpoint-path` 时存放于 `knowledge/.checkpoints/langgraph.db`。不使用 `--checkpoint-path` 时默认使用内存级 `MemorySaver`。

#### 场景: 首次运行执行全量爬取
- **WHEN** 图首次运行，无 checkpoint
- **THEN** `last_crawl_dates` 为空，`collect_source` 跨所有页面获取全部可用条目

#### 场景: 第二次运行执行增量爬取
- **WHEN** 图第二次运行，有持久化 checkpoint
- **THEN** `last_crawl_dates[source]` 从 checkpoint 恢复，`collect_source` 将日期作为 `since_date` 传入，当条目全部更旧时停止翻页

#### 场景: Checkpoint 丢失导致全量爬取（安全）
- **WHEN** checkpoint 存储被删除或不可用
- **THEN** `collect_source` 执行全量爬取；但已下载文件通过文件存在性检查跳过，下游节点通过幂等性检查跳过已处理文件
