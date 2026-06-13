# analyzer-retry

## ADDED Requirements

### Requirement: `chat_with_retry` SHALL 接受 RetryConfig 参数化重试行为

`chat_with_retry` SHALL 接受可选的 `RetryConfig` dataclass，该 dataclass 封装所有重试参数：`max_attempts`、`base_delay`、`total_timeout`、`jitter_strategy`、`jitter_factor`。传入 `None` 时使用默认值。

#### Scenario: 传入自定义 total_timeout 的 RetryConfig
- **WHEN** 调用方传入 `RetryConfig(total_timeout=60.0)` 给 `chat_with_retry`
- **THEN** 重试 SHALL 使用 60 秒作为总 wall-clock 预算

#### Scenario: 传入 None 时使用默认值
- **WHEN** 调用方传入 `retry_config=None` 或省略参数
- **THEN** 重试 SHALL 使用默认值：max_attempts=3, base_delay=1.0, total_timeout=20.0, jitter_strategy="proportional", jitter_factor=0.5

### Requirement: JitterStrategy SHALL 支持四种策略

`JitterStrategy` SHALL 是一个枚举，包含四个值：`proportional`、`full_jitter`、`equal_jitter`、`none`。传入未知字符串 SHALL 抛出 `ValueError`。

#### Scenario: 未知 jitter 策略抛出 ValueError
- **WHEN** 调用方向 `RetryConfig` 传入 `jitter_strategy="unknown_strategy"`
- **THEN** `chat_with_retry` SHALL 抛出 `ValueError`

#### Scenario: 各 jitter 策略按正确公式计算
- **WHEN** `jitter_strategy` 分别设为四种支持的值
- **THEN** 退避延迟 SHALL 按对应公式计算：proportional (`delay * (1 + random(0, jitter_factor))`)、full_jitter (`random(0, delay)`)、equal_jitter (`delay/2 + random(0, delay/2)`)、none (`delay`)

### Requirement: 总超时 SHALL 封顶重试的 wall-clock 时长

`total_timeout` SHALL 定义整个 `chat_with_retry` 调用的最大 wall-clock 预算，包括原始请求耗时、退避休眠和重试请求耗时。即使 `max_attempts` 尚未达到，预算耗尽时函数 SHALL 停止重试并返回降级结果。

#### Scenario: 重试过程中总超时到达
- **WHEN** 总耗时超过 `total_timeout`
- **THEN** `chat_with_retry` SHALL 停止重试并返回降级结果

#### Scenario: 重试前剩余预算不足 base_delay
- **WHEN** 计划重试前剩余预算小于 `base_delay`
- **THEN** `chat_with_retry` SHALL 跳过重试直接返回降级结果

#### Scenario: total_timeout 前已达 max_attempts
- **WHEN** `max_attempts` 次重试在 `total_timeout` 到达前已耗尽
- **THEN** `chat_with_retry` SHALL 停止重试并返回降级结果

### Requirement: 全部失败 SHALL 返回 degraded LLMResponse 而非抛异常

所有重试耗尽或总超时到达时，`chat_with_retry` SHALL 返回 `degraded=True` 且内容为空的 `LLMResponse`，而非抛出 `RuntimeError`。

#### Scenario: 降级结果包含 degraded=True
- **WHEN** 所有重试都失败
- **THEN** `chat_with_retry` SHALL 返回 `LLMResponse(degraded=True, content="")`
- **AND** SHALL NOT 抛出任何异常
- **AND** SHALL 通过 `CostTracker.record_failure()` 记录失败

### Requirement: 重试 SHALL 仅对白名单异常触发

`chat_with_retry` SHALL 仅对以下异常重试：`httpx.TimeoutException`、`httpx.ConnectError`、HTTP 429（请求过多）、HTTP 5xx（500/502/503/504）。其余异常 SHALL 立即上抛，不重试。

#### Scenario: 可重试异常触发退避
- **WHEN** `chat_with_retry` 捕获 `httpx.TimeoutException`
- **THEN** 它 SHALL 应用退避延迟并重试

#### Scenario: 不可重试异常立即上抛
- **WHEN** `chat_with_retry` 捕获 HTTP 400 或 `json.JSONDecodeError`
- **THEN** 它 SHALL 立即重新抛出异常，不重试

### Requirement: 失败调用 SHALL 记录到 CostTracker

`CostTracker` SHALL 提供 `record_failure(provider, exception, attempt)` 方法记录失败的 API 调用。失败记录 SHALL 包含提供商名称、完整异常 traceback 字符串、尝试轮次和时间戳。`report()` 和 `save_report()` SHALL 包含 failures 部分。

#### Scenario: 失败记录出现在成本报表中
- **WHEN** `chat_with_retry` 所有重试后失败
- **THEN** 每次失败的尝试 SHALL 调用 `CostTracker.record_failure()`
- **AND** `report()` 输出 SHALL 包含失败次数和每次尝试的详情
- **AND** `save_report()` 输出 JSON SHALL 包含 `"failures"` 数组，包含 `provider`、`exception`、`attempt` 字段
