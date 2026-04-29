"""中国结算业务规则文档采集与下载 API.

数据源：http://www.chinaclear.cn/zdjs/fywgz/law_flist.shtml

栏目结构（一级 → 二级 → 三级）：
  法律规则 → 业务规则 → {
      账户管理, 登记与存管, 清算与交收, 证券发行, 债券业务,
      股票期权, 融资融券与转融通, 基金与资产管理业务,
      涉外与跨境业务, 协助执法, 其他, 已废止业务规则
  }

页面特征：
  规则列表通过 <iframe> 加载子页面 `law_flist/code_1.shtml`，
  支持分页 `code_1_{n}.shtml`。每页完整渲染所有条目，可直接解析。

爬取字段说明：
  title          — 规则标题（取自 <a> 文本或 title 属性）
  publish_date   — 发布日期（取自 <span class="date">）
  url            — PDF/HTML 原文链接
  sub_category   — 二级栏目中文名（如"账户管理"）
  category       — 一级栏目名，固定为"业务规则"
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

BASE_URL = "http://www.chinaclear.cn"
RAW_STORAGE = Path("knowledge/raw/chinaclear")

SUBCATEGORIES: dict[str, str] = {
    "账户管理": "/zdjs/fzhgl/law_flist/",
    "登记与存管": "/zdjs/fdjycg/law_flist/",
    "清算与交收": "/zdjs/fqsyjs/law_flist/",
    "证券发行": "/zdjs/zqfb/law_flist/",
    "债券业务": "/zdjs/zqyw/law_flist/",
    "股票期权": "/zdjs/gpqq/law_flist/",
    "融资融券与转融通": "/zdjs/rzrqyzrt/law_flist/",
    "基金与资产管理业务": "/zdjs/kfsjje/law_flist/",
    "涉外与跨境业务": "/zdjs/fswyw/law_flist/",
    "协助执法": "/zdjs/fxzzf/law_flist/",
    "其他": "/zdjs/fqt/law_flist/",
    "已废止业务规则": "/zdjs/yfzywgz/law_flist/",
}

CATEGORY_NAME = "业务规则"
_DOWNLOADABLE_EXTS = {"pdf", "doc", "docx", "xls", "xlsx", "zip", "rar", "txt"}


@dataclass
class CsdcDocItem:
    """中国结算业务规则单条文档记录。."""

    title: str
    publish_date: str
    url: str
    category: str
    sub_category: str
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
            "sub_category": self.sub_category,
            "file_format": self.file_format,
            "file_size": self.file_size,
            "local_path": self.local_path,
            "crawl_time": self.crawl_time,
        }


def _is_downloadable(item: CsdcDocItem) -> bool:
    return item.file_format in _DOWNLOADABLE_EXTS


def _safe_filename(item: CsdcDocItem) -> str:
    import re

    date_part = item.publish_date.replace("-", "") if item.publish_date else "unknown"
    safe_title = re.sub(r'[<>:"/\\|?*]', "_", item.title)[:80]
    return f"{date_part}_{safe_title}.{item.file_format}"


def _infer_file_format(url: str) -> str:
    ext = url.rsplit(".", 1)[-1].split("?")[0].lower()
    known = {"pdf", "doc", "docx", "xls", "xlsx", "zip", "rar", "txt", "html", "shtml"}
    return ext if ext in known else "html"


def _build_page_url(sub_category_path: str, page: int) -> str:
    """构建 iframe 内容页 URL。."""
    path = sub_category_path.rstrip("/")
    if page <= 1:
        return urljoin(BASE_URL, f"{path}/code_1.shtml")
    return urljoin(BASE_URL, f"{path}/code_1_{page}.shtml")


def _parse_list_html(
    html: str, sub_category: str, max_items: int | None = None
) -> list[CsdcDocItem]:
    """解析 iframe 列表 HTML，返回文档项列表。."""
    soup = BeautifulSoup(html, "html.parser")
    items: list[CsdcDocItem] = []

    for li in soup.select("li.item"):
        a_tag = li.find("a")
        date_span = li.find("span", class_="date")
        if not isinstance(a_tag, Tag):
            continue

        title = (a_tag.get("title") or a_tag.get_text(strip=True) or "").strip()
        if not title:
            continue

        href = a_tag.get("href", "")
        url = urljoin(BASE_URL, href)
        publish_date = (
            date_span.get_text(strip=True) if isinstance(date_span, Tag) else ""
        )
        file_format = _infer_file_format(url)

        items.append(
            CsdcDocItem(
                title=title,
                publish_date=publish_date,
                url=url,
                category=CATEGORY_NAME,
                sub_category=sub_category,
                file_format=file_format,
            )
        )
        if max_items and len(items) >= max_items:
            break

    return items


def _get_total_pages(html: str) -> int:
    """从 HTML 中提取总页数。."""
    import re

    match = re.search(r"newCreatePageHTML\([^,]+,[^,]+,[^,]+,[^,]+,[^,]+,(\d+)\)", html)
    if match:
        return int(match.group(1))
    return 1


def _fetch_paginated(
    sub_category_name: str,
    sub_path: str,
    max_pages: int,
    max_items: int | None,
    request_delay: float,
) -> list[CsdcDocItem]:
    """带分页的内部采集逻辑。"""
    all_items: list[CsdcDocItem] = []
    with httpx.Client(timeout=30, follow_redirects=True) as client:
        for page in range(1, max_pages + 1):
            url = _build_page_url(sub_path, page)
            try:
                resp = client.get(url, headers={"User-Agent": "Mozilla/5.0"})
                resp.encoding = "utf-8"
                resp.raise_for_status()
            except httpx.HTTPError as exc:
                logger.warning(
                    "请求失败 [%s] page=%d: %s", sub_category_name, page, exc
                )
                break

            items = _parse_list_html(resp.text, sub_category_name, max_items)
            if not items:
                logger.info("无更多条目 [%s] page=%d，停止", sub_category_name, page)
                break

            all_items.extend(items)
            logger.info(
                "采集 [%s] page=%d -> %d 条 (累计 %d)",
                sub_category_name,
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


def fetch_subcategory(
    sub_category_name: str,
    max_pages: int = 10,
    max_items: int | None = None,
    request_delay: float = 1.0,
) -> list[CsdcDocItem]:
    """采集指定二级子栏目的规则列表。.

    Args:
        sub_category_name: 子栏目中文名（如 "账户管理"），需在 SUBCATEGORIES 中。
        max_pages: 最大爬取页数。
        max_items: 最大爬取条目数。
        request_delay: 请求间隔（秒）。

    Returns:
        文档项列表。

    Raises:
        ValueError: 子栏目名称不存在。

    """
    if sub_category_name not in SUBCATEGORIES:
        raise ValueError(
            f"未知子栏目: {sub_category_name}，可选: {list(SUBCATEGORIES.keys())}"
        )

    return _fetch_paginated(
        sub_category_name,
        SUBCATEGORIES[sub_category_name],
        max_pages,
        max_items,
        request_delay,
    )


def fetch_all_subcategories(
    max_pages_per_sub: int = 5,
    max_items_per_sub: int | None = None,
    request_delay: float = 1.0,
) -> dict[str, list[CsdcDocItem]]:
    """采集所有业务规则子栏目。.

    Returns:
        {子栏目名: [文档项, ...]} 字典。

    """
    result: dict[str, list[CsdcDocItem]] = {}
    for name in SUBCATEGORIES:
        logger.info("开始采集子栏目: %s", name)
        result[name] = fetch_subcategory(
            name,
            max_pages=max_pages_per_sub,
            max_items=max_items_per_sub,
            request_delay=request_delay,
        )
    return result


def download_doc(
    item: CsdcDocItem,
    storage_dir: Path = RAW_STORAGE,
    client: httpx.Client | None = None,
    overwrite: bool = False,
) -> CsdcDocItem:
    """下载单个文档文件到本地。."""
    if not _is_downloadable(item):
        return item

    sub_dir = storage_dir / item.sub_category
    sub_dir.mkdir(parents=True, exist_ok=True)

    filename = _safe_filename(item)
    local_path = sub_dir / filename

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


def download_subcategory(
    items: list[CsdcDocItem],
    storage_dir: Path = RAW_STORAGE,
    overwrite: bool = False,
    request_delay: float = 0.5,
    max_workers: int = 3,
) -> list[CsdcDocItem]:
    """批量下载子栏目文档。."""
    import concurrent.futures

    results: list[CsdcDocItem] = []
    with httpx.Client(timeout=60, follow_redirects=True) as client:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_map: dict[concurrent.futures.Future, CsdcDocItem] = {}

            def _submit(item: CsdcDocItem) -> concurrent.futures.Future:
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
