## 1. Data Models & Configuration

- [x] 1.1 Add `JitterStrategy` enum with `proportional`/`full_jitter`/`equal_jitter`/`none` variants
- [x] 1.2 Add `RetryConfig` dataclass (`max_attempts`/`base_delay`/`total_timeout`/`jitter_strategy`/`jitter_factor`)
- [x] 1.3 Add `retry_config` attribute to `OpenAICompatibleProvider`
- [x] 1.4 Add `_is_retryable()` function with retryable exception whitelist (`httpx.TimeoutException`, `httpx.ConnectError`, HTTP 429/5xx)

## 2. Retry Logic Rewrite

- [x] 2.1 Rewrite `chat_with_retry` — remove `max_retries`/`base_delay` params, read `provider.retry_config` instead
- [x] 2.2 Implement total wall-clock timeout loop with adaptive default calculation
- [x] 2.3 Integrate jitter function dispatch per `JitterStrategy`
- [x] 2.4 Implement dual-termination (total_timeout OR max_attempts, whichever first)
- [x] 2.5 Implement early skip when remaining budget < base_delay

## 3. Degraded Result Path

- [x] 3.1 Add `degraded: bool = False` field to `LLMResponse` dataclass
- [x] 3.2 Return `LLMResponse(degraded=True)` when all retries exhausted or budget hit
- [x] 3.3 Ensure `chat_with_retry` never raises `RuntimeError` on total failure

## 4. CostTracker Extension

- [x] 4.1 Add `FailureRecord` dataclass (`provider`/`exception`/`attempt`/`timestamp`)
- [x] 4.2 Add `record_failure()` method to `CostTracker`
- [x] 4.3 Call `record_failure()` for each failed attempt inside `chat_with_retry`
- [x] 4.4 Update `report()` to include failure count and per-attempt details
- [x] 4.5 Update `save_report()` to include `"failures"` array in output JSON

## 5. Pipeline Adaptation

- [x] 5.0 Set `provider.retry_config` during provider initialization
- [x] 5.1 Detect `resp.degraded` in `_llm_analyze`, return dict with `degraded: True`
- [x] 5.2 Update `_llm_analyze` caller to check `degraded` flag and fall back to rule_result

## 6. Testing

- [x] 6.1 Test retryable vs non-retryable exception routing
- [x] 6.2 Test total timeout exhaustion mid-retry
- [x] 6.3 Test degraded result propagation through pipeline
- [x] 6.4 Test CostTracker failure record generation
