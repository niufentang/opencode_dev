# AGENTS.md — AI 知识库助手 · 项目 Memory 文件

## 项目概述

本项目是一个面向证券行业基础设施的 AI 知识库助手，自动从上交所交易技术支持专区、深交所技术服务、中国结算业务规则三大数据源爬取技术与规则文档，通过 AI 解析分析技术变更与规则变更，结构化存储为 JSON 和 Markdown，支持精确检索、版本追溯、关联发现，并通过多渠道（邮件/飞书）分发变更通知。

## 技术栈

- 语言: Python 3.12
- 框架/平台: OpenCode + 国产大模型
- 工作流: LangGraph
- 部署: OpenClaw
- 爬虫: playwright-cli
- 测试: pytest
- 格式化: ruff
- 依赖管理: pip + requirements.txt
- 版本控制: Git

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
- 文件编码统一 UTF-8

## 项目结构

```
ai-knowledge-base/
├── AGENTS.md                    # 项目 Memory 文件
├── opencode.json                — OpenCode 配置
├── .opencode/
│   ├── agents/                  — Agent 角色定义文件
│   │   ├── collector.md         — 采集 Agent 
│   │   ├── parser.md            — 解析 Agent  
│   │   ├── analyzer.md          — 分析 Agent
│   │   └── organizer.md         — 整理 Agent
│   └── skills/                  — 可复用技能包
│       ├── ...
│       └── ...
├── knowledge/
│   ├── raw/                     — 原始爬取数据（PDF/Word/ZIP/HTML，只读归档）
│   └── articles/                — 解析 + 分析 + 整理产物
│       ├── sse/                 — 上交所
│       │   ├── markdown/        — 全文转 Markdown（解析 Agent 产出）
│       │   ├── metadata/        — 元数据 JSON（解析 Agent 产出）
│       │   ├── analyzed/        — 变更分析与关联发现结果（分析 Agent 产出）
│       │   └── entries/         — 最终标准知识条目 JSON（整理 Agent 产出）
│       ├── szse/                — 深交所（同上）
│       └── chinaclear/          — 中国结算（同上）
├── pipeline/                    — 自动化流水线
├── workflows/                   — LangGraph 工作流
└── openclaw/                    — OpenClaw 部署配置
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
  "superseded_by": null,
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
| superseded_by | 被替代此条目的新条目 ID（仅 status=superseded 时有值） |
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
- 不在日志中输出 API Key 或敏感信息
- 不执行 rm -rf 等危险命令
- 不修改 AGENTS.md 本身（除非明确要求）

## 工具使用约束与能力说明
## 一、Watt Toolkit（Steam++）

### 定位
解决海外依赖（如 github OpenCode 插件）拉取问题
开源跨平台本地反向代理工具，合规加速 GitHub、Steam 等海外开发服务；不属于 VPN、不开启全局代理，仅定向优化特定域名。

### 加速原理
- 基于 YARP 实现本地反向代理，精准拦截目标海外域名流量
- 内置动态IP优选池、实时延迟测速，自动切换最优线路
- 替代手动修改 Hosts，稳定解决 GitHub 访问慢、拉取代码超时、依赖安装卡顿等问题
- 分离国内外路由，不影响国内常规网络访问
  
### 合规要求
仅用于正常开发场景下访问海外公开技术服务，禁止任何违规网络行为。

------

## 二、GitHub CLI (gh)

### 定位
对接项目版本控制、Agent 配置文件迭代流程

### 认证
```bash
# PowerShell（本项目默认）
$env:GH_TOKEN | gh auth login --with-token
# 或 cmd.exe
echo %GH_TOKEN% | gh auth login --with-token
```

### 使用规则
1. 涉及 GitHub 仓库、代码拉取、提交、推送、PR、Issue、Actions 相关操作，优先使用 gh 命令
2. 执行前确保系统环境变量 GH_TOKEN 已正确配置

### 常用命令
```bash
# 仓库
gh repo clone <repo>
gh repo create
# 代码拉取、提交、推送
git pull      # 拉取最新代码
git add .     # 添加变更
git commit -m "提交信息"  # 提交代码
git push      # 推送到远程
# Issue
gh issue list
gh issue create
# PR
gh pr list
gh pr create
gh pr checkout <num>
gh pr merge
# 帮助
gh help
```
------

## 三、Playwright CLI

### 定位
对接采集 Agent 的增量爬取、变更检测流程
端到端自动化测试工具，**可作为合法爬虫工具**，能渲染 JavaScript 动态页面、模拟浏览器操作、提取网页数据、文件下载。

### 爬虫用途
- 爬取动态渲染网站（JS 加载、Ajax、登录后页面）
- 网页数据提取、截图、PDF 导出
- 模拟点击、输入、滚动、表单提交等真人操作
  
### 项目用途
-上交所 / 深交所 / 中国结算官网动态页面爬取
-公告、PDF、文档自动下载与保存
-页面截图、变更检测

### 爬取网站常用命
```bash
# 1. 自动生成爬虫/自动化代码（最常用！）
playwright codegen https://目标网址.com
# 2. 打开浏览器访问网页（调试爬虫用）
playwright open https://目标网址.com
# 3. 网页截图（无头模式）
playwright screenshot https://目标网址.com output.png
# 4. 网页导出 PDF
playwright pdf https://目标网址.com output.pdf
# 5. 运行爬虫/自动化脚本
playwright test 脚本名.spec.js
# 6. 无头模式运行（不显示浏览器窗口，后台爬取）
playwright test --headless
# 7. 查看执行报告（含爬取日志、截图）
playwright show-report
# 8. 帮助
playwright help
```

