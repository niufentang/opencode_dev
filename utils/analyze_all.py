"""批量分析脚本：为所有 Markdown 文档生成 _analysis.json。

用法：
    python utils/analyze_all.py                           # 分析所有文档
    python utils/analyze_all.py --source sse               # 仅上交所
    python utils/analyze_all.py --category 技术通知        # 仅指定类别
    python utils/analyze_all.py --limit 10                 # 仅前10篇
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.FileHandler(Path("log/analyze_all.log"), encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("analyze_all")

ARTICLES_DIR = Path("knowledge/articles")
RAW_DIR = Path("knowledge/raw")

SOURCE_SHORT = {"sse": "sse", "szse": "szse", "chinaclear": "chinaclear"}

# Cache crawl_metadata.json for source_url backfill
_CRAWL_META_CACHE: list[dict] | None = None


def _load_crawl_meta() -> list[dict]:
    global _CRAWL_META_CACHE
    if _CRAWL_META_CACHE is None:
        path = RAW_DIR / "crawl_metadata.json"
        if path.exists():
            _CRAWL_META_CACHE = json.loads(path.read_text(encoding="utf-8"))
        else:
            _CRAWL_META_CACHE = []
    return _CRAWL_META_CACHE


def _find_source_url(md_file: Path, meta: dict) -> str | None:
    if meta.get("source_url"):
        return meta["source_url"]
    raw_path = meta.get("raw_path") or ""
    fname = Path(raw_path).name if raw_path else md_file.stem
    for item in _load_crawl_meta():
        lp = item.get("local_path")
        u = item.get("url")
        if lp and fname in lp:
            return u
        if u and fname in u:
            return u
    # Try filename-based match
    for item in _load_crawl_meta():
        title = item.get("title") or ""
        if title and title[:20] in md_file.stem:
            return item.get("url")
    return None
TYPE_SHORT = {
    "technical_notice": "tech", "interface_spec": "iface",
    "business_rule": "rule", "guide": "guide",
    "software": "soft", "test_doc": "test", "magazine": "mag",
}

CHANGE_TYPE_KEYWORDS = {
    "接口字段": "接口字段变更", "字段长度": "接口字段变更",
    "字段类型": "接口字段变更", "必填": "接口字段变更",
    "枚举": "接口字段变更", "代码": "接口字段变更",
    "流程": "业务流程变更", "步骤": "业务流程变更",
    "办理": "业务流程变更", "线上": "业务流程变更",
    "线下": "业务流程变更", "规则": "规则条款变更",
    "条款": "规则条款变更", "适用": "规则条款变更",
    "架构": "技术架构变更", "通信": "技术架构变更",
    "FTP": "技术架构变更", "SFTP": "技术架构变更",
    "协议": "技术架构变更", "网关": "技术架构变更",
    "版本": "版本升级", "V1": "版本升级", "V2": "版本升级",
    "V3": "版本升级", "时限": "时效变更",
    "过渡期": "时效变更", "生效": "时效变更",
    "废止": "废止", "停止使用": "废止",
    "不再支持": "废止", "下线": "废止",
}

SEVERITY_KEYWORDS = {
    "critical": ["安全", "风险", "数据丢失", "资金"],
    "major": ["新增", "删除", "废止", "修改", "调整", "变更", "替换", "迁移"],
    "minor": ["优化", "说明", "补充", "调整", "微调", "扩容"],
    "cosmetic": ["格式", "排版", "文案", "描述", "更正", "勘误"],
}


def _classify_change_type(text: str) -> str:
    for kw, ct in CHANGE_TYPE_KEYWORDS.items():
        if kw in text:
            return ct
    return "规则条款变更"


def _classify_severity(text: str) -> str:
    for sev, kws in SEVERITY_KEYWORDS.items():
        for kw in kws:
            if kw in text:
                return sev
    return "minor"


def _is_valid_change_text(text: str) -> bool:
    text = text.strip()
    if len(text) < 4:
        return False
    punctuation_only = all(c in "，。、；：？！""''（）【】《》—…·\n\r\t " for c in text)
    if punctuation_only:
        return False
    number_only = all(c in "0123456789.%" for c in text)
    if number_only:
        return len(text) >= 3
    return True


def _is_page_header_or_artifact(text: str) -> bool:
    """Filter out page-level formatting artifacts that are not real changes."""
    stripped = text.strip()
    if len(stripped) <= 1:
        return True
    if re.match(r"^\d{1,3}$", stripped):
        return True
    if re.match(r"^第\s*\d+\s*页", stripped):
        return True
    if re.match(r"^Page\s+\d+", stripped, re.IGNORECASE):
        return True
    if re.match(r"^\d+\s*/\s*\d+$", stripped):
        return True
    if re.match(r"^(上海证券交易所|深圳证券交易所|中国结算)", stripped) and len(stripped) < 30:
        return True
    return False


def _parse_span_changes(markdown: str) -> list[dict]:
    seen = set()
    changes = []
    pattern = r'<span style="color:(\w+)">(?:\[([^\]]*)\])?\s*(.*?)</span>'
    for m in re.finditer(pattern, markdown):
        color = m.group(1)
        prefix = (m.group(2) or "").strip()
        raw_text = m.group(3)
        text = raw_text.strip()
        if not text or not _is_valid_change_text(text):
            continue
        if _is_page_header_or_artifact(text):
            continue
        dedup_key = f"{color}|{prefix}|{text[:100]}"
        if dedup_key in seen:
            continue
        seen.add(dedup_key)

        if prefix in ("新增", "修改", "删除", "废止"):
            change_type = prefix
        else:
            change_type = _classify_change_type(text)

        severity = _classify_severity(text)
        if color == "blue":
            if severity == "major":
                severity = "minor"

        changes.append({
            "type": change_type,
            "color": color,
            "summary": text[:120],
            "detail": text[:300],
            "severity": severity,
            "source": "parser_span",
        })
    return changes


def _extract_keywords(text: str, title: str) -> list[str]:
    tags = set()
    kw_patterns = [
        r"(新竞价新综业|新固定收益|独立IOPV|ETF申赎清单|REITs|科创成长层|科创板|"
        r"港股通|UniTrans|EzOES|IS\d{3}|STEP|BINARY|行情网关|交易网关|"
        r"报盘软件|证通云盘|期权|债券|注册制|做市商|融资融券)"
    ]
    for p in kw_patterns:
        for m in re.finditer(p, text):
            tags.add(m.group(1))
    for m in re.finditer(r"(IS\d{3})", title):
        tags.add(m.group(1))
    return sorted(tags)[:8]


def _detect_deprecation(text: str) -> tuple[str | None, str | None]:
    patterns = [
        (r"自\s*(\d{4}[-.]\d{1,2}[-.]\d{1,2})\s*起\s*(废止|停止|下线)", "deprecated"),
        (r"(废止|停止使用|不再支持|已下线).*?(\d{4}年\d{1,2}月\d{1,2}日)", "deprecated"),
        (r"由\s*([^\s，。]+)\s*(替代|取代)", "superseded"),
        (r"(替代|取代)\s*(为|：|:)\s*([^\s，。]+)", "superseded"),
    ]
    for pat, status in patterns:
        m = re.search(pat, text)
        if m:
            return status, m.group(1) if m.lastindex else None
    return None, None


def _find_version_pairs(markdown_files: list[Path]) -> dict:
    pairs = {}
    for f in markdown_files:
        meta = _read_meta(f)
        if meta and meta.get("version"):
            key = f.parent.name + "/" + meta["doc_type"]
            pairs.setdefault(key, []).append((meta["version"], f))
    result = {}
    for key, versions in pairs.items():
        versions.sort(key=lambda x: x[0] if x[0] else "")
        result[key] = versions
    return result


def _read_meta(md_file: Path) -> dict | None:
    meta_file = _meta_path(md_file)
    if meta_file.exists():
        return json.loads(meta_file.read_text(encoding="utf-8"))
    content = md_file.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"<metadata>(.*?)</metadata>", content, re.DOTALL)
    if m:
        return json.loads(m.group(1))
    return None


def _meta_path(md_file: Path) -> Path:
    rel = md_file.relative_to(ARTICLES_DIR)
    parts = rel.parts
    return ARTICLES_DIR / parts[0] / "metadata" / parts[2] / (parts[3].replace(".md", "_meta.json"))


def _extract_date_from_filename(filename: str) -> str:
    m = re.match(r"(\d{4})(\d{2})(\d{2})_", filename)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.search(r"(\d{4})(\d{2})(\d{2})", filename)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.search(r"t(\d{4})(\d{2})(\d{2})", filename)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return None


def _doc_id(meta: dict, seq: int, filename: str = "") -> str:
    raw = meta.get("raw_path", "")
    if "sse" in raw:
        source = "sse"
    elif "szse" in raw:
        source = "szse"
    elif "chinaclear" in raw:
        source = "chinaclear"
    elif "sse" in filename:
        source = "sse"
    else:
        source = "sse"

    doc_type = meta.get("doc_type", "technical_notice")
    short_type = TYPE_SHORT.get(doc_type, "tech")

    date_str = meta.get("public_date")
    if not date_str:
        date_str = _extract_date_from_filename(filename)
    date = (date_str or "00000000").replace("-", "")
    return f"{source}-{short_type}-{date}-{seq:03d}"


def _generate_summary(changes: list[dict], meta: dict) -> str:
    ver = meta.get("version") or "无"
    if not changes:
        return f"初始版本，无历史变更。文档类型：{meta.get('doc_type', '未知')}，版本：{ver}。"
    parts = [f"本次涉及{len(changes)}项变更。"]
    for ct in set(c["type"] for c in changes):
        count = sum(1 for c in changes if c["type"] == ct)
        parts.append(f"{ct}: {count}项。")
    majors = sum(1 for c in changes if c["severity"] == "major")
    if majors:
        parts.append(f"其中重大变更{majors}项。")
    return " ".join(parts)[:200]


def _extract_title(md_file: Path, meta: dict) -> str:
    title = meta.get("title", "") or ""
    if not title:
        title = md_file.stem
    title = re.sub(r"^\d{8}_", "", title)
    return title


def _merge_adjacent_changes(changes: list[dict]) -> list[dict]:
    if not changes:
        return []
    merged = [changes[0]]
    for c in changes[1:]:
        last = merged[-1]
        same_color = c.get("color") == last.get("color")
        same_type = c["type"] == last["type"]
        if same_color and same_type and len(last["summary"]) < 150:
            last["summary"] = (last["summary"] + " " + c["summary"])[:200]
            last["detail"] = (last["detail"] + "\n" + c["detail"])[:500]
        else:
            merged.append(c)
    for c in merged:
        c.pop("color", None)
    return merged


def analyze_document(md_file: Path, seq: int) -> dict:
    content = md_file.read_text(encoding="utf-8", errors="replace")
    meta = _read_meta(md_file) or {}

    raw_changes = _parse_span_changes(content)
    changes = _merge_adjacent_changes(raw_changes)
    has_span_changes = len(changes) > 0

    if not has_span_changes:
        status, ref = _detect_deprecation(content)
        if status:
            changes.append({
                "type": "废止" if status == "deprecated" else "修改",
                "summary": f"文档声明{status}状态",
                "detail": f"状态: {status}, 参考: {ref or '无'}",
                "severity": "major",
                "source": "keyword_detect",
            })

    title = _extract_title(md_file, meta)
    tags = _extract_keywords(content, title)

    raw_path = meta.get("raw_path", "")
    if "sse" in raw_path:
        tags.insert(0, "sse")
    elif "szse" in raw_path:
        tags.insert(0, "szse")
    elif "chinaclear" in raw_path:
        tags.insert(0, "chinaclear")

    doc_type = meta.get("doc_type", "technical_notice")
    tags.insert(1, doc_type)

    if changes:
        tags.append("has_changes")
    if any("废止" in c["type"] or "下线" in c["type"] for c in changes):
        tags.append("deprecated")

    status = "active"
    deprecated_date = None
    superseded_by = None
    for c in changes:
        if c["type"] == "废止":
            status = "deprecated"
            m = re.search(r"(\d{4}[-.]\d{1,2}[-.]\d{1,2})", c["detail"])
            if m:
                deprecated_date = m.group(1)
            sm = re.search(r"(IS\d{3}|替代为\s*\S+)", c["detail"])
            if sm:
                superseded_by = sm.group(1)
            break

    summary = _generate_summary(changes, meta)
    confidence = 0.95 if has_span_changes else (0.85 if changes else 0.75)

    source_url = _find_source_url(md_file, meta)
    doc_id = _doc_id(meta, seq, md_file.name)

    return {
        "doc_id": doc_id,
        "title": title,
        "source": tags[0] if tags else "sse",
        "source_url": source_url,
        "analysis_date": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "version": meta.get("version"),
        "previous_version": meta.get("previous_version"),
        "changes": changes,
        "tags": tags,
        "related_ids": [],
        "deprecated_date": deprecated_date,
        "superseded_by": superseded_by,
        "summary": summary,
        "confidence": round(confidence, 2),
    }


def collect_markdown_files(source: str | None = None, category: str | None = None, limit: int | None = None) -> list[Path]:
    files = []
    for md_file in sorted(ARTICLES_DIR.rglob("markdown/**/*.md")):
        parts = md_file.relative_to(ARTICLES_DIR).parts
        if source and parts[0] != source:
            continue
        if category and parts[2] != category:
            continue
        files.append(md_file)
    if limit:
        files = files[:limit]
    return files


def save_analysis(md_file: Path, analysis: dict):
    rel = md_file.relative_to(ARTICLES_DIR)
    parts = rel.parts
    analyzed_dir = ARTICLES_DIR / parts[0] / "analyzed" / parts[2]
    analyzed_dir.mkdir(parents=True, exist_ok=True)
    out_path = analyzed_dir / parts[3].replace(".md", "_analysis.json")
    out_path.write_text(json.dumps(analysis, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="批量分析 Markdown 文档")
    parser.add_argument("--source", help="限定数据源: sse / szse / chinaclear")
    parser.add_argument("--category", help="限定类别")
    parser.add_argument("--limit", type=int, help="最大分析数")
    args = parser.parse_args()

    files = collect_markdown_files(args.source, args.category, args.limit)
    logger.info("Found %d markdown files to analyze", len(files))

    ok = fail = 0
    for i, md_file in enumerate(files, 1):
        try:
            analysis = analyze_document(md_file, i)
            out_path = save_analysis(md_file, analysis)
            has_c = "✓" if analysis["changes"] else " "
            logger.info("[%s] [%s] %s → %s", has_c, analysis["doc_id"], md_file.name, out_path.name)
            ok += 1
        except Exception as e:
            import traceback
            logger.error("Analysis failed [%s]: %s\n%s", md_file.name, e, traceback.format_exc())
            fail += 1

    logger.info("Done: %d success, %d failed", ok, fail)


if __name__ == "__main__":
    main()
