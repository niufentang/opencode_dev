# MCP 外部数据连接

---

## MCP 三种传输方式

| 传输方式 | 协议 | 适用场景 | 示例 |
|---------|------|---------|------|
| **stdio** | 标准输入输出 | 本地进程通信（最常用） | 本地 SQLite Server、本地文件系统 Server |
| **SSE** | Server-Sent Events（HTTP 流式） | 远程服务、需要实时推送 | 远程搜索引擎、实时数据监控 |
| **HTTP** | 标准 HTTP 请求 | 简单的远程调用、无状态请求 | REST API 封装、云服务集成 |

---

## 讨论和思考

**Skill + CLI 脚本 = MCP 的 80% 价值？**

| 方案 | 耗时 | 实现方式 |
|-----|------|---------|
| **Skill + Bash** | 20 分钟 | SKILL.md + scripts/check_deploy.sh，10 行 curl + jq 搞定 |
| **MCP 方案** | 半天到一天 | 写 Server（100+ 行 Node.js/Python），实现 tools/list、tools/call 协议，注册、调试、超时、重启 |

**分工协作：**
- **Skill 提供**：知识（什么时候用、怎么分析）
- **Bash 提供**：执行（curl 调 API、jq 解析）
- **组合 = 知识 + 执行 + 自动发现 = MCP 大部分价值**

**MCP 不可替代的场景：**
- 有状态长连接（连接池、事务）
- 复杂认证（OAuth2、mTLS）
- 同一服务 10+ 个工具
- 跨客户端复用（Cursor/Copilot）

**趋势：LLM 的理解能力正在消解结构化协议的必要性**
- Claude 能读 stderr、能解析非结构化输出
- = JSON Schema 约束的边际价值下降
