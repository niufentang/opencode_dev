"""上交所交易技术支持专区 — 采集与下载验证脚本。

用法：
    python test/test_sse.py                           # 全部栏目 × 全部分页 × 全部下载
    python test/test_sse.py --category 技术通知        # 仅采集指定栏目
    python test/test_sse.py --max-pages 3 --download-n 10   # 限制页数与下载数
    python test/test_sse.py --no-download              # 仅采集元数据，不下载
    python test/test_sse.py --download-only            # 仅从已有元数据下载

日志输出：log/test_sse.log（同时输出到控制台）
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils.sse_tech_support_doc_api import (
    CATEGORIES,
    SseDocItem,
    download_category,
    fetch_all_categories,
    fetch_category,
)

LOG_DIR = Path(__file__).resolve().parent.parent / "log"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_DIR / "test_sse.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("test_sse")


def run(args: argparse.Namespace) -> None:
    """执行采集与下载流程。"""
    # 参数转换：0 表示不限制（传给 API 时变为 None）
    max_pages = args.max_pages if args.max_pages > 0 else None

    # --- 阶段 1：采集元数据 ---
    if args.download_only:
        # 仅下载模式：从已有 metadata.json 读取
        metadata_file = Path("knowledge/raw/sse/metadata.json")
        if not metadata_file.exists():
            logger.error("--download-only 需要先运行采集生成 metadata.json")
            sys.exit(1)
        all_items = json.loads(metadata_file.read_text(encoding="utf-8"))
    elif args.category:
        # 指定单个栏目
        logger.info("采集栏目: %s", args.category)
        items = fetch_category(
            args.category, max_pages=max_pages, max_items=args.max_items
        )
        all_items = {args.category: [it.to_dict() for it in items]}
    else:
        # 全部栏目
        logger.info("采集全部 %d 个栏目", len(CATEGORIES))
        result = fetch_all_categories(
            max_pages_per_category=max_pages,
            max_items_per_category=args.max_items,
        )
        all_items = {k: [it.to_dict() for it in v] for k, v in result.items()}

    total = sum(len(v) for v in all_items.values())
    logger.info("元数据合计 %d 条", total)

    # 保存元数据到文件
    meta_dir = Path("knowledge/raw/sse")
    meta_dir.mkdir(parents=True, exist_ok=True)
    meta_file = meta_dir / "metadata.json"
    meta_file.write_text(
        json.dumps(all_items, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    logger.info("元数据已保存: %s", meta_file)

    if args.no_download:
        return

    # --- 阶段 2：下载文件 ---
    # 将所有条目展平为一维列表
    flat: list[SseDocItem] = []
    for cat_name, cat_items in [
        (k, [SseDocItem(**it) for it in v]) for k, v in all_items.items()
    ]:
        flat.extend(cat_items)

    # 过滤掉 HTML 页面（只下载 PDF/DOCX/ZIP 等实体文件）
    dl_items = [it for it in flat if it.file_format != "html"]
    dl_n = args.download_n if args.download_n > 0 else len(dl_items)
    logger.info("可下载文件 %d 个，开始下载 %d 个", len(dl_items), min(dl_n, len(dl_items)))

    results = download_category(
        dl_items[:dl_n],
        request_delay=args.request_delay,
        max_workers=args.max_workers,
    )

    # 统计下载结果
    ok = sum(1 for r in results if r.local_path)
    fail = sum(1 for r in results if not r.local_path)
    logger.info("下载完成: 成功 %d, 失败 %d", ok, fail)


def main() -> None:
    """解析命令行参数并启动采集。"""
    parser = argparse.ArgumentParser(description="上交所交易技术支持专区 验证脚本")
    parser.add_argument("--category", choices=list(CATEGORIES), help="指定栏目")
    parser.add_argument(
        "--max-pages", type=int, default=0, help="每栏目最大页数 (0=全部)"
    )
    parser.add_argument("--max-items", type=int, help="每栏目最大条目数")
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
