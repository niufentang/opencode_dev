# Memory 工程

## 第5页 — AI Memory：各编程工具的文件

| 工具 | Memory 文件 | 位置 | 格式 |
|------|-------------|------|------|
| Claude Code | CLAUDE.md | 项目根目录 | Markdown |
| OpenCode | AGENTS.md | 项目根目录 | Markdown |
| Cursor | .cursorrules | 项目根目录 | 纯文本/Markdown |
| Windsurf | .windsurfrules | 项目根目录 | 纯文本/Markdown |
| GitHub Copilot | copilot-instructions.md | .github/ | Markdown |
| Cline | .clinerules | 项目根目录 | 纯文本/Markdown |

---

## 第10页 — (AGENTS.md) 声明式配置

**AGENTS.md | Markdown**

```markdown
# AGENTS.md — 项目 Memory 文件

## 项目概述
本项目是一个 Python Web API 服务，使用 FastAPI 框架。

## 技术栈
- 语言: Python 3.12
- 框架: FastAPI + Uvicorn
- 数据库: PostgreSQL + SQLAlchemy
- 测试: pytest + httpx

## 编码规范
- 遵循 Google Python Style Guide
- 所有函数必须有 docstring
- 函数不超过 50 行
- 使用 type hints
- 变量命名: snake_case
- 禁止裸 print()，使用 logging 模块

## 项目结构
- src/api/ — API 路由
- src/models/ — 数据模型
- src/services/ — 业务逻辑
- tests/ — 测试文件
```

---

## 第13页 — Memory SDD（从规范驱动开发）

| 层级 | 文件 | 作用 | 课节 |
|------|------|------|------|
| 项目规范 | AGENTS.md | 项目的技术栈、编码规范、架构约束 | 本节（第 2 节） |
| 角色规范 | agents/*.md | 每个 Agent 的身份、权限、职责 | 第 3 节 |
| 能力规范 | skills/*/SKILL.md | 每个可复用技能的步骤和输入输出 | 第 4 节 |

---

## 第14页 — AGENTS.md 的 6 个组成部分

- **项目概述** — 一句话说清项目是什么、做什么（让 Agent 建立全局认知）
- **技术栈** — 语言、框架、数据库、测试工具等（防止 Agent 推荐错误的技术）
- **编码规范** — 命名规则、代码风格、禁止项（统一团队代码风格）
- **项目结构** — 目录布局和职责（让 Agent 知道代码该放哪里）
- **工作流程** — 提交规范、分支策略、CI/CD（与团队流程对齐）
- **特殊约束** — 安全要求、性能要求、合规要求等（守住底线红线）

---

## 第15页 — AGENTS.md 实战：编写知识库项目的 AGENTS.md

**AGENTS.md | Markdown**

```markdown
# AGENTS.md

## 项目概述
个人知识库管理系统，支持 Markdown 文档的存储、检索和 AI 问答。

## 技术栈
- 前端: Vue 3 + Vite + Element Plus
- 后端: Python 3.12 + FastAPI
- 数据库: SQLite (开发) / PostgreSQL (生产)
- 向量数据库: ChromaDB
- AI 模型: 通过 OpenAI 兼容 API 调用 DeepSeek

## 编码规范
- Python: 遵循 PEP 8，使用 ruff 格式化
- Vue: 使用 Composition API + `<script setup>` 语法
- 所有 API 端点必须有 Pydantic 请求/响应模型
- 错误处理: 使用自定义异常类，禁止裸 except

## 项目结构
- frontend/src/ — Vue 前端源码
- backend/api/ — FastAPI 路由
- backend/core/ — 核心业务逻辑
- backend/models/ — 数据模型定义
```

---

## 第16页 — Agent 编码规范注入：让 Agent 自动遵守团队规则

**AGENTS.md — 编码规范部分 | Markdown**

```markdown
## 编码规范 (详细版)

### 命名规则
- 文件名: kebab-case (如 user-service.py)
- 类名: PascalCase (如 UserService)
- 函数/变量: snake_case (如 get_user_by_id)
- 常量: UPPER_SNAKE_CASE (如 MAX_RETRY_COUNT)
- 私有方法: 前缀下划线 (如 _validate_input)

### 必须遵守
- 每个函数不超过 30 行
- 每个文件不超过 300 行
- 所有公开函数必须有 docstring (Google 风格)
- 所有 API 返回统一格式: {"code": 0, "data": ..., "msg": ""}

### 禁止事项
- 禁止使用 print() 调试，使用 logging
- 禁止 import *
- 禁止在循环中进行数据库查询 (N+1 问题)
- 禁止硬编码密钥或密码
```

---

## 第17页 — Memory 上下文管理策略：让 Agent 更高效

- **分层配置** — 根目录 AGENTS.md 放通用规则，子目录放特定规则
- **保持精简** — 控制在 500 行以内，太长反而稀释关键信息
- **优先级明确** — 最重要的规则放最前面，Agent 注意力有衰减
- **定期维护** — 随项目演进更新 Memory，过期规则及时清理
- **团队共建** — Memory 文件纳入 Code Review 流程，团队共同维护
