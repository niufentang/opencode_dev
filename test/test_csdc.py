"""中国结算业务规则 — 采集与下载验证脚本。

用法：
    python test/test_csdc.py                  # 默认：采集全部子栏目、每栏 5 页、全部下载
    python test/test_csdc.py --sub-category 账户管理
    python test/test_csdc.py --max-pages 3 --download-n 10
    python test/test_csdc.py --no-download
    python test/test_csdc.py --download-only
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils.csdc_biz_rule_doc_api import (
    SUBCATEGORIES,
    CsdcDocItem,
    download_subcategory,
    fetch_all_subcategories,
    fetch_subcategory,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("test_csdc")


def run(args: argparse.Namespace) -> None:
    """执行采集与下载流程。"""
    max_pages = args.max_pages if args.max_pages > 0 else None
    if args.download_only:
        metadata_file = Path("knowledge/raw/chinaclear/metadata.json")
        if not metadata_file.exists():
            logger.error("--download-only 需要先运行采集生成 metadata.json")
            sys.exit(1)
        all_items = json.loads(metadata_file.read_text(encoding="utf-8"))
    elif args.sub_category:
        logger.info("采集子栏目: %s", args.sub_category)
        items = fetch_subcategory(
            args.sub_category,
            max_pages=max_pages,
            max_items=args.max_items,
        )
        all_items = {args.sub_category: [it.to_dict() for it in items]}
    else:
        logger.info("采集全部 %d 个子栏目", len(SUBCATEGORIES))
        result = fetch_all_subcategories(
            max_pages_per_sub=max_pages,
            max_items_per_sub=args.max_items,
        )
        all_items = {k: [it.to_dict() for it in v] for k, v in result.items()}

    total = sum(len(v) for v in all_items.values())
    logger.info("元数据合计 %d 条", total)

    meta_dir = Path("knowledge/raw/chinaclear")
    meta_dir.mkdir(parents=True, exist_ok=True)
    meta_file = meta_dir / "metadata.json"
    meta_file.write_text(
        json.dumps(all_items, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    logger.info("元数据已保存: %s", meta_file)

    if args.no_download:
        return

    flat: list[CsdcDocItem] = []
    for cat_items in all_items.values():
        flat.extend(CsdcDocItem(**it) for it in cat_items)

    dl_items = [it for it in flat if it.file_format != "html"]
    dl_n = args.download_n if args.download_n > 0 else len(dl_items)
    logger.info("可下载文件 %d 个，开始下载 %d 个", len(dl_items), min(dl_n, len(dl_items)))

    results = download_subcategory(
        dl_items[:dl_n],
        request_delay=args.request_delay,
        max_workers=args.max_workers,
    )

    ok = sum(1 for r in results if r.local_path)
    fail = sum(1 for r in results if not r.local_path)
    logger.info("下载完成: 成功 %d, 失败 %d", ok, fail)


def main() -> None:
    """解析命令行参数并启动采集。"""
    parser = argparse.ArgumentParser(description="中国结算业务规则 验证脚本")
    parser.add_argument(
        "--sub-category", choices=list(SUBCATEGORIES), help="指定子栏目"
    )
    parser.add_argument(
        "--max-pages", type=int, default=0, help="每子栏目最大页数 (0=全部)"
    )
    parser.add_argument("--max-items", type=int, help="每子栏目最大条目数")
    parser.add_argument("--download-n", type=int, default=0, help="下载文件数 (0=全部下载)")
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
