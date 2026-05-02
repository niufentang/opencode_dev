#!/usr/bin/env python3
"""验证知识条目 JSON 文件的字段完整性和合法性。

用法:
    python hooks/validate_json.py knowledge/articles/sse/entries/entries.json
    python hooks/validate_json.py --source sse --full knowledge/articles/*/entries/*.json
    python hooks/validate_json.py --fix entries.json

退出码:
    0: 全部通过
    1: 存在 error
"""

import argparse
import json
import logging
import re
import sys
from datetime import datetime
from pathlib import Path


class ValidationError(Exception):
    """自定义校验异常。"""


# ─── 常量 ───────────────────────────────────────────────────────────────────

VALID_SOURCES = {"sse", "szse", "chinaclear"}

VALID_TYPES = {
    "technical_notice",
    "interface_spec",
    "business_rule",
    "guide",
    "software",
    "test_doc",
    "magazine",
}

VALID_STATUSES = {"active", "deprecated", "superseded"}

VALID_FILE_FORMATS = {"html", "pdf", "doc", "docx", "zip"}

REQUIRED_FIELDS = [
    "id", "type", "title", "source", "source_url", "summary", "tags",
    "status", "version", "previous_version", "public_date", "crawl_date",
    "effective_date", "deprecated_date", "superseded_by", "related_ids",
    "file_format", "file_hash", "content_markdown",
]

TYPE_TO_ABBR = {
    "technical_notice": "tech",
    "interface_spec": "iface",
    "business_rule": "rule",
    "guide": "guide",
    "software": "soft",
    "test_doc": "test",
    "magazine": "mag",
}

ABBR_TO_TYPE = {v: k for k, v in TYPE_TO_ABBR.items()}

TYPE_ABBR_PATTERN = "|".join(re.escape(a) for a in sorted(ABBR_TO_TYPE, key=len, reverse=True))
ID_PATTERN = re.compile(
    rf"^(sse|szse|chinaclear)-({TYPE_ABBR_PATTERN})-(\d{{8}})-(\d{{3}})$"
)

logger = logging.getLogger("validate_json")


# ─── 工具函数 ──────────────────────────────────────────────────────────────


def _validate_date(date_str, field_name):
    """校验日期格式是否为 YYYY-MM-DD。

    Args:
        date_str: 日期字符串或 None。
        field_name: 字段名，用于错误报告。

    Returns:
        list[dict]: 校验问题列表。
    """
    errors = []
    if date_str is None:
        return errors
    if not isinstance(date_str, str):
        errors.append(_issue(field_name, "ERROR",
                             f"应为字符串，实际为 {type(date_str).__name__}"))
        return errors
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, date_str):
        errors.append(_issue(field_name, "ERROR",
                             f"日期格式无效 \"{date_str}\"，应为 YYYY-MM-DD"))
    else:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            errors.append(_issue(field_name, "ERROR",
                                 f"日期不存在 \"{date_str}\""))
    return errors


def _validate_iso8601(dt_str, field_name):
    """校验 ISO 8601 日期时间格式。

    Args:
        dt_str: 日期时间字符串或 None。
        field_name: 字段名，用于错误报告。

    Returns:
        list[dict]: 校验问题列表。
    """
    errors = []
    if dt_str is None:
        return errors
    if not isinstance(dt_str, str):
        errors.append(_issue(field_name, "ERROR",
                             f"应为字符串，实际为 {type(dt_str).__name__}"))
        return errors
    pattern = (
        r"^\d{4}-\d{2}-\d{2}T"
        r"\d{2}:\d{2}:\d{2}"
        r"(\.\d+)?"
        r"(Z|[+-]\d{2}:\d{2})?$"
    )
    if not re.match(pattern, dt_str):
        errors.append(_issue(field_name, "ERROR",
                             f"ISO 8601 格式无效 \"{dt_str}\""))
    return errors


def _issue(field, level, message):
    """构造校验问题字典。

    Args:
        field: 字段名。
        level: 问题级别 (ERROR/WARNING)。
        message: 问题描述。

    Returns:
        dict: 校验问题字典。
    """
    return {"field": field, "level": level, "message": message}


# ─── 单条目校验 ────────────────────────────────────────────────────────────


def validate_entry(entry, entry_index=0):
    """对单个知识条目执行完整性校验。

    覆盖字段存在性、枚举值、格式、类型、条件必填和一致性检查。

    Args:
        entry: 单个知识条目字典。
        entry_index: 条目序号（1-indexed），用于报告定位。

    Returns:
        list[dict]: 校验问题列表，每条包含 field / level / message。
    """
    errors = []

    # 3.1 必填字段存在性
    for field in REQUIRED_FIELDS:
        if field not in entry:
            errors.append(_issue(field, "ERROR",
                                 f"缺少必填字段 \"{field}\""))

    # 3.2 枚举值校验
    _check_enum(entry, "source", VALID_SOURCES, errors)
    _check_enum(entry, "type", VALID_TYPES, errors)
    _check_enum(entry, "status", VALID_STATUSES, errors)
    _check_enum(entry, "file_format", VALID_FILE_FORMATS, errors)

    # 3.3 + 3.4 格式与类型校验
    entry_id = entry.get("id", "")
    if entry_id and isinstance(entry_id, str):
        if not ID_PATTERN.match(entry_id):
            errors.append(_issue("id", "ERROR",
                                 f"id 格式无效 \"{entry_id}\""
                                 f"，应为 {{source}}-{{type_abbr}}-{{YYYYMMDD}}-{{seq}}"))
    elif entry_id and not isinstance(entry_id, str):
        errors.append(_issue("id", "ERROR",
                             f"id 应为字符串，实际为 {type(entry_id).__name__}"))

    errors.extend(_validate_date(entry.get("public_date"), "public_date"))
    errors.extend(_validate_date(entry.get("effective_date"), "effective_date"))
    errors.extend(_validate_date(entry.get("deprecated_date"), "deprecated_date"))
    errors.extend(_validate_iso8601(entry.get("crawl_date"), "crawl_date"))

    _check_non_empty_str(entry, "title", errors)
    _check_str_or_none(entry, "summary", errors, allow_empty=True)
    _check_str_or_none(entry, "version", errors, allow_empty=True)
    _check_str_or_none(entry, "previous_version", errors, allow_empty=True)
    _check_str_or_none(entry, "superseded_by", errors, allow_empty=True)
    _check_str_or_none(entry, "source_url", errors, allow_empty=True)

    _check_str_list(entry, "tags", errors)
    _check_str_list(entry, "related_ids", errors)

    _check_file_hash(entry, errors)
    _check_content_md(entry, errors)

    # 3.5 条件必填
    status = entry.get("status")
    if status == "deprecated" and entry.get("deprecated_date") is None:
        errors.append(_issue("deprecated_date", "ERROR",
                             "status 为 \"deprecated\" 时 deprecated_date 不能为空"))
    if status == "superseded" and entry.get("superseded_by") is None:
        errors.append(_issue("superseded_by", "ERROR",
                             "status 为 \"superseded\" 时 superseded_by 不能为空"))

    # 3.6 id 一致性校验（warning）
    if isinstance(entry_id, str):
        m = ID_PATTERN.match(entry_id)
        if m:
            id_source, id_abbr, id_date, _id_seq = m.groups()
            entry_source = entry.get("source")
            if isinstance(entry_source, str) and id_source != entry_source:
                errors.append(_issue("id", "WARNING",
                                     f"id 中的 source 段 \"{id_source}\""
                                     f" 与 source 字段 \"{entry_source}\" 不一致"))
            entry_type = entry.get("type")
            if isinstance(entry_type, str):
                expected_abbr = TYPE_TO_ABBR.get(entry_type)
                if expected_abbr and id_abbr != expected_abbr:
                    errors.append(_issue("id", "WARNING",
                                         f"id 中的 type 缩写 \"{id_abbr}\""
                                         f" 与 type 字段 \"{entry_type}\" 不一致"
                                         f"（应为 \"{expected_abbr}\"）"))
            pub_date = entry.get("public_date", "")
            if isinstance(pub_date, str):
                pub_compact = pub_date.replace("-", "")
                if pub_compact and id_date != pub_compact:
                    errors.append(_issue("id", "WARNING",
                                         f"id 中的日期 \"{id_date}\""
                                         f" 与 public_date \"{pub_date}\" 不一致"))

    return errors


def _check_enum(entry, field, valid_set, errors):
    """校验枚举类型字段。

    Args:
        entry: 条目字典。
        field: 字段名。
        valid_set: 有效值集合。
        errors: 错误列表（原地追加）。
    """
    val = entry.get(field)
    if val is not None and val not in valid_set:
        errors.append(_issue(field, "ERROR",
                             f"值 \"{val}\" 不在允许范围内 {sorted(valid_set)}"))


def _check_non_empty_str(entry, field, errors):
    """校验字段为非空字符串。

    Args:
        entry: 条目字典。
        field: 字段名。
        errors: 错误列表（原地追加）。
    """
    val = entry.get(field)
    if val is None:
        return
    if not isinstance(val, str):
        errors.append(_issue(field, "ERROR",
                             f"应为字符串，实际为 {type(val).__name__}"))
    elif not val.strip():
        errors.append(_issue(field, "ERROR", "不能为空"))


def _check_str_or_none(entry, field, errors, allow_empty=False):
    """校验字段为字符串或 None。

    Args:
        entry: 条目字典。
        field: 字段名。
        errors: 错误列表（原地追加）。
        allow_empty: 是否允许空字符串。
    """
    val = entry.get(field)
    if val is None:
        return
    if not isinstance(val, str):
        errors.append(_issue(field, "ERROR",
                             f"应为字符串，实际为 {type(val).__name__}"))
    elif not allow_empty and not val.strip():
        errors.append(_issue(field, "ERROR", "不能为空"))


def _check_str_list(entry, field, errors):
    """校验字段为字符串数组。

    Args:
        entry: 条目字典。
        field: 字段名。
        errors: 错误列表（原地追加）。
    """
    val = entry.get(field)
    if val is None:
        return
    if not isinstance(val, list):
        errors.append(_issue(field, "ERROR",
                             f"应为数组，实际为 {type(val).__name__}"))
    elif any(not isinstance(item, str) for item in val):
        errors.append(_issue(field, "ERROR", "数组元素必须为字符串"))


def _check_file_hash(entry, errors):
    """校验 file_hash 字段格式。

    Args:
        entry: 条目字典。
        errors: 错误列表（原地追加）。
    """
    val = entry.get("file_hash")
    if val is None:
        return
    if not isinstance(val, str):
        errors.append(_issue("file_hash", "ERROR",
                             f"应为字符串，实际为 {type(val).__name__}"))
        return
    if not val.startswith("sha256:"):
        preview = val if len(val) <= 30 else val[:27] + "..."
        errors.append(_issue("file_hash", "WARNING",
                             f"应以 \"sha256:\" 开头，当前值 \"{preview}\""))


def _check_content_md(entry, errors):
    """校验 content_markdown 字段。

    Args:
        entry: 条目字典。
        errors: 错误列表（原地追加）。
    """
    val = entry.get("content_markdown")
    if val is None:
        return
    if not isinstance(val, str):
        errors.append(_issue("content_markdown", "ERROR",
                             f"应为字符串，实际为 {type(val).__name__}"))


# ─── 跨条目校验 ──────────────────────────────────────────────────────────


def validate_cross_entry(entries):
    """执行跨条目校验：id 唯一性、superseded_by 引用有效性。

    Args:
        entries: 条目列表。

    Returns:
        list[dict]: 校验问题列表。
    """
    errors = []
    seen_ids = {}

    for idx, entry in enumerate(entries):
        entry_id = entry.get("id")
        if not entry_id or not isinstance(entry_id, str):
            continue
        if entry_id in seen_ids:
            errors.append(_issue("id", "ERROR",
                                 f"id \"{entry_id}\" 重复"
                                 f"（第 {seen_ids[entry_id]} 条和第 {idx + 1} 条）"))
        else:
            seen_ids[entry_id] = idx + 1

    all_ids = set(seen_ids.keys())
    for entry in entries:
        superseded_by = entry.get("superseded_by")
        if superseded_by and isinstance(superseded_by, str) and superseded_by not in all_ids:
            errors.append(_issue("superseded_by", "WARNING",
                                 f"superseded_by \"{superseded_by}\""
                                 f" 引用的条目在当前文件中不存在"))

    return errors


# ─── 修复器 ───────────────────────────────────────────────────────────────


def fix_entry(entry):
    """自动修复条目中的可修补问题。

    当前支持:
    - 标准化 file_hash 前缀（补 sha256:）
    - 去除日期字段首尾空白

    Args:
        entry: 原始条目字典。

    Returns:
        dict: 修复后的条目字典。
    """
    fixed = dict(entry)

    fh = fixed.get("file_hash")
    if isinstance(fh, str) and fh and not fh.startswith("sha256:"):
        fixed["file_hash"] = f"sha256:{fh}"

    for date_field in ("public_date", "effective_date", "deprecated_date"):
        val = fixed.get(date_field)
        if isinstance(val, str):
            stripped = val.strip()
            if stripped != val:
                fixed[date_field] = stripped

    return fixed


# ─── 文件读写 ─────────────────────────────────────────────────────────────


def read_json_file(filepath):
    """读取 JSON 文件，返回条目列表。

    支持三种顶层结构：
    1. 直接数组 `[...]`
    2. 包裹对象 `{"entries": [...], ...}`
    3. 单对象 `{...}`

    Args:
        filepath: Path 对象。

    Returns:
        list[dict]: 条目列表。

    Raises:
        ValidationError: 文件读取或解析失败。
    """
    try:
        content = filepath.read_text(encoding="utf-8-sig")
    except Exception as e:
        raise ValidationError(f"无法读取文件: {e}") from e

    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        raise ValidationError(f"JSON 解析失败: {e}") from e

    if isinstance(data, list):
        entries = data
    elif isinstance(data, dict):
        for key in ("entries", "items"):
            if key in data:
                val = data[key]
                if isinstance(val, list):
                    entries = val
                    break
                if isinstance(val, dict):
                    entries = [val]
                    break
        else:
            entries = [data]
    else:
        raise ValidationError("无法识别的 JSON 结构，顶层应为数组或对象")

    if not isinstance(entries, list):
        raise ValidationError("条目列表格式异常")

    return entries


# ─── 格式化输出 ───────────────────────────────────────────────────────────


def format_issue(issue, filepath="", entry_index=0):
    """将校验问题格式化为可读字符串。

    Args:
        issue: 校验问题字典（含 field / level / message）。
        filepath: 文件路径。
        entry_index: 条目序号。

    Returns:
        str: 格式化后的问题描述。
    """
    parts = []
    if filepath:
        parts.append(f"{filepath}#{entry_index}" if entry_index else filepath)
    parts.append(issue.get("level", "ERROR"))
    parts.append(issue.get("field", "?"))
    parts.append(issue.get("message", ""))
    return " ".join(parts)


# ─── CLI ──────────────────────────────────────────────────────────────────


def parse_args(argv=None):
    """解析命令行参数。

    Args:
        argv: 参数列表，默认使用 sys.argv[1:]。

    Returns:
        argparse.Namespace: 解析后的参数。
    """
    parser = argparse.ArgumentParser(
        description="验证知识条目 JSON 文件的字段完整性和合法性",
    )
    parser.add_argument(
        "files", nargs="*",
        help="JSON 文件路径（支持 glob 通配符）",
    )
    parser.add_argument(
        "--source", choices=sorted(VALID_SOURCES),
        help="限定校验特定数据源",
    )
    parser.add_argument(
        "--fix", action="store_true", default=False,
        help="自动修补小问题",
    )
    parser.add_argument(
        "--full", action="store_true", default=False,
        help="启用跨条目一致性校验",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", default=False,
        help="输出调试日志",
    )
    return parser.parse_args(argv)


def _resolve_file_patterns(patterns):
    """解析文件模式，返回 Path 列表。

    Args:
        patterns: 文件路径模式列表。

    Returns:
        list[Path]: 匹配的文件路径。
    """
    filepaths = []
    for pattern in patterns:
        path = Path(pattern)
        if path.is_absolute():
            if path.exists():
                filepaths.append(path)
            else:
                filepaths.append(path)
        else:
            matched = list(Path().glob(pattern))
            if matched:
                filepaths.extend(matched)
            else:
                filepaths.append(path)
    return filepaths


def main(argv=None):
    """主入口函数。

    Args:
        argv: 命令行参数列表。

    Returns:
        int: 退出码（0=通过, 1=有 error）。
    """
    args = parse_args(argv)

    log_level = logging.DEBUG if args.verbose else logging.WARNING
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    filepaths = _resolve_file_patterns(args.files)

    if not filepaths:
        logger.warning("未指定校验文件")
        print(__doc__.split("\n\n")[1])
        return 0

    has_error = False
    all_issues = []

    for filepath in filepaths:
        if not filepath.exists():
            all_issues.append(f"{filepath} ERROR 文件不存在")
            has_error = True
            continue

        logger.info("校验文件: %s", filepath)

        try:
            entries = read_json_file(filepath)
        except ValidationError as e:
            all_issues.append(f"{filepath} ERROR {e}")
            has_error = True
            continue

        if not entries:
            all_issues.append(f"{filepath} WARNING 空条目列表（无内容可校验）")
            continue

        # 按数据源过滤
        if args.source:
            entries = [e for e in entries if e.get("source") == args.source]
            if not entries:
                continue

        # 逐条目校验
        for idx, entry in enumerate(entries):
            e_num = idx + 1
            issues = validate_entry(entry, entry_index=e_num)
            if args.fix:
                entries[idx] = fix_entry(entry)
            for iss in issues:
                all_issues.append(format_issue(iss, str(filepath), e_num))
                if iss.get("level") == "ERROR":
                    has_error = True

        # 跨条目校验
        if args.full and len(entries) > 1:
            cross_issues = validate_cross_entry(entries)
            for iss in cross_issues:
                all_issues.append(format_issue(iss, str(filepath), 0))
                if iss.get("level") == "ERROR":
                    has_error = True

        # --fix 写回
        if args.fix:
            try:
                filepath.write_text(
                    json.dumps(entries, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
                logger.info("已自动修复文件: %s", filepath)
            except Exception as e:
                all_issues.append(f"{filepath} ERROR 写入修复内容失败: {e}")
                has_error = True

    # 输出结果（按 ERROR → WARNING 排序）
    errors = [i for i in all_issues if " ERROR " in i]
    warnings = [i for i in all_issues if " WARNING " in i]
    for issue in errors + warnings:
        print(issue)

    if errors:
        logger.info("共 %d 个 ERROR, %d 个 WARNING", len(errors), len(warnings))
    elif warnings:
        logger.info("共 %d 个 WARNING（无 ERROR）", len(warnings))
    else:
        logger.info("全部通过 ✓")

    return 1 if has_error else 0


if __name__ == "__main__":
    sys.exit(main())
