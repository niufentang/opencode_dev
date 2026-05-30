## Context

当前知识库以 JSON 条目文件（`knowledge/articles/{sse,szse,chinaclear}/entries/*.json`）存储在本地，共约 230 条目 / ~5MB 数据。AI Agent 访问知识库的唯一方式是通过预配置的 Skill + Bash grep，无法被通用 MCP 客户端发现和使用，且搜索能力仅限于子串匹配。

需要一个标准的 MCP Server 作为知识库的统一访问入口，通过 JSON-RPC 2.0 over stdio 协议暴露搜索、检索、统计能力。

## Goals / Non-Goals

**Goals:**
- 实现符合 MCP 协议的 stdio Server，支持 initialize / tools/list / tools/call / ping
- 提供 4 个 MCP 工具：search_articles、get_article、get_article_content、knowledge_stats
- 引入 jieba 分词 + 倒排索引，提升中文搜索精度
- 支持同义词扩展（ETF ↔ 交易型开放式指数基金）
- 支持 MCP Resources 协议（resources/list + resources/read），以 `knowledge://` URI 暴露条目
- 启动时全量加载数据到内存，search 响应时间 < 10ms
- 单元测试 + 集成测试覆盖核心场景

**Non-Goals:**
- 不做知识库写入/修改（只读访问）
- 不做文件变更热更新（需重启 Server 感知新条目）
- 不做向量检索或语义搜索（Tier 0 阶段）
- 不做分布式部署（单进程 stdio 模式）

## Decisions

- **单文件架构**：整个 Server 放在 `mcp_knowledge_server.py`（~400 行），最小心智负担。后续条目 > 1000 时再拆出 `data_layer.py`
- **jieba 分词 + 倒排索引**：替代 grep 子串匹配。jieba 是纯 Python 中文分词行业标准，无外部系统依赖。构建索引时对 title + summary + tags + content_markdown 分词，确保全文可检索
- **全量内存加载**：当前 ~5MB 数据 + ~15MB 全文倒排索引，启动后常驻内存。搜索 O(log n)，get_article O(1)。后续条目 > 5000 时将索引从内存迁移到 SQLite
- **stdio 传输层**：标准 MCP 协议方式，无需 HTTP 服务、端口监听。日志输出到 stderr 不污染协议流
- **resources 补充暴露**：除 tools 外同步实现 resources/list + resources/read，让通用 MCP 客户端也能浏览知识库
- **requirements-mcp.txt 独立文件**：避免污染主项目的 requirements.txt，jieba 是 MCP Server 独有依赖

## Deployment

MCP Server 通过 opencode.json 的 `mcpServers` 段注册，由 OpenCode 按需启动。

```json
{
  "mcpServers": {
    "knowledge-base": {
      "command": "python",
      "args": ["mcp_knowledge_server.py"],
      "env": {
        "LOG_LEVEL": "INFO",
        "SYNONYM_FILE": ""
      }
    }
  }
}
```

**环境变量接口：**

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `LOG_LEVEL` | `INFO` | 日志级别：DEBUG / INFO / WARNING / ERROR |
| `SYNONYM_FILE` | `""` | 外部同义词表 JSON 文件路径，为空则使用内置映射 |
| `KNOWLEDGE_DIR` | `./knowledge/articles` | 知识条目根目录，可覆盖以支持非标准部署路径 |

**启动约束：**

- CWD 必须为项目根目录（包含 `knowledge/` 的目录），或通过 `KNOWLEDGE_DIR` 指定
- 依赖 `jieba`，需先执行 `pip install -r requirements-mcp.txt`
- 仅支持 stdio 传输（单进程模式），不监听端口

**启动校验：**
- 扫描 `KNOWLEDGE_DIR` 下的所有 `entries/*.json`
- 若加载到 0 条条目，输出 WARNING 日志（含可能原因：目录不存在/为空/JSON 格式全部错误）后继续启动，不阻塞
- 若部分 JSON 文件解析失败，输出 ERROR 日志（含文件名和具体异常）并跳过该文件

## Risks / Trade-offs

- **全量内存加载在条目增长后不可持续**：当前 ~5MB + ~15MB 索引无压力。达到 5000 条目 / ~200MB 时需将索引从内存迁移到 SQLite（设计文档已有 Tier 1 方案）
- **jieba 分词无语义相关性**：纯词频匹配，无法理解"申购赎回规则"与"认购/申赎"的语义关系。后续可按需升级至 Meilisearch（Tier 3）
- **同义词表以自动挖掘为主，硬编码补充**：启动时从现有条目的 tags 和带有英文括号注释的摘要中自动扫描映射（如"交易型开放式指数基金（ETF）"），再补充 ~20 组硬编码高频术语映射。支持通过环境变量 `SYNONYM_FILE` 外部覆盖
- **无增量更新**：Server 运行中知识库新增条目需重启才能感知，可通过 watchdog 或定期轮询解决（Tier 1+）
