# AI 知识库助手

自动从上交所（SSE）交易技术支持专区、深交所（SZSE）技术服务、中国结算（ChinaClear）业务规则三大数据源爬取技术与规则文档，通过 AI 解析分析技术变更与规则变更，结构化存储为 JSON 和 Markdown，支持精确检索、版本追溯、关联发现，并通过多渠道分发变更通知。

## 架构

```
Collect (raw/) ──→ Parse ──→ Analyze ──→ Organize ──→ Save
                       │            │              │
                   markdown/   analyzed/       entries/
                   metadata/
```

**5 步流水线：**
1. **Collect** — 三大数据源增量爬取与文件下载
2. **Parse** — 异构文件（PDF/Word/ZIP/HTML）转 Markdown + 元数据
3. **Analyze** — 规则分析 + 可选 LLM 语义增强，输出变更检测与关联发现
4. **Organize** — 去重、过滤、格式化，输出标准知识条目 JSON
5. **Save** — 质量门禁校验 + 版本追溯 + 索引维护

另有**对照实验路径**（`ParserAnalyzer`）：合并解析与分析为一步，跳过中间 Markdown，直出 `_analysis.json`。

### Pipeline 数据流

```
main()
  └─ PipelineRunner.run()
       ├─ tracker._records.clear()        ← 重置成本统计
       ├─ collect step                    ← 爬取 + 下载到 knowledge/raw/
       ├─ parse step                      ← 生成 markdown/ + metadata/
       ├─ analyze step
       │    ├─ rule-based 分析
       │    └─ _llm_analyze → chat_with_retry → tracker.record()  ← LLM 语义增强
       ├─ organize step                   ← 输出 entries/
       ├─ save step                       ← 质量校验 + 版本追溯
       └─ _print_report()                 ← 报告面板（含 LLM cost 行）
  ├─ tracker.report()                     ← 日志输出详细成本报告
  └─ tracker.save_report()                ← JSON 落盘 log/cost_report_*.json
```

## 快速开始

```bash
# 安装依赖
pip install httpx python-dotenv

# 配置 API 密钥（或复制 .env.example 为 .env 后填入）
cp .env.example .env

# 全量运行
python pipeline/pipeline.py

# 快速测试（limit 3 控制每栏目处理量）
python pipeline/pipeline.py --limit 3

# 启用 LLM 语义增强
python pipeline/pipeline.py --limit 3 --use-llm

# 查看帮助
python pipeline/pipeline.py --help
```

## 数据源

| 数据源 | 网站 | 栏目数 | 爬虫实现 |
|--------|------|--------|----------|
| **上交所 (SSE)** | 交易技术支持专区 | 8 栏目 | `utils/sse_tech_support_doc_api.py` |
| **深交所 (SZSE)** | 技术服务 | 5 栏目 | `utils/szse_tech_service_doc_api.py` |
| **中国结算 (ChinaClear)** | 业务规则 | 12 子类 | `utils/csdc_biz_rule_doc_api.py` |

## 项目结构

```
├── pipeline/                   # 流水线核心
│   ├── pipeline.py             # 5 步编排器（CLI 入口）
│   └── model_client.py         # 统一 LLM 调用客户端 + CostTracker
├── utils/                      # 各步骤实现
│   ├── sse_tech_support_doc_api.py
│   ├── szse_tech_service_doc_api.py
│   ├── csdc_biz_rule_doc_api.py
│   ├── parse_all.py            # 批量解析
│   ├── analyze_all.py          # 批量分析
│   ├── parse_and_analyze.py    # 解析分析合并（实验）
│   └── organize_all.py         # 批量整理
├── hooks/                      # 质量门禁
│   ├── validate_json.py        # JSON Schema 校验
│   └── check_quality.py        # 五维度质量评分
├── knowledge/                  # 数据存储
│   ├── raw/                    # 原始爬取数据（只读归档）
│   │   ├── sse/
│   │   ├── szse/
│   │   └── chinaclear/
│   └── articles/               # 解析+分析+整理产物
│       ├── sse/                # (markdown/ metadata/ analyzed/ entries/)
│       ├── szse/
│       ├── chinaclear/
│       └── parseranalyzer/     # 对照实验
├── test/                       # 爬虫验证脚本
│   ├── test_sse.py
│   ├── test_szse.py
│   └── test_csdc.py
├── doc/                        # 设计文档
├── log/                        # 运行日志
└── .opencode/                  # OpenCode Agent 配置
    ├── agents/                 # 5 个 Agent 角色定义
    └── skills/                 # 可复用技能包
```

## 知识条目 JSON 格式

最终产出的标准知识条目格式（位于 `knowledge/articles/{source}/entries/`）：

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 唯一标识：`{source}-{type}-{日期}-{序号}` |
| `type` | enum | 文档类型（technical_notice / interface_spec / business_rule / guide / software / test_doc / magazine） |
| `title` | string | 文档标题 |
| `source` | enum | 数据源（sse / szse / chinaclear） |
| `source_url` | string | 原文链接 |
| `summary` | string | AI 生成的摘要 |
| `tags` | string[] | 标签数组 |
| `status` | enum | active / deprecated / superseded |
| `version` | string | 文档版本号 |
| `public_date` | date | 发布日期 |
| `effective_date` | date | 生效日期 |
| `content_markdown` | string | 全文 Markdown 内容 |

## LLM 调用成本追踪

每次 LLM API 调用自动记录 token 消耗，Pipeline 结束时输出成本报告：

```bash
# 运行后自动输出成本报告
python pipeline/pipeline.py --limit 3 --use-llm --llm-threshold 0.95

# 报告输出到日志 + 保存到 log/cost_report_{timestamp}.json
```

`CostTracker` 全局实例支持：`tracker.report()`（打印）、`tracker.save_report(path)`（JSON 落盘）、`tracker.estimated_cost()`（查询）。

## Agent 角色

| 角色 | 职责 | 核心能力 |
|------|------|----------|
| **Collector** | 三个网站定向爬取 | 增量抓取与去重、下载排队与重试、变更检测 |
| **Parser** | 异构文件解析 | PDF/Word/ZIP 解析、HTML 提取、转 Markdown |
| **Analyzer** | 变更分析与关联发现 | 版本差异比对、废止检测、跨站关联、标签分类 |
| **Organizer** | 知识条目结构化 | 去重、过滤、格式化、版本追溯 |

## CLI 场景示例

```bash
# 仅爬取下载
python pipeline/pipeline.py --step collect --limit 10 --per-category-limit 5

# SZSE 已下载数据，直接走分析链路
python pipeline/pipeline.py --sources szse --from parse --to save

# 增量模式（跳过已完成的文件）
python pipeline/pipeline.py --incremental

# 强制 LLM 增强（调低置信度阈值）
python pipeline/pipeline.py --limit 3 --use-llm --llm-threshold 0.95

# 试运行（不写入文件）
python pipeline/pipeline.py --step save --dry-run

# 仅整理已有分析结果
python pipeline/pipeline.py --sources sse,szse --from organize
```

## 开发指南

### 编码规范

- PEP 8，使用 ruff 格式化
- snake_case 变量/函数，PascalCase 类，UPPER_SNAKE_CASE 常量
- Google 风格 docstring
- 禁止 `print()`（使用 logging）、禁止 `import *`、禁止硬编码密钥
- 函数不超过 50 行，文件不超过 500 行

### 测试

```bash
# 爬虫测试
python test/test_sse.py --category 技术通知
python test/test_szse.py --download-n 2
python test/test_csdc.py --max-pages 2
```

### 技术栈

- **语言:** Python 3.12
- **框架:** OpenCode + 国产大模型
- **爬虫:** playwright-cli + httpx
- **工作流:** LangGraph（规划中）
- **部署:** OpenClaw（规划中）
- **LLM 提供商:** DeepSeek / Qwen / Kimi（OpenAI 兼容 API 统一接入）
