"""Tests for model_client retry logic."""

import time
from unittest.mock import MagicMock, patch

import httpx
import pytest

from pipeline.model_client import (
    LLMResponse,
    FailureRecord,
    JitterStrategy,
    RetryConfig,
    Usage,
    _apply_jitter,
    _default_total_timeout,
    _is_retryable,
    chat_with_retry,
    tracker,
)


@pytest.fixture(autouse=True)
def reset_tracker():
    tracker._records.clear()
    tracker._failures.clear()
    yield


def make_mock_provider(config: RetryConfig | None = None, timeout: int = 60):
    provider = MagicMock()
    provider.provider_name = "deepseek"
    provider.model = "test-model"
    provider.timeout = timeout
    provider.retry_config = config
    return provider


# ---------------------------------------------------------------------------
# 1.1-1.2: JitterStrategy & _is_retryable
# ---------------------------------------------------------------------------


class TestIsRetryable:
    def test_retryable_timeout(self):
        exc = httpx.TimeoutException("timeout", request=MagicMock())
        assert _is_retryable(exc) is True

    def test_retryable_connect_error(self):
        exc = httpx.ConnectError("connection refused", request=MagicMock())
        assert _is_retryable(exc) is True

    @pytest.mark.parametrize("code", [429, 500, 502, 503, 504])
    def test_retryable_http_status(self, code):
        resp = MagicMock()
        resp.status_code = code
        exc = httpx.HTTPStatusError("error", request=MagicMock(), response=resp)
        assert _is_retryable(exc) is True

    @pytest.mark.parametrize("code", [400, 401, 403, 413])
    def test_non_retryable_http_status(self, code):
        resp = MagicMock()
        resp.status_code = code
        exc = httpx.HTTPStatusError("error", request=MagicMock(), response=resp)
        assert _is_retryable(exc) is False

    def test_non_retryable_generic(self):
        exc = ValueError("bad input")
        assert _is_retryable(exc) is False


# ---------------------------------------------------------------------------
# 1.4: JitterStrategy unknown value
# ---------------------------------------------------------------------------


class TestJitterStrategy:
    def test_unknown_strategy_raises(self):
        with pytest.raises(ValueError):
            JitterStrategy("unknown_strategy")


# ---------------------------------------------------------------------------
# 2: Retry logic
# ---------------------------------------------------------------------------


class TestChatWithRetry:
    def test_success_first_attempt(self):
        provider = make_mock_provider(RetryConfig())
        expected = LLMResponse(content="ok", usage=Usage(10, 20), provider="deepseek")
        provider.chat.return_value = expected

        result = chat_with_retry(provider, [{"role": "user", "content": "hi"}])

        assert result.content == "ok"
        assert result.degraded is False
        assert len(tracker._records) == 1

    def test_non_retryable_raises_immediately(self):
        provider = make_mock_provider(RetryConfig(max_attempts=3))
        resp = MagicMock()
        resp.status_code = 400
        provider.chat.side_effect = httpx.HTTPStatusError(
            "bad request", request=MagicMock(), response=resp
        )

        with pytest.raises(httpx.HTTPStatusError):
            chat_with_retry(provider, [{"role": "user", "content": "hi"}])

        assert len(tracker._failures) == 1

    def test_all_retries_exhausted_returns_degraded(self):
        provider = make_mock_provider(RetryConfig(max_attempts=2, base_delay=0.01))
        provider.chat.side_effect = httpx.TimeoutException(
            "timeout", request=MagicMock()
        )

        result = chat_with_retry(provider, [{"role": "user", "content": "hi"}])

        assert result.degraded is True
        assert result.content == ""
        assert len(tracker._failures) == 3  # attempt 0 + 1 + 2

    def test_unknown_jitter_strategy_raises_value_error(self):
        provider = make_mock_provider(
            RetryConfig(jitter_strategy="nonexistent", base_delay=0.01)
        )

        with pytest.raises(ValueError, match="未知抖动策略"):
            chat_with_retry(provider, [{"role": "user", "content": "hi"}])


# ---------------------------------------------------------------------------
# 2.2: Total timeout exhaustion
# ---------------------------------------------------------------------------


class TestTotalTimeout:
    def test_timeout_exhausted_mid_retry(self):
        config = RetryConfig(max_attempts=5, base_delay=0.5, total_timeout=0.5)
        provider = make_mock_provider(config, timeout=10)

        def slow_chat(*args, **kwargs):
            time.sleep(0.4)
            raise httpx.TimeoutException("timeout", request=MagicMock())

        provider.chat.side_effect = slow_chat

        result = chat_with_retry(provider, [{"role": "user", "content": "hi"}])

        assert result.degraded is True

    def test_adaptive_default_total_timeout(self):
        result = _default_total_timeout(httpx_timeout=60, max_attempts=3, base_delay=1.0)
        assert result == 60 * 3 + (1 + 2)


# ---------------------------------------------------------------------------
# 3: Degraded result
# ---------------------------------------------------------------------------


class TestDegradedResult:
    def test_degraded_replaces_runtime_error(self):
        provider = make_mock_provider(RetryConfig(max_attempts=1, base_delay=0.01))
        provider.chat.side_effect = httpx.TimeoutException(
            "timeout", request=MagicMock()
        )

        result = chat_with_retry(provider, [{"role": "user", "content": "hi"}])

        assert result.degraded is True
        assert result.usage.total_tokens == 0

    def test_degraded_does_not_raise(self):
        provider = make_mock_provider(RetryConfig(max_attempts=1, base_delay=0.01))
        provider.chat.side_effect = httpx.TimeoutException(
            "timeout", request=MagicMock()
        )

        chat_with_retry(provider, [{"role": "user", "content": "hi"}])


# ---------------------------------------------------------------------------
# 4: CostTracker failure recording
# ---------------------------------------------------------------------------


class TestCostTrackerFailures:
    def test_record_failure_stores_full_traceback(self):
        tracker.record_failure(
            provider="deepseek",
            exception="Traceback (most recent call last):\n  ...\nhttpx.TimeoutException",
            attempt=0,
        )
        assert len(tracker._failures) == 1
        f = tracker._failures[0]
        assert f.provider == "deepseek"
        assert "httpx.TimeoutException" in f.exception
        assert f.attempt == 0

    def test_report_includes_failure_count(self, caplog):
        import logging
        caplog.set_level(logging.INFO)
        tracker.record_failure("deepseek", "error", 0)
        tracker.record_failure("deepseek", "error", 1)
        tracker.record(Usage(prompt_tokens=10, completion_tokens=5), "deepseek")
        tracker.report()

        assert "失败次数: 2" in caplog.text

    def test_save_report_includes_failures(self, tmp_path):
        tracker.record_failure("deepseek", "TimeoutException", 0)
        tracker.record(Usage(prompt_tokens=10, completion_tokens=20), "deepseek")

        report_path = tmp_path / "report.json"
        tracker.save_report(str(report_path))

        import json
        data = json.loads(report_path.read_text(encoding="utf-8"))
        assert data["total_failures"] == 1
        assert len(data["failures"]) == 1
        assert data["failures"][0]["provider"] == "deepseek"
        assert data["failures"][0]["attempt"] == 0
