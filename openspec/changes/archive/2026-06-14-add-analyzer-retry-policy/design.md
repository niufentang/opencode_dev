## 设计：Analyzer 重试策略

### 概述

将 `chat_with_retry` 从简陋的重试包装升级为生产级重试引擎，支持可配置的 jitter 策略、总时间预算封顶、失败成本追踪，以及降级结果回退机制，确保 pipeline 不因 LLM 失败而中断。

---

### 1. RetryConfig

用 dataclass 封装所有重试参数，作为可选参数传入：

```python
@dataclass
class RetryConfig:
    max_attempts: int = 3
    base_delay: float = 1.0
    total_timeout: float | None = None  # None=自适应计算，详见第 3 节
    jitter_strategy: str = "proportional"  # 策略名，见下文
    jitter_factor: float = 0.5          # 抖动幅度，仅 proportional 策略有效
```

`jitter_factor` 控制抖动幅度：`实际等待 = base_delay × (1 + random(0, jitter_factor))`。值越大离散度越高错峰效果越强，但最坏等待也越长。默认 0.5 即等待 1.0× ~ 1.5× base_delay，是一个兼顾发散和平滑的折中值。

传 `None` 则使用默认值——不需要关心重试调优的调用方获得合理默认行为。

**传递方式**：`RetryConfig` 挂载到 `OpenAICompatibleProvider` 实例上作为属性，`chat_with_retry` 内部从 `provider.retry_config` 读取。pipeline 初始化 provider 时统一设置：

```python
provider = OpenAICompatibleProvider(...)
provider.retry_config = RetryConfig(total_timeout=60.0)
```

**废弃旧参数**：`chat_with_retry` 的函数签名将移除 `max_retries` 和 `base_delay` 参数，统一走 `provider.retry_config`。调用方若需定制，在 provider 上设置即可。

---

### 2. JitterStrategy（抖动策略）

设计决策：**字符串枚举 + 注册表模式**——避免紧耦合同时保持可扩展性。

| 策略 | 公式 | 适用场景 |
|------|------|----------|
| `proportional`（默认） | `delay * (1 + random(0, jitter_factor))` | 通用，对下游 SLA 友好 |
| `full_jitter` | `random(0, delay)` | 高并发，收敛最快 |
| `equal_jitter` | `delay/2 + random(0, delay/2)` | 折中方案 |
| `none` | `delay`（纯指数退避） | 需要确定性等待时间 |

```python
class JitterStrategy(str, Enum):
    PROPORTIONAL = "proportional"
    FULL_JITTER = "full_jitter"
    EQUAL_JITTER = "equal_jitter"
    NONE = "none"
```

传入未知字符串 → 抛出 `ValueError`，不静默降级到默认值。

---

### 3. 总超时语义（proposal 中的 `max_delay`）

**探索中明确的决策**：`max_delay=20s` 指整个 `chat_with_retry` 调用的 **总 wall-clock 预算**，不是每次退避的封顶值。

```
时间线：
├── 第 1 次请求 ──[请求耗时 15s]──┤  剩余预算: 5s
├── 退避休眠   ──[休眠 1.3s]──────┤  剩余预算: 3.7s
├── 第 2 次请求 ──[请求 3.7s→超时]──┤  预算耗尽
└── 返回降级结果 ✅
```

**边界规则**：

- 预算从函数入口开始计时
- 原始请求耗时、退避休眠、重试请求耗时**全部计入**
- 重试前剩余预算不足一个 `base_delay` → 跳过重试直接降级
- `max_attempts` 是第二重约束——**任一条件满足即终止**

**自适应默认值**：`total_timeout` 默认值为 `None`，此时自动根据 httpx 单次超时、`max_attempts`、`base_delay` 计算：

```python
def _default_total_timeout(httpx_timeout: int, max_attempts: int, base_delay: float) -> float:
    backoff_total = base_delay * (2 ** (max_attempts - 1) - 1)
    return httpx_timeout * max_attempts + backoff_total

# httpx_timeout=60, max_attempts=3, base_delay=1.0 → 183s
# httpx_timeout=30, max_attempts=3, base_delay=1.0 → 93s
```

传具体值则使用该值覆盖自适应结果，不做验证（调用方自己负责合理性）。

```
  总超时到达? ──→ 降级
       ↓ 否
  重试次数用完? ──→ 降级
       ↓ 否
  继续重试
```

---

### 4. 返回类型：降级路径

**当前**：`chat_with_retry` 全部失败后抛出 `RuntimeError`，调用方必须靠 `try/except` 兜底，异常信息中断了 pipeline 流程。

**新设计**：为 `LLMResponse` 添加 `degraded` 字段。核心作用是让调用方有能力区分"正常结果"和"尽力而为的兜底结果"，同时保持方法签名的类型安全。

```
改造前:
chat_with_retry ── 成功 → LLMResponse
                └── 失败 → 抛 RuntimeError ✗

改造后:
chat_with_retry ── 成功 → LLMResponse(degraded=False)
                └── 全部重试失败 → LLMResponse(degraded=True)
                                   ↑ 不抛异常，返回空内容
```

引入 `degraded` 标记带来几个好处：

- **类型安全** — 始终返回 `LLMResponse`，从不抛异常，调用方不需要做空值判断
- **可追溯** — `save_report()` 报表中可统计 degraded 次数，而非在日志中无声吞掉
- **可扩展** — 后续可以针对 degraded 的文件做二次重试、人工审核等策略，无需改动方法签名

```python
@dataclass
class LLMResponse:
    content: str
    usage: Usage = field(default_factory=Usage)
    provider: str = ""
    model: str = ""
    degraded: bool = False          # 新增
```

重试耗尽或预算触顶时返回：

```python
return LLMResponse(
    content="",
    usage=Usage(prompt_tokens=0, completion_tokens=0),
    provider=provider.provider_name,
    model=provider.model,
    degraded=True,
)
```

**非法 JSON 处理**：degraded 的空内容和 LLM 返回的非法 JSON 统一走同一路径——`_llm_analyze` 检测到 degraded 时直接返回 `{"degraded": True}`，不执行 `json.loads`；非法 JSON 同样走 `except` 降级到规则通道。不做细粒度区分。

**Pipeline 影响**（`_llm_analyze` 在 pipeline.py 中）：

```
改造前:                        改造后:
resp = chat_with_retry(...)    resp = chat_with_retry(...)
                                if resp.degraded:
                                    return {"degraded": True, ...}
return json.loads(...)         return json.loads(...)
```

调用方（`_merge_analysis`）检测 `degraded` 标记，回退到仅用规则通道结果，并记录警告：

```python
if llm_result and not llm_result.get("degraded"):
    final = self._merge_analysis(rule_result, llm_result)
else:
    if llm_result and llm_result.get("degraded"):
        logger.warning("  LLM 降级，使用规则通道结果 [%s]", md_file.name)
    final = rule_result
```

这是**向后兼容的变更**——降级结果不再返回 `None`，调用方类型签名保持稳定，pipeline 永不在 LLM 失败时崩溃。

---

### 5. CostTracker 扩展

CostTracker 是整个 pipeline 的 LLM 调用成本追踪器，职责链：

```
每次 chat_with_retry
  ├─ 成功 → tracker.record(usage, provider)   ← 记录 token 用量
  └─ 失败 → tracker.record_failure(...)       ← 新增：记录失败
                          ↓
pipeline 结束时 → tracker.report()       → 日志输出（按提供商拆分）
               → tracker.save_report()  → JSON 文件持久化
```

它解决一个实际问题：**LLM 花了多少钱、花在哪里、哪些调用失败了但仍在计费**。报表按提供商拆分 token 数和费用（USD/CNY 双币种），方便做成本归属和异常排查。

当前已有 `record()`、`report()`、`save_report()`，本次新增 `record_failure()`。

proposal 要求："失败的 API 调用也计入 CostTracker（tokens=0）".

当前 `CostTracker.record()` 接收 `Usage` 对象。对于失败调用，传入空 `Usage()` 并记录异常信息：

```python
tracker.record_failure(provider_name=..., exception=..., attempt=...)
```

新增独立方法而非重载 `record()`，使成功/失败在报表中可区分：

```python
@dataclass
class FailureRecord:
    provider: str
    exception: str          # 完整 traceback 字符串，便于排查
    attempt: int
    timestamp: float

class CostTracker:
    def record(self, usage: Usage, provider: str) -> None: ...
    def record_failure(self, provider: str, exception: str, attempt: int) -> None:
        """记录一次失败的 API 调用。

        Args:
            provider: 提供商名称。
            exception: 异常完整 traceback 字符串（便于排查）。
            attempt: 失败时的重试轮次（0 = 首次请求）。
        """
```

**报表影响**：`save_report` 和 `report()` 增加 `"failures"` 部分：

```json
{
  "total_calls": 12,
  "total_failures": 3,
  "failures": [
    {"provider": "deepseek", "exception": "ConnectTimeout", "attempt": 1}
  ]
}
```

---

### 6. 可重试异常

**白名单制**——显示列出可重试的异常，其余立即上抛：

| 异常 / 条件 | 可重试 | 原因 |
|------------|--------|------|
| `httpx.TimeoutException` | ✅ | 瞬时网络问题 |
| `httpx.ConnectError` | ✅ | DNS/连接抖动 |
| HTTP 429（请求过多） | ✅ | 限流，服务端要求等待 |
| HTTP 5xx（服务端错误） | ✅ | 服务端瞬时故障 |
| `httpx.HTTPStatusError` (400/401/403/413) | ❌ | 客户端错误，重试无效 |
| `json.JSONDecodeError`（响应体） | ❌ | API 契约被破坏，快速失败 |
| `context_length_exceeded` (400) | ❌ | 请求过长，重试无效 |

实现：

```python
RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}

def _is_retryable(exc: Exception) -> bool:
    if isinstance(exc, (httpx.TimeoutException, httpx.ConnectError)):
        return True
    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code in RETRYABLE_HTTP_CODES
    return False
```

429 即使没有 `Retry-After` header 仍然重试（按 proposal："暂时不解析 Retry-After header"），指数退避 + jitter 已提供隐式间隔。

---

### 7. 实施计划

| 步骤 | 文件 | 变更内容 |
|------|------|----------|
| 1 | `model_client.py` | 新增 `RetryConfig`、`JitterStrategy`、`_is_retryable` |
| 2 | `model_client.py` | 重写 `chat_with_retry`，加入总超时循环 + jitter |
| 3 | `model_client.py` | 为 `LLMResponse` 增加 `degraded` 字段 |
| 4 | `model_client.py` | 为 `CostTracker` 增加 `record_failure`，更新 `report`/`save_report` |
| 5 | `pipeline.py` | `_llm_analyze` 调用方适配 `degraded` 标记 |

---

### 8. 待定问题

（已全部关闭）
