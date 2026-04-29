"""深交所技术服务文档采集与下载 API.

数据源：https://www.szse.cn/marketServices/technicalservice/index.html

栏目结构（一级栏目 → 二级栏目路径）：
  - 技术公告 (notice)       → ./notice/    （动态列表，全量加载 + 前端搜索过滤）
  - 第五代交易系统介绍 (introduce) → ./introduce/  （静态文档列表）
  - 服务指引 (serveGuide)   → ./serveGuide/
  - 数据接口 (interface)    → ./interface/
  - 技术指南 (guide)        → ./guide/

页面特征：
  技术公告页面将所有条目渲染在同一个 HTML 中（articleCount 递增），页码通过
  前端 JS 控制分页展示，实际数据均直接从 DOM 提取。其他栏目为静态文档页面，
  使用与栏目同级的 URL 路径直接提供 PDF 等文件下载。

爬取字段说明：
  title          — 文档标题（取自 <a> 文本或 title 属性）
  publish_date   — 发布日期（取自 <span class="time">）
  url            — 原文/文件链接（相对路径需拼全）
  category       — 一级栏目中文名
  file_format    — 文件格式（从 URL 扩展名推断）
  file_size      — 下载后的文件大小（字节），未下载时为 None
  local_path     — 本地保存路径，未下载时为 None
  crawl_time     — 采集时间戳
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup, Tag

logger = logging.getLogger(__name__)

BASE_URL = "https://www.szse.cn"
TECH_SERVICE_ROOT = "/marketServices/technicalservice"
RAW_STORAGE = Path("knowledge/raw/szse")

CATEGORIES: dict[str, str] = {
    "技术公告": f"{TECH_SERVICE_ROOT}/notice/",
    "交易系统介绍": f"{TECH_SERVICE_ROOT}/introduce/",
    "服务指引": f"{TECH_SERVICE_ROOT}/serveGuide/",
    "数据接口": f"{TECH_SERVICE_ROOT}/interface/",
    "技术指南": f"{TECH_SERVICE_ROOT}/guide/",
}

_DOWNLOADABLE_EXTS = {"pdf", "doc", "docx", "xls", "xlsx", "zip", "rar", "txt"}


@dataclass
class SzseDocItem:
    """深交所技术服务单条文档记录。."""

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


def _is_downloadable(item: SzseDocItem) -> bool:
    """判断是否为可下载的文件类型（非 HTML 页面）。."""
    return item.file_format in _DOWNLOADABLE_EXTS


def _safe_filename(item: SzseDocItem) -> str:
    """从文档项生成安全的本地文件名。."""
    import re

    date_part = item.publish_date.replace("-", "") if item.publish_date else "unknown"
    safe_title = re.sub(r'[<>:"/\\|?*]', "_", item.title)[:80]
    return f"{date_part}_{safe_title}.{item.file_format}"


def _infer_file_format(url: str) -> str:
    ext = url.rsplit(".", 1)[-1].split("?")[0].lower()
    known = {"pdf", "doc", "docx", "xls", "xlsx", "zip", "rar", "txt", "html"}
    return ext if ext in known else "html"


def _resolve_url(href: str) -> str:
    if href.startswith("http://") or href.startswith("https://"):
        return href
    resolved = urljoin(BASE_URL, href)
    return resolved


def _parse_article_list(soup: BeautifulSoup, category: str) -> list[SzseDocItem]:
    """从页面中提取文章列表。."""
    items: list[SzseDocItem] = []

    # 尝试多种列表容器
    for container_sel in (
        "ul.newslist.date-right",
        "ul.newslist",
        ".article-list ul",
        ".g-content-list ul",
    ):
        ul = soup.select_one(container_sel)
        if isinstance(ul, Tag):
            break
    else:
        return items

    for li in ul.find_all("li", recursive=False):
        a_tag = li.find("a")
        time_span = li.find("span", class_="time")

        if not isinstance(a_tag, Tag):
            continue

        title = (a_tag.get("title") or a_tag.get_text(strip=True) or "").strip()
        if not title:
            continue

        href = a_tag.get("href", "")
        url = _resolve_url(href)
        publish_date = (
            time_span.get_text(strip=True) if isinstance(time_span, Tag) else ""
        )
        file_format = _infer_file_format(url)

        items.append(
            SzseDocItem(
                title=title,
                publish_date=publish_date,
                url=url,
                category=category,
                file_format=file_format,
            )
        )

    return items


def fetch_category(
    category_name: str,
    max_items: int | None = None,
    request_delay: float = 0.5,
) -> list[SzseDocItem]:
    """采集指定栏目的文档列表。.

    深交所技术服务页面将所有数据渲染在首屏 HTML 中（包含所有历史条目），
    前端通过 JS 实现客户端分页。本函数一次请求即可获取全量数据。

    Args:
        category_name: 栏目中文名（如 "技术公告"），需在 CATEGORIES 中。
        max_items: 最大爬取条目数。
        request_delay: 请求间隔（秒）。

    Returns:
        文档项列表。

    Raises:
        ValueError: 栏目名称不存在。
        httpx.HTTPError: HTTP 请求失败。

    """
    if category_name not in CATEGORIES:
        raise ValueError(f"未知栏目: {category_name}，可选: {list(CATEGORIES.keys())}")

    url = _resolve_url(CATEGORIES[category_name])
    with httpx.Client(timeout=30, follow_redirects=True) as client:
        try:
            resp = client.get(url, headers={"User-Agent": "Mozilla/5.0"})
            resp.encoding = "utf-8"
            resp.raise_for_status()
        except httpx.HTTPError as exc:
            logger.error("请求失败 [%s]: %s", category_name, exc)
            raise

        soup = BeautifulSoup(resp.text, "html.parser")
        items = _parse_article_list(soup, category_name)

        if max_items:
            items = items[:max_items]

        logger.info("采集 [%s] → %d 条", category_name, len(items))
        time.sleep(request_delay)

    return items


def fetch_all_categories(
    max_items_per_category: int | None = None,
    request_delay: float = 0.5,
) -> dict[str, list[SzseDocItem]]:
    """采集所有栏目的文档列表。.

    Returns:
        {栏目名: [文档项, ...]} 字典。

    """
    result: dict[str, list[SzseDocItem]] = {}
    for name in CATEGORIES:
        logger.info("开始采集栏目: %s", name)
        result[name] = fetch_category(
            name, max_items=max_items_per_category, request_delay=request_delay
        )
    return result


def download_doc(
    item: SzseDocItem,
    storage_dir: Path = RAW_STORAGE,
    client: httpx.Client | None = None,
    overwrite: bool = False,
) -> SzseDocItem:
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

    close_client = False
    if client is None:
        client = httpx.Client(timeout=60, follow_redirects=True)
        close_client = True

    try:
        resp = client.get(item.url, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        local_path.write_bytes(resp.content)
        item.local_path = str(local_path)
        item.file_size = len(resp.content)
        logger.info("已下载: %s (%d bytes)", local_path, item.file_size)
    except httpx.HTTPError as exc:
        logger.warning("下载失败 [%s]: %s", item.title, exc)
    finally:
        if close_client:
            client.close()

    return item


def download_category(
    items: list[SzseDocItem],
    storage_dir: Path = RAW_STORAGE,
    overwrite: bool = False,
    request_delay: float = 0.5,
    max_workers: int = 3,
) -> list[SzseDocItem]:
    """批量下载栏目文档。."""
    import concurrent.futures

    results: list[SzseDocItem] = []
    with httpx.Client(timeout=60, follow_redirects=True) as client:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_map: dict[concurrent.futures.Future, SzseDocItem] = {}

            def _submit(item: SzseDocItem) -> concurrent.futures.Future:
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
