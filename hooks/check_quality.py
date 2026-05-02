#!/usr/bin/env python3
"""对知识条目 JSON 文件进行 5 维度质量评分。

评分维度（总分 100）：
  1. 摘要变更精度 (25 分) — summary 是否捕获变更要点
  2. 变更完整性 (25 分)  — 版本链 + 状态一致性 + 实质内容
  3. 元数据规范 (20 分)  — 必填字段格式与条件一致性
  4. 可检索性 (15 分)    — 标签覆盖面 + title 标识性
  5. 信息密度 (15 分)    — 无模板套话 + 无冗余 + 有效内容

等级：A >= 80, B >= 60, C < 60
退出码：存在 C 级返回 1，否则返回 0

用法：
  python hooks/check_quality.py <file> [file ...]
  python hooks/check_quality.py knowledge/articles/sse/entries/*.json
"""

import argparse
import json
import logging
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


# ─── 常量 ───────────────────────────────────────────────────────────────────

# 公告模板套话（维度五）
_HAS_COLOR = True


def _init_color() -> bool:
    """初始化终端颜色支持。

    Windows 下优先尝试 colorama（如已安装），再尝试 Win32 API；
    均失败则降级为无颜色。
    """
    if sys.platform == "win32":
        try:
            import colorama
            colorama.init()
            return True
        except ImportError:
            pass
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            STD_OUTPUT_HANDLE = -11
            ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            handle = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
            mode = ctypes.c_uint32()
            kernel32.GetConsoleMode(handle, ctypes.byref(mode))
            mode.value |= ENABLE_VIRTUAL_TERMINAL_PROCESSING
            kernel32.SetConsoleMode(handle, mode)
            return True
        except Exception:
            return False
    return True


def _no_color() -> str:
    """禁用颜色输出。"""
    global _HAS_COLOR
    _HAS_COLOR = False
    return ""


def _c(code: str) -> str:
    """返回 ANSI 颜色码（颜色禁用时返回空串）。"""
    return code if _HAS_COLOR else ""


TEMPLATE_PADDING = [
    "特此通知", "请遵照执行", "特此通告",
    "有关事项通知如下", "具体事项通知如下",
    "为进一步", "根据.*相关.*规定",
    "附件[:：]", "请各.*(?:单位|会员|参与人).*遵照执行",
]
TEMPLATE_PATTERNS = [re.compile(p) for p in TEMPLATE_PADDING]

# 接口编号模式 IS\d+
IS_PATTERN = re.compile(r"IS\d+")
VERSION_PATTERN = re.compile(r"[vV]\d+(\.\d+)+")
FIELD_PATTERN = re.compile(r"(?:字段|参数|域)\s*\w+")

# 占位摘要检测
PLACEHOLDER_PATTERNS = [
    re.compile(r"暂无.*摘要|无.*内容|待补充|placeholder", re.IGNORECASE),
    re.compile(r"^\d+条变更", re.IGNORECASE),
    re.compile(r"涉及\d+条.*(?:技术|规则|变更)", re.IGNORECASE),
]
INITIAL_VERSION_PATTERN = re.compile(r"初始版本", re.IGNORECASE)

ID_PATTERN = re.compile(
    r"^(sse|szse|chinaclear)-(tech|iface|rule|guide|soft|test|mag)-\d{8}-\d{3}$"
)
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ISO8601_PATTERN = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$"
)

# 文档类型 → 期望的标签名
TYPE_TO_TAG = {
    "technical_notice": "technical_notice",
    "interface_spec": "interface_spec",
    "business_rule": "business_rule",
    "guide": "guide",
    "software": "software",
    "test_doc": "test_doc",
    "magazine": "magazine",
}

# 业务领域标签集合
BUSINESS_TAGS = {
    "债券", "股权", "期权", "基金", "融资融券", "固收",
    "IOPV", "REITs", "ETF", "ETF申购赎回", "ETF定义文件",
    "港股通", "转融通", "优先股", "可转债",
}

# 系统/平台标签集合
SYSTEM_TAGS = {
    "STEP", "BINARY", "EzOES", "EzSTEP", "EzDA", "EzTrans", "EzSR",
    "TDGW", "MDGW", "EzNTP", "UniTrans", "ITCS",
}

# 满分配置
# ANSI 颜色（通过 _c() 包装，禁用颜色时返回空串）
def _C_BOLD(): return _c("\033[1m")
def _C_GREEN(): return _c("\033[92m")
def _C_YELLOW(): return _c("\033[93m")
def _C_RED(): return _c("\033[91m")
def _C_CYAN(): return _c("\033[96m")
def _C_GRAY(): return _c("\033[90m")
def _C_DIM(): return _c("\033[2m")
def _C_RESET(): return _c("\033[0m")

def _sep_line() -> str:
    """返回灰色分隔线。"""
    return _C_GRAY() + "────────────────────────────────────────" + _C_RESET()

def _dsep_line() -> str:
    """返回双灰色分隔线。"""
    b = _sep_line()
    return b + "\n" + b


# 中文字符（CJK）正则，用于计算显示宽度
_CJK_RE = re.compile(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]")


def _display_width(s: str) -> int:
    """计算字符串在终端的显示宽度（CJK 字符算 2 列）。

    Args:
        s: 输入字符串。

    Returns:
        显示宽度。
    """
    return len(s) + len(_CJK_RE.findall(s))


def _visual_ljust(s: str, width: int) -> str:
    """按视觉宽度左对齐，不足补空格。

    Args:
        s: 输入字符串。
        width: 目标视觉宽度。

    Returns:
        填充后的字符串。
    """
    current = _display_width(s)
    pad = max(0, width - current)
    return s + " " * pad


def _color_score(ratio: float) -> str:
    """根据得分比例返回 ANSI 颜色码。"""
    if ratio >= 0.8:
        return _C_GREEN()
    if ratio >= 0.6:
        return _C_YELLOW()
    return _C_RED()


def _color_grade(grade: str) -> str:
    """根据等级返回 ANSI 颜色码。"""
    return {"A": _C_GREEN(), "B": _C_YELLOW(), "C": _C_RED()}.get(grade, _C_RESET())


MAX_SCORES = {
    "summary_quality": 25,
    "change_completeness": 25,
    "format_compliance": 20,
    "retrievability": 15,
    "info_density": 15,
}

logger = logging.getLogger("check_quality")


# ─── 数据结构 ──────────────────────────────────────────────────────────────


@dataclass
class DimensionScore:
    """单个维度评分。"""

    name: str
    score: float
    max_score: float
    detail: str = ""


@dataclass
class QualityReport:
    """条目质量报告。"""

    file: str
    entry_index: int
    dimensions: list = field(default_factory=list)
    total: float = 0.0
    grade: str = "C"

    @property
    def summary_line(self) -> str:
        """生成一行（带颜色等级）。"""
        dims = " | ".join(
            f"{d.name}={d.score:.0f}/{d.max_score:.0f}" for d in self.dimensions
        )
        gc = _color_grade(self.grade)
        return (
            f"[{gc}{_C_BOLD()}{self.grade}{_C_RESET()}]"
            f" {Path(self.file).name}#{self.entry_index}"
            f"  {self.total:.0f}/100  {dims}"
        )

    def detailed_block(self, bar_width: int = 18) -> str:
        """生成带彩色进度条的详细评分块。"""
        gc = _color_grade(self.grade)
        header = (
            f"{_C_CYAN()}文件：{_C_RESET()}"
            f"{_C_BOLD()}{Path(self.file).name}#{self.entry_index}{_C_RESET()}"
        )
        dims_lines = []
        for d in self.dimensions:
            ratio = d.score / d.max_score if d.max_score > 0 else 0
            filled = int(ratio * bar_width)
            bar_filled = "█" * filled
            bar_empty = "─" * (bar_width - filled)
            sc = _color_score(ratio)
            color_tag = _C_GREEN() if ratio >= 0.8 else (_C_YELLOW() if ratio >= 0.6 else _C_RED())
            tag = f"[{color_tag}■{_C_RESET()}]" if filled > 0 else "[ ]"
            name_padded = _visual_ljust(d.name, 14)
            dims_lines.append(
                f"  {tag} {name_padded} [{sc}{bar_filled}{_C_RESET()}{bar_empty}]"
                f" {d.score:.0f}/{d.max_score:.0f}"
            )
        footer = (
            f"  {_C_BOLD()}总分：{self.total:.0f}，等级：{gc}{_C_BOLD()}{self.grade}{_C_RESET()}"
        )
        return "\n".join([header, _sep_line()] + dims_lines + [_sep_line(), footer])


# ─── 评分函数 ──────────────────────────────────────────────────────────────


def grade_from_score(total: float) -> str:
    """根据总分返回等级。

    Args:
        total: 总分 (0-100)。

    Returns:
        A 或 B 或 C。
    """
    if total >= 80:
        return "A"
    if total >= 60:
        return "B"
    return "C"


def _summary_change_bonus(summary: str) -> tuple[int, list[str]]:
    """计算摘要中变更信息的奖励分，上限 +10。

    检测接口编号、版本号、字段名等变更相关关键词。

    Args:
        summary: 摘要文本。

    Returns:
        (奖励分数, 奖励说明列表)。
    """
    bonus = 0
    parts = []
    if IS_PATTERN.search(summary):
        bonus += 5
        parts.append("接口号 +5")
    if VERSION_PATTERN.search(summary):
        bonus += 3
        parts.append("版本号 +3")
    if FIELD_PATTERN.search(summary):
        bonus += 3
        parts.append("字段名 +3")
    return min(bonus, 10), parts


def score_summary_quality(entry: dict) -> DimensionScore:
    """评估摘要变更精度 (满分 25)。

    规则：
    - summary 为空 → 0
    - 占位摘要（不含"初始版本"）→ 0
    - 仅"初始版本"标记 → 12
    - 普通摘要 → 15
    - 含接口编号 +5，含版本号 +3，含具体字段 +3（上限 25）

    Args:
        entry: 知识条目。

    Returns:
        DimensionScore。
    """
    max_score = MAX_SCORES["summary_quality"]
    summary = entry.get("summary", "") or ""
    summary = summary.strip()

    if not summary:
        return DimensionScore("摘要变更精度", 0, max_score, "summary 为空")

    # 占位摘要（排除"初始版本"）
    for pat in PLACEHOLDER_PATTERNS:
        if pat.search(summary):
            return DimensionScore(
                "摘要变更精度", 0, max_score, f"占位摘要: \"{summary[:40]}...\""
            )

    # 仅"初始版本" → 有效初始状态
    if INITIAL_VERSION_PATTERN.search(summary):
        return DimensionScore(
            "摘要变更精度", 12, max_score, "初始版本（无历史变更）"
        )

    # 普通摘要：基础 15 分 + 变更奖励
    base = 15
    bonus, bonus_parts = _summary_change_bonus(summary)
    score = min(base + bonus, max_score)

    detail_parts = bonus_parts if bonus_parts else ["普通摘要"]

    return DimensionScore(
        "摘要变更精度", score, max_score, f"{len(summary)} 字 | {' '.join(detail_parts)}"
    )


def score_change_completeness(entry: dict) -> DimensionScore:
    """评估变更完整性 (满分 25)。

    4 个子项：
    - 版本链完整 (8 分)
    - 状态一致性 (7 分)
    - 变更内容实质 (5 分)
    - has_changes 准确 (5 分)

    Args:
        entry: 知识条目。

    Returns:
        DimensionScore。
    """
    max_score = MAX_SCORES["change_completeness"]
    score = 0.0
    details = []
    status = entry.get("status")
    prev_ver = entry.get("previous_version")
    sup_by = entry.get("superseded_by")
    dep_date = entry.get("deprecated_date")
    tags = entry.get("tags", []) or []
    md = entry.get("content_markdown") or ""
    version = entry.get("version")

    # 版本链完整 (8 分)
    has_prev = bool(prev_ver and isinstance(prev_ver, str) and prev_ver.strip())
    has_sup = bool(sup_by and isinstance(sup_by, str) and sup_by.strip())
    if has_prev or has_sup:
        score += 8
        links = []
        if has_prev:
            links.append(f"previous={prev_ver}")
        if has_sup:
            links.append(f"superseded_by={sup_by}")
        details.append(f"版本链 8/8 ({', '.join(links)})")
    elif status == "active" and not prev_ver and not sup_by:
        score += 6
        details.append("版本链 6/8 (首次发布)")
    else:
        details.append("版本链 0/8 (异常)")

    # 状态一致性 (7 分)
    if status == "active":
        score += 7
        details.append("状态一致 7/7")
    elif status == "superseded":
        if has_sup:
            score += 7
            details.append("状态一致 7/7")
        else:
            details.append("状态一致 0/7 (缺 superseded_by)")
    elif status == "deprecated":
        dep_ok = bool(dep_date and isinstance(dep_date, str) and dep_date.strip())
        if dep_ok:
            score += 7
            details.append("状态一致 7/7")
        else:
            details.append("状态一致 0/7 (缺 deprecated_date)")
    else:
        details.append(f"状态一致 0/7 (status=\"{status}\" 非法)")

    # 变更内容实质 (5 分)
    md_score = 0
    if "|" in md:
        md_score += 2
    if "```" in md:
        md_score += 2
    tech_keywords_count = sum(1 for kw in [
        "接口", "协议", "规范", "STEP", "BINARY", "TCP", "FIX",
    ] if kw in md)
    if tech_keywords_count >= 5:
        md_score += 1
    md_score = min(md_score, 5)
    score += md_score
    details.append(f"内容实质 {md_score}/5")

    # has_changes 准确 (5 分)
    has_changes = "has_changes" in tags
    has_history = (
        bool(version and version != "1" and version != "")
        or status in ("deprecated", "superseded")
        or has_prev
        or has_sup
    )
    if has_history and has_changes:
        score += 5
        details.append("has_changes 准确 5/5")
    elif not has_history and not has_changes:
        score += 5
        details.append("has_changes 准确 5/5 (无变更)")
    else:
        details.append("has_changes 准确 0/5 (不匹配)")

    return DimensionScore("变更完整性", score, max_score, " | ".join(details))


def score_format_compliance(entry: dict) -> DimensionScore:
    """评估元数据规范 (满分 20)。

    5 个子项：
    - id 格式 (4 分)
    - title 非空 (4 分)
    - source_url (3 分)
    - status + 版本链一致性 (5 分)
    - 时间戳 (4 分)

    Args:
        entry: 知识条目。

    Returns:
        DimensionScore。
    """
    max_score = MAX_SCORES["format_compliance"]
    score = 0.0
    details = []

    # id 格式 (4 分)
    eid = entry.get("id", "")
    if eid and ID_PATTERN.match(str(eid)):
        score += 4
        details.append("id ✓")
    else:
        details.append("id ✗")

    # title 非空 (4 分)
    title = entry.get("title", "")
    if title and isinstance(title, str) and title.strip():
        score += 4
        details.append("title ✓")
    else:
        details.append("title ✗")

    # source_url (3 分)
    url = entry.get("source_url")
    if url and isinstance(url, str) and url.strip():
        score += 3
        details.append("url ✓")
    else:
        details.append("url ✗")

    # status + 版本链一致性 (5 分)
    status = entry.get("status")
    sub = 0
    if status in ("active", "deprecated", "superseded"):
        sub += 4
        if status == "deprecated":
            dep_ok = bool(entry.get("deprecated_date"))
            if dep_ok:
                sub += 1
            else:
                details.append("缺deprecated_date")
        elif status == "superseded":
            sup_ok = bool(entry.get("superseded_by"))
            if sup_ok:
                sub += 1
            else:
                details.append("缺superseded_by")
        else:
            sub += 1  # active: 额外 1 分作为奖励
        score += sub
        details.append(f"status {sub}/5")
    else:
        details.append("status 0/5")

    # 时间戳 (4 分)
    pub = entry.get("public_date")
    crawl = entry.get("crawl_date")
    has_pub = bool(pub and DATE_PATTERN.match(str(pub)))
    has_crawl = bool(crawl and ISO8601_PATTERN.match(str(crawl)))
    ts_score = 0
    if has_pub:
        ts_score += 3
    if has_crawl:
        ts_score += 1
    score += ts_score
    details.append(f"日期 {ts_score}/4")

    return DimensionScore("元数据规范", score, max_score, " | ".join(details))


def score_retrievability(entry: dict) -> DimensionScore:
    """评估可检索性 (满分 15)。

    5 个子项各 3 分：
    - 数据源标签
    - 文档类型标签
    - 接口/系统标签
    - 业务领域标签
    - title 含关键标识

    Args:
        entry: 知识条目。

    Returns:
        DimensionScore。
    """
    max_score = MAX_SCORES["retrievability"]
    score = 0.0
    details = []
    tags = entry.get("tags", [])
    if not isinstance(tags, list):
        tags = []
    title = entry.get("title", "") or ""

    # 数据源标签 (3)
    if any(t in ("sse", "szse", "chinaclear") for t in tags):
        score += 3
        details.append("数据源 3")
    else:
        details.append("数据源 0")

    # 文档类型标签 (3)
    entry_type = entry.get("type")
    expected = TYPE_TO_TAG.get(entry_type) if entry_type else None
    if expected and expected in tags:
        score += 3
        details.append("类型标签 3")
    else:
        details.append("类型标签 0")

    # 接口/系统标签 (3)
    has_is = any(IS_PATTERN.match(t) for t in tags)
    has_sys = any(t in SYSTEM_TAGS for t in tags)
    if has_is or has_sys:
        score += 3
        details.append("接口/系统 3")
    else:
        details.append("接口/系统 0")

    # 业务领域标签 (3)
    if any(t in BUSINESS_TAGS for t in tags):
        score += 3
        details.append("业务领域 3")
    else:
        details.append("业务领域 0")

    # title 含关键标识 (3)
    if IS_PATTERN.search(title) or VERSION_PATTERN.search(title):
        score += 3
        details.append("title标识 3")
    else:
        details.append("title标识 0")

    return DimensionScore("可检索性", score, max_score, " | ".join(details))


def score_info_density(entry: dict) -> DimensionScore:
    """评估信息密度 (满分 15)。

    3 个子项各 5 分：
    - 无公告模板套话
    - title/summary 不冗余
    - 正文有效内容占比

    Args:
        entry: 知识条目。

    Returns:
        DimensionScore。
    """
    max_score = MAX_SCORES["info_density"]
    score = 0.0
    details = []
    md = entry.get("content_markdown") or ""
    title = entry.get("title", "") or ""
    summary = entry.get("summary", "") or ""

    # 无公告模板套话 (5)
    template_hits = 0
    for pat in TEMPLATE_PATTERNS:
        template_hits += len(pat.findall(md))
    penalty = min(template_hits * 2, 5)
    template_score = max(0, 5 - penalty)
    score += template_score
    if template_hits:
        details.append(f"模板套话 {template_score}/5 (-{penalty})")
    else:
        details.append("模板套话 5/5")

    # title/summary 不冗余 (5)
    if not summary:
        details.append("冗余 0/5 (无摘要)")
    else:
        # 简单重复判定：title 中的连续 5 字以上片段出现在 summary 中
        redundant = False
        for i in range(len(title) - 4):
            segment = title[i:i + 5]
            if segment in summary:
                redundant = True
                break
        if redundant:
            details.append("冗余 0/5")
        else:
            score += 5
            details.append("冗余 5/5")

    # 正文有效内容占比 (5)
    if not md:
        details.append("有效内容 0/5")
    else:
        lines = md.splitlines()
        total_lines = max(len(lines), 1)
        # 表格行、代码块行、列表项
        structured = sum(
            1 for line in lines
            if line.strip().startswith("|")
            or line.strip().startswith("```")
            or line.strip().startswith("- ")
            or line.strip().startswith("* ")
            or line.strip().startswith("1.")
        )
        ratio = structured / total_lines
        if ratio >= 0.3:
            ratio_score = 5
        elif ratio >= 0.15:
            ratio_score = 3
        elif ratio >= 0.05:
            ratio_score = 1
        else:
            ratio_score = 0
        score += ratio_score
        details.append(f"有效内容 {ratio_score}/5 ({ratio:.0%})")

    return DimensionScore("信息密度", score, max_score, " | ".join(details))


# ─── 报告生成 ──────────────────────────────────────────────────────────────


def build_report(filepath: str, entry_index: int, entry: dict) -> QualityReport:
    """对单个条目构建质量报告。

    Args:
        filepath: 文件路径。
        entry_index: 条目序号。
        entry: 条目字典。

    Returns:
        QualityReport。
    """
    dimensions = [
        score_summary_quality(entry),
        score_change_completeness(entry),
        score_format_compliance(entry),
        score_retrievability(entry),
        score_info_density(entry),
    ]

    total = round(sum(d.score for d in dimensions), 1)
    grade = grade_from_score(total)

    return QualityReport(
        file=filepath,
        entry_index=entry_index,
        dimensions=dimensions,
        total=total,
        grade=grade,
    )


# ─── 进度条 ──────────────────────────────────────────────────────────────


def print_progress(current: int, total: int, bar_width: int = 40):
    """在终端输出进度条。

    Args:
        current: 当前进度。
        total: 总数量。
        bar_width: 进度条字符宽度。
    """
    if total == 0:
        return
    ratio = current / total
    filled = int(ratio * bar_width)
    bar = "#" * filled + "-" * (bar_width - filled)
    sys.stdout.write(f"\r  Progress [{bar}] {current}/{total} ({ratio*100:.0f}%)")
    sys.stdout.flush()
    if current == total:
        sys.stdout.write("\n")


# ─── 文件读取 ─────────────────────────────────────────────────────────────


def read_entries(filepath: Path) -> list[dict]:
    """读取 JSON 文件，返回条目列表。

    Args:
        filepath: 文件路径。

    Returns:
        条目列表。

    Raises:
        ValueError: 文件不存在或解析失败。
    """
    if not filepath.exists():
        raise ValueError(f"文件不存在: {filepath}")

    try:
        content = filepath.read_text(encoding="utf-8-sig")
    except Exception as e:
        raise ValueError(f"无法读取文件: {filepath}: {e}") from e

    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON 解析失败: {filepath}: {e}") from e

    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("entries", "items"):
            if key in data:
                val = data[key]
                if isinstance(val, list):
                    return val
                if isinstance(val, dict):
                    return [val]
        return [data]

    raise ValueError(f"无法识别的 JSON 结构: {filepath}")


# ─── CLI ──────────────────────────────────────────────────────────────────


def parse_args(argv=None) -> argparse.Namespace:
    """解析命令行参数。

    Args:
        argv: 参数列表。

    Returns:
        解析后的参数。
    """
    parser = argparse.ArgumentParser(
        description="对知识条目做 5 维度质量评分",
    )
    parser.add_argument(
        "files", nargs="*",
        help="JSON 文件路径（支持 glob 通配符）",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", default=False,
        help="输出详细信息",
    )
    parser.add_argument(
        "--no-progress", action="store_true", default=False,
        help="不显示进度条",
    )
    parser.add_argument(
        "--compact", action="store_true", default=False,
        help="使用单行摘要输出（不显示维度进度条）",
    )
    parser.add_argument(
        "--no-color", action="store_true", default=False,
        help="禁用颜色输出",
    )
    return parser.parse_args(argv)


def resolve_files(patterns: list[str]) -> list[Path]:
    """解析文件路径模式。

    Args:
        patterns: 文件路径模式。

    Returns:
        Path 列表。
    """
    result = []
    for pattern in patterns:
        if "*" in pattern or "?" in pattern:
            if not Path(pattern).is_absolute():
                matched = list(Path().glob(pattern))
            else:
                parent = Path(pattern).parent
                name = Path(pattern).name
                if parent.exists():
                    matched = list(parent.glob(name))
                else:
                    matched = []
            if matched:
                result.extend(matched)
            else:
                result.append(Path(pattern))
        else:
            path = Path(pattern)
            if path.is_absolute():
                if path.exists():
                    result.append(path)
                else:
                    result.append(path)
            else:
                matched = list(Path().glob(pattern))
                if matched:
                    result.extend(matched)
                else:
                    result.append(path)
    return result


def main(argv=None) -> int:
    """主入口。

    Args:
        argv: 命令行参数。

    Returns:
        退出码 (0=全部通过, 1=有 C 级)。
    """
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
    args = parse_args(argv)
    if args.no_color:
        _no_color()
    elif not sys.stdout.isatty():
        _no_color()
    else:
        ok = _init_color()
        if not ok:
            _no_color()
    log_level = logging.DEBUG if args.verbose else logging.WARNING
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    filepaths = resolve_files(args.files)

    if not filepaths:
        print(__doc__.split("\n\n")[2])
        return 0

    all_entries: list[tuple[str, int, dict]] = []
    for fp in filepaths:
        if not fp.exists():
            logger.warning("文件不存在，跳过: %s", fp)
            continue
        try:
            entries = read_entries(fp)
        except ValueError as e:
            logger.warning("%s, 跳过", e)
            continue
        for idx, entry in enumerate(entries, start=1):
            all_entries.append((str(fp), idx, entry))

    if not all_entries:
        logger.warning("无有效条目")
        return 0

    has_c = False
    reports: list[QualityReport] = []

    for filepath, idx, entry in all_entries:
        report = build_report(filepath, idx, entry)
        reports.append(report)
        if report.grade == "C":
            has_c = True

    grades: dict[str, int] = {}
    for idx, report in enumerate(reports):
        grades[report.grade] = grades.get(report.grade, 0) + 1
        if args.compact:
            print(report.summary_line)
        else:
            print(report.detailed_block())
            if idx < len(reports) - 1:
                print()
                print(_dsep_line())
                print()

    total = len(reports)
    print()
    print(_sep_line())
    print(f"  {_C_CYAN()}{_C_BOLD()}质量评估汇总{_C_RESET()}  {_C_DIM()}{total} 个条目{_C_RESET()}")
    print(_sep_line())
    grade_colors = {"A": _C_GREEN(), "B": _C_YELLOW(), "C": _C_RED()}
    for g in ("A", "B", "C"):
        cnt = grades.get(g, 0)
        gc = grade_colors.get(g, _C_RESET())
        label = {"A": "高质量", "B": "合格", "C": "需改进"}.get(g, "")
        print(f"  {gc}{_C_BOLD()}{g}{_C_RESET()} (>= {60 if g == 'B' else 80 if g == 'A' else 0}): {cnt} 条  {label}")
    print(_sep_line())

    return 1 if has_c else 0


if __name__ == "__main__":
    sys.exit(main())
