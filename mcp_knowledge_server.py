"""MCP Knowledge Server — exposes local knowledge base via MCP protocol.

Provides search, retrieval, statistics, and resource browsing over stdio
using JSON-RPC 2.0 (MCP spec). Loads all entries into memory at startup.
"""

import json
import logging
import os
import signal
import sys
import glob as glob_module
from collections import Counter
from typing import Any

import jieba

logger = logging.getLogger("mcp-knowledge-server")

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
KNOWLEDGE_DIR = os.environ.get(
    "KNOWLEDGE_DIR", os.path.join(os.getcwd(), "knowledge", "articles")
)
SYNONYM_FILE = os.environ.get("SYNONYM_FILE", "")

HARDCODED_SYNONYMS: dict[str, list[str]] = {
    "ETF": ["交易型开放式指数基金"],
    "交易型开放式指数基金": ["ETF"],
    "科创板": ["STAR Market", "Science and Technology Innovation Board"],
    "STAR Market": ["科创板"],
    "STAR": ["科创板"],
    "集合竞价": ["竞价交易"],
    "竞价交易": ["集合竞价"],
    "T+1": ["T+1交收"],
    "T+1交收": ["T+1"],
    "退市": ["终止上市"],
    "终止上市": ["退市"],
    "上证": ["上海证券交易所"],
    "上海证券交易所": ["上证"],
    "深证": ["深圳证券交易所"],
    "深圳证券交易所": ["深证"],
    "北交所": ["北京证券交易所"],
    "北京证券交易所": ["北交所"],
    "创业板": ["GEM", "Growth Enterprise Market"],
    "GEM": ["创业板"],
    "港股通": ["沪港通", "深港通"],
    "回购": ["股份回购", "股票回购"],
    "质押": ["证券质押", "质押登记"],
    "沪股通": ["沪港通"],
    "深股通": ["深港通"],
    "股东大会": ["股东会"],
    "股东会": ["股东大会"],
    "ST": ["特别处理", "风险警示"],
    "退市整理期": ["退市整理"],
}
SOURCES = ("sse", "szse", "chinaclear")

FIELD_WEIGHTS = {"title": 5, "summary": 3, "tags": 2, "content": 1}

MCP_VERSION = "0.1.0"
SERVER_NAME = "mcp-knowledge-server"


class ArticleStore:
    """In-memory store for knowledge entries with inverted index."""

    def __init__(self) -> None:
        self._entries: dict[str, dict] = {}
        self._inverted_index: dict[str, dict[str, dict[str, int]]] = {}
        self._synonym_map: dict[str, list[str]] = {}
        self._loaded = False

    def load(self, knowledge_dir: str) -> None:
        self._entries = {}
        self._inverted_index = {}
        self._synonym_map = {}

        entry_dirs = [os.path.join(knowledge_dir, s, "entries") for s in SOURCES]
        parse_errors = []

        for ed in entry_dirs:
            if not os.path.isdir(ed):
                logger.warning("Directory not found, skipping: %s", ed)
                continue
            pattern = os.path.join(ed, "*.json")
            for fpath in sorted(glob_module.glob(pattern)):
                if os.path.basename(fpath) == "entries.json":
                    continue
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        entry = json.load(f)
                except Exception as exc:
                    logger.error("Failed to parse %s: %s", fpath, exc)
                    parse_errors.append((fpath, str(exc)))
                    continue
                doc_id = entry.get("id", "")
                if not doc_id:
                    logger.warning("Entry missing id, skipping: %s", fpath)
                    continue
                self._entries[doc_id] = entry
                tokens = self._tokenize_entry(entry)
                for field_name, word_counts in tokens.items():
                    weight = FIELD_WEIGHTS.get(field_name, 1)
                    for word, count in word_counts.items():
                        idx = self._inverted_index.setdefault(word, {})
                        doc_data = idx.setdefault(doc_id, {})
                        doc_data[field_name] = (
                            doc_data.get(field_name, 0) + count * weight
                        )

        self._auto_discover_synonyms()

        total = len(self._entries)
        logger.info(
            "Loaded %d entries from %d sources",
            total,
            sum(
                1
                for s in SOURCES
                if os.path.isdir(os.path.join(knowledge_dir, s, "entries"))
            ),
        )
        if total == 0:
            logger.warning(
                "Loaded 0 entries. Check KNOWLEDGE_DIR=%s. Possible causes: "
                "directory does not exist, empty, or all JSON files are malformed.",
                knowledge_dir,
            )
        if parse_errors:
            logger.warning("%d file(s) failed to parse", len(parse_errors))
        self._loaded = True

    def _tokenize_entry(self, entry: dict) -> dict[str, Counter]:
        result: dict[str, Counter] = {}
        title = entry.get("title", "") or ""
        if title:
            result["title"] = Counter(jieba.lcut(title))
        summary = entry.get("summary", "") or ""
        if summary:
            result["summary"] = Counter(jieba.lcut(summary))
        tags_list = entry.get("tags", []) or []
        if tags_list:
            combined = " ".join(str(t) for t in tags_list if t)
            result["tags"] = Counter(jieba.lcut(combined))
        content = entry.get("content_markdown", "") or ""
        if content:
            result["content"] = Counter(jieba.lcut(content))
        return result

    def _auto_discover_synonyms(self) -> None:
        self._synonym_map = {}
        for src_map in (HARDCODED_SYNONYMS,):
            for k, vlist in src_map.items():
                existing = self._synonym_map.setdefault(k, [])
                for v in vlist:
                    if v not in existing:
                        existing.append(v)

        import re

        cn_en_pattern = re.compile(
            r"([\u4e00-\u9fff\w]+)[（(]([A-Za-z][A-Za-z0-9\s\-/.]*)[）)]"
        )
        for doc_id, entry in self._entries.items():
            text = (
                (entry.get("summary", "") or "") + " " + (entry.get("title", "") or "")
            )
            for match in cn_en_pattern.finditer(text):
                cn_term = match.group(1).strip()
                en_term = match.group(2).strip()
                if cn_term and en_term:
                    self._synonym_map.setdefault(cn_term, [])
                    if en_term not in self._synonym_map[cn_term]:
                        self._synonym_map[cn_term].append(en_term)
                    self._synonym_map.setdefault(en_term, [])
                    if cn_term not in self._synonym_map[en_term]:
                        self._synonym_map[en_term].append(cn_term)

        if SYNONYM_FILE:
            try:
                with open(SYNONYM_FILE, "r", encoding="utf-8") as f:
                    external = json.load(f)
                for k, vlist in external.items():
                    existing = self._synonym_map.setdefault(k, [])
                    for v in vlist:
                        if v not in existing:
                            existing.append(v)
                logger.info(
                    "Loaded %d synonym entries from %s", len(external), SYNONYM_FILE
                )
            except Exception as exc:
                logger.error("Failed to load synonym file %s: %s", SYNONYM_FILE, exc)

        logger.info("Synonym map has %d entries", len(self._synonym_map))

    def get_synonyms(self, word: str) -> list[str]:
        return self._synonym_map.get(word, [])

    def get_entry(self, doc_id: str) -> dict | None:
        return self._entries.get(doc_id)

    def get_entry_content(self, doc_id: str) -> str | None:
        entry = self._entries.get(doc_id)
        if entry is None:
            return None
        return entry.get("content_markdown", "") or ""

    def search(self, keyword: str, limit: int = 5, source: str | None = None) -> str:
        if not keyword:
            return "keyword 不能为空"
        tokens = jieba.lcut(keyword)
        expanded_tokens = list(tokens)
        for t in tokens:
            expanded_tokens.extend(self.get_synonyms(t))
        expanded_tokens = list(set(expanded_tokens))

        if len(keyword) < 2:
            valid_fields = {"title", "summary"}
        else:
            valid_fields = set(FIELD_WEIGHTS.keys())

        scores: dict[str, float] = {}
        for token in expanded_tokens:
            idx = self._inverted_index.get(token)
            if idx is None:
                continue
            for doc_id, field_hits in idx.items():
                if source and not doc_id.startswith(source):
                    continue
                score = 0.0
                for field, hits in field_hits.items():
                    if field in valid_fields:
                        score += hits
                if score > 0:
                    scores[doc_id] = scores.get(doc_id, 0) + score

        if not scores:
            return "未找到匹配文章"

        sorted_ids = sorted(scores, key=scores.get, reverse=True)[:limit]
        lines = []
        for i, doc_id in enumerate(sorted_ids, 1):
            entry = self._entries[doc_id]
            summary = (entry.get("summary", "") or "")[:120]
            lines.append(
                f"{i}. [{entry.get('id', '')}] {entry.get('title', '')} "
                f"| 来源: {entry.get('source', '')} 类型: {entry.get('type', '')} "
                f"| 标签: {', '.join(entry.get('tags', []) or [])} "
                f"| {summary}"
            )
        return "\n".join(lines)

    def get_stats(self) -> str:
        total = len(self._entries)
        if total == 0:
            return "知识库统计:\n  总条目数: 0\n  来源分布: 无\n  类型分布: 无\n  状态分布: 无\n  热门标签: 无\n  最近发布: 无\n  最近采集: 无"

        by_source: Counter[str] = Counter()
        by_type: Counter[str] = Counter()
        by_status: Counter[str] = Counter()
        all_tags: list[str] = []

        for entry in self._entries.values():
            by_source[entry.get("source", "unknown")] += 1
            by_type[entry.get("type", "unknown")] += 1
            by_status[entry.get("status", "unknown")] += 1
            all_tags.extend(entry.get("tags", []) or [])

        top_tags = Counter(all_tags).most_common(10)

        by_public = sorted(
            self._entries.values(),
            key=lambda e: e.get("public_date", "") or "",
            reverse=True,
        )[:5]
        by_crawl = sorted(
            self._entries.values(),
            key=lambda e: e.get("crawl_date", "") or "",
            reverse=True,
        )[:5]

        lines = [
            "知识库统计:",
            f"  总条目数: {total}",
            "  来源分布:",
        ]
        for s, c in sorted(by_source.items()):
            lines.append(f"    {s}: {c}")
        lines.append("  类型分布:")
        for t, c in sorted(by_type.items()):
            lines.append(f"    {t}: {c}")
        lines.append("  状态分布:")
        for s, c in sorted(by_status.items()):
            lines.append(f"    {s}: {c}")
        lines.append("  热门标签:")
        for tag, count in top_tags:
            lines.append(f"    {tag}: {count}")
        lines.append("  最近发布 (public_date):")
        for e in by_public:
            lines.append(f"    {e.get('id', '')} ({e.get('public_date', '')})")
        lines.append("  最近采集 (crawl_date):")
        for e in by_crawl:
            lines.append(f"    {e.get('id', '')} ({e.get('crawl_date', '')})")
        return "\n".join(lines)

    def list_resources(self, cursor: str | None = None) -> dict:
        sorted_ids = sorted(self._entries.keys())
        page_size = 50
        start_idx = 0
        if cursor:
            try:
                start_idx = sorted_ids.index(cursor) + 1
            except ValueError:
                start_idx = 0
        page = sorted_ids[start_idx : start_idx + page_size]
        resources = []
        for doc_id in page:
            entry = self._entries[doc_id]
            uri = f"knowledge://{entry.get('source', 'unknown')}/entries/{doc_id}"
            resources.append(
                {
                    "uri": uri,
                    "name": entry.get("title", ""),
                    "description": (entry.get("summary", "") or "")[:200],
                    "mimeType": "text/markdown",
                }
            )
        result: dict[str, Any] = {"resources": resources}
        if start_idx + page_size < len(sorted_ids):
            result["nextCursor"] = page[-1]
        return result

    def read_resource(self, uri: str) -> str | None:
        parts = uri.split("/")
        if len(parts) < 2:
            return None
        doc_id = parts[-1]
        entry = self._entries.get(doc_id)
        if entry is None:
            return None
        return json.dumps(entry, ensure_ascii=False, indent=2)

    @property
    def loaded(self) -> bool:
        return self._loaded


class MCPServer:
    """MCP protocol server over stdio transport."""

    def __init__(self, store: ArticleStore) -> None:
        self._store = store
        self._running = False
        self._request_id_counter = 0

    def _next_request_id(self) -> str:
        self._request_id_counter += 1
        return f"mcp-{self._request_id_counter}"

    def _make_error(self, code: int, message: str, msg_id: Any = None) -> str:
        resp = {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": code, "message": message},
        }
        return json.dumps(resp, ensure_ascii=False)

    def _make_result(self, result: Any, msg_id: Any = None) -> str:
        resp = {"jsonrpc": "2.0", "id": msg_id, "result": result}
        return json.dumps(resp, ensure_ascii=False)

    def _handle_message(self, raw: str) -> str | None:
        try:
            msg = json.loads(raw)
        except json.JSONDecodeError:
            return self._make_error(-32700, "Parse error: invalid JSON")

        if not isinstance(msg, dict):
            return self._make_error(-32700, "Parse error: expected object")

        msg_id = msg.get("id")
        method = msg.get("method", "")
        params = msg.get("params", {})

        if method == "initialize":
            return self._make_result(
                {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {},
                        "resources": {},
                    },
                    "serverInfo": {
                        "name": SERVER_NAME,
                        "version": MCP_VERSION,
                    },
                },
                msg_id,
            )

        if method == "ping":
            return self._make_result({}, msg_id)

        if method == "tools/list":
            return self._handle_tools_list(msg_id)

        if method == "tools/call":
            return self._handle_tools_call(params, msg_id)

        if method == "resources/list":
            cursor = None
            if isinstance(params, dict):
                cursor = params.get("cursor")
            return self._handle_resources_list(cursor, msg_id)

        if method == "resources/read":
            uri = ""
            if isinstance(params, dict):
                uri = params.get("uri", "")
            return self._handle_resources_read(uri, msg_id)

        return self._make_error(-32601, f"Method not found: {method}", msg_id)

    def _handle_tools_list(self, msg_id: Any) -> str:
        tools = [
            {
                "name": "search_articles",
                "description": "按关键词搜索知识库文章（基于 jieba 分词 + 倒排索引，支持中英文混合搜索）",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "keyword": {"type": "string", "description": "搜索关键词"},
                        "limit": {
                            "type": "number",
                            "description": "最大返回条数，默认5，最大50",
                        },
                        "source": {
                            "type": "string",
                            "enum": ["sse", "szse", "chinaclear"],
                            "description": "限定数据源",
                        },
                    },
                    "required": ["keyword"],
                },
            },
            {
                "name": "get_article",
                "description": "按文章 ID 获取文章元数据（不含全文）",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "文章 ID，如 sse-tech-20250428-001",
                        },
                    },
                    "required": ["article_id"],
                },
            },
            {
                "name": "get_article_content",
                "description": "分页获取文章全文 Markdown 内容",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string", "description": "文章 ID"},
                        "offset": {
                            "type": "number",
                            "description": "字符偏移量，默认0",
                        },
                        "limit": {
                            "type": "number",
                            "description": "返回字符数，默认3000，最大10000",
                        },
                    },
                    "required": ["article_id"],
                },
            },
            {
                "name": "knowledge_stats",
                "description": "获取知识库统计信息：总数、来源分布、类型分布、热门标签",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                },
            },
        ]
        return self._make_result({"tools": tools}, msg_id)

    def _handle_tools_call(self, params: Any, msg_id: Any) -> str:
        if not isinstance(params, dict):
            return self._make_error(-32602, "Invalid params: expected object", msg_id)
        name = params.get("name", "")
        arguments = params.get("arguments", {})

        if name == "search_articles":
            keyword = arguments.get("keyword", "")
            limit = int(arguments.get("limit", 5))
            limit = max(1, min(limit, 50))
            source = arguments.get("source")
            result = self._store.search(keyword, limit=limit, source=source)
            return self._make_result(
                {"content": [{"type": "text", "text": result}]}, msg_id
            )

        if name == "get_article":
            article_id = arguments.get("article_id", "")
            entry = self._store.get_entry(article_id)
            if entry is None:
                return self._make_result(
                    {
                        "content": [
                            {"type": "text", "text": f"未找到文章: {article_id}"}
                        ]
                    },
                    msg_id,
                )
            meta = {k: v for k, v in entry.items() if k != "content_markdown"}
            total_chars = len(entry.get("content_markdown", "") or "")
            meta["_content_char_count"] = total_chars
            return self._make_result(
                {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(meta, ensure_ascii=False, indent=2),
                        }
                    ]
                },
                msg_id,
            )

        if name == "get_article_content":
            article_id = arguments.get("article_id", "")
            offset = int(arguments.get("offset", 0))
            limit = int(arguments.get("limit", 3000))
            limit = max(1, min(limit, 10000))
            content = self._store.get_entry_content(article_id)
            if content is None:
                return self._make_result(
                    {
                        "content": [
                            {"type": "text", "text": f"未找到文章: {article_id}"}
                        ]
                    },
                    msg_id,
                )
            offset = max(0, offset)
            total_len = len(content)
            sliced = content[offset : offset + limit]
            annotation = f"[全文共 {total_len} 字符，已返回第 {offset}-{offset + len(sliced)} 字符]"
            return self._make_result(
                {"content": [{"type": "text", "text": sliced + "\n\n" + annotation}]},
                msg_id,
            )

        if name == "knowledge_stats":
            result = self._store.get_stats()
            return self._make_result(
                {"content": [{"type": "text", "text": result}]}, msg_id
            )

        return self._make_error(-32602, f"Unknown tool: {name}", msg_id)

    def _handle_resources_list(self, cursor: str | None, msg_id: Any) -> str:
        result = self._store.list_resources(cursor=cursor)
        return self._make_result(result, msg_id)

    def _handle_resources_read(self, uri: str, msg_id: Any) -> str:
        content = self._store.read_resource(uri)
        if content is None:
            return self._make_result(
                {"content": [{"type": "text", "text": f"未找到资源: {uri}"}]},
                msg_id,
            )
        return self._make_result(
            {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": "text/markdown",
                        "text": content,
                    }
                ]
            },
            msg_id,
        )

    def run(self) -> None:
        logger.info("MCP Knowledge Server starting (pid=%d)", os.getpid())
        self._running = True

        def handle_sigterm(signum: int, frame) -> None:
            logger.info("Received signal %d, shutting down", signum)
            self._running = False

        signal.signal(signal.SIGTERM, handle_sigterm)
        if hasattr(signal, "SIGINT"):
            signal.signal(signal.SIGINT, handle_sigterm)

        for line in sys.stdin:
            if not self._running:
                break
            if not line.strip():
                continue
            request_id = self._next_request_id()
            logger.debug("Request %s: %s", request_id, line.rstrip())
            try:
                response = self._handle_message(line)
                if response is not None:
                    sys.stdout.write(response + "\n")
                    sys.stdout.flush()
            except Exception:
                logger.exception("Unhandled error processing message")
                error_resp = self._make_error(-32603, "Internal error")
                sys.stdout.write(error_resp + "\n")
                sys.stdout.flush()

        logger.info("MCP Knowledge Server stopped")


def main() -> None:
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL, logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stderr,
    )

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    store = ArticleStore()
    store.load(KNOWLEDGE_DIR)

    server = MCPServer(store)
    server.run()


if __name__ == "__main__":
    main()
