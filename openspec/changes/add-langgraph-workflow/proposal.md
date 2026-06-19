## Why

当前知识库自动化流水线是命令式编排（`pipeline/pipeline.py`），5 步线性执行，流程控制、状态管理、重试逻辑都硬编码在 `PipelineRunner` 类中。随着需求演进（按源并行、审查循环、人工介入、断点续跑），命令式架构的灵活性和可观测性已达瓶颈。LangGraph 提供声明式 StateGraph，将流水线从"类方法调用"重构为"节点+边+条件路由"，天然支持并行分派、审查回路和 checkpoint 持久化。

## What Changes

- **新增** `workflows/` 下的 LangGraph 工作流定义（节点、图、路由），与现有 `pipeline/pipeline.py` 共存过渡
- **新增** 6 个 LangGraph 节点函数，拆分至 `workflows/nodes/` 独立文件
- **新增** 条件路由函数（源分派、审查退回）
- **新增** 审查节点（`review_router`），在 organize 之后、save 之前逐源质检
- **新增** 人工审核节点（`human_review`），支持可配置的 `log` / `interrupt` 模式
- **扩展** `KBState` TypedDict，增加 `sources`、`source_status`、`workflow_config` 字段
- **迁移** 增量状态机制从 `.pipeline_state.json` 到 LangGraph Checkpointer

## Capabilities

### New Capabilities

- `langgraph-workflow`: 基于 LangGraph StateGraph 的声明式工作流，含节点定义、条件路由、子图分派
- `parallel-source-pipeline`: 按数据源（SSE/SZSE/ChinaClear）并行执行的 Collect→Parse 子图，用 Send() 分派
- `review-loop`: 逐源质量审查 + 退回重跑 + 超限人工介入的闭环审查机制

### Modified Capabilities

- *无* — 这是全新工作流，与现有 `pipeline/pipeline.py` 共存，不修改现有 specs

## Impact

- **新增文件**: `workflows/nodes/` 下 7 个节点文件 + `workflows/graph.py` + `workflows/router.py`
- **修改文件**: `workflows/state.py`（扩展 KBState 字段）
- **依赖**: `langgraph>=1.2.0` 已在 `requirements.txt`
- **入口**: 新增独立 CLI 入口 `python -m workflows.run`，与 `python pipeline/pipeline.py` 并存
- **数据兼容**: 两种模式读写同一份 `knowledge/` 目录，产出格式一致
