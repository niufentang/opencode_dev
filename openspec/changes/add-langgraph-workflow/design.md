## Context

当前知识库流水线实现在 `pipeline/pipeline.py`（1070 行），采用命令式 `PipelineRunner` 类编排 Collect→Parse→Analyze→Organize→Save 五步。增量状态通过 `knowledge/.pipeline_state.json` 文件维护。

`workflows/state.py` 已定义 `KBState` TypedDict（123 行），预置了 review 循环相关字段，但无图结构和节点函数。`requirements.txt` 已有 `langgraph>=1.2.0` 依赖但未使用。

约束条件：
- 不能破坏现有 `pipeline/pipeline.py` 的功能，两者并存过渡
- 节点逻辑复用 `utils/*.py` 的已有函数，不重复实现
- 产出文件路径和 JSON 格式与现有 pipeline 完全一致

## Goals / Non-Goals

**Goals:**
- 基于 LangGraph StateGraph 构建声明式工作流，替代命令式编排
- 三个数据源（SSE/SZSE/ChinaClear）的 Collect→Parse 阶段并行执行
- Analyze/Organize 阶段统一处理，支持跨站关联
- 审查循环（review）在 organize 之后、save 之前，逐源质检，按源退回
- 人工审核策略可配置（log / interrupt）
- 增量状态迁移至 LangGraph Checkpointer
- 与现有 `pipeline/pipeline.py` 共享同一个 `knowledge/` 目录和 `utils/*.py` 工具函数

**Non-Goals:**
- 不修改 `utils/*.py`、`hooks/*.py`、`pipeline/model_client.py` 等已有文件
- 不重写爬虫逻辑、解析逻辑、分析逻辑、整理逻辑
- 不实现飞书/邮件通知分发（继续占位）
- 不替换 OpenClaw 部署配置

## Decisions

### D1: 图结构——主图 + 子图并行

```
                     START
                       │ Send()
           ┌───────┼───────┐
           ▼       ▼       ▼
    [SSE子图] [SZSE子图] [CC子图]      ← collect→parse，并行执行
           │       │       │
           └───┬───┴───┬───┘
               ▼       ▼
          ┌──────────────────┐
     ┌───▶│   analyze_all    │            ← 统一节点
     │    ├──────────────────┤
     │    │   organize_all   │            ← 统一节点
     │    ├──────────────────┤
     │    │  review_router   │            ← 逐源质检
     │    ├──────────────────┤
     │    │    save_all      │            ← 仅通过审查后执行
     │    └──────────────────┘
     │               │
     │               ▼
     │          ┌────────┐
     │          │  END   │
     │          └────────┘
     │
     └── 退回 analyze_all 或 organize_all
         (不经过 fan_out_sources)
```

每个数据源是一个独立的 LangGraph StateGraph（子图），包含 `collect_source` → `parse_source` 两个节点。主图用 `Send()` 将所有活跃源分派到各自子图执行。Analyze 之后的所有阶段在主图中统一完成。

退回路径直达 `analyze_all` 或 `organize_all`，不经过 `fan_out_sources`。通过 `source_status[source]["force_reanalyze"]` 或 `source_status[source]["force_reorganize"]` 信号控制目标节点只重跑指定源。

**备选方案**:

| 方案 | 优点 | 缺点 |
|------|------|------|
| A: 全串行（当前 pipeline 风格） | 最简单，无并发复杂度 | 浪费 3 倍等待时间 |
| B: 全周期子图并行（每个源独立跑完整个流程） | 最大并行度 | Analyze 无法跨站关联，无法统一 review |
| **C: 混合（选定）** | Collect+Parse 并行节省阻塞时间；Analyze+Review 统一保证全局质量 | 需要 fan-in/fan-out 机制 |

### D2: 审查位置——Review 在 organize 之后、save 之前

```
organize_all → review_router → (pass → save_all | fail → 退回)
```

**理由**: save_node 包含质量门禁和版本追溯，对残次条目执行这些操作是浪费。review 的语义审查决策不需要质量门禁的机械校验结果。退回路径不包含 save，每次迭代节省一轮 I/O 和计算。

### D3: 按源退回

`state.source_status` 记录每个源的处理结果，review 时逐源独立检查：

```python
source_status: dict[str, SourceStatus] = {
    "sse": {
        "analyze_attempts": 0,
        "organize_attempts": 0,
        "articles_passed": True,
    },
    "szse": {
        "analyze_attempts": 1,
        "organize_attempts": 0,
        "articles_passed": False,
    },
}
```

review_router 判断某源不合格时，不在 `fan_out_sources` 处退回，而是直接路由到 `analyze_all` 或 `organize_all`。

路由前，review_router 设置信号字段：

```python
source_status["szse"]["force_reanalyze"] = True   # 退回 analyze_all
# 或
source_status["szse"]["force_reorganize"] = True  # 退回 organize_all
```

目标节点读取信号：

```python
def analyze_all(state):
    for source in state["sources"]:
        if state["source_status"][source].get("force_reanalyze"):
            # 即使 _analysis.json 已存在也强制重跑
            # 跑完后清除信号
            state["source_status"][source]["force_reanalyze"] = False
        else:
            # 常规幂等跳过
            if _analysis.json 已存在:
                continue
    ...
```

同理 `force_reorganize` 给 `organize_all`。

此机制与幂等性一致：**不额外新增 state 字段，复用 `source_status`，用完即清**。

### D4: 报告式通信

KBState 不承载文档原始内容或完整 Markdown，只存储结构化摘要和文件路径索引。数据流动：

```
文件系统: knowledge/raw/         ← raw 文件
         knowledge/articles/     ← markdown / metadata / analyzed / entries

KBState : sources[doc_id]       ← 采集摘要（标题/URL/路径）
          analyses[doc_id]      ← 分析摘要（变更类型/置信度/标签）
          articles[doc_id]      ← 条目摘要（ID/状态/版本）
```

节点从 KBState 获知哪些文件需要处理，通过文件系统读写具体内容。

### D5: 增量状态迁移

从 `knowledge/.pipeline_state.json` 迁移到 LangGraph 内置的 `MemorySaver` / `SqliteSaver` checkpointer。

| 项目 | 旧 (.pipeline_state.json) | 新 (LangGraph Checkpointer) |
|------|--------------------------|----------------------------|
| 存储 | 手动 JSON 文件 | 自动 checkpoint |
| 粒度 | 文件级 + 步骤级 | 每次 state 更新 |
| crash 恢复 | `--incremental` 参数 | checkpointer 原生支持 |
| 重置 | `--reset` | 删除 checkpoint store |

过渡期两者共存——LangGraph 模式用 checkpointer，传统模式继续用 `.pipeline_state.json`。

`--incremental` 不直接映射为 checkpointer 的某个参数，而是被拆解为两层：

**1. Crash 恢复** → Checkpointer 原生。恢复 checkpoint 后自动从崩溃节点继续。

**2. 跳过已完成文件** → 节点内自行判断文件系统产出是否存在，不再依赖 `.pipeline_state.json` 的步骤标记：

| 节点 | 判断条件 |
|------|---------|
| `collect_source(source)` | `raw/{source}/metadata.json` 已存在 且 `last_crawl_dates[source]` 有值 → 只传 since_date 增量抓取 |
| `parse_source(source)` | `articles/{source}/markdown/{fname}.md` 已存在 且 SHA256 未变 → 跳过该文件 |
| `analyze_all(state)` | `articles/{source}/analyzed/{fname}_analysis.json` 已存在 → 跳过该文件 |
| `organize_all(state)` | `articles/{source}/entries/{doc_id}.json` 已存在 → 跳过该文件 |
| `save_all(state)` | 不需要跳过，只对通过 review 的源执行一次 |

这样每个节点天然幂等——不管之前是否执行过，检查产出、有则跳过、无则执行。不再需要显式的 `mark_step_done()` 调用。

**Checkpointer 后端**：默认 `MemorySaver`（零配置，进程级），配置 `--checkpoint-path <path>` 时自动切换为 `SqliteSaver(path)`。

**Checkpointer 存储位置**：

```
knowledge/
├── .checkpoints/
│   └── langgraph.db     ← 解析度:每次 state 更新
│                         ← 重置:删除此目录即可
├── .pipeline_state.json ← (传统模式继续使用)
├── raw/
└── articles/
```

`.checkpoints/` 以点号开头，被 `.gitignore` 覆盖，不进入版本控制。

**since_date 采集增量**：`state.last_crawl_dates[source]` 字段存储，由 checkpointer 持久化。

```
第1次运行 (无 checkpoint):
  last_crawl_dates = {}
  collect_source("sse"): since_date=None → 全量抓取 → state.last_crawl_dates["sse"]="2025-06-20"
  子图写入 state → checkpointer 保存
  注: 并行子图下每个子图结束时手动调用 graph.put(state) 独立保存

第2次运行 (checkpoint 恢复):
  last_crawl_dates = {"sse": "2025-06-20"}
  collect_source("sse"): since_date="2025-06-20" → 增量抓取 → 更新 last_crawl_dates
```

**并行子图的 checkpointer 问题**：Send() 分派后，子图对 state 的修改只有在返回主图后才被 checkpointer 统一保存。如果某个子图崩溃，其他子图的 last_crawl_dates 更新会丢失。

解决策略（v1 简单 + 预留优化接口）：

| 方案 | v1 | 说明 |
|------|----|------|
| **A（推荐 v1）** | ✅ | 丢失一天 since_date 无害——下次全量抓取比增量多抓几条，爬虫下游去重。**零额外复杂度** |
| **B（预留）** | 接口 | 子图内显式引用 checkpointer 实例，每个子图结束后独立保存 state。v1 预留 checkpointer 传递接口 |

**collect_node 的幂等性**：即使全量抓取，`parse_source` 会通过文件已存在 + SHA256 比对跳过已解析文件。全量不等于重跑全部，实际增量效果由下游节点保障。

### D6: Human Review 策略

`WorkflowConfig.human_review_mode: Literal["log", "interrupt"]`：

- **log**: 设置 `needs_human_review=True`，将待审数据写入 `knowledge/pending_review/pending-{timestamp}.json`（独立于主库），工作流正常结束。适合自动化定时任务。
- **interrupt**: 通过 `Command` 暂停图执行，等待 `graph.invoke(None, config)` 恢复。适合交互式调试。

### D8: 节点异常处理——自防御

所有节点必须将主体逻辑包裹在 `try/except` 中，捕获异常后返回 fallback 值而非向上传播。每个节点独立防御，永不崩溃：

```
collect_source 抛异常 → source_status[source]["collect_failed"] = True
parse_source    抛异常 → source_status[source]["parse_failed"]   = True
analyze_all 中某文件失败 → 记录失败，跳过该文件，继续处理其他文件
```

异常源不阻止其他源的正常执行。`analyze_all` 读 `source_status` 时跳过标记为 `failed` 的源。

此行为与现有 pipeline 的默认策略（skip-and-continue）一致。优雅降级使用的次数计入 `source_status` 但不消耗 `analyze_attempts` / `organize_attempts`——因为问题出在爬取或解析环节，而非分析或整理的质量问题。

### D7: 每个节点独立文件

`workflows/nodes/` 包，每个节点一个文件，节点函数在 `__init__.py` 中 re-export：

```
nodes/
├── __init__.py
├── collect_source.py     # 采集一个数据源
├── parse_source.py       # 解析一个数据源
├── analyze_all.py        # 统一分析（规则+LLM+跨站关联）
├── organize_all.py       # 统一整理（去重+格式化+索引）
├── review_router.py      # 逐源质检 + 退回决策
├── save_all.py           # 质量门禁 + 版本追溯 + 通知
└── human_review.py       # 人工审核入口
```

| 方案 | 优点 | 缺点 |
|------|------|------|
| 合并在 nodes.py | 文件少，跨节点共享 | 单文件 ~500 行，不利于独立测试 |
| **独立文件（选定）** | 职责单一，每个文件 30-80 行，易于测试和修改 | 文件数量略多 |

### D9: 写入原子性与读取校验

产出文件写入采用两层防御，确保幂等跳过的正确性：

**第一层：写入原子性（预防）**

```
写入任何产出文件时:
  1. json.dumps() 到内存
  2. 写 knowledge/.../xxx.tmp
  3. os.replace("xxx.tmp", "xxx.json")  ← NTFS 上原子操作
```

若写入中途崩溃 → `.json` 未被替换 → 节点看不到 `.json` → 重新处理。

适用范围：`metadata.json`、`_analysis.json`、`entries/*.json`。

**第二层：读取时校验（兜底）**

幂等跳过时附加 `try: json.loads()` 校验：

```python
def _output_exists(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        json.loads(path.read_text(encoding="utf-8"))
        return True
    except (json.JSONDecodeError, OSError):
        path.unlink(missing_ok=True)
        return False
```

| 场景 | 第一层 | 第二层 |
|------|--------|--------|
| 写入中崩溃 | ✅ 阻止了坏文件的产生 | — |
| 磁盘写坏（位翻转、空间满） | — | ✅ 检测并修复 |
| 手动编辑导致 JSON 语法错误 | — | ✅ 检测并修复 |
| 旧版本写入格式不兼容 | — | ✅ 检测并修复 |

### D10: 参考——LLM 调用工具函数

参考 demo 的 `chat_json` 模式，在 `workflows/` 下新增 LLM 工具模块（不修改已有的 `pipeline/model_client.py`）：

```
workflows/
├── llm_utils.py          ← 新增：chat_json() + accumulate_usage()
│                          ← chat_json:  调用 pipeline.model_client 自带 3 层 JSON 容错
│                          ← accumulate_usage: 累加 token、估算费用
```

节点通过 `workflows.llm_utils.chat_json()` 调用 LLM，而非直接调用 `model_client`。

## Risks / Trade-offs

| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|----------|
| LangGraph Send 分派的 state reducer 冲突（多个子图写同一个 state key） | 中 | 高 | 子图节点只写 `sources[source]` 和 `source_status[source]`，按 source 键隔离，reducer 为 `replace` |
| 现有 pipeline 和 LangGraph 工作流并行运行导致状态冲突 | 低 | 中 | 两种模式读写的目录相同但不修改对方的状态文件；设计阶段确保互斥使用 |
| Checkpointer 迁移后 `.pipeline_state.json` 数据丢失 | 低 | 低 | 过渡期两种模式各维护自己的增量状态，互不影响 |
| subgraph 之间共享 `analyze_all` 节点的 LLM 调用导致并发超限 | 中 | 中 | analyze_all 是统一节点，在所有子图完成后串行执行，不存在并发 LLM 调用 |
| review 逻辑过于简单导致误判 | 中 | 中 | human_review 作为安全阀；review 维度可在后续迭代中丰富 |
| 手动删除 `articles/` 下某层文件导致 checkpoint 与文件系统不一致（如上层的 analysis.json 残留但下层 markdown 已删） | 低 | 低 | **不修复，文档化**。此场景仅出现于手动修改 `knowledge/` 目录的非正常操作路径；正常重跑应清空整个源目录。Checkpoint 不存储文件级进度，各节点依赖文件系统存在性检查做幂等，出现不一致时最坏情况是分析结果基于已删除的 markdown——用户只需删除对应源的全部产出后重跑即可恢复 |

## Migration Plan

1. **Phase 1**: 创建 `workflows/nodes/` 下 7 个节点文件 + `router.py` + `graph.py`，引入 LangGraph 依赖
2. **Phase 2**: 实现主图 + 子图构建，用 `Send()` 分派三个数据源
3. **Phase 3**: 实现 `review_router` 和按源退回逻辑
4. **Phase 4**: 集成 LangGraph Checkpointer，迁移增量状态
5. **Phase 5**: 新增 `python -m workflows.run` CLI 入口，与 `pipeline/pipeline.py` 并存
6. **Phase 6**: 验证——对同一份数据源/数据运行两种模式，产出一致

**回退策略**: 删除 `workflows/` 新增文件，继续使用 `python pipeline/pipeline.py`。

## Open Questions (已决议)

以下三个问题在设计中已讨论并锁定，此处记录最终决定：

| # | 问题 | 决议 |
|---|------|------|
| 1 | review_router v1 质检维度 | **轻量**：空标题/空 id 过滤 + 每个 source 至少产出 1 条有效条目。够让条件路由跑通即可，质检维度后续逐步加码 |
| 2 | Checkpointer 存储后端 | **默认 MemorySaver**（零配置），配置 `--checkpoint-path knowledge/.checkpoints/langgraph.db` 时切换为 **SqliteSaver**。存储目录 `knowledge/.checkpoints/`，点号开头，被 `.gitignore` 覆盖 |
| 3 | `workflows.run` CLI 参数 | **适中子集**：`--sources`, `--limit`, `--download-limit`, `--per-category-limit`, `--use-llm`, `--llm-provider`, `--llm-threshold`, `--skip-quality`, `--dry-run`, `--files`, `--verbose`, `--checkpoint-path`, `--human-review`。排除 `--from/--to/--step/--incremental/--reset/--fail-fast`（被 LangGraph 图结构或 Checkpointer 替代） |
