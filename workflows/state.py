"""LangGraph 工作流共享状态定义。

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

    sources: list[dict]
    """采集阶段产出：每个 dict 为一条文档元数据。

    格式: {"source": "sse|szse|chinaclear", "category": str,
           "title": str, "url": str, "file_path": str,
           "public_date": str, "crawl_date": str}
    原始文件位于 knowledge/raw/{source}/{category}/... 下。
    """

    analyses: list[dict]
    """分析阶段产出：LLM 或规则引擎对每篇文档的结构化分析结果。

    格式: {"doc_id": str, "change_type": str,
           "summary": str, "tags": list[str],
           "confidence": float, "analysis_detail": dict}
    """

    articles: list[dict]
    """整理阶段产出：格式化、去重、合并后的最终知识条目。

    格式: 见 AGENTS.md「知识条目 JSON 格式」章节定义。
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
    当 iteration >= max_iterations（通常为 3）时强制终止，
    标记为"需人工介入"。
    """

    cost_tracker: dict
    """Token 用量与费用追踪。

    由 model_client.py 的 tracker 对象在每个 LLM 调用后更新。
    格式: {"total_tokens": int, "total_cost_usd": float,
           "total_cost_cny": float, "calls": int,
           "by_model": {"model_name": {"tokens": int, "cost": float}}}
    """
