"""Tests for collect incremental (since_date / last_crawl_date)."""

from unittest.mock import MagicMock, patch

import pytest

from pipeline.pipeline import PipelineState


# ---------------------------------------------------------------------------
# PipelineState: last_crawl_date 存储与状态管理
# ---------------------------------------------------------------------------


class TestPipelineStateLastCrawlDate:
    """验证 PipelineState 按 source 独立存储 last_crawl_date 的能力。"""

    def test_default_no_last_crawl_date(self, tmp_path):
        """新创建的 state 中 last_crawl_date 默认不存在。"""
        state = PipelineState(path=tmp_path / "state.json")
        assert state.get_last_crawl_date("sse") is None

    def test_set_and_get(self, tmp_path):
        """设置后能正确读取。"""
        state = PipelineState(path=tmp_path / "state.json")
        state.set_last_crawl_date("sse", "2026-06-14")
        assert state.get_last_crawl_date("sse") == "2026-06-14"

    def test_per_source_independence(self, tmp_path):
        """不同 source 的 last_crawl_date 互不影响。"""
        state = PipelineState(path=tmp_path / "state.json")
        state.set_last_crawl_date("sse", "2026-06-14")
        state.set_last_crawl_date("szse", "2026-06-10")
        assert state.get_last_crawl_date("sse") == "2026-06-14"
        assert state.get_last_crawl_date("szse") == "2026-06-10"

    def test_set_saves_immediately(self, tmp_path):
        """set_last_crawl_date 后立即持久化，新实例能读到。"""
        state = PipelineState(path=tmp_path / "state.json")
        state.set_last_crawl_date("sse", "2026-06-14")
        state2 = PipelineState(path=tmp_path / "state.json")
        assert state2.get_last_crawl_date("sse") == "2026-06-14"

    def test_reset_clears_last_crawl_date(self, tmp_path):
        """reset() 后 last_crawl_date 被清空，下次全量爬取。"""
        state = PipelineState(path=tmp_path / "state.json")
        state.set_last_crawl_date("sse", "2026-06-14")
        state.reset()
        assert state.get_last_crawl_date("sse") is None


# ---------------------------------------------------------------------------
# SSE _fetch_paginated: since_date 截断逻辑
# ---------------------------------------------------------------------------


@pytest.fixture
def sse_items():
    """构造可控制 publish_date 的 SSE 文档项。"""
    from utils.sse_tech_support_doc_api import SseDocItem

    def make(date: str) -> SseDocItem:
        return SseDocItem(
            title=f"doc-{date}",
            publish_date=date,
            url=f"https://example.com/{date}.pdf",
            category="测试栏目",
            file_format="pdf",
        )

    return make


class TestSseFetchPaginated:
    """验证 SSE _fetch_paginated 传入 since_date 后的截断行为。"""

    def test_since_date_stops_at_all_old_page(self, sse_items):
        """第 2 页全旧（均 < since_date）时停止翻页，不返回第 2 页的项。"""
        from utils.sse_tech_support_doc_api import _fetch_paginated

        CATEGORY = "测试栏目"
        PATH = "/test"

        page1 = [sse_items("2026-06-10"), sse_items("2026-06-08")]
        page2 = [sse_items("2026-05-25"), sse_items("2026-05-20")]

        with (
            patch("utils.sse_tech_support_doc_api.httpx.Client") as mock_http,
            patch("utils.sse_tech_support_doc_api._request_page") as mock_req,
            patch("utils.sse_tech_support_doc_api._parse_list_html") as mock_parse,
            patch("utils.sse_tech_support_doc_api._get_total_pages") as mock_pages,
        ):
            mock_req.side_effect = [MagicMock(), MagicMock()]
            mock_parse.side_effect = [page1, page2]
            mock_pages.return_value = 5

            result = _fetch_paginated(
                CATEGORY, PATH,
                max_pages=None, max_items=None,
                request_delay=0.01,
                since_date="2026-06-01",
            )

        # 只返回第 1 页的 2 条
        assert len(result) == 2
        assert result[0].publish_date == "2026-06-10"
        assert result[1].publish_date == "2026-06-08"
        # 第 2 页被请求（用于检查是否全旧），但 items 不被加入结果集
        assert mock_parse.call_count == 2

    def test_since_date_none_fetches_all(self, sse_items):
        """since_date=None 时行为不变，所有页面全部返回。"""
        from utils.sse_tech_support_doc_api import _fetch_paginated

        CATEGORY = "测试栏目"
        PATH = "/test"

        page1 = [sse_items("2026-06-10")]
        page2 = [sse_items("2026-05-20")]

        with (
            patch("utils.sse_tech_support_doc_api.httpx.Client") as mock_http,
            patch("utils.sse_tech_support_doc_api._request_page") as mock_req,
            patch("utils.sse_tech_support_doc_api._parse_list_html") as mock_parse,
            patch("utils.sse_tech_support_doc_api._get_total_pages") as mock_pages,
        ):
            mock_req.side_effect = [MagicMock(), MagicMock(), None]
            mock_parse.side_effect = [page1, page2, []]
            mock_pages.return_value = 3

            result = _fetch_paginated(
                CATEGORY, PATH,
                max_pages=None, max_items=None,
                request_delay=0.01,
                since_date=None,
            )

        assert len(result) == 2

    def test_mixed_page_does_not_trigger_stop(self, sse_items):
        """页内新旧混杂（既有 >= since_date 又有 < since_date）时继续翻页，不截断。"""
        from utils.sse_tech_support_doc_api import _fetch_paginated

        CATEGORY = "测试栏目"
        PATH = "/test"

        # page1 混合：06-10 >= since, 05-20 < since
        page1 = [sse_items("2026-06-10"), sse_items("2026-05-20")]
        # page2 全旧：被截断
        page2 = [sse_items("2026-04-01")]

        with (
            patch("utils.sse_tech_support_doc_api.httpx.Client") as mock_http,
            patch("utils.sse_tech_support_doc_api._request_page") as mock_req,
            patch("utils.sse_tech_support_doc_api._parse_list_html") as mock_parse,
            patch("utils.sse_tech_support_doc_api._get_total_pages") as mock_pages,
        ):
            mock_req.side_effect = [MagicMock(), MagicMock(), None]
            mock_parse.side_effect = [page1, page2, []]
            mock_pages.return_value = 3

            result = _fetch_paginated(
                CATEGORY, PATH,
                max_pages=None, max_items=None,
                request_delay=0.01,
                since_date="2026-06-01",
            )

        # page1 混合 → 2 条全部添加，循环继续
        # page2 全旧 → since_date 触发 break，page2 items 不加入结果
        assert len(result) == 2
        assert result[0].publish_date == "2026-06-10"
        assert result[1].publish_date == "2026-05-20"

    def test_empty_date_not_affect_truncation(self, sse_items):
        """publish_date 为空的文档不参与截断判断，不会阻断翻页。"""
        from utils.sse_tech_support_doc_api import _fetch_paginated

        CATEGORY = "测试栏目"
        PATH = "/test"

        page1 = [sse_items("2026-06-10")]
        item_no_date = sse_items("")
        item_no_date.publish_date = ""
        page2 = [item_no_date]

        with (
            patch("utils.sse_tech_support_doc_api.httpx.Client") as mock_http,
            patch("utils.sse_tech_support_doc_api._request_page") as mock_req,
            patch("utils.sse_tech_support_doc_api._parse_list_html") as mock_parse,
            patch("utils.sse_tech_support_doc_api._get_total_pages") as mock_pages,
        ):
            mock_req.side_effect = [MagicMock(), MagicMock(), None]
            mock_parse.side_effect = [page1, page2, []]
            mock_pages.return_value = 3

            result = _fetch_paginated(
                CATEGORY, PATH,
                max_pages=None, max_items=None,
                request_delay=0.01,
                since_date="2026-06-01",
            )

        # page2 只有空日期文档 → valid_dates 为空 → 不触发截断
        # mock_parse 第 3 次返回空列表停止翻页
        assert len(result) == 2


# ---------------------------------------------------------------------------
# SZSE fetch_category: since_date 截断逻辑（内联分页，与 SSE/CC 结构不同）
# ---------------------------------------------------------------------------


@pytest.fixture
def szse_items():
    """构造可控制 publish_date 的 SZSE 文档项。"""
    from utils.szse_tech_service_doc_api import SzseDocItem

    def make(date: str) -> SzseDocItem:
        return SzseDocItem(
            title=f"doc-{date}",
            publish_date=date,
            url=f"https://szse.example.com/{date}.pdf",
            category="测试公告",
            file_format="pdf",
        )

    return make


class TestSzseFetchCategory:
    """验证 SZSE fetch_category 传入 since_date 后的截断行为。

    SZSE 的分页逻辑内联在 fetch_category 中，与 SSE/CC 的 _fetch_paginated 不同。
    """

    def _make_mock_html_response(self, text: str = "<html><body></body></html>"):
        """构造一个模拟的 HTML 响应，使 BeautifulSoup 能正常解析。"""
        resp = MagicMock()
        resp.status_code = 200
        resp.text = text
        resp.encoding = "utf-8"
        return resp

    def test_since_date_stops_at_all_old_page(self, szse_items):
        """第 2 页全旧时停止翻页（因 extend 在截断前，第 2 页 items 仍加入结果）。"""
        from utils.szse_tech_service_doc_api import fetch_category

        with (
            patch("utils.szse_tech_service_doc_api.httpx.Client") as mock_http,
            patch("utils.szse_tech_service_doc_api._build_page_url") as mock_url,
            patch("utils.szse_tech_service_doc_api._get_page_count") as mock_pages,
            patch("utils.szse_tech_service_doc_api._parse_article_list") as mock_parse,
            patch("utils.szse_tech_service_doc_api.CATEGORIES", {"测试公告": "/test"}),
        ):
            mock_url.return_value = "https://test/"
            mock_pages.return_value = 5
            mock_http.return_value.__enter__.return_value.get.return_value = self._make_mock_html_response()

            page1 = [szse_items("2026-06-10"), szse_items("2026-06-08")]
            page2 = [szse_items("2026-05-25")]
            mock_parse.side_effect = [page1, page2]

            result = fetch_category(
                "测试公告",
                max_pages=None, max_items=None,
                request_delay=0.01,
                since_date="2026-06-01",
            )

        # SZSE 在 extend 之后才执行 since_date 检查，所以第 2 页的 1 条也被加入
        assert len(result) == 3
        # 确认没有继续请求第 3 页
        assert mock_parse.call_count == 2

    def test_since_date_none_fetches_all(self, szse_items):
        """since_date=None 时所有页面均返回。"""
        from utils.szse_tech_service_doc_api import fetch_category

        with (
            patch("utils.szse_tech_service_doc_api.httpx.Client") as mock_http,
            patch("utils.szse_tech_service_doc_api._build_page_url") as mock_url,
            patch("utils.szse_tech_service_doc_api._get_page_count") as mock_pages,
            patch("utils.szse_tech_service_doc_api._parse_article_list") as mock_parse,
            patch("utils.szse_tech_service_doc_api.CATEGORIES", {"测试公告": "/test"}),
        ):
            mock_url.return_value = "https://test/"
            mock_pages.return_value = 3
            mock_http.return_value.__enter__.return_value.get.return_value = self._make_mock_html_response()

            page1 = [szse_items("2026-06-10")]
            page2 = [szse_items("2026-05-20")]
            mock_parse.side_effect = [page1, page2, []]

            result = fetch_category(
                "测试公告",
                max_pages=None, max_items=None,
                request_delay=0.01,
                since_date=None,
            )

        assert len(result) == 2


# ---------------------------------------------------------------------------
# ChinaClear _fetch_paginated: since_date 截断逻辑
# ---------------------------------------------------------------------------


@pytest.fixture
def csdc_items():
    """构造可控制 publish_date 的中国结算文档项。"""
    from utils.csdc_biz_rule_doc_api import CsdcDocItem

    def make(date: str) -> CsdcDocItem:
        return CsdcDocItem(
            title=f"doc-{date}",
            publish_date=date,
            url=f"https://cc.example.com/{date}.pdf",
            category="业务规则",
            sub_category="测试子栏目",
            file_format="pdf",
        )

    return make


class TestCsdcFetchPaginated:
    """验证 ChinaClear _fetch_paginated 传入 since_date 后的截断行为。"""

    def test_since_date_stops_at_all_old_page(self, csdc_items):
        """第 2 页全旧时停止翻页（与 SSE 行为一致）。"""
        from utils.csdc_biz_rule_doc_api import _fetch_paginated

        page1 = [csdc_items("2026-06-10")]
        page2 = [csdc_items("2026-04-01")]

        with (
            patch("utils.csdc_biz_rule_doc_api.httpx.Client") as mock_http,
            patch("utils.csdc_biz_rule_doc_api._build_page_url") as mock_url,
            patch("utils.csdc_biz_rule_doc_api._parse_list_html") as mock_parse,
            patch("utils.csdc_biz_rule_doc_api._get_total_pages") as mock_pages,
        ):
            mock_url.return_value = "https://test/"
            mock_parse.side_effect = [page1, page2]
            mock_pages.return_value = 5

            result = _fetch_paginated(
                "测试子栏目", "/test",
                max_pages=None, max_items=None,
                request_delay=0.01,
                since_date="2026-06-01",
            )

        assert len(result) == 1
        assert result[0].publish_date == "2026-06-10"
