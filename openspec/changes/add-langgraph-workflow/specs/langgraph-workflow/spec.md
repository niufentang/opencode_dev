## 新增需求

### 需求: 图定义

系统必须提供一个 LangGraph `StateGraph`，将知识库工作流定义为带类型节点和条件路由的有向图。

图结构必须支持以下模式：
- 线性边用于顺序执行（如 `collect → parse`）
- 通过 `Send()` 进行扇出，用于并行子图分发
- 条件边用于审查路由
- 通过 `StateGraph` 嵌套实现子图组合

#### 场景: 图编译成功
- **WHEN** 通过节点定义和边声明构建图
- **THEN** 返回一个编译后的 `CompiledGraph` 实例，无配置错误

#### 场景: 图可以被调用
- **WHEN** 调用 `graph.invoke(initial_state)`
- **THEN** 图按依赖顺序执行所有可达节点，返回最终 `KBState`

---

### 需求: 节点函数

每个图节点必须是签名 `(state: KBState) -> dict[str, Any]` 的函数，只返回它修改的 `KBState` 字段。

节点必须按独立文件组织在 `workflows/nodes/` 下，每节点一个文件：

| 文件 | 节点函数 | 角色 |
|------|---------|------|
| `collect_source.py` | `collect_source(source)` | 子图节点 |
| `parse_source.py` | `parse_source(source)` | 子图节点 |
| `analyze_all.py` | `analyze_all(state)` | 主图节点 |
| `organize_all.py` | `organize_all(state)` | 主图节点 |
| `review_router.py` | `review_router(state)` | 主图节点 |
| `save_all.py` | `save_all(state)` | 主图节点 |
| `human_review.py` | `human_review(state)` | 主图节点 |

所有节点函数必须从 `workflows/nodes/__init__.py` 中 re-export。

#### 场景: 节点函数只返回修改的字段
- **WHEN** 用 `KBState` 实例调用节点函数
- **THEN** 返回的 dict 只包含该节点负责的字段，由 `StateGraph` 通过 reducer 合并

#### 场景: 节点可从包中导入
- **WHEN** 执行 `from workflows.nodes import collect_source`
- **THEN** `collect_source` 是可调用函数，而非模块

---

### 需求: 节点幂等性

每个节点必须是幂等的——在执行工作前检查文件系统的输出是否已存在。节点必须跳过输出已存在的文件，规则如下：

幂等检查附加 JSON 校验：文件存在但内容非法的（`json.JSONDecodeError`）视为不存在，自动删除坏文件并触发重新处理。

写入产出文件时采用原子写入模式：先写 `.tmp` 后缀文件，成功后 `os.replace()` 覆盖目标文件名，确保写入中途崩溃不会残留半截文件。

| 节点 | 跳过条件 |
|------|---------|
| `collect_source(source)` | `knowledge/raw/{source}/metadata.json` 已存在 |
| `parse_source(source)` | `knowledge/articles/{source}/markdown/{fname}.md` 已存在 且 SHA256 未变 |
| `analyze_all(state)` | `knowledge/articles/{source}/analyzed/{fname}_analysis.json` 已存在 |
| `organize_all(state)` | `knowledge/articles/{source}/entries/{doc_id}.json` 已存在 |
| `save_all(state)` | 不适用——仅对通过 review 的源执行一次 |

#### 场景: 节点跳过已处理文件
- **WHEN** 节点遇到输出目标已存在于磁盘的文件
- **THEN** 节点记录日志 "跳过 {filename}" 并处理下一个文件，不重新处理

#### 场景: 节点重新处理已变更文件
- **WHEN** 原始文件的 SHA256 与之前处理的版本不同
- **THEN** 节点重新解析该文件并覆盖现有输出

---

### 需求: 节点自防御

每个节点必须将主体逻辑包裹在 `try/except` 中。捕获异常后：
- 子图节点（`collect_source`、`parse_source`）：设置对应 `source_status[source]["collect_failed"]` 或 `["parse_failed"]` 标志，不阻止其他源
- 主图节点（`analyze_all`、`organize_all` 等）：记录单文件失败，跳过该文件，继续处理剩余文件

节点必须永不向上传播异常。

#### 场景: 采集节点捕获网络错误
- **WHEN** `collect_source` 请求目标网站超时
- **THEN** 节点捕获异常，设置 `source_status["sse"]["collect_failed"] = True`，返回部分结果而非崩溃

#### 场景: 分析节点跳过失败文件
- **WHEN** `analyze_all` 处理到某文件时 LLM 调用异常
- **THEN** 节点捕获异常，跳过该文件，继续处理下一个文件

---

### 需求: LLM 工具函数

系统必须在 `workflows/llm_utils.py` 中提供两个工具函数，封装 LLM 调用：

1. **`chat_json(prompt, system, **kwargs) -> (dict|list, usage_dict)`**：调用 `pipeline.model_client.chat_with_retry()`，自带 3 层 JSON 容错——去 markdown 代码块包裹、直接 `json.loads`、正则提取最外层 JSON 结构
2. **`accumulate_usage(tracker, new_usage) -> dict`**：累加 prompt/completion token 数，按 DeepSeek 定价估算费用，返回更新后的 cost_tracker

所有需要 LLM 调用的节点（`analyze_all`）必须通过 `chat_json` 而非直接调用 `model_client`。

#### 场景: chat_json 正确解析 LLM 返回的 JSON
- **WHEN** LLM 返回带 markdown 代码块包裹的 JSON（如 "```json\n{...}\n```"）
- **THEN** `chat_json` 剥离包裹，成功解析为 Python dict

#### 场景: accumulate_usage 累加 token 费用
- **WHEN** 连续两次调用 `chat_json`，每次返回不同的 usage
- **THEN** `accumulate_usage` 将两次的 prompt_tokens 和 completion_tokens 分别累加，并重新计算总费用

---

### 需求: 成本追踪

每个调用 LLM 的节点，必须在每次 LLM 调用后将 token 用量和费用数据追加到 `state.cost_tracker`，使用 `llm_utils.accumulate_usage`。

#### 场景: LLM 调用费用被追踪
- **WHEN** `analyze_all` 调用 `chat_json`
- **THEN** `state.cost_tracker` 中更新该调用的 token 数、费用（USD/CNY）和模型名称
