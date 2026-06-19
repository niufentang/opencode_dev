"""LangGraph 工作流共享状态定义。

┌────────────  写入  ┌────────────────────┐
│  Collect    │ ───→ │ sources: dict      │ → knowledge/raw/
└────────────       │ (doc_id → meta)    │
                    └────────────────────┘
                           │ Analyze 读
                           ▼
┌────────────  写入  ┌────────────────────┐
│  Parse      │ ───→ │ (无字段，走文件系统) │ → knowledge/articles/
└────────────       │ {markdown,metadata} │   {markdown, metadata}/
                    └────────────────────┘
                           │ Analyze 读
                           ▼
┌────────────  写入  ┌────────────────────┐
│  Analyze    │ ───→ │ analyses: dict     │ → knowledge/articles/
└────────────       │ (doc_id → result)  │   analyzed/
                    └────────────────────┘
                           │ Organize 读
                           ▼
┌────────────  写入  ┌────────────────────┐
│  Organize   │ ───→ │ articles: dict     │ → knowledge/articles/
└────────────       │ (doc_id → entry)   │   entries/
                    └────────────────────┘
                           │ Save + Review 读
                           ▼
┌────────────  写入  ┌────────────────────┐
│  Save       │ ───→ │ save_report: dict  │ → 分发通知
└────────────       │ (摘要报告)          │
                    └────────────────────┘

审核循环: Review 节点读 analyses + articles
  ├─ 退回 Analyze  → 重写 analyses
  ├─ 退回 Organize → 重写 articles
  └─ 通过 → Save 节点执行

遵循"报告式通信"原则：状态字段存储的是结构化摘要，
而非原始数据。原始数据通过文件系统路径引用（knowledge/raw/）。
"""

from __future__ import annotations

from typing import TypedDict


class KBState(TypedDict):
    """知识库工作流的全局共享状态。

    该状态在 LangGraph 的各个节点之间传递，每个节点读取
    上游产出、写入自身产出，形成有向无环的数据流。
    审核循环通过 iteration / review_passed / review_feedback
    三个字段控制回退与终止。
    """

    sources: dict[str, dict]
    """采集阶段产出（对应 pipeline.Collect）：doc_id → 文档元数据。

    每个 value 的格式: {"source": "sse|szse|chinaclear", "category": str,
                        "title": str, "url": str, "file_path": str,
                        "public_date": str, "crawl_date": str}
    原始文件位于 knowledge/raw/{source}/{category}/... 下。
    """

    analyses: dict[str, dict]
    """分析阶段产出（对应 pipeline.Analyze）：doc_id → LLM 或规则引擎的结构化分析结果。

    Organize 节点读取此字段生成 articles。
    Review 节点退回 Analyze 时依赖本字段做回退判断。

    每个 value 的格式: {"doc_id": str, "change_type": str,
                        "summary": str, "tags": list[str],
                        "confidence": float, "analysis_detail": dict}
    """

    articles: dict[str, dict]
    """整理阶段产出（对应 pipeline.Organize + Save）：doc_id → 最终知识条目。

    由 Organize 节点写入，Save 节点读取入库并分发。
    Review 节点退回 Organize 时依赖本字段做回退判断。

    每个 value 的格式: 见 AGENTS.md「知识条目 JSON 格式」章节定义。
          包含 id / title / summary / content_markdown / status 等字段。
    """

    review_feedback: str
    """审核反馈意见：描述未通过的原因或修改建议。

    由审核节点（人工或自动规则）写入，供上游节点参考修正。
    空字符串表示无反馈。
    """

    review_passed: bool
    """审核是否通过。

    True  → 工作流结束，进入分发阶段。
    False → 触发 review 循环重试，iteration 自增。
    """

    iteration: int
    """当前审核循环次数，从 0 开始计数。

    每次 review_passed=False 时自增 1。
    当 iteration >= max_iterations（通常为 3）时
    将 needs_human_review 设为 True 并终止循环。
    """

    needs_human_review: bool
    """是否标记为需人工介入。

    当审核循环耗尽（iteration >= 3）仍未通过时设为 True，
    此时不再继续循环，但工作流仍可结束并通知人工处理。
    """

    save_report: dict
    """保存阶段执行报告（对应 pipeline.Save）。

    由 Save 节点在完成入库与分发后写入，仅用于工作流结束后的
    结果回溯，下游无节点消费此字段。

    格式: {"total": int, "saved": int, "skipped": int, "failed": int,
           "quality_warnings": list[str],
           "notifications": {"email": bool, "feishu": bool}}
    """

    cost_tracker: dict
    """Token 用量与费用追踪快照。

    每个 LLM 调用节点结束时，从 model_client.tracker.get_summary()
    读取当前累计值写入，后续节点覆盖前值。
    初始值为空 dict，首次调用后即获得实际数据。

    格式: {"total_tokens": int, "total_cost_usd": float,
           "total_cost_cny": float, "calls": int,
           "by_model": {"model_name": {"tokens": int, "cost": float}}}
    """
