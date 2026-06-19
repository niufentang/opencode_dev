## 新增需求

### 需求: 先审查后保存的放置顺序

`review_router` 节点必须在 `organize_all` 之后、`save_all` 之前执行。这确保只有审查通过的内容才会进入质量门禁和版本追溯阶段。

#### 场景: 审查通过，执行保存
- **WHEN** `review_router` 为所有源设置 `review_passed = True`
- **THEN** 图路由到 `save_all`

#### 场景: 审查失败，跳过保存
- **WHEN** `review_router` 为任一源设置 `review_passed = False`
- **THEN** 图路由回失败源的子图，直到所有源通过后才执行 `save_all`

---

### 需求: 按源审查路由

`review_router` 必须独立评估每个源，在 `state.source_status[source]` 中跟踪每个源的审查状态：

| 字段 | 类型 | 描述 |
|------|------|------|
| `articles_passed` | `bool` | 该源整理后的条目是否通过审查 |
| `analyze_attempts` | `int` | analyze 已重试次数（由 review_router 递增） |
| `organize_attempts` | `int` | organize 已重试次数（由 review_router 递增） |
| `force_reanalyze` | `bool` | 信号：通知 analyze_all 强制重跑该源（用完即清） |
| `force_reorganize` | `bool` | 信号：通知 organize_all 强制重跑该源（用完即清） |

路由决策按源独立：

| 条件 | 动作 |
|------|------|
| 所有源 `articles_passed = True` | 路由到 `save_all` |
| 某源 `articles_passed = False`、分析质量问题 | 设 `force_reanalyze = True`，路由到 `analyze_all` |
| 某源 `articles_passed = False`、整理质量问题 | 设 `force_reorganize = True`，路由到 `organize_all` |
| 某源 `attempts >= 3` | 路由到 `human_review`，不再退回重跑 |

#### 场景: 单个源审查失败
- **WHEN** SSE 条目通过审查但 SZSE 条目失败
- **THEN** 图仅重新分发 SZSE 子图，SSE 结果保留在 state 中

#### 场景: 所有源通过
- **WHEN** 所有源都有 `articles_passed = True`
- **THEN** 图路由到 `save_all`

#### 场景: 源耗尽重试次数
- **WHEN** 源的 `analyze_attempts >= 3` 或 `organize_attempts >= 3`
- **THEN** 图路由到 `human_review`，而非重新分发

---

### 需求: 审查质检维度（v1）

`review_router` v1 必须执行轻量级质量检查：

1. **空标题/空 id 过滤** —— 拒绝 `title` 或 `id` 缺失或为空的条目
2. **最小条目数检查** —— 每个源必须至少生成一条有效条目；整理后产出 0 条条目的源标记为失败

失败的条目必须在 `review_feedback` 中记录源名称和原因。

#### 场景: 空标题条目被标记
- **WHEN** 条目的 `title` 为 `""`
- **THEN** review 在 `review_feedback` 中记录失败，并为该源设置 `articles_passed = False`

#### 场景: 零条目的源标记失败
- **WHEN** 整理后某源产出 0 条条目
- **THEN** review 为该源设置 `articles_passed = False`，反馈信息为"未产出条目"

---

### 需求: 人工审核策略

人工审核行为必须通过 `WorkflowConfig.human_review_mode` 配置：

| 模式 | 行为 |
|------|------|
| `"log"`（默认） | 设置 `needs_human_review = True`，将待审数据写入 `knowledge/pending_review/pending-{timestamp}.json`，记录审查反馈和源状态后结束图执行 |
| `"interrupt"` | 通过 `Command` 中断暂停图执行，等待 `graph.invoke(None, config)` 恢复 |

#### 场景: 日志模式将待审数据写入磁盘
- **WHEN** `human_review_mode = "log"` 且审查次数耗尽
- **THEN** 图将待审 analyses 和反馈写入 `knowledge/pending_review/pending-{timestamp}.json`，设置 `needs_human_review = True` 后进入 `END`

#### 场景: 中断模式等待人工输入
- **WHEN** `human_review_mode = "interrupt"` 且审查次数耗尽
- **THEN** 图在 `human_review` 节点暂停执行，等待外部恢复调用
