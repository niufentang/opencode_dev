"""上交所交易技术支持专区文档采集与下载 API.

数据源：https://www.sse.com.cn/services/tradingtech/home/

栏目结构（一级栏目 → 二级栏目路径）：
  - 技术通知 (notice)         → /services/tradingtech/notice/
  - 服务指引 (services)       → /services/tradingtech/services/
  - 技术接口 (data)           → /services/tradingtech/data/
  - 技术指南 (policy)         → /services/tradingtech/policy/
  - 软件下载 (download)       → /services/tradingtech/download/
  - 测试文档 (development)    → /services/tradingtech/development/
  - 技术杂志 (transaction)    → /services/tradingtech/transaction/
  - 历史资料 (historicaldata) → /services/tradingtech/historicaldata/

分页机制：
  每个栏目通过 `s_list.shtml` 提供列表片段，分页 URL 格式为：
    {category}/s_list.shtml      — 第 1 页
    {category}/s_list_{n}.shtml  — 第 n 页

爬取字段说明：
  title          — 文档标题（取自 <a> 的 title 属性）
  publish_date   — 发布日期（取自 <span> 文本，格式 YYYY-MM-DD）
  url            — 原文/文件链接
  category       — 一级栏目中文名
  file_format    — 文件格式（从 URL 扩展名推断：pdf/doc/docx/xlsx/zip/shtml 等）
  file_size      — 下载后的文件大小（字节），未下载时为 None
  local_path     — 本地保存路径，未下载时为 None
  crawl_time     — 采集时间戳
"""

from __future__ import annotations

import logging
import re
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup, Tag

logger = logging.getLogger(__name__)

BASE_URL = "https://www.sse.com.cn"
RAW_STORAGE = Path("knowledge/raw/sse")

CATEGORIES: dict[str, str] = {
    "技术通知": "/services/tradingtech/notice/",
    "服务指引": "/services/tradingtech/services/",
    "技术接口": "/services/tradingtech/data/",
    "技术指南": "/services/tradingtech/policy/",
    "软件下载": "/services/tradingtech/download/",
    "测试文档": "/services/tradingtech/development/",
    "技术杂志": "/services/tradingtech/transaction/",
    "历史资料": "/services/tradingtech/historicaldata/",
}

_DOWNLOADABLE_EXTS = {"pdf", "doc", "docx", "xls", "xlsx", "zip", "rar", "txt"}


@dataclass
class SseDocItem:
    """上交所交易技术支持专区单条文档记录。."""

    title: str
    publish_date: str
    url: str
    category: str
    file_format: str
    file_size: int | None = None
    local_path: str | None = None
    crawl_time: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> dict[str, Any]:
        """转换为字典。"""
        return {
            "title": self.title,
            "publish_date": self.publish_date,
            "url": self.url,
            "category": self.category,
            "file_format": self.file_format,
            "file_size": self.file_size,
            "local_path": self.local_path,
            "crawl_time": self.crawl_time,
        }


def _infer_file_format(url: str) -> str:
    """从 URL 中推断文件格式。."""
    ext = url.rsplit(".", 1)[-1].split("?")[0].lower()
    known = {
        "pdf",
        "doc",
        "docx",
        "xls",
        "xlsx",
        "zip",
        "rar",
        "txt",
        "xml",
        "html",
        "shtml",
    }
    return ext if ext in known else "html"


def _build_page_url(category_path: str, page: int) -> str:
    """构建分页 URL。."""
    path = category_path.rstrip("/")
    if page <= 1:
        return urljoin(BASE_URL, f"{path}/s_list.shtml")
    return urljoin(BASE_URL, f"{path}/s_list_{page}.shtml")


def _parse_list_html(
    html: str, category: str, max_items: int | None = None
) -> list[SseDocItem]:
    """解析栏目列表 HTML 片段，返回文档项列表。."""
    soup = BeautifulSoup(html, "html.parser")
    items: list[SseDocItem] = []

    for dd in soup.select("dl dd"):
        a_tag = dd.find("a")
        span_tag = dd.find("span")
        if not isinstance(a_tag, Tag):
            continue

        title = (a_tag.get("title") or a_tag.get_text(strip=True) or "").strip()
        if not title:
            continue

        href = a_tag.get("href", "")
        url = urljoin(BASE_URL, href)
        publish_date = (
            span_tag.get_text(strip=True) if isinstance(span_tag, Tag) else ""
        )
        file_format = _infer_file_format(url)

        items.append(
            SseDocItem(
                title=title,
                publish_date=publish_date,
                url=url,
                category=category,
                file_format=file_format,
            )
        )
        if max_items and len(items) >= max_items:
            break

    return items


def _get_total_pages(html: str) -> int:
    """从 HTML 中提取总页数。."""
    import re

    match = re.search(r"createPageHTML\([^,]+,[^,]+,[^,]+,[^,]+,[^,]+,(\d+)\)", html)
    if match:
        return int(match.group(1))
    return 1


def _fetch_paginated(
    category_name: str,
    category_path: str,
    max_pages: int,
    max_items: int | None,
    request_delay: float,
) -> list[SseDocItem]:
    """带分页的内部采集逻辑。"""
    all_items: list[SseDocItem] = []
    with httpx.Client(timeout=30, follow_redirects=True) as client:
        for page in range(1, max_pages + 1):
            url = _build_page_url(category_path, page)
            resp = _request_page(client, url, category_name, page)
            if resp is None:
                break

            items = _parse_list_html(resp.text, category_name, max_items)
            if not items:
                logger.info("无更多条目 [%s] page=%d，停止", category_name, page)
                break

            all_items.extend(items)
            logger.info(
                "采集 [%s] page=%d -> %d 条 (累计 %d)",
                category_name,
                page,
                len(items),
                len(all_items),
            )

            if max_items and len(all_items) >= max_items:
                return all_items[:max_items]

            total_pages = _get_total_pages(resp.text)
            if page >= total_pages:
                break

            time.sleep(request_delay)
    return all_items


def _request_page(
    client: httpx.Client, url: str, label: str, page: int
) -> httpx.Response | None:
    """请求单页并返回响应，失败时返回 None。"""
    try:
        resp = client.get(url, headers={"User-Agent": "Mozilla/5.0"})
        resp.encoding = "utf-8"
        resp.raise_for_status()
        return resp
    except httpx.HTTPError as exc:
        logger.warning("请求失败 [%s] page=%d: %s", label, page, exc)
        return None


def fetch_category(
    category_name: str,
    max_pages: int = 10,
    max_items: int | None = None,
    request_delay: float = 1.0,
) -> list[SseDocItem]:
    """采集指定栏目的文档列表。.

    Args:
        category_name: 栏目中文名（如 "技术通知"），需在 CATEGORIES 中。
        max_pages: 最大爬取页数。
        max_items: 最大爬取条目数。
        request_delay: 请求间隔（秒）。

    Returns:
        文档项列表。

    Raises:
        ValueError: 栏目名称不存在。

    """
    if category_name not in CATEGORIES:
        raise ValueError(f"未知栏目: {category_name}，可选: {list(CATEGORIES.keys())}")

    return _fetch_paginated(
        category_name,
        CATEGORIES[category_name],
        max_pages,
        max_items,
        request_delay,
    )


def fetch_all_categories(
    max_pages_per_category: int = 5,
    max_items_per_category: int | None = None,
    request_delay: float = 1.0,
) -> dict[str, list[SseDocItem]]:
    """采集所有栏目的文档列表。.

    Returns:
        {栏目名: [文档项, ...]} 字典。

    """
    result: dict[str, list[SseDocItem]] = {}
    for name in CATEGORIES:
        logger.info("开始采集栏目: %s", name)
        result[name] = fetch_category(
            name,
            max_pages=max_pages_per_category,
            max_items=max_items_per_category,
            request_delay=request_delay,
        )
    return result


def _is_downloadable(item: SseDocItem) -> bool:
    """判断是否为可下载的文件类型（非 HTML/SHTML 页面）。."""
    return item.file_format in _DOWNLOADABLE_EXTS


def _safe_filename(item: SseDocItem) -> str:
    """从文档项生成安全的本地文件名。."""
    date_part = item.publish_date.replace("-", "") if item.publish_date else "unknown"
    safe_title = re.sub(r'[<>:"/\\|?*]', "_", item.title)[:80]
    return f"{date_part}_{safe_title}.{item.file_format}"


def download_doc(
    item: SseDocItem,
    storage_dir: Path = RAW_STORAGE,
    client: httpx.Client | None = None,
    overwrite: bool = False,
) -> SseDocItem:
    """下载单个文档文件到本地。."""
    if not _is_downloadable(item):
        return item

    category_dir = storage_dir / item.category
    category_dir.mkdir(parents=True, exist_ok=True)

    filename = _safe_filename(item)
    local_path = category_dir / filename

    if local_path.exists() and not overwrite:
        item.local_path = str(local_path)
        item.file_size = local_path.stat().st_size
        return item

    if client is None:
        client = httpx.Client(timeout=60, follow_redirects=True)

    try:
        resp = client.get(item.url, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        local_path.write_bytes(resp.content)
        item.local_path = str(local_path)
        item.file_size = len(resp.content)
        logger.info("已下载: %s (%d bytes)", local_path, item.file_size)
    except httpx.HTTPError as exc:
        logger.warning("下载失败 [%s]: %s", item.title, exc)

    return item


def download_category(
    items: list[SseDocItem],
    storage_dir: Path = RAW_STORAGE,
    overwrite: bool = False,
    request_delay: float = 0.5,
    max_workers: int = 3,
) -> list[SseDocItem]:
    """批量下载栏目文档。.

    Args:
        items: 文档项列表。
        storage_dir: 存储根目录。
        overwrite: 是否覆盖已存在的文件。
        request_delay: 请求间隔（秒）。
        max_workers: 并发下载数。

    Returns:
        更新后的文档项列表。

    """
    import concurrent.futures

    results: list[SseDocItem] = []
    with httpx.Client(timeout=60, follow_redirects=True) as client:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_map: dict[concurrent.futures.Future, SseDocItem] = {}

            def _submit(item: SseDocItem) -> concurrent.futures.Future:
                return executor.submit(
                    download_doc, item, storage_dir, client, overwrite
                )

            for item in items:
                future = _submit(item)
                future_map[future] = item
                time.sleep(request_delay)

            for future in concurrent.futures.as_completed(future_map):
                try:
                    results.append(future.result())
                except Exception as exc:
                    logger.error("下载异常: %s", exc)
                    results.append(future_map[future])

    return results
