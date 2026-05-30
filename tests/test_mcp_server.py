"""Tests for MCP Knowledge Server."""

import json
import os
import signal
import subprocess
import sys
import time

import pytest

from mcp_knowledge_server import ArticleStore

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")


# ---------------------------------------------------------------------------
# Unit tests for ArticleStore
# ---------------------------------------------------------------------------


@pytest.fixture
def store() -> ArticleStore:
    s = ArticleStore()
    s.load(FIXTURES_DIR)
    return s


def test_load_entries(store: ArticleStore) -> None:
    assert store.loaded
    assert len(store._entries) >= 6


def test_get_entry_exists(store: ArticleStore) -> None:
    entry = store.get_entry("sse-tech-20250428-001")
    assert entry is not None
    assert entry["title"] == "关于ETF申赎接口规范V3.2发布的通知"


def test_get_entry_not_found(store: ArticleStore) -> None:
    assert store.get_entry("nonexistent-id") is None


def test_get_entry_content_exists(store: ArticleStore) -> None:
    content = store.get_entry_content("sse-tech-20250428-001")
    assert content is not None
    assert "# 关于ETF申赎接口规范V3.2发布的通知" in content


def test_get_entry_content_not_found(store: ArticleStore) -> None:
    assert store.get_entry_content("nonexistent-id") is None


def test_search_basic(store: ArticleStore) -> None:
    result = store.search("ETF", limit=3)
    assert "未找到匹配文章" not in result
    assert "ETF" in result


def test_search_empty_keyword(store: ArticleStore) -> None:
    result = store.search("")
    assert "keyword 不能为空" in result


def test_search_no_match(store: ArticleStore) -> None:
    result = store.search("XYZZYX9876543210")
    assert "未找到匹配文章" in result


def test_search_filter_by_source(store: ArticleStore) -> None:
    result = store.search("接口", limit=10, source="chinaclear")
    assert "chinaclear" in result
    assert "sse-tech" not in result


def test_search_short_keyword(store: ArticleStore) -> None:
    result = store.search("a")
    assert isinstance(result, str)


def test_search_synonym_expansion(store: ArticleStore) -> None:
    result = store.search("交易型开放式指数基金", limit=5)
    assert "未找到匹配文章" not in result


def test_stats(store: ArticleStore) -> None:
    stats = store.get_stats()
    assert "总条目数: 6" in stats
    assert "来源分布" in stats
    assert "类型分布" in stats
    assert "热门标签" in stats


def test_list_resources(store: ArticleStore) -> None:
    result = store.list_resources()
    assert "resources" in result
    assert len(result["resources"]) >= 6


def test_list_resources_with_cursor(store: ArticleStore) -> None:
    result = store.list_resources(cursor=None)
    resources = result["resources"]
    assert len(resources) >= 6
    if "nextCursor" in result:
        cursor = result["nextCursor"]
        next_page = store.list_resources(cursor=cursor)
        assert "resources" in next_page


def test_read_resource_exists(store: ArticleStore) -> None:
    content = store.read_resource("knowledge://sse/entries/sse-tech-20250428-001")
    assert content is not None
    assert "关于ETF申赎接口规范V3.2发布的通知" in content


def test_read_resource_not_found(store: ArticleStore) -> None:
    content = store.read_resource("knowledge://sse/entries/nonexistent")
    assert content is None


# ---------------------------------------------------------------------------
# Unit tests for inverted index builder
# ---------------------------------------------------------------------------


def test_inverted_index_tokenizes_title(store: ArticleStore) -> None:
    idx = store._inverted_index
    has_title_token = False
    for word, docs in idx.items():
        for doc_id, fields in docs.items():
            if doc_id == "sse-tech-20250428-001" and "title" in fields:
                has_title_token = True
                break
    assert has_title_token


def test_inverted_index_tokenizes_content(store: ArticleStore) -> None:
    idx = store._inverted_index
    has_content_token = False
    for word, docs in idx.items():
        for doc_id, fields in docs.items():
            if doc_id == "sse-tech-20250428-001" and "content" in fields:
                has_content_token = True
                break
    assert has_content_token


def test_field_weighting(store: ArticleStore) -> None:
    assert store._entries
    idx = store._inverted_index
    for word, docs in idx.items():
        for doc_id, fields in docs.items():
            for hits in fields.values():
                assert isinstance(hits, (int, float))
                assert hits >= 0


# ---------------------------------------------------------------------------
# Unit tests for synonym expansion
# ---------------------------------------------------------------------------


def test_synonym_map_has_hardcoded(store: ArticleStore) -> None:
    assert "ETF" in store._synonym_map
    assert "交易型开放式指数基金" in store._synonym_map["ETF"]


def test_synonym_expansion_during_search(store: ArticleStore) -> None:
    result = store.search("科创板", limit=5)
    assert result and "未找到匹配文章" not in result


def test_synonym_auto_discovery(store: ArticleStore) -> None:
    syns = store._synonym_map
    for term in syns:
        assert isinstance(term, str), f"Synonym key not string: {term}"
        assert isinstance(syns[term], list), f"Synonym value not list: {term}"


# ---------------------------------------------------------------------------
# Integration tests with subprocess
# ---------------------------------------------------------------------------


def test_initialize_and_tools_list() -> None:
    env = os.environ.copy()
    env["LOG_LEVEL"] = "ERROR"
    env["KNOWLEDGE_DIR"] = os.path.join(os.path.dirname(__file__), "fixtures")
    env["PYTHONIOENCODING"] = "utf-8"

    proc = subprocess.Popen(
        [sys.executable, "-m", "mcp_knowledge_server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        text=True,
        encoding="utf-8",
    )

    try:

        def send(msg: dict) -> dict:
            proc.stdin.write(json.dumps(msg) + "\n")
            proc.stdin.flush()
            return json.loads(proc.stdout.readline().strip())

        resp = send({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
        assert resp.get("id") == 1
        assert "result" in resp
        assert "capabilities" in resp["result"]
        assert "serverInfo" in resp["result"]

        resp2 = send({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        assert resp2.get("id") == 2
        assert "result" in resp2
        tools = resp2["result"]["tools"]
        tool_names = [t["name"] for t in tools]
        assert "search_articles" in tool_names
        assert "get_article" in tool_names
        assert "get_article_content" in tool_names
        assert "knowledge_stats" in tool_names

    finally:
        proc.send_signal(signal.SIGTERM)
        proc.wait(timeout=5)


def test_search_articles_integration() -> None:
    env = os.environ.copy()
    env["LOG_LEVEL"] = "ERROR"
    env["KNOWLEDGE_DIR"] = os.path.join(os.path.dirname(__file__), "fixtures")
    env["PYTHONIOENCODING"] = "utf-8"

    proc = subprocess.Popen(
        [sys.executable, "-m", "mcp_knowledge_server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        text=True,
        encoding="utf-8",
    )

    try:

        def send(msg: dict) -> dict:
            proc.stdin.write(json.dumps(msg) + "\n")
            proc.stdin.flush()
            return json.loads(proc.stdout.readline().strip())

        send({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})

        resp = send(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {
                    "name": "search_articles",
                    "arguments": {"keyword": "ETF", "limit": 3},
                },
            }
        )
        assert resp.get("id") == 2
        assert "result" in resp

    finally:
        proc.send_signal(signal.SIGTERM)
        proc.wait(timeout=5)


def test_get_article_and_content_integration() -> None:
    env = os.environ.copy()
    env["LOG_LEVEL"] = "ERROR"
    env["KNOWLEDGE_DIR"] = os.path.join(os.path.dirname(__file__), "fixtures")
    env["PYTHONIOENCODING"] = "utf-8"

    proc = subprocess.Popen(
        [sys.executable, "-m", "mcp_knowledge_server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        text=True,
        encoding="utf-8",
    )

    try:

        def send(msg: dict) -> dict:
            proc.stdin.write(json.dumps(msg) + "\n")
            proc.stdin.flush()
            return json.loads(proc.stdout.readline().strip())

        send({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})

        resp = send(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {
                    "name": "get_article",
                    "arguments": {"article_id": "sse-tech-20250428-001"},
                },
            }
        )
        assert resp.get("id") == 2
        assert "result" in resp

        resp2 = send(
            {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {
                    "name": "get_article_content",
                    "arguments": {
                        "article_id": "sse-tech-20250428-001",
                        "offset": 0,
                        "limit": 100,
                    },
                },
            }
        )
        assert resp2.get("id") == 3
        assert "result" in resp2

    finally:
        proc.send_signal(signal.SIGTERM)
        proc.wait(timeout=5)


def test_knowledge_stats_integration() -> None:
    env = os.environ.copy()
    env["LOG_LEVEL"] = "ERROR"
    env["KNOWLEDGE_DIR"] = os.path.join(os.path.dirname(__file__), "fixtures")
    env["PYTHONIOENCODING"] = "utf-8"

    proc = subprocess.Popen(
        [sys.executable, "-m", "mcp_knowledge_server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        text=True,
        encoding="utf-8",
    )

    try:

        def send(msg: dict) -> dict:
            proc.stdin.write(json.dumps(msg) + "\n")
            proc.stdin.flush()
            return json.loads(proc.stdout.readline().strip())

        send({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})

        resp = send(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {"name": "knowledge_stats", "arguments": {}},
            }
        )
        assert resp.get("id") == 2
        assert "result" in resp

    finally:
        proc.send_signal(signal.SIGTERM)
        proc.wait(timeout=5)


def test_resources_list_and_read_integration() -> None:
    env = os.environ.copy()
    env["LOG_LEVEL"] = "ERROR"
    env["KNOWLEDGE_DIR"] = os.path.join(os.path.dirname(__file__), "fixtures")
    env["PYTHONIOENCODING"] = "utf-8"

    proc = subprocess.Popen(
        [sys.executable, "-m", "mcp_knowledge_server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        text=True,
        encoding="utf-8",
    )

    try:

        def send(msg: dict) -> dict:
            proc.stdin.write(json.dumps(msg) + "\n")
            proc.stdin.flush()
            return json.loads(proc.stdout.readline().strip())

        send({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})

        resp = send(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "resources/list",
                "params": {},
            }
        )
        assert resp.get("id") == 2
        assert "result" in resp
        resources = resp["result"]["resources"]
        assert len(resources) >= 6

        if resources:
            uri = resources[0]["uri"]
            resp2 = send(
                {
                    "jsonrpc": "2.0",
                    "id": 3,
                    "method": "resources/read",
                    "params": {"uri": uri},
                }
            )
            assert resp2.get("id") == 3
            assert "result" in resp2

    finally:
        proc.send_signal(signal.SIGTERM)
        proc.wait(timeout=5)


def test_error_scenarios() -> None:
    env = os.environ.copy()
    env["LOG_LEVEL"] = "ERROR"
    env["KNOWLEDGE_DIR"] = os.path.join(os.path.dirname(__file__), "fixtures")
    env["PYTHONIOENCODING"] = "utf-8"

    proc = subprocess.Popen(
        [sys.executable, "-m", "mcp_knowledge_server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        text=True,
        encoding="utf-8",
    )

    try:

        def send(msg: dict) -> dict:
            proc.stdin.write(json.dumps(msg) + "\n")
            proc.stdin.flush()
            return json.loads(proc.stdout.readline().strip())

        send({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})

        proc.stdin.write("not json\n")
        proc.stdin.flush()
        resp_line = proc.stdout.readline().strip()
        if resp_line:
            resp_invalid_json = json.loads(resp_line)
            assert resp_invalid_json.get("error", {}).get("code") == -32700

        resp_unknown_method = send(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "unknown_method",
            }
        )
        assert resp_unknown_method.get("error", {}).get("code") == -32601

        resp_unknown_tool = send(
            {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {"name": "nonexistent_tool", "arguments": {}},
            }
        )
        assert "error" in resp_unknown_tool
        assert resp_unknown_tool["error"]["code"] in (-32602,)

        not_found = send(
            {
                "jsonrpc": "2.0",
                "id": 4,
                "method": "tools/call",
                "params": {
                    "name": "get_article",
                    "arguments": {"article_id": "nonexistent-id"},
                },
            }
        )
        assert "result" in not_found

    finally:
        proc.send_signal(signal.SIGTERM)
        proc.wait(timeout=5)


def test_graceful_shutdown() -> None:
    env = os.environ.copy()
    env["LOG_LEVEL"] = "ERROR"
    env["KNOWLEDGE_DIR"] = os.path.join(os.path.dirname(__file__), "fixtures")
    env["PYTHONIOENCODING"] = "utf-8"

    proc = subprocess.Popen(
        [sys.executable, "-m", "mcp_knowledge_server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        text=True,
        encoding="utf-8",
    )

    time.sleep(0.3)

    proc.send_signal(signal.SIGTERM)
    try:
        proc.wait(timeout=5)
        assert proc.returncode is not None, "Process did not exit on SIGTERM"
    except subprocess.TimeoutExpired:
        proc.kill()
        pytest.fail("Server did not exit on SIGTERM")
