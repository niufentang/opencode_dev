# MCP Knowledge Server 设计方案

> 编写日期：2026-05-14
> 状态：方案评估，待决策

---

## 一、需求概要

构建一个 **MCP Server（mcp_knowledge_server.py）**，将本地知识库（`knowledge/articles/sse|szse|chinaclear/entries/*.json`）通过 MCP 协议暴露给 AI 工具，提供搜索、查询、统计三大能力。

数据现状：
| 数据源 | entries 数 | 单文件大小 | 总数据量 |
|--------|-----------|-----------|---------|
| sse | 171 | ~5-50KB | ~3-5MB |
| szse | 60 | ~5-50KB | ~1-2MB |
| chinaclear | 0 | — | — |

---

## 二、架构设计

### 2.1 整体架构

```
AI 工具（OpenCode / Cursor）
        ↕ JSON-RPC 2.0 over stdio
┌──────────────────────────────────┐
│      mcp_knowledge_server.py      │
│  ┌────────────────────────────┐  │
│  │   Transport Layer (stdio)  │  │
│  │   ─ 读取 stdin            │  │
│  │   ─ 写入 stdout           │  │
│  │   ─ 日志写入 stderr       │  │
│  └──────────┬─────────────────┘  │
│             │ dispatcher         │
│  ┌──────────▼─────────────────┐  │
│  │   MCP Protocol Handler     │  │
│  │   ─ initialize             │  │
│  │   ─ tools/list             │  │
│  │   ─ tools/call             │  │
│  └──────────┬─────────────────┘  │
│             │                    │
│  ┌──────────▼─────────────────┐  │
│  │   Knowledge Engine         │  │
│  │   ─ search_articles()      │  │
│  │   ─ get_article()          │  │
│  │   ─ knowledge_stats()      │  │
│  └──────────┬─────────────────┘  │
│             │                    │
│  ┌──────────▼─────────────────┐  │
│  │   Data Layer               │  │
│  │   ─ 启动时扫描加载所有 JSON │  │
│  │   ─ 内存 dict 缓存          │  │
│  │   ─ {source}/entries/*.json │  │
│  └────────────────────────────┘  │
└──────────────────────────────────┘
```

### 2.2 启动行为

```
启动 → 扫描 knowledge/articles/{sse,szse,chinaclear}/entries/ → 排除 entries.json
     → 加载所有 *.json → 构建内存索引 (dict[doc_id, entry])
     → 监听 stdin → 等待 MCP initialize 消息
```

### 2.3 关键设计决策

| 决策 | 选择 | 理由 |
|------|------|------|
| **数据加载时机** | 启动时全量加载到内存 | 仅 ~230 条目 / ~5MB，内存友好；避免每次搜索都 IO |
| **搜索实现** | jieba 分词 + 倒排索引 + 同义词表 | 中文需要分词才能有效检索；倒排索引提供 O(log n) 查询 |
| **搜索范围** | title + summary + tags + content_markdown，基于倒排索引 | 分词后统一建索引，不区分字段优先级 |
| **第三方依赖** | 仅 `jieba`（纯 Python，~15MB） | 中文搜索的行业标准轻量方案，无额外系统依赖 |
| **stderr 日志** | 标准 logging，仅输出到 stderr | MCP stdio 协议规范：stdout 走协议，stderr 走日志 |
| **协议解析** | 逐行读取 stdin 完整 JSON 行，`json.loads` 解析 | 标准 MCP stdio 实现方式 |
| **进程生命周期** | 单次 request → response 循环，EOF 退出；支持 SIGTERM/SIGINT graceful shutdown | MCP stdio 标准模式 |
| **可观测性** | 日志级别可配（LOG_LEVEL），请求追踪（request_id），启动统计 | stderr 标准日志，不污染 stdout 协议流 |

---

## 三、MCP 协议实现

### 3.1 支持的 MCP 方法

#### ping

MCP 协议要求支持 `ping` 用于健康检查。Server 收到 `ping` 请求后返回空 `result`。

Request:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "ping"
}
```

Response:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {}
}
```

#### resources/list 和 resources/read（可选，建议实现）

除了暴露工具，MCP 协议还支持将知识条目以 **Resource URI** 形式暴露，AI 客户端可以像浏览文件系统一样浏览知识库。

Resource URI 格式：
```
knowledge://{source}/entries/{doc_id}
```

示例：
```
knowledge://sse/entries/sse-tech-20250428-001
knowledge://szse/entries/szse-iface-20250512-103
```

`resources/list` 返回所有可用的 resource URI 列表（可分页），`resources/read` 按 URI 返回对应条目的完整内容。此方案比 `get_article` tool 更符合 MCP 协议惯用法，且让不感知 tool 名的通用 MCP 客户端也能访问知识库。

建议：保留 `get_article` tool 作为工具入口，同时实现 `resources/list` 和 `resources/read` 作为补充暴露方式。

### 3.2 协议方法详情

#### initialize

Request:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {"name": "opencode", "version": "1.0.0"}
  }
}
```

Response:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {"tools": {}},
    "serverInfo": {"name": "mcp-knowledge-server", "version": "0.1.0"}
  }
}
```

#### tools/list

Response:
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "tools": [
      {
        "name": "search_articles",
        "description": "按关键词搜索知识库文章（基于 jieba 分词 + 倒排索引，支持中英文混合搜索）",
        "inputSchema": {
          "type": "object",
          "properties": {
            "keyword": {"type": "string", "description": "搜索关键词"},
            "limit": {"type": "number", "description": "最大返回条数，默认 5，最大 50"},
            "source": {"type": "string", "description": "限定数据源：sse / szse / chinaclear，不传则搜索全部"}
          },
          "required": ["keyword"]
        }
      },
      {
        "name": "get_article",
        "description": "按文章 ID 获取文章元数据（不含全文），返回字符数信息",
        "inputSchema": {
          "type": "object",
          "properties": {
            "article_id": {"type": "string", "description": "文章 ID，如 sse-tech-20250428-001"}
          },
          "required": ["article_id"]
        }
      },
      {
        "name": "get_article_content",
        "description": "分页获取文章全文 Markdown 内容（配合 get_article 使用）",
        "inputSchema": {
          "type": "object",
          "properties": {
            "article_id": {"type": "string", "description": "文章 ID"},
            "offset": {"type": "number", "description": "字符偏移量，默认 0"},
            "limit": {"type": "number", "description": "返回字符数，默认 3000，最大 10000"}
          },
          "required": ["article_id"]
        }
      },
      {
        "name": "knowledge_stats",
        "description": "获取知识库统计信息：总数、来源分布、类型分布、热门标签",
        "inputSchema": {
          "type": "object",
          "properties": {}
        }
      }
    ]
  }
}
```

#### tools/call

Request 示例（search_articles）：
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "search_articles",
    "arguments": {"keyword": "ETF", "limit": 3, "source": "sse"}
  }
}
```

Response 示例：
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "找到 5 条结果：\n\n1. sse-tech-00000000-032\n   标题：关于TXT版ETF定义文件上传功能下线的通知\n   来源：sse | 类型：technical_notice\n   标签：sse, technical_notice, 证通云盘\n   摘要：初始版本，无历史变更。\n---"
      }
    ]
  }
}
```

Request 示例（get_article_content 分页拉取全文）：
```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "tools/call",
  "params": {
    "name": "get_article_content",
    "arguments": {"article_id": "sse-tech-20250428-001", "offset": 0, "limit": 3000}
  }
}
```

Response 示例：
```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "# 正文内容前 3000 字符...\n[全文共 12400 字符，已返回第 0-3000 字符]"
      }
    ]
  }
}
```

---

## 四、四个 MCP 工具详细设计

### 4.1 search_articles(keyword, limit=5, source=null)

| 项目 | 说明 |
|------|------|
| **入参** | `keyword: str`（必填），`limit: int`（可选，默认 5，最大 50），`source: str`（可选，'sse' / 'szse' / 'chinaclear'，不传则搜索全部） |
| **搜索范围** | title + summary + tags + content_markdown，基于倒排索引快速定位 |
| **匹配逻辑** | 1. 对 keyword 进行 jieba 分词，得到关键词列表<br>2. 在倒排索引中查找每个词，合并命中结果并按命中次数排序<br>3. 命中次数相同时按 id 字母序 |
| **返回** | 格式化文本：序号、ID、标题、来源、类型、标签、摘要截断（120 字） |
| **空结果** | 返回 `"未找到匹配文章"` |

**搜索实现方案：**

采用 **jieba 分词 + 倒排索引**，替代纯 `in` 匹配。构建方式：

```python
from collections import defaultdict
import jieba

# 启动时构建倒排索引（开箱即用，无外部依赖）
inverted_index = defaultdict(list)  # word → [(doc_id, field_type), ...]
for entry in entries:
    text = f'{entry["title"]} {entry.get("summary", "")} {" ".join(entry.get("tags", []))}'
    words = set(jieba.lcut(text))
    for w in words:
        inverted_index[w].append(entry["id"])
```

搜索时先分词，再取交集 / 并集查询倒排索引。此方案解决中文场景的核心痛点：
- "交易型开放式指数基金" 与 "ETF" 可通过同义词表关联
- "涨跌幅限制" 分词后可与 "涨跌停" 部分匹配
- 英文词（IS101, ETF）原词保留，不影响英文搜索

**同义词表配置（可选增强）：**

```python
SYNONYM_MAP = {
    "交易型开放式指数基金": ["etf", "ETF"],
    "涨跌幅限制": ["涨跌停", "涨跌幅"],
    "接口规格说明书": ["is", "接口规范"],
}
```

搜索 keyword 命中同义词表时，自动扩展搜索词列表，无需改造索引结构。

### 4.2 get_article(article_id)

| 项目 | 说明 |
|------|------|
| **入参** | `article_id: str`（必填） |
| **查找方式** | 内存 dict 直接 O(1) 查找 |
| **返回** | 文章元数据（所有 JSON 字段，不含 content_markdown），标注全文总字符数 |
| **not found** | 返回 `"未找到文章: {article_id}"` |
| **content_markdown 处理** | 不再直接附带全文；如需全文内容，调用 `get_article_content` 分页拉取 |

### 4.3 get_article_content(article_id, offset=0, limit=3000)

| 项目 | 说明 |
|------|------|
| **入参** | `article_id: str`（必填），`offset: int`（可选，默认 0），`limit: int`（可选，默认 3000，最大 10000） |
| **查找方式** | 内存 dict 直接 O(1) 查找 |
| **返回** | content_markdown 的 `[offset:offset+limit]` 切片，末尾标注 `[全文共 N 字符，已返回 offset-offset+len]` |
| **not found** | 返回 `"未找到文章: {article_id}"` |
| **边界处理** | - offset < 0 时自动设为 0<br>- limit 超过剩余长度时自动截断<br>- 返回 `content_markdown` 时去掉尾部 `<metadata>...</metadata>` 块 |

### 4.4 knowledge_stats()

| 项目 | 说明 |
|------|------|
| **入参** | 无 |
| **计算方式** | 实时从内存数据聚合 |
| **返回内容** | - 总文章数<br>- 按 source 分布（sse / szse / chinaclear）<br>- 按 type 分布（technical_notice / interface_spec / guide / …）<br>- 按 status 分布（active / superseded / deprecated）<br>- Top 10 热门标签（按出现频次排序）<br>- 最近更新的 5 篇文章（按 crawl_date 或 id 日期排序） |
| **返回格式** | 格式化文本 |

---

## 五、文件结构

```
ai-knowledge-base/
├── mcp_knowledge_server.py      ← MCP Server 主文件（单文件，~400 行）
├── tests/
│   └── test_mcp_server.py       ← 单元测试 + 集成测试
├── knowledge/articles/
│   ├── sse/entries/*.json       ← 数据源（只读）
│   └── szse/entries/*.json
├── requirements-mcp.txt         ← jieba 依赖声明
└── doc/
    └── mcp_knowledge_server_plan.md  ← 本方案文档
```

单文件设计理由：
- 最小依赖：仅引入 `jieba`（纯 Python，成熟稳定）
- ~400 行，适合单文件维护
- 降低部署心智负担（`pip install jieba && python mcp_knowledge_server.py` 即可运行）

---

## 六、错误处理

| 场景 | 处理方式 |
|------|---------|
| knowledge 目录不存在 | 启动时告警到 stderr，仍正常启动（online 但有 0 条数据） |
| 某个 JSON 文件解析失败 | 跳过该文件，stderr 记录错误路径和原因 |
| tools/call 传入未知 tool name | 返回 JSON-RPC 错误码 `-32601` (Method not found) |
| tools/call 缺少必填参数 | 返回 JSON-RPC 错误码 `-32602` (Invalid params) |
| stdin 读取到无效 JSON | 返回 JSON-RPC 错误码 `-32700` (Parse error) |
| 搜索 keyword 为空字符串 | 返回 `"keyword 不能为空"` |
| get_article ID 格式不合法 | 返回提示信息，而非直接抛异常 |
| search_articles keyword 过短（< 2 字符） | 仅搜索 title + summary，不触发全文搜索，避免噪声过多 |
| get_article_content offset 超出范围 | 自动截断为有效范围，返回空字符串 + 字符数标注 |
| content_markdown 分页拉取 | 通过 `get_article_content` 分页拉取，不再一刀切截断 |
| 进程信号退出 | 详见下方 **6.1 Graceful Shutdown** |

### 6.1 Graceful Shutdown

捕获 `SIGTERM` / `SIGINT` 信号，确保进程退出前完成日志 flush 和资源清理：

```python
import signal

def _handle_shutdown(signum, frame):
    logging.info("收到关闭信号 %s, MCP Knowledge Server 退出", signum)
    sys.exit(0)

signal.signal(signal.SIGTERM, _handle_shutdown)
signal.signal(signal.SIGINT, _handle_shutdown)
```

### 6.2 可观测性

| 项目 | 说明 |
|------|------|
| **日志输出** | 使用标准 `logging` 模块，全部输出到 stderr（不污染 stdout 协议流） |
| **日志级别控制** | 支持环境变量 `LOG_LEVEL=DEBUG|INFO|WARN|ERROR`，默认 INFO |
| **启动统计** | 启动时打印：已加载条目数、数据源分布、总内存占用估算 |
| **请求追踪** | 每条 request 打上递增 `request_id`，跨日志行关联，便于调试 |
| **性能指标** | 可选 `--stats` 启动参数，定期（每 100 次请求）打印：总请求数、平均响应时间、工具调用分布 |

---

## 七、测试方案

### 7.1 单元测试

mock stdin/stdout，验证 JSON-RPC request/response 的匹配和工具行为：

```python
import json
import subprocess
import pytest

@pytest.fixture
def server():
    proc = subprocess.Popen(
        ["python", "mcp_knowledge_server.py"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    yield proc
    proc.terminate()
    proc.wait()

def _send(proc, msg: dict) -> dict:
    proc.stdin.write((json.dumps(msg, ensure_ascii=False) + "\n").encode())
    proc.stdin.flush()
    return json.loads(proc.stdout.readline().decode())

def test_initialize(server):
    resp = _send(server, {
        "jsonrpc": "2.0", "id": 1, "method": "initialize",
        "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {}}
    })
    assert resp["result"]["serverInfo"]["name"] == "mcp-knowledge-server"

def test_tools_list(server):
    resp = _send(server, {"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
    assert len(resp["result"]["tools"]) >= 4  # search_articles, get_article, get_article_content, knowledge_stats
    tool_names = [t["name"] for t in resp["result"]["tools"]]
    assert "search_articles" in tool_names
    assert "get_article_content" in tool_names

def test_search_articles(server, capsys):
    init(server)
    resp = _send(server, {
        "jsonrpc": "2.0", "id": 3, "method": "tools/call",
        "params": {"name": "search_articles", "arguments": {"keyword": "ETF", "limit": 3}}
    })
    assert "result" in resp
    assert "未找到匹配文章" not in resp["result"]["content"][0]["text"]

def test_get_article_not_found(server):
    init(server)
    resp = _send(server, {
        "jsonrpc": "2.0", "id": 4, "method": "tools/call",
        "params": {"name": "get_article", "arguments": {"article_id": "nonexistent-id"}}
    })
    assert "未找到文章" in resp["result"]["content"][0]["text"]
```

### 7.2 集成测试

使用 MCP Client SDK 或直接 subprocess 启动 server，模拟完整使用场景：

| 测试场景 | 验证点 |
|---------|--------|
| 正常启动 + 加载数据 | 日志输出条目数，ping 通过 |
| 搜索中文关键词 | 返回正确的结果数，同义词扩展生效 |
| 搜索英文/数字 | IS101、ETF、V3.2 等能正确匹配 |
| 分页拉取全文 | 多次 get_article_content 拼接后能得到完整文本 |
| 过滤 source | source=sse 时只返回上交所条目 |
| 非法 JSON 输入 | 返回 `-32700` 错误码 |
| 空数据目录 | 正常启动，返回 0 条统计 |
| SIGTERM 退出 | 进程 1 秒内退出，stderr 有退出日志 |

### 7.3 测试文件结构

```
ai-knowledge-base/
├── tests/
│   └── test_mcp_server.py     ← 单元测试 + 集成测试
└── mcp_knowledge_server.py
```

---

## 八、安全性注意

| 项目 | 说明 |
|------|------|
| **只读访问** | 本 Server 不做任何写入操作，不会修改知识库文件 |
| **路径遍历** | get_article 仅从内存 dict 中按 ID 查找，不拼接文件路径，无路径遍历风险 |
| **拒绝服务** | search 的 limit 上限设为 50，防止单次返回过大 |
| **输入清洗** | keyword 不做特殊清洗（仅在文本中做 `in` 匹配，无注入风险） |

---

## 九、方案评估

### 9.1 优势

| 维度 | 评分 | 说明 |
|------|------|------|
| **实现成本** | ⭐⭐⭐⭐ | 单文件 ~400 行，引入 jieba 分词（pip install jieba） |
| **性能** | ⭐⭐⭐⭐⭐ | ~5MB 数据全量加载 + 倒排索引，搜索 O(log n) |
| **部署便捷性** | ⭐⭐⭐⭐⭐ | `pip install jieba && python mcp_knowledge_server.py` 即运行 |
| **协议兼容性** | ⭐⭐⭐⭐⭐ | 严格遵循 MCP JSON-RPC 2.0 over stdio，支持 ping + tools + resources |
| **搜索精度** | ⭐⭐⭐⭐ | jieba 分词 + 倒排索引 + 同义词表，满足中文知识库检索需求 |
| **可扩展性** | ⭐⭐⭐ | 单文件架构，条目 < 500 时够用；超 1000 条需考虑懒加载 + LRU |

### 9.2 局限性

1. **全量内存加载**：条目数增长到 5000+（~100MB）时，启动时间和内存占用会成问题。届时需改为懒加载 + LRU 缓存。

2. **无增量更新**：Server 启动后知识库文件变更需重启 Server 才能感知。可通过文件 watch（`watchdog` 第三方库）实现热更新，但引入后需维护文件变更事件处理。

3. **分词依赖 jieba**：引入 `jieba` 作为唯一第三方依赖。jieba 成熟稳定、纯 Python，但大文本分词有 ~0.1ms 的固定开销。如后续条目超 10000，可考虑离线预分词 + pickle 序列化索引。

4. **跨语言搜索弱**：中文分词 + 英文原词保留，但中英混合查询（如"ETF 申购赎回规则"）的关联排序依赖命中次数，无语义相关性评价。

5. **同义词表需维护**：同义词扩展依赖人工维护的 `SYNONYM_MAP`，初始版本可集成常见证券术语（ETF、IS101、IOPV 等），后续需业务侧持续补充。

### 9.3 与现有项目设计的对比

| 对比维度 | 本方案（MCP Server） | 现有 Skill + Bash 方案 |
|---------|-------------------|---------------------|
| 协议 | JSON-RPC 2.0 MCP | SKILL.md 描述 + bash 脚本 |
| 发现机制 | tools/list 自动发现 | Agent 需预配置 skill |
| 交互模式 | 有状态长连接 | 无状态单次调用 |
| 搜索能力 | 分词 + 倒排索引 + 同义词 | grep / findstr 子串匹配 |
| 适用范围 | 兼容任何 MCP 客户端 | 仅限本项目 Agent |
| 学习成本 | 需理解 MCP 协议 | 直接写 shell 脚本 |

### 9.4 决策建议

| 场景 | 建议 |
|------|------|
| **仅本项目 Agent 使用** | Skill + Bash 方案更轻量（参考 `doc/MCP外部数据连接.md` 结论） |
| **需要跨客户端复用**（Cursor/Copilot） | MCP Server 方案是唯一选择 |
| **本方案的搜索能力提升明显** | jieba 分词 + 倒排索引远优于 grep，首次接入即推荐 |
| **后续搜索需求复杂** | MCP Server 可作为搜索能力的统一入口，逐步升级搜索算法 |
| **快速验证** | 先 Skill + Bash，需要时再封装为 MCP Server（内部的 dispatch 逻辑可复用） |

---

## 十、数据量增大后的分档改造方案

### 10.1 分档总览

| 档位 | 条目数 | 数据量 | 阶段名称 | 核心变更 | 侵入性 |
|------|--------|--------|---------|---------|--------|
| **Tier 0** | ~230 | ~5MB | 初始方案 | 单文件 + 全量内存 + jieba 在线分词 | — |
| **Tier 1** | ~5,000 | ~100MB | 懒加载 + LRU | 元数据/索引全量加载，正文懒加载；引入 LRU 缓存 | 中 |
| **Tier 2** | ~10,000 | ~200MB–500MB | 离线预索引 + SQLite | 离线预分词并持久化到 SQLite；正文存 SQLite BLOB | 大 |
| **Tier 3** | ~50,000+ | >1GB | 专用检索引擎 | 切到 Elasticsearch/Meilisearch；支持向量检索 | 重构 |

---

### 10.2 Tier 1（~5K 条目 / ~100MB）— 懒加载 + LRU 缓存

#### 触发条件

- 启动时间 > 3 秒（当前方案预计 5K 条目全量加载 + jieba 分词约 5–8 秒）
- 内存占用 > 300MB（当前方案 100MB 数据 + Python 进程开销 ~2–3x）

#### 架构变更

```
┌──────────────────────────────────────────┐
│              Data Layer                    │
│  ┌──────────────────┐  ┌───────────────┐  │
│  │  Metadata Store   │  │  Content Store │  │
│  │  (全量内存 dict)   │  │  (LRU 缓存)    │  │
│  │  ~5K × 2KB = 10MB │  │  最多 200 篇   │  │
│  └──────────────────┘  └───────┬───────┘  │
│                                │ miss     │
│  ┌──────────────────┐         │          │
│  │  Inverted Index   │   ┌────▼───────┐  │
│  │  (全量内存)        │   │  File I/O   │  │
│  │  ~50K term → doc  │   │  按需读取    │  │
│  └──────────────────┘   │  *.json     │  │
│                          └────────────┘  │
└──────────────────────────────────────────┘
```

#### 具体变更

**（1）元数据与索引全量加载，正文按需读取**

```python
class ContentStore:
    def __init__(self, entries_dir: Path, maxsize: int = 200):
        self.entries_dir = entries_dir
        self._content_cache: dict[str, str] = {}
        self._access_order: list[str] = []
        self.maxsize = maxsize

    def get(self, doc_id: str) -> str | None:
        if doc_id in self._content_cache:
            self._touch(doc_id)
            return self._content_cache[doc_id]
        content = self._load_from_disk(doc_id)
        if content is None:
            return None
        self._evict_if_needed()
        self._content_cache[doc_id] = content
        self._access_order.append(doc_id)
        return content

    def _load_from_disk(self, doc_id: str) -> str | None:
        source, _, date_seq = doc_id.split("-", 2)
        source_dir = {"sse": "sse", "szse": "szse", "chinaclear": "chinaclear"}.get(source)
        if not source_dir:
            return None
        fpath = self.entries_dir / source_dir / "entries" / f"{doc_id}.json"
        if not fpath.exists():
            return None
        data = json.loads(fpath.read_text(encoding="utf-8"))
        return data.get("content_markdown")
```

**（2）构建倒排索引时只索引元数据，不索引正文**

| 变更前 | 变更后 |
|--------|--------|
| `text = title + summary + tags + content_markdown` | `text = title + summary + tags` |
| 索引大小 ~100MB | 索引大小 ~10MB |
| 分词耗时 ~5s | 分词耗时 ~0.5s |

**（3）get_article_content 改为走 ContentStore**

```python
def handle_get_article_content(self, doc_id: str, offset: int = 0, limit: int = 3000) -> str:
    content = self.content_store.get(doc_id)
    if content is None:
        return f"未找到文章: {doc_id}"
    content = re.sub(r'\n?<metadata>.*?</metadata>\s*$', '', content, flags=re.DOTALL)
    total = len(content)
    offset = max(0, offset)
    snippet = content[offset:offset + limit]
    return f"{snippet}\n[全文共 {total} 字符，已返回第 {offset}-{offset + len(snippet)} 字符]"
```

**（4）新增启动参数 `--lazy`**

```
python mcp_knowledge_server.py --lazy --cache-size 200
```

Tier 0 模式下忽略该参数保持原有全量加载行为。

#### 性能预期

| 指标 | Tier 0 全量 | Tier 1 懒加载 |
|------|------------|-------------|
| 启动时间 | ~5–8s | ~0.8–1.2s |
| 常驻内存 | ~300MB | ~50MB（元数据 10MB + 索引 10MB + LRU 200 篇 ~30MB）|
| search 延迟 | O(log n) | O(log n)（不变）|
| get_article_content 延迟 | O(1) 内存 | 首次 ~5ms 磁盘 I/O，后续 O(1) 缓存命中 |

#### 迁移路径

1. 文件结构不变，元数据 JSON 仍保持 `content_markdown` 字段
2. 引入 `ContentStore` 类，替换原直接 `entries[doc_id]["content_markdown"]`
3. `search_articles` 不受影响（索引未变）
4. `knowledge_stats` 不受影响（元数据全量在内存）

---

### 10.3 Tier 2（~10K 条目 / 200–500MB）— 离线预索引 + SQLite

#### 触发条件

- 启动时间 > 5 秒（jieba 分词 10K 条目的元数据约 1–2s，但累积分发仍需时间）
- jieba 在线分词成为 search 性能瓶颈（高并发场景）
- 文件系统上 10K 个零散 JSON 文件，目录操作耗时

#### 架构变更

```
┌────────────────────────────────────────────┐
│              Data Layer                      │
│  ┌────────────────────┐  ┌──────────────┐  │
│  │   SQLite 数据库     │  │  LRU Content  │  │
│  │                    │  │     Cache     │  │
│  │  entries 表         │  └──────────────┘  │
│  │  inverted_index 表  │                     │
│  │  synonyms 表        │                     │
│  └────────────────────┘                     │
└────────────────────────────────────────────┘
```

#### 10.3.1 离线预索引流程

新增独立脚本 `build_index.py`，在知识库更新后异步运行，产出 SQLite 索引文件：

```python
# build_index.py — 离线索引构建脚本，用法: python build_index.py [--sources sse,szse]
# 产出: knowledge/articles/mcp_index.db

import json
import sqlite3
from pathlib import Path
import jieba
from collections import defaultdict

ARTICLES_DIR = Path("knowledge/articles")
INDEX_DB = ARTICLES_DIR / "mcp_index.db"


def build_index(sources: list[str] | None = None):
    sources = sources or ["sse", "szse", "chinaclear"]
    conn = sqlite3.connect(str(INDEX_DB))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=OFF")

    conn.executescript("""
        CREATE TABLE IF NOT EXISTS entries (
            doc_id TEXT PRIMARY KEY,
            source TEXT NOT NULL,
            title TEXT NOT NULL,
            metadata TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now'))
        );
        CREATE TABLE IF NOT EXISTS content (
            doc_id TEXT PRIMARY KEY,
            body TEXT NOT NULL,
            char_count INTEGER NOT NULL,
            FOREIGN KEY (doc_id) REFERENCES entries(doc_id)
        );
        CREATE TABLE IF NOT EXISTS inverted_index (
            term TEXT NOT NULL,
            doc_id TEXT NOT NULL,
            freq INTEGER DEFAULT 1,
            PRIMARY KEY (term, doc_id)
        );
        CREATE INDEX IF NOT EXISTS idx_inverted_term ON inverted_index(term);
        CREATE INDEX IF NOT EXISTS idx_entries_source ON entries(source);
    """)

    term_docs = defaultdict(lambda: defaultdict(int))
    entries_batch = []

    for source in sources:
        entries_dir = ARTICLES_DIR / source / "entries"
        if not entries_dir.exists():
            continue
        for fpath in sorted(entries_dir.glob("*.json")):
            if fpath.name == "entries.json":
                continue
            data = json.loads(fpath.read_text(encoding="utf-8"))
            doc_id = data.get("id") or fpath.stem
            content_md = data.pop("content_markdown", "")

            entries_batch.append((doc_id, source, data.get("title", ""),
                                  json.dumps(data, ensure_ascii=False), content_md))

            index_text = f'{data.get("title", "")} {data.get("summary", "")} {" ".join(data.get("tags", []))}'
            words = set(jieba.lcut(index_text))
            for w in words:
                if len(w.strip()) < 2:
                    continue
                term_docs[w][doc_id] += 1

    conn.executemany(
        "INSERT OR REPLACE INTO entries (doc_id, source, title, metadata) VALUES (?, ?, ?, ?)",
        [(e[0], e[1], e[2], e[3]) for e in entries_batch],
    )
    conn.executemany(
        "INSERT OR REPLACE INTO content (doc_id, body, char_count) VALUES (?, ?, ?)",
        [(e[0], e[4], len(e[4])) for e in entries_batch],
    )
    conn.executemany(
        "INSERT OR REPLACE INTO inverted_index (term, doc_id, freq) VALUES (?, ?, ?)",
        [(term, doc_id, freq) for term, docs in term_docs.items() for doc_id, freq in docs.items()],
    )

    conn.commit()
    conn.close()
    print(f"[build_index] 完成: {len(entries_batch)} 条目, {len(term_docs)} 词项")


if __name__ == "__main__":
    build_index()
```

#### 10.3.2 MCP Server 变更

**（1）数据层替换为 SQLite 查询**

```python
class SQLiteDataLayer:
    def __init__(self, db_path: str = "knowledge/articles/mcp_index.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA journal_mode=WAL")
        self._init_cache()

    def _init_cache(self):
        cursor = self.conn.execute("SELECT doc_id, metadata FROM entries")
        self.metadata: dict[str, dict] = {
            row["doc_id"]: json.loads(row["metadata"]) for row in cursor.fetchall()
        }
        cursor = self.conn.execute("SELECT term, doc_id FROM inverted_index")
        self.inverted_index: dict[str, list[str]] = defaultdict(list)
        for row in cursor.fetchall():
            self.inverted_index[row["term"]].append(row["doc_id"])
        self.content_cache: dict[str, str] = {}
        self.content_lru: list[str] = []
        self.content_maxsize = 200

    def get_content(self, doc_id: str) -> str | None:
        if doc_id in self.content_cache:
            self._touch_lru(doc_id)
            return self.content_cache[doc_id]
        cursor = self.conn.execute("SELECT body FROM content WHERE doc_id=?", (doc_id,))
        row = cursor.fetchone()
        if row is None:
            return None
        body = row["body"]
        self._evict_content_lru()
        self.content_cache[doc_id] = body
        self.content_lru.append(doc_id)
        return body
```

**（2）Server 结构不变，仅 DataLayer 模块替换**

```
mcp_knowledge_server.py       ← 主入口（不变）
data_layer.py                 ← 新增：DataLayer 抽象基类 + 3 种实现
build_index.py                ← 新增：离线索引构建
```

DataLayer 抽象：

```python
class DataLayer(ABC):
    @abstractmethod
    def search(self, keyword: str, source: str | None, limit: int) -> list[dict]: ...
    @abstractmethod
    def get_metadata(self, doc_id: str) -> dict | None: ...
    @abstractmethod
    def get_content(self, doc_id: str, offset: int, limit: int) -> tuple[str | None, int]: ...
    @abstractmethod
    def stats(self) -> dict: ...
```

三种实现：

| 实现类 | 适用阶段 | 存储后端 |
|--------|---------|---------|
| `MemoryDataLayer` | Tier 0 | 全量 dict |
| `LazyDataLayer` | Tier 1 | 元数据 dict + 文件懒加载 |
| `SQLiteDataLayer` | Tier 2 | SQLite + 内存缓存 |

启动时自动探测：

```python
def _create_data_layer() -> DataLayer:
    db_path = ARTICLES_DIR / "mcp_index.db"
    if db_path.exists():
        return SQLiteDataLayer(str(db_path))
    if _count_entries() > 1000:
        return LazyDataLayer(ARTICLES_DIR, cache_size=200)
    return MemoryDataLayer(ARTICLES_DIR)
```

#### 10.3.3 同义词表升级

从内存 dict 升级为 SQLite 表，支持自动化扩展：

```python
# build_index.py 中新增
conn.executescript("""
    CREATE TABLE IF NOT EXISTS synonyms (
        term TEXT NOT NULL,
        synonym TEXT NOT NULL,
        source TEXT DEFAULT 'manual',
        PRIMARY KEY (term, synonym)
    );
""")

SYNONYM_DATA = [
    ("ETF", "交易型开放式指数基金"),
    ("交易型开放式指数基金", "ETF"),
    ("涨跌幅限制", "涨跌停"),
    ("涨跌停", "涨跌幅限制"),
    ("接口规格说明书", "IS"),
    ("IS", "接口规格说明书"),
]
conn.executemany(
    "INSERT OR IGNORE INTO synonyms (term, synonym, source) VALUES (?, ?, 'manual')",
    [(t, s) for t, s in SYNONYM_DATA],
)
```

搜索时同义词自动扩展：

```python
def _expand_synonyms(self, words: list[str]) -> list[str]:
    expanded = list(words)
    cursor = self.conn.execute(
        f"SELECT term, synonym FROM synonyms WHERE term IN ({','.join('?' * len(words))})",
        words,
    )
    for row in cursor.fetchall():
        expanded.append(row["synonym"])
    return expanded
```

#### 性能预期

| 指标 | Tier 1 | Tier 2 |
|------|--------|--------|
| 启动时间 | ~1s | ~0.5s |
| 常驻内存 | ~50MB | ~30MB 或更小 |
| search 延迟 | O(log n) | O(log n) + 同义词查表（~0.1ms）|
| get_article_content 延迟 | 首次 ~5ms | 首次 ~2ms（SQLite BLOB 读取）|
| 索引构建时间 | 启动时 ~1s | 离线 ~3s |
| 增量更新 | 需重启 | 重新 build_index.py（~3s）|

---

### 10.4 Tier 3（~50K+ 条目 / >1GB）— 专用检索引擎

#### 触发条件

- SQLite 全文检索延迟 > 100ms
- 需要语义搜索（如"申购赎回规则"可匹配到"认购/申赎/T日申购"等变体）
- 写入端（pipeline）与读取端（MCP Server）分离部署
- 需要高并发（多个 AI 客户端同时查询）

#### 架构变更

```
  Pipeline (写入端)                       MCP Server (读取端)
┌──────────────────┐              ┌──────────────────────────┐
│  build_index.py   │ ──写入──→   │  mcp_knowledge_server.py  │
│  (弃用 SQLite)    │  Elasticsearch│ ┌────────────────────┐  │
│                   │  /           │ │  ES Client          │  │
│  → Elasticsearch  │  Meilisearch │ │  (meilisearch-py)   │  │
│  → Vector DB      │              │ └─────────┬──────────┘  │
│  (Milvus/Qdrant)  │              │           │ REST API     │
└──────────────────┘              │  ┌─────────▼──────────┐  │
                                    │  Content Store       │  │
                                    │  (S3/MinIO/本地)      │  │
                                    └─────────────────────┘  │
                                    └──────────────────────────┘
```

#### 10.4.1 检索引擎选型

| 引擎 | 适合场景 | 优势 | 劣势 |
|------|---------|------|------|
| **Elasticsearch** | 复杂全文搜索 + 聚合分析 | 生态成熟，中文分词插件（IK/THULAC），DSL 灵活 | 部署重（JVM），~1GB 内存起 |
| **Meilisearch** | 轻量即用搜索 | 零配置，Rust 实现，自带中文分词，~100MB 内存起 | 高级查询能力有限 |
| **SQLite FTS5** | 原地升级（不引入新服务） | 无需额外服务 | 中文需自定义分词器，无语义排序 |

**推荐优先级**：Meilisearch > Elasticsearch > SQLite FTS5

#### 10.4.2 使用 Meilisearch 的实现

```python
# Tier 3 DataLayer 实现
import meilisearch

class MeilisearchDataLayer(DataLayer):
    def __init__(self, host: str = "http://localhost:7700", api_key: str | None = None):
        self.client = meilisearch.Client(host, api_key)
        self.index = self.client.index("knowledge_entries")
        self.content_store = ObjectContentStore()

    def search(self, keyword: str, source: str | None, limit: int = 5) -> list[dict]:
        filters = []
        if source:
            filters.append(f"source = {source}")
        results = self.index.search(keyword, {
            "limit": limit,
            "filter": filters if filters else None,
            "attributesToHighlight": ["title", "summary"],
        })
        return [{
            "doc_id": hit["id"],
            "title": hit.get("_formatted", {}).get("title", hit["title"]),
            "source": hit["source"],
            "type": hit["type"],
            "tags": hit.get("tags", []),
            "summary": hit.get("summary", ""),
            "score": hit["_rankingScore"],
        } for hit in results["hits"]]
```

构建索引（pipeline 侧）：

```python
def index_to_meilisearch():
    client = meilisearch.Client("http://localhost:7700")
    client.create_index("knowledge_entries", {"primaryKey": "id"})
    index = client.index("knowledge_entries")

    documents = []
    for entry in load_all_entries():
        documents.append({
            "id": entry["id"],
            "title": entry["title"],
            "summary": entry.get("summary", ""),
            "source": entry["source"],
            "type": entry.get("type", ""),
            "tags": entry.get("tags", []),
            "status": entry.get("status", "active"),
            "version": entry.get("version", ""),
            "public_date": entry.get("public_date", ""),
        })
    index.add_documents(documents)
```

#### 10.4.3 正文存储分离

| 方案 | 适合场景 | 示例 |
|------|---------|------|
| 本地文件系统 | 单机部署 | `knowledge/articles/sse/contents/{doc_id}.md` |
| MinIO / S3 | 分布式部署 | `bucket/knowledge/sse/{doc_id}.md` |
| 数据库 BLOB | 已有 PostgreSQL | `content_store` 表 |

```python
class ObjectContentStore:
    def __init__(self, backend: str = "local", bucket: str = "", base_dir: Path | None = None):
        self.backend = backend
        self.base_dir = base_dir or Path("knowledge/articles")
        self._cache: dict[str, str] = {}
        self._lru: list[str] = []
        self._maxsize = 200

    def get(self, doc_id: str) -> str | None:
        if doc_id in self._cache:
            self._touch(doc_id)
            return self._cache[doc_id]
        content = self._fetch(doc_id)
        if content:
            self._cache_content(doc_id, content)
        return content

    def _fetch(self, doc_id: str) -> str | None:
        if self.backend == "local":
            source = doc_id.split("-", 1)[0]
            fpath = self.base_dir / source / "contents" / f"{doc_id}.md"
            return fpath.read_text(encoding="utf-8") if fpath.exists() else None
        elif self.backend == "s3":
            raise NotImplementedError
```

#### 10.4.4 向量检索（进阶）

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("shibing624/text2vec-base-chinese")

def build_vector_index():
    entries = load_all_entries()
    vectors = model.encode([
        f'{e["title"]} {e.get("summary", "")} {" ".join(e.get("tags", []))}'
        for e in entries
    ])
    # 写入向量数据库（Milvus / Qdrant / FAISS）

def hybrid_search(keyword: str, alpha: float = 0.3):
    fts_results = fulltext_search(keyword)
    vec_results = vector_search(keyword)
    return reciprocal_rank_fusion(fts_results, vec_results, alpha)
```

#### 性能预期

| 指标 | Tier 2（SQLite） | Tier 3（Meilisearch） | Tier 3 + 向量 |
|------|---------------|---------------------|-------------|
| 启动时间 | ~0.5s | ~0.2s | ~0.2s |
| 常驻内存 | ~30MB | ~50MB | ~200MB（含模型）|
| search 延迟 | ~5ms | ~3ms | ~20ms（含推理）|
| 语义搜索 | ❌ | ❌ | ✅ |
| 增量更新 | 手动 build_index.py | API 实时更新 | API 实时更新 |
| 高并发 | 单进程锁 | 水平扩展 | 水平扩展 |

---

### 10.5 文件结构汇总

```
Tier 0 / Tier 1:
├── mcp_knowledge_server.py
├── requirements-mcp.txt
├── knowledge/articles/{sse,szse}/entries/*.json
└── tests/test_mcp_server.py

Tier 2:
├── mcp_knowledge_server.py
├── data_layer.py                    ← 新增
├── build_index.py                    ← 新增
├── knowledge/articles/mcp_index.db  ← 新增 (.gitignore)
├── knowledge/articles/{sse,szse}/entries/*.json
└── tests/test_mcp_server.py

Tier 3:
├── mcp_knowledge_server.py
├── config.yaml                      ← 新增
├── knowledge/articles/{sse,szse}/entries/*.json
├── knowledge/articles/{sse,szse}/contents/*.md  ← 新增
├── docker-compose.yml               ← 新增
└── tests/test_mcp_server.py
```

---

### 10.6 迁移决策树

```
当前 Tier 0 (~230 条目 / ~5MB)
 │
 ├── 条目数 < 1000 → ✅ 维持 Tier 0
 │
 ├── 条目数 1000–5000 或启动时间 > 3s
 │   └── 引入 --lazy，切到 LazyDataLayer (Tier 1)
 │
 ├── 条目数 5000–10000 或目录操作慢
 │   └── 引入 build_index.py + SQLiteDataLayer (Tier 2)
 │
 ├── 条目数 > 10000 或需要语义搜索
 │   └── 部署 Meilisearch + 正文剥离 (Tier 3)
 │
 └── 高并发 / 分布式 / 实时增量
     └── Tier 3 + 向量检索 + 对象存储
```

---

### 10.7 引入成本汇总

| 成本项 | Tier 0 → 1 | Tier 1 → 2 | Tier 2 → 3 |
|--------|-----------|-----------|-----------|
| **新增代码** | ~100 行 | ~300 行 | ~200 行 + 配置 |
| **新增依赖** | 无 | 无（sqlite3 内置）| meilisearch / boto3 |
| **新增服务** | 无 | 无 | Meilisearch + 对象存储 |
| **数据迁移** | 无 | 运行一次 build_index.py | 导入脚本 |
| **部署变更** | 无 | 无 | docker-compose 编排 |
| **维护成本** | 低 | 中 | 高 |
| **回退难度** | 低（去掉 --lazy）| 低（删 mcp_index.db）| 中（改配置）|

---

### 10.8 建议升级时机

| 指标 | 建议升级至 |
|------|----------|
| 条目数 > 1,000 | 引入 `--lazy`（Tier 1），无需大重构 |
| 条目数 > 5,000 或启动时间 > 5s | 实施 build_index.py（Tier 2），收益最大 |
| 条目数 > 10,000 | 评估 Meilisearch（Tier 3），启动 PoC |
| 需要语义搜索 | 直接跳 Tier 3 + 向量检索 |
| 多客户端高并发 | 直接跳 Tier 3 |
| pipeline 日更新 > 1 次 | 引入 watchdog 或 Tier 3 实时更新 |

---

*（本章为原设计方案的可扩展性详细展开，对应 9.2 局限性内容。）*
