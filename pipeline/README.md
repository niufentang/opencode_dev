# Pipeline — 知识库自动化流水线

五步编排器：**Collect → Parse → Analyze → Organize → Save**

```
pipeline/
├── __init__.py
├── pipeline.py        # 五步编排器
├── model_client.py    # LLM 统一客户端（DeepSeek/Qwen/Kimi）
└── README.md
```

## 架构概述

```
                   ┌──────────┐
  SSE/SZSE/CC     │ Collect  │  爬取元数据 + 下载文件
    ─────────────▶│ (Step 1) │─────────▶ knowledge/raw/
                   └──────────┘
                        │
                   ┌──────────┐
                   │  Parse   │  PDF/Word/HTML → Markdown + 元数据
                   │ (Step 2) │─────────▶ knowledge/articles/{source}/
                   └──────────┘         markdown/ + metadata/
                        │
                   ┌──────────┐
                   │ Analyze  │  规则分析 + 可选 LLM 语义增强
                   │ (Step 3) │─────────▶ knowledge/articles/{source}/
                   └──────────┘         analyzed/
                        │
                   ┌──────────┐
                   │ Organize │  去重、过滤、格式化 → 标准知识条目
                   │ (Step 4) │─────────▶ knowledge/articles/{source}/
                   └──────────┘         entries/
                        │
                   ┌──────────┐
                   │   Save   │  质量门禁 + 版本追溯 + 通知分发
                   │ (Step 5) │
                   └──────────┘
```

## 快速开始

```bash
# 全量运行
python pipeline/pipeline.py

# 从解析开始（爬取已完成时）
python pipeline/pipeline.py --from parse --to save

# 单步试运行
python pipeline/pipeline.py --step save --dry-run

# 增量模式（跳过已完成的文件）
python pipeline/pipeline.py --incremental
```

## CLI 参数

| 参数 | 说明 |
|------|------|
| `--sources` | 数据源，逗号分隔：sse,szse,chinaclear（默认全部） |
| `--step` | 单步执行：collect / parse / analyze / organize / save |
| `--from` / `--to` | 步范围，例如 `--from parse --to organize` |
| `--limit` | 每步最多处理文件数（Collect 时=每栏目元数据上限） |
| `--download-limit` | Collect 时总下载上限 |
| `--per-category-limit` | Collect 时每栏目最多下载文件数 |
| `--incremental` | 增量模式，跳过已完成的文件 |
| `--reset` | 重置增量状态 |
| `--use-llm` | 启用 LLM 语义增强分析 |
| `--llm-provider` | LLM 提供商：deepseek（默认）/ qwen / kimi |
| `--llm-threshold` | LLM 触发置信度阈值（默认 0.7） |
| `--skip-quality` | 跳过质量门禁 |
| `--fail-fast` | 遇错即停 |
| `--dry-run` | 试运行，不写入任何文件 |

## 场景示例

```bash
# 仅爬取下载（每栏目 10 条元数据，最多下载 5 个文件）
python pipeline/pipeline.py --step collect --limit 10 --per-category-limit 5

# SZSE 已下载数据，直接分析链路
python pipeline/pipeline.py --sources szse --from parse --to save

# 只做 Analyze → Organize（Parse 已完成时）
python pipeline/pipeline.py --sources szse --from analyze --to organize

# 启用 LLM 增强，调低置信度阈值强制更多触发
python pipeline/pipeline.py --limit 3 --use-llm --llm-threshold 0.95

# 混合：SSE 增量 + SZSE 全量
python pipeline/pipeline.py --sources sse,szse --from parse
```

## 五步详解

### Step 1: Collect — 采集

调用三个数据源的采集 API：
- **SSE**: `utils.sse_tech_support_doc_api`
- **SZSE**: `utils.szse_tech_service_doc_api`
- **ChinaClear**: `utils.csdc_biz_rule_doc_api`

- 按栏目抓取元数据，保存为 `knowledge/raw/{source}/metadata.json`
- 下载非 HTML 文件到 `knowledge/raw/{source}/{category}/`
- 支持按栏目/总数限制下载量

### Step 2: Parse — 解析

调用 `utils.parse_all`：

- 扫描 `knowledge/raw/` 中未解析的原始文件
- PDF/Word 转 Markdown → `articles/{source}/markdown/`
- 提取元数据（标题、版本、日期）→ `articles/{source}/metadata/`
- 匹配爬取元数据，补充 URL、发布时间等信息
- 计算 SHA256 文件哈希用于去重

### Step 3: Analyze — 分析

调用 `utils.analyze_all`：

- **规则通道**：基于文档格式标注（红色/蓝色文本）检测变更
- **LLM 通道**（可选）：当规则通道置信度 < 阈值时，调用大模型做语义分析
  - 支持 DeepSeek / Qwen / Kimi
  - 自动合并规则 + LLM 结果
  - Token 用量追踪和费用估算
- 输出 `_analysis.json` 到 `articles/{source}/analyzed/`

### Step 4: Organize — 整理

调用 `utils.organize_all`：

- 扫描分析结果，去重和过滤
- 格式化为标准知识条目 JSON
- 生成 `entries.json` 索引文件

### Step 5: Save — 保存与分发

- **质量门禁**：使用 `hooks.validate_json` 校验条目字段完整性
- **版本追溯**：自动构建 previous_version / superseded_by 链
- **通知分发**：预留邮件/飞书分发接口
- 输出执行报告，含 LLM 费用汇总

## LLM 客户端

`model_client.py` 提供统一的 LLM 调用接口：

- 抽象基类 `BaseProvider`，各家继承实现（DeepSeek / Qwen / Kimi）
- `chat_with_retry()`: 指数退避自动重试
- `CostTracker`: Token 用量记录与费用计算（USD / CNY）
- `quick_chat()`: 便捷单次调用

### 环境变量

| 变量 | 用途 |
|------|------|
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 |
| `DEEPSEEK_BASE_URL` | DeepSeek 接口地址（可选） |
| `QWEN_API_KEY` | 通义千问 API 密钥 |
| `MOONSHOT_API_KEY` | Kimi API 密钥 |

## 增量状态

Pipeline 在 `knowledge/.pipeline_state.json` 中维护每个文件的步完成状态：

```json
{
  "version": 1,
  "last_run": "2025-04-28T10:30:00+00:00",
  "files": {
    "knowledge/raw/sse/xxx.pdf": {
      "sha256": "abc...",
      "mtime": "",
      "steps": {
        "parse": { "done": true, "timestamp": "..." },
        "analyze": { "done": true, "timestamp": "..." }
      }
    }
  }
}
```

使用 `--incremental` 跳过已完成的文件；使用 `--reset` 重置状态。
