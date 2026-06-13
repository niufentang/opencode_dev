"""统一的 LLM 调用客户端，通过 OpenAI 兼容 API 支持多家模型提供商。

支持 DeepSeek、Qwen（DashScope）、Kimi（Moonshot）：
- 抽象基类接口设计
- 指数退避重试
- Token 估算与费用计算（USD/CNY）
- quick_chat 便捷调用函数
"""

from __future__ import annotations

import logging
import os
import random
import re
import time
import traceback
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

import httpx
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# 自动读取 .env 文件到环境变量，后续 os.environ.get() 可直接取值
load_dotenv()


# ---------------------------------------------------------------------------
# 数据模型
# ---------------------------------------------------------------------------


class JitterStrategy(str, Enum):
    """抖动策略枚举。

    控制重试退避的随机化算法，用于分散重试时间点，避免惊群效应。
    """

    PROPORTIONAL = "proportional"
    FULL_JITTER = "full_jitter"
    EQUAL_JITTER = "equal_jitter"
    NONE = "none"


@dataclass
class RetryConfig:
    """重试配置，封装所有可调参数。

    Attributes:
        max_attempts: 最大重试次数（不含首次请求）。
        base_delay: 首次退避的基准秒数。
        total_timeout: 总 wall-clock 预算（秒），None 表示自适应计算。
        jitter_strategy: 抖动策略名，对应 JitterStrategy 枚举。
        jitter_factor: 抖动幅度，仅 proportional 策略有效。
    """
    max_attempts: int = 3
    base_delay: float = 1.0
    total_timeout: float | None = None
    jitter_strategy: str = "proportional"
    jitter_factor: float = 0.5


@dataclass
class Usage:
    """LLM API 调用的 token 用量统计。

    Attributes:
        prompt_tokens: 提示（输入）的 token 数。
        completion_tokens: 补全（输出）的 token 数。
    """
    prompt_tokens: int = 0
    completion_tokens: int = 0

    @property
    def total_tokens(self) -> int:
        return self.prompt_tokens + self.completion_tokens

    def to_dict(self) -> dict[str, int]:
        return {
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "total_tokens": self.total_tokens,
        }


@dataclass
class LLMResponse:
    """LLM 调用的统一响应结果。

    Attributes:
        content: 生成的文本内容。
        usage: token 用量统计。
        provider: 使用的提供商名称。
        model: 使用的模型名称。
    """
    content: str
    usage: Usage = field(default_factory=Usage)
    provider: str = ""
    model: str = ""
    degraded: bool = False

    def to_dict(self) -> dict:
        return {
            "content": self.content,
            "usage": self.usage.to_dict(),
            "provider": self.provider,
            "model": self.model,
        }


# ---------------------------------------------------------------------------
# 提供商配置
# ---------------------------------------------------------------------------

PROVIDER_CONFIGS: dict[str, dict] = {
    "deepseek": {
        "base_url": "https://api.deepseek.com",
        "model": "deepseek-v4-flash",
        "env_key": "DEEPSEEK_API_KEY",
        "model_env": "DEEPSEEK_MODEL",
        "price_input_per_1m": 0.14,
        "price_output_per_1m": 0.28,
        "price_input_per_1m_cny": 1.0,
        "price_output_per_1m_cny": 2.0,
    },
    "qwen": {
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "qwen3.6-plus",
        "env_key": "DASHSCOPE_API_KEY",
        "model_env": "QWEN_MODEL",
        "price_input_per_1m": 0.28,
        "price_output_per_1m": 1.67,
        "price_input_per_1m_cny": 2.0,
        "price_output_per_1m_cny": 12.0,
    },
    "kimi": {
        "base_url": "https://api.moonshot.cn/v1",
        "model": "kimi-k2.6",
        "env_key": "MOONSHOT_API_KEY",
        "model_env": "KIMI_MODEL",
        "price_input_per_1m": 0.90,
        "price_output_per_1m": 3.75,
        "price_input_per_1m_cny": 6.5,
        "price_output_per_1m_cny": 27.0,
    },
}


# ---------------------------------------------------------------------------
# 抽象基类
# ---------------------------------------------------------------------------


class LLMProvider(ABC):
    """LLM 提供商抽象基类。"""

    @abstractmethod
    def chat(self, messages: list[dict], **kwargs) -> LLMResponse:
        """发送对话补全请求。

        Args:
            messages: 消息字典列表，每项含 'role' 和 'content'。
            **kwargs: 额外参数（temperature、max_tokens 等）。

        Returns:
            LLMResponse，包含生成内容和用量统计。
        """


# ---------------------------------------------------------------------------
# OpenAI 兼容提供商实现
# ---------------------------------------------------------------------------


class OpenAICompatibleProvider(LLMProvider):
    """基于 httpx 调用 OpenAI 兼容 API 的 LLM 提供商。

    Args:
        provider_name: PROVIDER_CONFIGS 中的键名（'deepseek'、'qwen'、'kimi'）。
        api_key: API 密钥，未传入时从环境变量读取。
        base_url: API 基础地址，未传入时使用配置默认值。
        model: 模型名称，未传入时使用配置默认值。
        timeout: 请求超时时间（秒）。
    """

    def __init__(
        self,
        provider_name: str = "deepseek",
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None,
        timeout: int = 60,
    ):
        if provider_name not in PROVIDER_CONFIGS:
            raise ValueError(
                f"未知提供商: {provider_name}。"
                f"可选: {', '.join(PROVIDER_CONFIGS)}"
            )

        cfg = PROVIDER_CONFIGS[provider_name]
        self.provider_name = provider_name
        self.api_key = api_key or os.environ.get(cfg["env_key"], "")
        if not self.api_key:
            raise ValueError(
                f"未找到 {provider_name} 的 API 密钥，"
                f"请设置环境变量 {cfg['env_key']}"
            )
        self.base_url = (base_url or cfg["base_url"]).rstrip("/")
        # 模型选择优先级：显式传参 > 环境变量 > 配置默认值
        self.model = model or os.environ.get(cfg.get("model_env", "")) or cfg["model"]
        self.timeout = timeout
        self.retry_config: Optional[RetryConfig] = None
        pool_limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
        self._client = httpx.Client(timeout=self.timeout, limits=pool_limits)

    def close(self) -> None:
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def chat(self, messages: list[dict], **kwargs) -> LLMResponse:
        """通过 OpenAI 兼容 API 发送对话补全请求。

        Args:
            messages: 消息字典列表，每项含 'role' 和 'content'。
            **kwargs: 覆盖参数（temperature、max_tokens、model 等）。

        Returns:
            LLMResponse，包含内容和用量统计。

        Raises:
            httpx.HTTPError: API 请求失败时抛出。
        """
        model = kwargs.pop("model", self.model)
        temperature = kwargs.pop("temperature", 0.7)
        max_tokens = kwargs.pop("max_tokens", 4096)

        payload: dict = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        payload.update(kwargs)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        url = f"{self.base_url}/chat/completions"

        logger.debug("发送请求至 %s，模型: %s", url, model)

        resp = self._client.post(url, json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()

        choice = data["choices"][0]
        content = choice["message"]["content"] or ""

        usage_data = data.get("usage", {})
        usage = Usage(
            prompt_tokens=usage_data.get("prompt_tokens", 0),
            completion_tokens=usage_data.get("completion_tokens", 0),
        )

        return LLMResponse(
            content=content,
            usage=usage,
            provider=self.provider_name,
            model=model,
        )


# ---------------------------------------------------------------------------
# 重试包装
# ---------------------------------------------------------------------------


RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}


def _is_retryable(exc: Exception) -> bool:
    """判断异常是否可重试。

    白名单制：仅网络层和限流异常可重试，其余立即上抛。
    """
    if isinstance(exc, (httpx.TimeoutException, httpx.ConnectError)):
        return True
    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code in RETRYABLE_HTTP_CODES
    return False


def _apply_jitter(delay: float, strategy: str, jitter_factor: float = 0.5) -> float:
    """对退避延迟施加随机抖动。

    Args:
        delay: 退避基准延迟（秒）。
        strategy: JitterStrategy 枚举值。
        jitter_factor: 抖动幅度，仅 proportional 策略有效。

    Returns:
        施加抖动后的延迟（秒）。
    """
    if strategy == JitterStrategy.PROPORTIONAL:
        return delay * (1 + random.random() * jitter_factor)
    elif strategy == JitterStrategy.FULL_JITTER:
        return random.random() * delay
    elif strategy == JitterStrategy.EQUAL_JITTER:
        return delay / 2 + random.random() * delay / 2
    else:
        return delay


def _default_total_timeout(httpx_timeout: int, max_attempts: int, base_delay: float) -> float:
    """自适应计算 total_timeout 默认值。

    公式：单次请求超时 × 请求次数 + 退避总和。
    """
    backoff_total = base_delay * (2 ** (max_attempts - 1) - 1)
    return httpx_timeout * max_attempts + backoff_total


def chat_with_retry(
    provider: LLMProvider,
    messages: list[dict],
    **kwargs,
) -> LLMResponse:
    """带指数退避重试的对话请求。

    支持可配置的 RetryConfig（挂在 provider.retry_config 上），
    总时间预算封顶、抖动策略、仅白名单异常可重试。

    Args:
        provider: LLMProvider 实例（需已设置 retry_config）。
        messages: 消息字典列表。
        **kwargs: 传递给 provider.chat() 的额外参数。

    Returns:
        成功时返回 LLMResponse；全部失败后返回 LLMResponse(degraded=True)。
    """
    config = getattr(provider, "retry_config", None) or RetryConfig()

    if not isinstance(config.jitter_strategy, JitterStrategy):
        try:
            config.jitter_strategy = JitterStrategy(config.jitter_strategy)
        except ValueError:
            raise ValueError(
                f"未知抖动策略: {config.jitter_strategy}。"
                f"可选: {[e.value for e in JitterStrategy]}"
            )

    httpx_timeout = getattr(provider, "timeout", 60)
    total_timeout = config.total_timeout
    if total_timeout is None:
        total_timeout = _default_total_timeout(httpx_timeout, config.max_attempts, config.base_delay)

    deadline = time.monotonic() + total_timeout
    last_exc: Optional[Exception] = None

    for attempt in range(1 + config.max_attempts):
        try:
            resp = provider.chat(messages, **kwargs)
            tracker.record(resp.usage, provider.provider_name)
            return resp
        except Exception as e:
            last_exc = e
            tracker.record_failure(provider.provider_name, traceback.format_exc(), attempt)

            if not _is_retryable(e):
                raise

            if attempt >= config.max_attempts:
                logger.error("全部 %d 次对话均失败。", 1 + config.max_attempts)
                break

            now = time.monotonic()
            remaining = deadline - now

            if remaining < config.base_delay:
                logger.warning("预算不足，跳过重试: %.1fs 剩余", remaining)
                break

            delay = config.base_delay * (2**attempt)
            delay = _apply_jitter(delay, config.jitter_strategy, config.jitter_factor)
            delay = min(delay, remaining)

            logger.warning(
                "第 %d 次对话失败: %s，%.1fs 后重试...",
                attempt + 1,
                e,
                delay,
            )
            time.sleep(delay)

    return LLMResponse(
        content="",
        usage=Usage(prompt_tokens=0, completion_tokens=0),
        provider=getattr(provider, "provider_name", ""),
        model=getattr(provider, "model", ""),
        degraded=True,
    )


# ---------------------------------------------------------------------------
# Token 估算与费用计算
# ---------------------------------------------------------------------------


def estimate_tokens(text: str) -> int:
    """估算文本的 token 数量。

    启发式规则：英文约 4 字符/token，中文约 1.5 字符/token。

    Args:
        text: 输入文本。

    Returns:
        估算的 token 数。
    """
    if not text:
        return 0

    # 用正则找出所有中文字符（Unicode 范围涵盖常用汉字和生僻字），统计个数
    cjk_chars = len(re.findall(r"[\u4e00-\u9fff\u3400-\u4dbf]", text))
    other_chars = len(text) - cjk_chars

    estimated = round(cjk_chars / 1.5 + other_chars / 4.0)
    return max(1, estimated)


def calculate_cost(
    usage: Usage,
    provider_name: str = "deepseek",
    currency: str = "usd",
) -> float:
    """根据 token 用量计算 API 调用费用。

    Args:
        usage: 用量统计（含 prompt/completion token 数）。
        provider_name: 提供商名称，对应 PROVIDER_CONFIGS 的键。
        currency: 币种，'usd' 或 'cny'（默认 'usd'）。

    Returns:
        指定币种的费用金额。
    """
    cfg = PROVIDER_CONFIGS.get(provider_name)
    if cfg is None:
        logger.warning("费用计算发现未知提供商: %s", provider_name)
        return 0.0

    if currency == "cny":
        input_key = "price_input_per_1m_cny"
        output_key = "price_output_per_1m_cny"
    else:
        input_key = "price_input_per_1m"
        output_key = "price_output_per_1m"

    input_cost = usage.prompt_tokens * cfg[input_key] / 1_000_000
    output_cost = usage.completion_tokens * cfg[output_key] / 1_000_000
    return round(input_cost + output_cost, 8)


def estimate_message_cost(
    messages: list[dict],
    provider_name: str = "deepseek",
    estimated_output_tokens: int = 500,
    currency: str = "usd",
) -> float:
    """在调用前预估一次对话的费用。

    Args:
        messages: 消息列表（与 chat API 格式相同）。
        provider_name: 提供商名称。
        estimated_output_tokens: 预估的输出 token 数。
        currency: 币种，'usd' 或 'cny'（默认 'usd'）。

    Returns:
        指定币种的预估费用金额。
    """
    # 原实现：prompt_text = " ".join(...) 仅拼接消息内容，丢失角色和消息边界
    # 修改为带上 role 前缀和双换行分隔，使 token 估算更接近实际 API 请求形态
    prompt_text = "\n\n".join(
        f"{m.get('role', 'user')}: {m.get('content', '') or ''}" for m in messages
    )
    prompt_tokens = estimate_tokens(prompt_text)

    usage = Usage(
        prompt_tokens=prompt_tokens,
        completion_tokens=estimated_output_tokens,
    )
    return calculate_cost(usage, provider_name, currency=currency)


# ---------------------------------------------------------------------------
# 成本追踪器
# ---------------------------------------------------------------------------


@dataclass
class FailureRecord:
    """一次失败的 API 调用记录。

    Attributes:
        provider: 提供商名称。
        exception: 完整 traceback 字符串，便于排查。
        attempt: 失败时的重试轮次（0 = 首次请求）。
        timestamp: 失败时间戳。
    """
    provider: str
    exception: str
    attempt: int
    timestamp: float


class CostTracker:
    """追踪 LLM 调用的 token 消耗和成本。

    全局单例使用 _tracker，Pipeline 结束后调 report() 输出汇总。
    """

    def __init__(self) -> None:
        self._records: list[dict] = []
        self._failures: list[FailureRecord] = []

    def record(self, usage: Usage, provider: str) -> None:
        """记录一次 API 调用。

        Args:
            usage: 本次调用的 token 用量。
            provider: 提供商名称（PROVIDER_CONFIGS 的键）。
        """
        self._records.append({
            "usage": usage,
            "provider": provider,
            "timestamp": time.time(),
        })

    def record_failure(self, provider: str, exception: str, attempt: int) -> None:
        """记录一次失败的 API 调用。

        Args:
            provider: 提供商名称。
            exception: 异常完整 traceback 字符串。
            attempt: 失败时的重试轮次（0 = 首次请求）。
        """
        self._failures.append(FailureRecord(
            provider=provider,
            exception=exception,
            attempt=attempt,
            timestamp=time.time(),
        ))

    def _filter(self, provider: Optional[str] = None) -> tuple[list[dict], list[FailureRecord]]:
        """按提供商过滤成功记录和失败记录。

        Returns:
            (records, failures) 元组。
        """
        records = (
            self._records
            if provider is None
            else [r for r in self._records if r["provider"] == provider]
        )
        failures = (
            self._failures
            if provider is None
            else [f for f in self._failures if f.provider == provider]
        )
        return records, failures

    def estimated_cost(
        self,
        provider: Optional[str] = None,
        currency: str = "cny",
    ) -> float:
        """返回指定提供商（或全部）的累计估算成本。

        Args:
            provider: 提供商名称，None 表示汇总全部。
            currency: 币种，'cny' 或 'usd'。

        Returns:
            累计成本金额（元/美元）。
        """
        total = 0.0
        for r in self._records:
            if provider is None or r["provider"] == provider:
                total += calculate_cost(r["usage"], r["provider"], currency=currency)
        return round(total, 4)

    def report(self, provider: Optional[str] = None) -> None:
        """打印成本报告到日志。

        Args:
            provider: 仅输出该提供商的汇总，None 输出全部。
        """
        logger.info("=" * 60)
        logger.info("LLM 调用成本报告")
        logger.info("=" * 60)

        records, failures = self._filter(provider)
        if not records and not failures:
            logger.info("无调用记录。")
            logger.info("=" * 60)
            return

        providers = sorted({r["provider"] for r in records})
        grand_cny = 0.0
        grand_usd = 0.0

        for prov in providers:
            prov_records = [r for r in records if r["provider"] == prov]
            prov_failures = [f for f in failures if f.provider == prov]
            n_calls = len(prov_records)
            total_prompt = sum(r["usage"].prompt_tokens for r in prov_records)
            total_comp = sum(r["usage"].completion_tokens for r in prov_records)
            total_tok = total_prompt + total_comp
            cost_cny = sum(
                calculate_cost(r["usage"], prov, currency="cny")
                for r in prov_records
            )
            cost_usd = sum(
                calculate_cost(r["usage"], prov, currency="usd")
                for r in prov_records
            )
            grand_cny += cost_cny
            grand_usd += cost_usd

            logger.info("提供商: %s", prov)
            logger.info("  调用次数: %d", n_calls)
            logger.info("  失败次数: %d", len(prov_failures))
            logger.info("  总 Token: %d（输入 %d / 输出 %d）",
                        total_tok, total_prompt, total_comp)
            logger.info("  估算成本: ¥%.4f（USD $%.4f）", cost_cny, cost_usd)

        logger.info("-" * 60)
        logger.info("总计成本: ¥%.4f（USD $%.4f）", grand_cny, grand_usd)
        logger.info("=" * 60)

    def save_report(self, filepath: str, provider: Optional[str] = None) -> None:
        """将成本报告保存为 JSON 文件。

        Args:
            filepath: 输出文件路径（建议 .json）。
            provider: 仅保存该提供商的记录，None 保存全部。
        """
        records, failures = self._filter(provider)

        if not records and not failures:
            data = {
                "total_calls": 0,
                "total_failures": 0,
                "total_cost_cny": 0.0,
                "total_cost_usd": 0.0,
                "records": [],
                "failures": [],
            }
        else:
            providers = sorted({r["provider"] for r in records} | {f.provider for f in failures})
            per_provider = []
            total_cny = 0.0
            total_usd = 0.0

            for prov in providers:
                prov_records = [r for r in records if r["provider"] == prov]
                prov_failures = [f for f in failures if f.provider == prov]
                prompt = sum(r["usage"].prompt_tokens for r in prov_records)
                comp = sum(r["usage"].completion_tokens for r in prov_records)
                cost_cny = sum(
                    calculate_cost(r["usage"], prov, currency="cny")
                    for r in prov_records
                )
                cost_usd = sum(
                    calculate_cost(r["usage"], prov, currency="usd")
                    for r in prov_records
                )
                total_cny += cost_cny
                total_usd += cost_usd

                per_provider.append({
                    "provider": prov,
                    "calls": len(prov_records),
                    "failures": len(prov_failures),
                    "prompt_tokens": prompt,
                    "completion_tokens": comp,
                    "total_tokens": prompt + comp,
                    "cost_cny": round(cost_cny, 4),
                    "cost_usd": round(cost_usd, 4),
                })

            data = {
                "total_calls": len(records),
                "total_failures": len(failures),
                "total_cost_cny": round(total_cny, 4),
                "total_cost_usd": round(total_usd, 4),
                "providers": per_provider,
                "records": [
                    {
                        "provider": r["provider"],
                        "timestamp": r["timestamp"],
                        "prompt_tokens": r["usage"].prompt_tokens,
                        "completion_tokens": r["usage"].completion_tokens,
                        "total_tokens": r["usage"].total_tokens,
                        "cost_cny": round(
                            calculate_cost(r["usage"], r["provider"], currency="cny"), 8
                        ),
                        "cost_usd": round(
                            calculate_cost(r["usage"], r["provider"], currency="usd"), 8
                        ),
                    }
                    for r in records
                ],
                "failures": [
                    {
                        "provider": f.provider,
                        "exception": f.exception,
                        "attempt": f.attempt,
                        "timestamp": f.timestamp,
                    }
                    for f in failures
                ],
            }

        with open(filepath, "w", encoding="utf-8") as f:
            import json
            json.dump(data, f, ensure_ascii=False, indent=2)

        logger.info("成本报告已保存至: %s", filepath)


# 全局追踪器实例，Pipeline 结束时可通过 model_client.tracker.report() 输出报告
tracker = CostTracker()


# ---------------------------------------------------------------------------
# 便捷函数
# ---------------------------------------------------------------------------


def quick_chat(
    prompt: str,
    system_prompt: Optional[str] = None,
    provider_name: Optional[str] = None,
    **kwargs,
) -> LLMResponse:
    """一键快速对话。

    返回 LLMResponse 而非纯文本，调用方可通过 .content 取文本，
    通过 .usage 获取用量统计、.provider / .model 获取来源信息。

    Args:
        prompt: 用户消息内容。
        system_prompt: 可选的系统提示词。
        provider_name: 提供商名称（默认读取 LLM_PROVIDER 环境变量）。
        **kwargs: 传递给 chat_with_retry() 的额外参数。

    Returns:
        LLMResponse（含 content、usage、provider、model）。
    """
    provider_name = provider_name or os.environ.get("LLM_PROVIDER", "deepseek")
    provider = OpenAICompatibleProvider(provider_name=provider_name)

    messages: list[dict] = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    try:
        return chat_with_retry(provider, messages, **kwargs)
    finally:
        provider.close()


# ---------------------------------------------------------------------------
# 测试 / 演示
# ---------------------------------------------------------------------------
"""
# 安装依赖（httpx 发请求，python-dotenv 读 .env 文件）
pip install httpx python-dotenv

# 配置环境变量（或写入 .env 文件）
export LLM_PROVIDER=deepseek
export DEEPSEEK_API_KEY=你的密钥

# 运行测试
python pipeline/model_client.py

"""
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    provider = os.environ.get("LLM_PROVIDER", "deepseek")
    logger.info("当前提供商: %s", provider)

    # 做两次调用
    try:
        result1 = quick_chat("用一句话介绍 Python")
        print(f"回复 1: {result1.content[:80]}")

        result2 = quick_chat("用一句话介绍 JavaScript")
        print(f"回复 2: {result2.content[:80]}")

        # 验证 tracker 自动记录了两条
        assert len(tracker._records) == 2, (
            f"期望 2 条记录，实际 {len(tracker._records)}"
        )
        print(f"\n调用次数: {len(tracker._records)}")
        cost = tracker.estimated_cost(currency='cny')
        print(f"总成本: CNY {cost:.4f}")
        print()

    except RuntimeError as e:
        logger.error("LLM 调用失败: %s", e)
        print("\n请检查 .env 文件中的 API Key 配置。")
    except ValueError as e:
        logger.error("参数错误: %s", e)
        print(f"\n{e}")

    # 打印成本报告
    tracker.report()

    # 保存成本报告到文件（可选）
    tracker.save_report("cost_report.json")
    print("\n成本报告已保存到 cost_report.json")
