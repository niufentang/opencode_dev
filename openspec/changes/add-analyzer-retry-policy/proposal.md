## Why

当前 `chat_with_retry` 的重试机制过于简单：异常捕获范围偏宽（捕获业务错误浪费重试）、缺 jitter 易导致惊群效应、无封顶可能无限等待、失败不记成本无法排查、且全部失败后抛异常中断 pipeline。需要升级为生产级重试策略。

## What Changes

- 精确定义可重试异常列表（仅网络层/限流异常），其余直接上抛
- 指数退避参数调整：base_delay=1s, max_attempts=3, total_timeout=20s（总 wall-clock 预算封顶，含请求耗时 + 退避休眠 + 重试耗时）
- 增加 1.0-1.5× 随机抖动（只加不减），防雪崩
- 失败的 API 调用也计入 CostTracker（tokens=0），便于 debug 成本
- 全部重试失败后走降级路径，返回默认结果并标记 `degraded`，不中断 pipeline
- 暂时统一指数退避，不解析 Retry-After header

## Capabilities

### New Capabilities
- `analyzer-retry`: 升级 `chat_with_retry` 的重试策略为生产级实现

### Modified Capabilities
- （无，仅实现层变更，不涉及 spec 级行为变化）

## Impact

- `pipeline/model_client.py` — `chat_with_retry` 函数重写，CostTracker 扩展
- `pipeline/pipeline.py` — `_llm_analyze` 调用方适配降级返回值
