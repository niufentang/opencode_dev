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
import re
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional

import httpx
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# 自动读取 .env 文件到环境变量，后续 os.environ.get() 可直接取值
load_dotenv()


# ---------------------------------------------------------------------------
# 数据模型
# ---------------------------------------------------------------------------


@dataclass
class Usage:
    """LLM API 调用的 token 用量统计。

    Attributes:
        prompt_tokens: 提示（输入）的 token 数。
        completion_tokens: 补全（输出）的 token 数。
        total_tokens: 总 token 数。
    """
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


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
            logger.warning(
                "未找到 %s 的 API 密钥（环境变量: %s）",
                provider_name,
                cfg["env_key"],
            )
        self.base_url = (base_url or cfg["base_url"]).rstrip("/")
        # 模型选择优先级：显式传参 > 环境变量 > 配置默认值
        self.model = model or os.environ.get(cfg.get("model_env", "")) or cfg["model"]
        self.timeout = timeout

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

        # 原实现：with httpx.Client(timeout=self.timeout) — 每次新建 Client，无连接复用
        # 改为指定 limits 连接池参数，with 块结束时连接归还池而非销毁，减少高频调用开销
        pool_limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
        with httpx.Client(timeout=self.timeout, limits=pool_limits) as client:
            resp = client.post(url, json=payload, headers=headers)
            resp.raise_for_status()
            data = resp.json()

        choice = data["choices"][0]
        content = choice["message"]["content"] or ""

        usage_data = data.get("usage", {})
        usage = Usage(
            prompt_tokens=usage_data.get("prompt_tokens", 0),
            completion_tokens=usage_data.get("completion_tokens", 0),
            total_tokens=usage_data.get("total_tokens", 0),
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


def chat_with_retry(
    provider: LLMProvider,
    messages: list[dict],
    max_retries: int = 3,
    base_delay: float = 2.0,
    **kwargs,
) -> LLMResponse:
    """带指数退避重试的对话请求。

    指数退避：每次重试等待时间呈指数增长（2s → 4s → 8s），
    避免在服务端繁忙时高频重试加剧压力，给服务恢复时间。

    Args:
        provider: LLMProvider 实例。
        messages: 消息字典列表。
        max_retries: 最大重试次数（默认 3）。
        base_delay: 首次重试前的等待秒数。
        **kwargs: 传递给 provider.chat() 的额外参数。

    Returns:
        成功时的 LLMResponse。

    Raises:
        RuntimeError: 所有重试均失败时抛出。
    """
    last_exc: Optional[Exception] = None
    for attempt in range(1 + max_retries):
        try:
            return provider.chat(messages, **kwargs)
        except (httpx.HTTPError, httpx.TimeoutException) as e:
            last_exc = e
            if attempt < max_retries:
                delay = base_delay * (2**attempt)
                logger.warning(
                    "第 %d 次对话失败: %s，%.1fs 后重试...",
                    attempt + 1,
                    e,
                    delay,
                )
                time.sleep(delay)
            else:
                logger.error("全部 %d 次对话均失败。", 1 + max_retries)

    raise RuntimeError(
        f"对话失败，已重试 {1 + max_retries} 次"
    ) from last_exc


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
        total_tokens=prompt_tokens + estimated_output_tokens,
    )
    return calculate_cost(usage, provider_name, currency=currency)


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

    return chat_with_retry(provider, messages, **kwargs)


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

    chosen = os.environ.get("LLM_PROVIDER", "deepseek")
    logger.info("当前提供商: %s", chosen)

    # 1. 基础对话测试
    provider = OpenAICompatibleProvider(provider_name=chosen)
    msgs = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": 'Say "Hello from model_client.py" in 5 words.'},
    ]

    try:
        resp = chat_with_retry(provider, msgs)
        logger.info("响应: %s", resp.content)
        logger.info("用量: %s", resp.usage)
        logger.info("费用: $%.8f", calculate_cost(resp.usage, chosen))
    except RuntimeError as e:
        logger.error("对话失败: %s", e)

    # 2. Token 估算演示
    sample = "Hello world, this is a test message with some Chinese: \u4f60\u597d\u4e16\u754c"
    logger.info(
        "文本 \"%s\" 的估算 token 数: %d", sample, estimate_tokens(sample)
    )

    # 3. 费用预估演示
    est_cost = estimate_message_cost(msgs, chosen, estimated_output_tokens=100)
    logger.info("预估消息费用: $%.8f", est_cost)

    # 4. quick_chat 演示
    try:
        reply = quick_chat("Say hi in 3 words.", system_prompt="Be concise.")
        logger.info("quick_chat 回复: %s", reply.content)
        logger.info("quick_chat 用量: %s", reply.usage)
    except RuntimeError as e:
        logger.error("quick_chat 失败: %s", e)
