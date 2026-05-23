# 模型成本对比报告

**测试日期：** 2026-05-24

## 测试条件

| 项目 | 值 |
|------|-----|
| 任务类型 | 文档变更分析（规则降级后 LLM 语义增强） |
| Pipeline 参数 | `--from analyze --limit 3 --use-llm --llm-threshold 0.95` |
| 数据源 | SSE(3) + SZSE(3) + ChinaClear(3) = 9 个 Markdown 文件 |
| 调用触发条件 | 规则分析置信度 `< 0.95` 时触发 LLM |
| 模型 | DeepSeek: `deepseek-v4-flash` |
| 备注 | 仅 DeepSeek 成功跑完；Qwen 网络超时、Kimi 协议不兼容 |

## 各模型成本

### DeepSeek ✅

| 项目 | 值 |
|------|-----|
| 模型 | `deepseek-v4-flash` |
| 单价（输入） | $0.14 / 1M tokens（¥1.0） |
| 单价（输出） | $0.28 / 1M tokens（¥2.0） |
| 规则分析文件数 | 9 |
| LLM 触发文件数 | 8（1 个文件规则置信度 ≥ 0.95，未触发 LLM） |
| 总输入 tokens | 28,805 |
| 总输出 tokens | 7,329 |
| 总 tokens | 36,134 |
| 总成本（USD） | $0.0061 |
| 总成本（CNY） | ¥0.0435 |
| 平均每次调用成本 | ¥0.0054 |

### Qwen ❌

| 项目 | 值 |
|------|-----|
| 模型 | `qwen3.6-plus` |
| 状态 | **失败** — 每次 `POST /chat/completions` 在 60 秒后 `The read operation timed out` |
| 原因 | DashScope API 可达（`GET /v1/models` 正常返回），但模型推理响应过慢，超出 httpx 默认 60s 超时。需增大 timeout 或切换为更快模型（如 `qwen3.6-flash`） |
| 建议 | 将 `model_client.py` 中 Qwen 的 `model` 改为 `qwen3.6-flash` 并重试 |

### Kimi ❌

| 项目 | 值 |
|------|-----|
| 模型 | `kimi-k2.6` |
| 状态 | **失败** — 所有请求返回 `HTTP 400 Bad Request` |
| 原因 | Moonshot API 可达（模型 `kimi-k2.6` 存在），但请求体参数与 OpenAI 兼容规格不完全一致。需检查 Moonshot API 对 `max_tokens`、`temperature` 等参数的限制 |
| 建议 | 用 Python 独立测试最小 payload 调通 Kimi 后，同步修改 `model_client.py` 的参数格式 |

## 综合对比

| 指标 | DeepSeek | Qwen | Kimi |
|------|----------|------|------|
| 单价（输入）CNY/1M | ¥1.0 | ¥2.0 | ¥6.5 |
| 单价（输出）CNY/1M | ¥2.0 | ¥12.0 | ¥27.0 |
| 是否调通 | ✅ | ❌ | ❌ |
| LLM 调用次数 | 8 | - | - |
| 总成本 CNY | ¥0.0435 | - | - |
| 平均每次调用 CNY | ¥0.0054 | - | - |
| 响应速度 | 平均 ~9s / 次 | 超时（>60s） | - |

## 结论

> **DeepSeek `deepseek-v4-flash`** 是当前唯一可用的 LLM 提供商，单次调用平均 ¥0.0054（约 0.5 分钱），性价比可接受。
>
> **Qwen** 需换用更快的模型（`qwen3.6-flash`）或增大超时时间再测。
>
> **Kimi** 需先排查 HTTP 400 的具体原因（payload 格式差异），调通后方可对比。

## 运行命令

```bash
# DeepSeek — 成功
python pipeline/pipeline.py --from analyze --limit 3 --use-llm --llm-threshold 0.95

# Qwen — 超时
python pipeline/pipeline.py --from analyze --limit 3 --use-llm --llm-threshold 0.95 --llm-provider qwen

# Kimi — 400 Bad Request
python pipeline/pipeline.py --from analyze --limit 3 --use-llm --llm-threshold 0.95 --llm-provider kimi
```
