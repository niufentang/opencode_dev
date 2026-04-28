# AGENTS.md — AI 知识库助手 · 项目 Memory 文件

## 项目概述

本项目是一个面向证券行业基础设施的 AI 知识库助手，自动从上交所交易技术支持专区、深交所技术服务、中国结算业务规则三大数据源爬取技术与规则文档，通过 AI 解析分析技术变更与规则变更，结构化存储为 JSON 和 Markdown，支持精确检索、版本追溯、关联发现，并通过多渠道（邮件/飞书）分发变更通知。

## 技术栈

- 语言: Python 3.12
- 框架/平台: OpenCode + 国产大模型
- 工作流: LangGraph
- 爬虫: OpenClaw
- 测试: pytest
- 格式化: ruff

## 编码规范

- 遵循 PEP 8，使用 ruff 格式化
- 变量/函数命名: snake_case
- 类命名: PascalCase
- 常量命名: UPPER_SNAKE_CASE
- 所有公开函数必须有 Google 风格 docstring
- 禁止裸 print()，使用 logging 模块
- 禁止 import *
- 禁止硬编码密钥、密码或 URL
- 函数不超过 50 行，文件不超过 500 行
- 所有异常使用自定义异常类，禁止裸 except

## 项目结构

```
.opencode/
  agents/               # Agent 定义文件
  skills/               # 可复用技能定义
knowledge/
  raw/                  # 原始爬取数据（PDF/Word/ZIP/HTML）
  articles/             # 结构化知识条目（JSON + Markdown）
```

### 知识条目 JSON 格式

```json
{
  "id": "sse-tech-20250428-001",
  "type": "technical_notice",
  "title": "关于xx接口规范V3.2发布的通知",
  "source": "sse",
  "source_url": "https://www.sse.com.cn/...",
  "summary": "本次更新主要调整了xx字段的长度限制...",
  "tags": ["接口规范", "V3.2", "交易系统"],
  "status": "active",
  "version": "3.2",
  "previous_version": "3.1",
  "public_date": "2025-04-28",
  "crawl_date": "2025-04-28T10:30:00",
  "effective_date": "2025-05-15",
  "deprecated_date": null,
  "related_ids": ["csdc-rule-20250420-015"],
  "file_format": "pdf",
  "file_hash": "sha256:abc123...",
  "content_markdown": "# ...全文Markdown..."
}
```

| 字段 | 说明 |
|------|------|
| id | 唯一标识：`{source}-{type}-{日期}-{序号}` |
| type | 文档类型：technical_notice / interface_spec / business_rule / guide / software / test_doc / magazine |
| title | 文档标题 |
| source | 数据源：sse / szse / chinaclear |
| source_url | 原文链接 |
| summary | AI 生成的摘要 |
| tags | 标签数组，支持自动分类 |
| status | active / deprecated / superseded |
| version | 文档版本号 |
| previous_version | 上一版本号（用于追溯） |
| public_date | 发布日期 |
| crawl_date | 采集时间 |
| effective_date | 生效日期 |
| deprecated_date | 废止日期（status=deprecated 时必填） |
| related_ids | 关联知识条目 ID 列表 |
| file_format | 原始格式：html / pdf / doc / docx / zip |
| file_hash | 文件哈希（去重校验） |
| content_markdown | 全文 Markdown 内容 |

## Agent 角色概览

| 角色 | 职责 | 核心能力 |
|------|------|----------|
| **采集 Agent** | 三个网站定向爬取 | 增量抓取与去重、下载排队与重试、变更检测 Trigger |
| **解析 Agent** | 异构文件解析 | PDF/Word/ZIP 解析、HTML 结构化提取、全文转 Markdown、元数据抽取 |
| **分析 Agent** | 变更分析与关联发现 | 技术变更和规则变更分析、版本差异比对、废止/替代检测、跨站关联发现、标签自动分类 |
| **整理 Agent** | 知识条目结构化 | 分析后原始数据去重、过滤、格式化，输出为标准知识条目 JSON |

## 红线（绝对禁止）

- 禁止对爬取目标网站发起高频请求（必须遵守合理的请求间隔和限速策略）
- 禁止爬取或存储非公开/需登录的内容
- 禁止删除或修改原始爬取数据
- 禁止跳过版本差异比对直接覆盖已有知识条目
- 禁止在未标记废止状态的情况下替换旧版本条目
- 禁止将敏感或未公开的规则信息通过分发渠道外泄
- 禁止使用未经团队审核的自定义爬虫规则
