# 模型成本对比

## 测试条件

| 项目 | 值 |
|------|-----|
| 测试日期 | YYYY-MM-DD |
| 任务类型 | 文档变更分析 / 知识条目生成 / ... |
| 输入数据量 | xxx tokens（约 xxx 字符） |
| 调用次数 | xxx 次 |
| Pipeline 参数 | `--limit xxx --use-llm --llm-threshold xxx` |
| 备注 | |

## 各模型成本

### DeepSeek

| 项目 | 值 |
|------|-----|
| 模型 | `deepseek-v4-flash` |
| 单价（输入） | $0.14 / 1M tokens（¥1.0） |
| 单价（输出） | $0.28 / 1M tokens（¥2.0） |
| 总输入 tokens | xxx |
| 总输出 tokens | xxx |
| 总调用次数 | xxx |
| 总成本（USD） | $xxx.xxxx |
| 总成本（CNY） | ¥xxx.xxxx |
| 平均每次调用成本 | ¥xxx.xxxx |

### Qwen

| 项目 | 值 |
|------|-----|
| 模型 | `qwen3.6-plus` |
| 单价（输入） | $0.28 / 1M tokens（¥2.0） |
| 单价（输出） | $1.67 / 1M tokens（¥12.0） |
| 总输入 tokens | xxx |
| 总输出 tokens | xxx |
| 总调用次数 | xxx |
| 总成本（USD） | $xxx.xxxx |
| 总成本（CNY） | ¥xxx.xxxx |
| 平均每次调用成本 | ¥xxx.xxxx |

### Kimi

| 项目 | 值 |
|------|-----|
| 模型 | `kimi-k2.6` |
| 单价（输入） | $0.90 / 1M tokens（¥6.5） |
| 单价（输出） | $3.75 / 1M tokens（¥27.0） |
| 总输入 tokens | xxx |
| 总输出 tokens | xxx |
| 总调用次数 | xxx |
| 总成本（USD） | $xxx.xxxx |
| 总成本（CNY） | ¥xxx.xxxx |
| 平均每次调用成本 | ¥xxx.xxxx |

## 综合对比

| 指标 | DeepSeek | Qwen | Kimi |
|------|----------|------|------|
| 输入单价 CNY/1M | ¥1.0 | ¥2.0 | ¥6.5 |
| 输出单价 CNY/1M | ¥2.0 | ¥12.0 | ¥27.0 |
| 总调用次数 | xxx | xxx | xxx |
| 总输入 tokens | xxx | xxx | xxx |
| 总输出 tokens | xxx | xxx | xxx |
| 总成本 CNY | ¥xxx.xxxx | ¥xxx.xxxx | ¥xxx.xxxx |
| 输出质量评分 | x / 10 | x / 10 | x / 10 |
| 响应速度 | x / 10 | x / 10 | x / 10 |

## 结论

> 性价比最高：**xxx**
>
> 理由：...
>
> 建议：...

## 运行命令

```bash
# DeepSeek
python pipeline/pipeline.py --limit xxx --use-llm --llm-provider deepseek

# Qwen
python pipeline/pipeline.py --limit xxx --use-llm --llm-provider qwen

# Kimi
python pipeline/pipeline.py --limit xxx --use-llm --llm-provider kimi
```
