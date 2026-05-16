"""整理 Agent (Organizer) 批量处理脚本。

将分析后的 _analysis.json 文件转换为标准知识条目 JSON，
写入 knowledge/articles/{source}/entries/。

用法：
    python utils/organize_all.py                           # 处理所有文档
    python utils/organize_all.py --source sse               # 仅上交所
    python utils/organize_all.py --category 技术通知        # 仅指定类别
    python utils/organize_all.py --dry-run                  # 试运行，不写入
"""

from __future__ import annotations

import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.FileHandler(Path("log/organize_all.log"), encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("organize_all")

ARTICLES_DIR = Path("knowledge/articles")

# doc_id 中第二段的 type 到标准 type 的映射
TYPE_MAP = {
    "tech": "technical_notice",
    "iface": "interface_spec",
    "test": "test_doc",
    "guide": "guide",
    "soft": "software",
    "mag": "magazine",
}

# doc_id 中第二段的 type 到 category 目录的映射（用于查找对应的 meta/markdown）
TYPE_TO_CATEGORY = {
    "tech": "技术通知",
    "iface": "技术接口",
    "test": "测试文档",
    "guide": "技术指南",
    "soft": "软件",
    "mag": "技术杂志",
}


def parse_doc_id(doc_id: str) -> dict:
    """解析 doc_id 获取 source, type, date, seq 信息。"""
    parts = doc_id.split("-")
    if len(parts) < 4:
        return {"source": parts[0] if len(parts) > 0 else "", "type": "unknown", "date": "00000000", "seq": "000"}
    return {
        "source": parts[0],
        "type": parts[1],
        "date": parts[2],
        "seq": parts[3],
    }


def extract_date_from_doc_id(doc_id: str) -> str | None:
    """从 doc_id 中提取日期并格式化为 YYYY-MM-DD。"""
    info = parse_doc_id(doc_id)
    date_str = info["date"]
    if date_str == "00000000" or not date_str:
        return None
    try:
        return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    except (IndexError, ValueError):
        return None


def type_to_standard(type_str: str) -> str:
    """将 doc_id 中的简短类型映射为标准类型。"""
    return TYPE_MAP.get(type_str, type_str)


def clean_title(title: str, doc_id: str = "") -> str:
    """清理标题：移除 YYYYMMDD_ 前缀。"""
    if not title:
        return title
    # 移除开头的日期前缀如 "20260430_"
    cleaned = re.sub(r"^\d{8}_", "", title)
    # 移除 .cdr 后缀
    cleaned = re.sub(r"\.cdr$", "", cleaned)
    # 如果标题被截断（以数字结尾），可能是文件名问题
    # 尝试用 doc_id 信息补充
    if cleaned.endswith("1") and not cleaned.endswith("1.") and len(cleaned) > 10:
        pass  # 保留原样
    return cleaned


def find_meta_and_markdown(
    analysis_path: Path, analysis_data: dict
) -> tuple[dict | None, str | None]:
    """查找与 analysis 文件对应的 _meta.json 和 .md 文件。"""
    source = analysis_data.get("source", "")
    doc_id = analysis_data.get("doc_id", "")
    doc_id_info = parse_doc_id(doc_id)
    type_short = doc_id_info.get("type", "unknown")
    category_dir = TYPE_TO_CATEGORY.get(type_short, "")

    # 从 analysis 文件路径推断 category
    # analysis 路径: .../analyzed/{category}/{filename}_analysis.json
    category_from_path = analysis_path.parent.name

    # 构建可能的 meta 和 markdown 路径
    base_name = analysis_path.stem
    if base_name.endswith("_analysis"):
        base_name = base_name[:-9]  # 去掉 _analysis 后缀

    meta_paths_to_try = []
    md_paths_to_try = []

    # 尝试从 meta 中的 markdown_path 获取
    # 先尝试所有可能的 category
    for cat in [category_from_path, category_dir]:
        if not cat:
            continue
        meta_path = ARTICLES_DIR / source / "metadata" / cat / f"{base_name}_meta.json"
        md_path = ARTICLES_DIR / source / "markdown" / cat / f"{base_name}.md"
        meta_paths_to_try.append(meta_path)
        md_paths_to_try.append(md_path)

    # 也尝试直接使用 base_name 作为文件名（无 category）
    meta_path = ARTICLES_DIR / source / "metadata" / f"{base_name}_meta.json"
    md_path = ARTICLES_DIR / source / "markdown" / f"{base_name}.md"
    meta_paths_to_try.append(meta_path)
    md_paths_to_try.append(md_path)

    # 读取 meta
    meta_data = None
    for mp in meta_paths_to_try:
        if mp.exists():
            try:
                meta_data = json.loads(mp.read_text(encoding="utf-8"))
                break
            except (json.JSONDecodeError, OSError):
                continue

    # 读取 markdown
    markdown_content = None
    for mp in md_paths_to_try:
        if mp.exists():
            try:
                markdown_content = mp.read_text(encoding="utf-8")
                break
            except OSError:
                continue

    # 如果从文件名找不到，尝试从 meta_data 中获取 markdown_path
    if meta_data and not markdown_content:
        md_path_str = meta_data.get("markdown_path", "")
        if md_path_str:
            md_path = Path(md_path_str)
            if md_path.exists():
                markdown_content = md_path.read_text(encoding="utf-8")

    return meta_data, markdown_content


def extract_version_from_filename(filename: str) -> str | None:
    """从分析文件名中提取版本号。
    
    例如："IS105_上海证券交易所综合业务平台市场参与者接口规格说明书1.60版_20260430..." → "1.60"
    """
    patterns = [
        r'(\d+\.\d+)\s*版',
        r'V(\d+\.?\d*)\s*版',
        r'Ver(\d+\.?\d*)',
        r'_V(\d+\.?\d*)',
    ]
    for p in patterns:
        m = re.search(p, filename, re.IGNORECASE)
        if m:
            return m.group(1)
    return None


def build_entry(analysis_data: dict, meta_data: dict | None, markdown_content: str | None, analysis_path: Path | None = None) -> dict | None:
    """将分析数据组装为标准知识条目 JSON。"""
    doc_id = analysis_data.get("doc_id", "")
    doc_id_info = parse_doc_id(doc_id)
    type_short = doc_id_info.get("type", "unknown")

    # 基础字段
    entry = {
        "id": doc_id,
        "type": type_to_standard(type_short),
        "title": clean_title(analysis_data.get("title", ""), doc_id),
        "source": analysis_data.get("source", ""),
        "source_url": analysis_data.get("source_url", ""),
        "summary": analysis_data.get("summary", ""),
        "tags": analysis_data.get("tags", []),
        "status": analysis_data.get("status", "active"),
        "version": analysis_data.get("version"),
        "previous_version": analysis_data.get("previous_version"),
        "public_date": None,
        "crawl_date": None,
        "effective_date": None,
        "deprecated_date": analysis_data.get("deprecated_date"),
        "superseded_by": analysis_data.get("superseded_by"),
        "related_ids": analysis_data.get("related_ids", []),
        "file_format": "pdf",
        "file_hash": None,
        "content_markdown": None,
    }

    # 从文件名提取版本号（当 analysis_data 中没有 version 时）
    if not entry["version"] and analysis_path:
        filename_ver = extract_version_from_filename(analysis_path.stem)
        if filename_ver:
            entry["version"] = filename_ver

    # 从 meta 中提取信息
        if meta_data.get("file_hash"):
            entry["file_hash"] = meta_data["file_hash"]
        if meta_data.get("file_format"):
            entry["file_format"] = meta_data["file_format"]
        if meta_data.get("public_date"):
            entry["public_date"] = meta_data["public_date"]
        if meta_data.get("effective_date"):
            entry["effective_date"] = meta_data["effective_date"]

    # 从 doc_id 提取 public_date（如果 meta 中没有）
    if not entry["public_date"]:
        entry["public_date"] = extract_date_from_doc_id(doc_id)

    # 嵌入 markdown 内容
    if markdown_content:
        entry["content_markdown"] = markdown_content

    # 数据过滤检查
    if not entry["title"] or entry["title"].strip() == "":
        logger.warning(f"  跳过: {doc_id} 标题为空")
        return None

    # 检查置信度
    confidence = analysis_data.get("confidence", 0.75)
    if confidence < 0.3:
        logger.warning(f"  跳过: {doc_id} 置信度 {confidence} < 0.3")
        return None
    elif confidence < 0.7:
        if "needs_review" not in entry["tags"]:
            entry["tags"].append("needs_review")
        logger.info(f"  标记 needs_review: {doc_id} 置信度 {confidence}")

    return entry


def process_analysis_file(analysis_path: Path, dry_run: bool = False) -> dict | None:
    """处理单个 _analysis.json 文件，返回标准条目。"""
    logger.info(f"处理: {analysis_path.name}")

    try:
        analysis_data = json.loads(analysis_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        logger.error(f"  读取分析文件失败: {e}")
        return None

    doc_id = analysis_data.get("doc_id", "")
    if not doc_id:
        logger.warning(f"  跳过: 无 doc_id")
        return None

    # 查找对应 meta 和 markdown
    meta_data, markdown_content = find_meta_and_markdown(analysis_path, analysis_data)

    # 组装条目
    entry = build_entry(analysis_data, meta_data, markdown_content, analysis_path)
    if not entry:
        return None

    # 写入文件
    if not dry_run:
        source = entry["source"]
        entries_dir = ARTICLES_DIR / source / "entries"
        entries_dir.mkdir(parents=True, exist_ok=True)

        output_path = entries_dir / f"{doc_id}.json"
        output_path.write_text(
            json.dumps(entry, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        logger.info(f"  写入: {output_path.name}")
    else:
        logger.info(f"  [试运行] 准备写入: {source}/entries/{doc_id}.json")

    return entry


def build_index(source: str, entries: list[dict]) -> dict:
    """构建 entries.json 索引文件。"""
    index_entries = []
    for e in entries:
        index_entries.append({
            "id": e["id"],
            "title": e["title"],
            "type": e["type"],
            "status": e["status"],
            "public_date": e.get("public_date"),
            "tags": [t for t in e.get("tags", []) if t not in ("has_changes", "deprecated", "needs_review")][:5],
        })

    return {
        "source": source,
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        "total_entries": len(entries),
        "entries": index_entries,
    }


def scan_analysis_files(source: str | None = None, category: str | None = None) -> list[Path]:
    """扫描所有 _analysis.json 文件。"""
    pattern = "**/*_analysis.json"
    if source:
        base_path = ARTICLES_DIR / source / "analyzed"
    else:
        base_path = ARTICLES_DIR

    all_files = sorted(Path(base_path).glob(pattern))

    if category:
        all_files = [f for f in all_files if f.parent.name == category]

    return all_files


def _extract_version_info(title: str, doc_id: str = "", entry_version: str | None = None) -> list[tuple[str, str, float]]:
    """从标题和 doc_id 中提取版本信息。
    
    返回 [(is_id, version_str, version_float), ...]
    支持多种格式：
    - IS105 1.60版
    - IS105_...1.60版
    - IS105...1.60版_(truncated titles)
    - 实施指南V2.0版 / 实施指南1.2版
    - 规格说明书1.60版
    """
    results = []
    
    # Pattern 1: IS\d+ followed by version number (with or without 版 suffix)
    # Handle truncated titles like "规格说明书1" where version is "1.60" but cut off
    is_pattern = re.compile(r"(IS\d+)\D*?(\d+\.\d+)", re.IGNORECASE)
    for m in is_pattern.finditer(title):
        is_id = m.group(1)
        ver_str = m.group(2)
        try:
            ver_float = float(ver_str)
            results.append((is_id, ver_str, ver_float))
        except ValueError:
            continue

    # Pattern 2: IS119/IS120 etc with version numbers NOT in standard IS\d+ format
    # Try just finding IS\d+ and then looking for nearby numbers
    is_simple = re.compile(r"(IS\d+)", re.IGNORECASE)
    ver_near = re.compile(r"(\d+\.\d+)")
    for m in is_simple.finditer(title):
        is_id = m.group(1)
        # Check if we already matched this in pattern 1
        if any(r[0] == is_id for r in results):
            continue
        # Look for version numbers after the IS match
        after = title[m.end():m.end()+50]
        vm = ver_near.search(after)
        if vm:
            try:
                ver_float = float(vm.group(1))
                results.append((is_id, vm.group(1), ver_float))
            except ValueError:
                continue

    # Pattern 3: Guide version patterns (技术指南/实施指南 V1.0/1.2版 etc)
    guide_patterns = [
        re.compile(r"(技术实施指南|技术指南|实施指南).*?V?\s*(\d+\.?\d*)\s*版", re.IGNORECASE),
        re.compile(r"(技术实施指南|技术指南|实施指南).*?(\d+\.\d+)\s*版", re.IGNORECASE),
    ]
    for gp in guide_patterns:
        for m in gp.finditer(title):
            doc_type = m.group(1)
            ver_str = m.group(2)
            try:
                ver_float = float(ver_str)
                results.append((doc_type, ver_str, ver_float))
            except ValueError:
                continue

    # Pattern 4: Error code table version (IS111 3.29版 etc - often truncated)
    ect_pattern = re.compile(r"(IS111|报盘软件错误代码表).*?(\d+\.\d+)", re.IGNORECASE)
    for m in ect_pattern.finditer(title):
        key = m.group(1)
        ver_str = m.group(2)
        try:
            ver_float = float(ver_str)
            results.append((key, ver_str, ver_float))
        except ValueError:
            continue

    # Pattern 5: Use entry_version field if available (extracted from filename)
    if entry_version:
        # Try to determine the IS number or doc type
        is_match = re.search(r"(IS\d+)", title, re.IGNORECASE)
        if is_match:
            try:
                ver_float = float(entry_version)
                results.append((is_match.group(1), entry_version, ver_float))
            except ValueError:
                pass
        # Also try guide patterns
        guide_match = re.search(r"(技术实施指南|技术指南|实施指南)", title)
        if guide_match:
            try:
                ver_float = float(entry_version)
                results.append((guide_match.group(1), entry_version, ver_float))
            except ValueError:
                pass

    return results


def perform_version_traceability(source: str) -> None:
    """版本追溯：查找同文档的不同版本并建立前后版本关系。"""
    entries_dir = ARTICLES_DIR / source / "entries"
    if not entries_dir.exists():
        return

    entries = []
    for f in sorted(entries_dir.glob("*.json")):
        if f.name == "entries.json":
            continue
        try:
            entries.append(json.loads(f.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError):
            continue

    BUILT_VERSION_CHAINS: set[tuple[str, str]] = set()

    # 修复已存在的错误 superseded_by
    for entry in entries:
        sb = entry.get("superseded_by")
        if sb and not sb.startswith("sse-") and not sb.startswith("szse-"):
            # 这不是一个有效的条目 ID，清除它
            logger.warning(f"  修复无效 superseded_by: {entry['id']} superseded_by='{sb}'")
            entry["superseded_by"] = None
            entry_path = entries_dir / f"{entry['id']}.json"
            entry_path.write_text(
                json.dumps(entry, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

    # 先按 ID 中提取的日期排序（用于同系列版本比较）
    def extract_sort_date(entry: dict) -> str:
        eid = entry.get("id", "")
        parts = eid.split("-")
        return parts[2] if len(parts) >= 3 else "00000000"

    entries_sorted = sorted(entries, key=extract_sort_date)

    # 为每个条目提取版本信息
    entry_versions: dict[str, list] = {}
    for entry in entries_sorted:
        title = entry.get("title", "")
        doc_id = entry.get("id", "")
        entry_ver = entry.get("version")
        info = _extract_version_info(title, doc_id, entry_ver)
        if info:
            for is_id, ver_str, ver_float in info:
                if is_id not in entry_versions:
                    entry_versions[is_id] = []
                entry_versions[is_id].append((entry, ver_str, ver_float))

    # 对每个 IS 系列，按版本号排序并建立链
    for is_id, vers in entry_versions.items():
        # 按版本号排序
        vers_sorted = sorted(vers, key=lambda x: x[2])
        
        for i in range(1, len(vers_sorted)):
            older = vers_sorted[i-1]
            newer = vers_sorted[i]
            older_entry, older_ver, _ = older
            newer_entry, newer_ver, _ = newer
            
            chain_key = (older_entry["id"], newer_entry["id"])
            if chain_key in BUILT_VERSION_CHAINS:
                continue
            BUILT_VERSION_CHAINS.add(chain_key)

            # 设置 newer 的 previous_version
            if not newer_entry.get("previous_version") or newer_entry["previous_version"] != older_ver:
                newer_entry["previous_version"] = older_ver
                newer_path = entries_dir / f"{newer_entry['id']}.json"
                newer_path.write_text(
                    json.dumps(newer_entry, ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )
                logger.info(f"  版本追溯: {newer_entry['id']} previous_version → {older_ver}")

            # 设置 older 的 superseded_by
            if not older_entry.get("superseded_by"):
                older_entry["superseded_by"] = newer_entry["id"]
                if older_entry.get("status") == "active":
                    older_entry["status"] = "superseded"
                older_path = entries_dir / f"{older_entry['id']}.json"
                older_path.write_text(
                    json.dumps(older_entry, ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )
                logger.info(f"  版本追溯: {older_entry['id']} → {newer_entry['id']} (superseded)")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Organizer: 分析结果 → 标准知识条目")
    parser.add_argument("--source", choices=["sse", "szse", "chinaclear"], help="仅处理特定数据源")
    parser.add_argument("--category", help="仅处理特定类别（如 技术通知、测试文档）")
    parser.add_argument("--dry-run", action="store_true", help="试运行，不写入文件")
    parser.add_argument("--skip-version", action="store_true", help="跳过版本追溯")
    parser.add_argument("--trace-only", action="store_true", help="仅做版本追溯，不重新生成条目")
    args = parser.parse_args()

    # 如果仅追溯模式
    if args.trace_only:
        logger.info("=== 仅版本追溯模式 ===")
        sources_to_trace = [args.source] if args.source else ["sse", "szse"]
        for s in sources_to_trace:
            perform_version_traceability(s)
            entries_dir = ARTICLES_DIR / s / "entries"
            if entries_dir.exists():
                updated_entries = []
                for f in sorted(entries_dir.glob("*.json")):
                    if f.name == "entries.json":
                        continue
                    try:
                        updated_entries.append(json.loads(f.read_text(encoding="utf-8")))
                    except (json.JSONDecodeError, OSError):
                        continue
                index = build_index(s, updated_entries)
                index_path = entries_dir / "entries.json"
                index_path.write_text(
                    json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
                )
                logger.info(f"索引已更新: {index_path} ({len(updated_entries)} 条目，含版本追溯)")
        logger.info("版本追溯完成。")
        return

    # 扫描
    analysis_files = scan_analysis_files(args.source, args.category)
    logger.info(f"找到 {len(analysis_files)} 个分析文件")

    if args.dry_run:
        logger.info("=== 试运行模式 ===")

    # 按 source 分组
    by_source: dict[str, list[dict]] = {}

    for af in analysis_files:
        entry = process_analysis_file(af, dry_run=args.dry_run)
        if entry:
            source = entry["source"]
            if source not in by_source:
                by_source[source] = []
            by_source[source].append(entry)

    # 写入索引
    for source, entries in by_source.items():
        if not args.dry_run:
            entries_dir = ARTICLES_DIR / source / "entries"
            entries_dir.mkdir(parents=True, exist_ok=True)

            index = build_index(source, entries)
            index_path = entries_dir / "entries.json"
            index_path.write_text(
                json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            logger.info(f"索引已写入: {index_path} ({len(entries)} 条目)")

            # 版本追溯
            if not args.skip_version:
                perform_version_traceability(source)
                # 重新读取条目以更新索引
                updated_entries = []
                for f in sorted(entries_dir.glob("*.json")):
                    if f.name == "entries.json":
                        continue
                    try:
                        updated_entries.append(json.loads(f.read_text(encoding="utf-8")))
                    except (json.JSONDecodeError, OSError):
                        continue
                index = build_index(source, updated_entries)
                index_path.write_text(
                    json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
                )
                logger.info(f"索引已更新: {index_path} ({len(updated_entries)} 条目，含版本追溯)")

    total = sum(len(v) for v in by_source.values())
    logger.info(f"处理完成。共生成 {total} 个知识条目。")
    for source, entries in by_source.items():
        logger.info(f"  {source}: {len(entries)} 条目")


if __name__ == "__main__":
    main()
