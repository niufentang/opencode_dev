"""深交所技术服务 — 采集与下载验证脚本。

用法：
    python test/test_szse.py                  # 默认：采集全部栏目 + 下载 3 个文件
    python test/test_szse.py --category 数据接口
    python test/test_szse.py --no-download
    python test/test_szse.py --download-only
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils.szse_tech_service_doc_api import (
    CATEGORIES,
    SzseDocItem,
    download_category,
    fetch_all_categories,
    fetch_category,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("test_szse")


def run(args: argparse.Namespace) -> None:
    """执行采集与下载流程。"""
    if args.download_only:
        metadata_file = Path("knowledge/raw/szse/metadata.json")
        if not metadata_file.exists():
            logger.error("--download-only 需要先运行采集生成 metadata.json")
            sys.exit(1)
        all_items = json.loads(metadata_file.read_text(encoding="utf-8"))
    elif args.category:
        logger.info("采集栏目: %s", args.category)
        items = fetch_category(args.category, max_items=args.max_items)
        all_items = {args.category: [it.to_dict() for it in items]}
    else:
        logger.info("采集全部 %d 个栏目", len(CATEGORIES))
        result = fetch_all_categories(max_items_per_category=args.max_items)
        all_items = {k: [it.to_dict() for it in v] for k, v in result.items()}

    total = sum(len(v) for v in all_items.values())
    logger.info("元数据合计 %d 条", total)

    meta_dir = Path("knowledge/raw/szse")
    meta_dir.mkdir(parents=True, exist_ok=True)
    meta_file = meta_dir / "metadata.json"
    meta_file.write_text(
        json.dumps(all_items, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    logger.info("元数据已保存: %s", meta_file)

    if args.no_download:
        return

    flat: list[SzseDocItem] = []
    for cat_items in all_items.values():
        flat.extend(SzseDocItem(**it) for it in cat_items)

    dl_items = [it for it in flat if it.file_format != "html"]
    logger.info(
        "可下载文件 %d 个，开始下载 %d 个",
        len(dl_items),
        min(args.download_n, len(dl_items)),
    )

    results = download_category(
        dl_items[: args.download_n],
        request_delay=args.request_delay,
        max_workers=args.max_workers,
    )

    ok = sum(1 for r in results if r.local_path)
    fail = sum(1 for r in results if not r.local_path)
    logger.info("下载完成: 成功 %d, 失败 %d", ok, fail)


def main() -> None:
    """解析命令行参数并启动采集。"""
    parser = argparse.ArgumentParser(description="深交所技术服务 验证脚本")
    parser.add_argument("--category", choices=list(CATEGORIES), help="指定栏目")
    parser.add_argument("--max-items", type=int, help="每栏目最大条目数")
    parser.add_argument("--download-n", type=int, default=3, help="下载文件数 (默认 3)")
    parser.add_argument(
        "--request-delay", type=float, default=0.5, help="请求间隔秒数 (默认 0.5)"
    )
    parser.add_argument(
        "--max-workers", type=int, default=3, help="并发下载数 (默认 3)"
    )
    parser.add_argument("--no-download", action="store_true", help="仅采集元数据")
    parser.add_argument(
        "--download-only", action="store_true", help="仅从已有元数据下载"
    )
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
