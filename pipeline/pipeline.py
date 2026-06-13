"""知识库自动化流水线 — 五步编排器。

Collect → Parse → Analyze (规则+LLM混合) → Organize → Save (质量门禁)

用法：
    python pipeline/pipeline.py                          # 全量运行
    python pipeline/pipeline.py --from parse --to save   # 从解析开始
    python pipeline/pipeline.py --step save --dry-run    # 试运行
    python pipeline/pipeline.py --incremental            # 增量模式

场景示例：
    # 仅爬取下载（每栏目 10 条元数据，每栏目最多下载 3 个文件）
    python pipeline/pipeline.py --step collect --limit 10 --per-category-limit 5

    # SZSE 已下载数据，直接走分析链路
    python pipeline/pipeline.py --sources szse --from parse --to save

    # SSE 已有分析结果，只对新增/变更文件增量更新
    python pipeline/pipeline.py --sources sse --from parse --incremental

    # 混合：SSE 增量 + SZSE 全量
    python pipeline/pipeline.py --sources sse,szse --from parse

    # 只做 SZSE 的 Analyze → Organize（Parse 已完成时）
    python pipeline/pipeline.py --sources szse --from analyze --to organize

    # 启用 LLM 语义增强（仅规则分析置信度不足时触发 LLM）
    # --limit 3: Collect 每栏目最多抓 3 条元数据, Parse/Analyze 最多处理 3 个文件
    python pipeline/pipeline.py --limit 3 --use-llm

    # 强制 LLM 触发：调低置信度阈值，让更多文档走 LLM 分支
    python pipeline/pipeline.py --limit 3 --use-llm --llm-threshold 0.95

    # 指定文件处理：从解析到入库，仅处理匹配的文件（按路径关键词匹配）
    python pipeline/pipeline.py --sources szse --from parse --to save --files "szse/发行承销/20260424"

    # 指定多个文件或单个文件
    python pipeline/pipeline.py --sources szse --from parse --to save --files "szse/发行承销/20260424/t20260424_620191.html"
    python pipeline/pipeline.py --sources szse --step parse --files "szse/发行承销/20260424" "szse/技术公告/20260529"

    # 指定文件 + 单步运行（结合 --step / --from --to 使用）
    python pipeline/pipeline.py --sources szse --step analyze --files "szse/发行承销/20260424"

    # 完整 Pipeline 结束后查看 LLM 调用成本报告
    # (自动输出到日志 + 保存到 log/cost_report_{timestamp}.json)
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.model_client import tracker, calculate_cost

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.FileHandler(Path("log/pipeline.log"), encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("pipeline")

ARTICLES_DIR = Path("knowledge/articles")
RAW_DIR = Path("knowledge/raw")
PIPELINE_STATE_PATH = Path("knowledge/.pipeline_state.json")


class Step(Enum):
    COLLECT = "collect"
    PARSE = "parse"
    ANALYZE = "analyze"
    ORGANIZE = "organize"
    SAVE = "save"

    def __str__(self):
        return self.value


@dataclass
class PipelineConfig:
    sources: list[str]
    steps: list[Step]
    limit: int | None = None
    download_limit: int | None = None
    per_category_limit: int | None = None
    incremental: bool = False
    use_llm: bool = False
    llm_provider: str = "deepseek"
    llm_threshold: float = 0.7
    fail_fast: bool = False
    skip_quality: bool = False
    dry_run: bool = False
    files: list[str] | None = None


@dataclass
class StepResult:
    step: Step
    status: str  # success / partial / skipped / failed
    total: int = 0
    success: int = 0
    failed: int = 0
    duration: float = 0.0
    error: str | None = None
    detail: dict[str, Any] = field(default_factory=dict)


@dataclass
class PipelineReport:
    status: str
    total_duration: float
    per_step: dict[str, StepResult]


class PipelineState:
    """增量状态管理。"""

    def __init__(self, path: Path = PIPELINE_STATE_PATH):
        self.path = path
        self.data: dict = self._load()

    def _load(self) -> dict:
        if self.path.exists():
            try:
                return json.loads(self.path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                return {"version": 1, "last_run": None, "last_crawl_date": {}, "files": {}}
        return {"version": 1, "last_run": None, "last_crawl_date": {}, "files": {}}

    def save(self):
        self.data["last_run"] = datetime.now(timezone.utc).isoformat()
        self.path.write_text(
            json.dumps(self.data, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def reset(self):
        self.data = {"version": 1, "last_run": None, "last_crawl_date": {}, "files": {}}
        if self.path.exists():
            self.path.unlink()

    def get_last_crawl_date(self, source: str) -> str | None:
        return self.data.get("last_crawl_date", {}).get(source)

    def set_last_crawl_date(self, source: str, crawl_date: str):
        if "last_crawl_date" not in self.data:
            self.data["last_crawl_date"] = {}
        self.data["last_crawl_date"][source] = crawl_date
        self.save()

    def get_file_state(self, path: str) -> dict | None:
        return self.data["files"].get(path)

    def step_done(self, path: str, step: str) -> bool:
        fstate = self.get_file_state(path)
        if fstate:
            return fstate.get("steps", {}).get(step, {}).get("done", False)
        return False

    def mark_step_done(self, path: str, step: str):
        fstate = self.get_file_state(path)
        if not fstate:
            fstate = {"sha256": "", "mtime": "", "steps": {}}
            self.data["files"][path] = fstate
        fstate["steps"][step] = {"done": True, "timestamp": datetime.now(timezone.utc).isoformat()}


class PipelineRunner:
    """流水线编排器。"""

    STEPS_ORDER = [Step.COLLECT, Step.PARSE, Step.ANALYZE, Step.ORGANIZE, Step.SAVE]

    def __init__(self, config: PipelineConfig):
        self.config = config
        self.results: dict[Step, StepResult] = {}
        self.state = PipelineState()

    # ------------------------------------------------------------------
    # Run
    # ------------------------------------------------------------------

    def run(self) -> PipelineReport:
        tracker._records.clear()
        start = time.time()
        logger.info("=" * 60)
        logger.info(
            "Pipeline 启动 | 数据源: %s | 步骤: %s",
            ",".join(self.config.sources),
            " → ".join(str(s) for s in self.config.steps),
        )
        if self.config.dry_run:
            logger.info("  试运行模式 — 不写入任何文件")
        if self.config.incremental:
            logger.info("  增量模式 — 跳过已完成的文件")
        if self.config.use_llm:
            logger.info(
                "  LLM 增强通道已开启 (provider=%s, threshold=%.2f)",
                self.config.llm_provider,
                self.config.llm_threshold,
            )
        logger.info("=" * 60)

        for step in self.config.steps:
            logger.info("")
            logger.info("--- Step %d: %s ---", self.STEPS_ORDER.index(step) + 1, step.value.upper())
            result = self._execute_step(step)
            self.results[step] = result
            self._log_step_result(result)
            if result.status == "failed" and self.config.fail_fast:
                logger.error("fail-fast: 步骤 %s 失败，终止流水线", step.value)
                break

        total_time = time.time() - start
        report = self._build_report(total_time)
        self._print_report(report)
        logger.info("Pipeline 完成 | 总耗时: %.1fs | 状态: %s", total_time, report.status)
        return report

    # ------------------------------------------------------------------
    # Step executor
    # ------------------------------------------------------------------

    def _execute_step(self, step: Step) -> StepResult:
        t0 = time.time()
        try:
            handlers = {
                Step.COLLECT: self._execute_collect,
                Step.PARSE: self._execute_parse,
                Step.ANALYZE: self._execute_analyze,
                Step.ORGANIZE: self._execute_organize,
                Step.SAVE: self._execute_save,
            }
            return handlers[step]()
        except Exception as e:
            import traceback
            logger.error("步骤 %s 异常: %s\n%s", step.value, e, traceback.format_exc())
            return StepResult(step=step, status="failed", duration=time.time() - t0, error=str(e))

    # ---- Step 1: Collect ----

    def _execute_collect(self) -> StepResult:
        t0 = time.time()
        ok = fail = 0
        sources_detail = {}

        for source in self.config.sources:
            logger.info("  采集 %s...", source)

            since_date_str = None
            check_file_exists = False
            if self.config.incremental:
                since_date_str = self.state.get_last_crawl_date(source)
                if since_date_str is None:
                    check_file_exists = True  # 无 last_crawl_date，尝试文件存在性截断

            try:
                all_items = {}
                if source == "sse":
                    from utils.sse_tech_support_doc_api import (
                        fetch_all_categories, download_category, SseDocItem,
                    )
                    result = fetch_all_categories(
                        max_pages_per_category=None, max_items_per_category=self.config.limit,
                        since_date=since_date_str,
                        check_file_exists=check_file_exists,
                    )
                    all_items = {k: [it.to_dict() for it in v] for k, v in result.items()}
                elif source == "szse":
                    from utils.szse_tech_service_doc_api import (
                        fetch_all_categories, download_category, SzseDocItem,
                    )
                    result = fetch_all_categories(
                        max_items_per_category=self.config.limit,
                        since_date=since_date_str,
                        check_file_exists=check_file_exists,
                    )
                    all_items = {k: [it.to_dict() for it in v] for k, v in result.items()}
                elif source == "chinaclear":
                    from utils.csdc_biz_rule_doc_api import (
                        fetch_all_subcategories, download_subcategory, CsdcDocItem,
                    )
                    result = fetch_all_subcategories(
                        max_items_per_sub=self.config.limit,
                        since_date=since_date_str,
                        check_file_exists=check_file_exists,
                    )
                    all_items = {k: [it.to_dict() for it in v] for k, v in result.items()}
                else:
                    logger.warning("    未知数据源: %s", source)
                    fail += 1
                    continue

                total = sum(len(v) for v in all_items.values())
                source_detail = {"status": "metadata_fetched", "total_items": total}

                # 保存 metadata.json（非 dry-run 时）
                if not self.config.dry_run:
                    meta_dir = RAW_DIR / source
                    meta_dir.mkdir(parents=True, exist_ok=True)
                    meta_file = meta_dir / "metadata.json"
                    meta_file.write_text(
                        json.dumps(all_items, ensure_ascii=False, indent=2), encoding="utf-8",
                    )

                # 下载文件（非 dry-run 时）
                if not self.config.dry_run:
                    flat = []
                    pc_limit = self.config.per_category_limit
                    for cat_name, cat_items in all_items.items():
                        if source == "chinaclear":
                            from utils.csdc_biz_rule_doc_api import CsdcDocItem
                            item_cls = CsdcDocItem
                        elif source == "szse":
                            from utils.szse_tech_service_doc_api import SzseDocItem
                            item_cls = SzseDocItem
                        else:
                            from utils.sse_tech_support_doc_api import SseDocItem
                            item_cls = SseDocItem
                        cat_files = []
                        for it in cat_items:
                            item = item_cls(**it)
                            if getattr(item, "file_format", "") != "html":
                                cat_files.append(item)
                        if pc_limit is not None:
                            cat_files = cat_files[:pc_limit]
                            logger.info("    [%s] 每栏目下载上限: %d 个文件", cat_name, pc_limit)
                        flat.extend(cat_files)

                    dl_limit = self.config.download_limit
                    if dl_limit is not None:
                        logger.info("    下载上限: %d 个文件", dl_limit)
                        flat = flat[:dl_limit]

                    if source == "chinaclear":
                        dl_result = download_subcategory(flat)
                    else:
                        dl_result = download_category(flat)

                    dl_ok = sum(1 for r in dl_result if getattr(r, "local_path", None))
                    dl_fail = sum(1 for r in dl_result if not getattr(r, "local_path", None))
                    source_detail["download_ok"] = dl_ok
                    source_detail["download_fail"] = dl_fail
                    logger.info("    %s: 元数据 %d 条, 下载成功 %d, 失败 %d", source, total, dl_ok, dl_fail)
                else:
                    logger.info("    [试运行] %s: 元数据 %d 条", source, total)

                sources_detail[source] = source_detail
                ok += 1

                if self.config.incremental and not self.config.dry_run:
                    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
                    self.state.set_last_crawl_date(source, today)
            except Exception as e:
                logger.error("    %s 采集失败: %s", source, e)
                sources_detail[source] = {"status": "failed", "error": str(e)}
                fail += 1
                if self.config.fail_fast:
                    return StepResult(
                        step=Step.COLLECT, status="failed",
                        success=ok, failed=fail, duration=time.time() - t0,
                        error=str(e), detail=sources_detail,
                    )

        status = "success" if fail == 0 else ("partial" if ok > 0 else "failed")
        return StepResult(
            step=Step.COLLECT, status=status,
            total=ok + fail, success=ok, failed=fail,
            duration=time.time() - t0, detail=sources_detail,
        )

    # ---- Step 2: Parse ----

    def _execute_parse(self) -> StepResult:
        t0 = time.time()
        from utils.parse_all import (
            collect_raw_files, parse_file, save_output,
            load_crawl_meta, match_crawl_meta,
        )

        ok = fail = 0
        crawl_items = load_crawl_meta()
        source_detail = {}

        for source in self.config.sources:
            files = collect_raw_files(source_filter=source, limit=self.config.limit)
            if not files:
                logger.info("  %s: 无待解析文件", source)
                source_detail[source] = {"status": "skipped", "total": 0}
                continue

            # 文件级过滤：仅保留匹配 --files 指定路径的文件
            if self.config.files:
                filtered = []
                for f in files:
                    fpath_str = str(f[3]).replace("\\", "/")
                    if any(fn in fpath_str for fn in self.config.files):
                        filtered.append(f)
                files = filtered
                if not files:
                    logger.info("  %s: 无匹配指定文件的待解析文件", source)
                    source_detail[source] = {"status": "skipped", "total": 0}
                    continue

            source_ok = source_fail = 0
            for src, category, sub_category, fpath in files:
                rel_path = str(fpath)
                if self.config.incremental and self.state.step_done(rel_path, "parse"):
                    continue

                crawl_item = match_crawl_meta(fpath, crawl_items)
                if self.config.dry_run:
                    logger.info("  [试运行] 解析 %s", fpath.name)
                    source_ok += 1
                    continue

                result = parse_file(src, category, sub_category, fpath)
                if result is None:
                    logger.warning("  ⚠️ 解析失败: %s", fpath.name)
                    source_fail += 1
                    if self.config.fail_fast:
                        break
                    continue

                try:
                    save_output(src, category, sub_category, fpath, result, crawl_item)
                    state_path = str(fpath)
                    self.state.mark_step_done(state_path, "parse")
                    source_ok += 1
                except Exception as e:
                    logger.error("  ❌ 保存失败 [%s]: %s", fpath.name, e)
                    source_fail += 1
                    if self.config.fail_fast:
                        break

            source_detail[source] = {"status": "success", "ok": source_ok, "fail": source_fail}
            ok += source_ok
            fail += source_fail

        if not self.config.dry_run:
            self.state.save()

        status = "success" if fail == 0 else ("partial" if ok > 0 else "failed")
        return StepResult(
            step=Step.PARSE, status=status,
            total=ok + fail, success=ok, failed=fail,
            duration=time.time() - t0, detail=source_detail,
        )

    # ---- Step 3: Analyze ----

    def _execute_analyze(self) -> StepResult:
        t0 = time.time()
        from utils.analyze_all import collect_markdown_files, analyze_document, save_analysis

        ok = fail = 0
        llm_calls = 0
        llm_provider = None

        if self.config.use_llm:
            from pipeline.model_client import OpenAICompatibleProvider, RetryConfig
            try:
                llm_provider = OpenAICompatibleProvider(
                    provider_name=self.config.llm_provider,
                )
                llm_provider.retry_config = RetryConfig()
                logger.info("  LLM 提供商: %s", self.config.llm_provider)
            except Exception as e:
                logger.warning("  LLM 初始化失败，降级到纯规则: %s", e)

        source_detail = {}

        for source in self.config.sources:
            md_files = collect_markdown_files(source=source, limit=self.config.limit)
            if not md_files:
                logger.info("  %s: 无待分析 Markdown 文件", source)
                source_detail[source] = {"status": "skipped", "total": 0}
                continue

            # 文件级过滤：将 --files 中提取的关键词（最后两级路径）用于匹配
            if self.config.files:
                filter_keys = set()
                for fn in self.config.files:
                    parts = fn.strip("/\\").replace("\\", "/").split("/")
                    # 取最后两级路径作为匹配关键词
                    for k in parts[-2:]:
                        filter_keys.add(k)
                    # 也取文件名（不含扩展名）作为关键词
                    base = Path(fn).stem
                    if base:
                        filter_keys.add(base)
                filtered = []
                for mf in md_files:
                    mf_str = str(mf).replace("\\", "/")
                    if any(k in mf_str for k in filter_keys):
                        filtered.append(mf)
                md_files = filtered
                if not md_files:
                    logger.info("  %s: 无匹配指定文件的 Markdown 文件", source)
                    source_detail[source] = {"status": "skipped", "total": 0}
                    continue

            source_ok = source_fail = 0
            source_llm = 0

            for i, md_file in enumerate(md_files, 1):
                rel_path = str(md_file)
                if self.config.incremental and self.state.step_done(rel_path, "analyze"):
                    continue

                if self.config.dry_run:
                    logger.info("  [试运行] 分析 %s", md_file.name)
                    source_ok += 1
                    continue

                try:
                    rule_result = analyze_document(md_file, i)
                    should_use_llm = self._should_use_llm(rule_result, llm_provider)

                    if should_use_llm:
                        llm_result = self._llm_analyze(llm_provider, md_file, rule_result)
                        if llm_result and not llm_result.get("degraded"):
                            final = self._merge_analysis(rule_result, llm_result)
                            source_llm += 1
                        else:
                            if llm_result and llm_result.get("degraded"):
                                logger.warning("  LLM 降级，使用规则通道结果 [%s]", md_file.name)
                            final = rule_result
                    else:
                        final = rule_result

                    save_analysis(md_file, final)
                    self.state.mark_step_done(rel_path, "analyze")
                    source_ok += 1
                except Exception as e:
                    logger.error("  ❌ 分析失败 [%s]: %s", md_file.name, e)
                    source_fail += 1
                    if self.config.fail_fast:
                        break

            source_detail[source] = {
                "status": "success",
                "ok": source_ok,
                "fail": source_fail,
                "llm_enhanced": source_llm,
            }
            ok += source_ok
            fail += source_fail
            llm_calls += source_llm

        if not self.config.dry_run:
            self.state.save()

        status = "success" if fail == 0 else ("partial" if ok > 0 else "failed")
        detail = {"llm_calls": llm_calls, "per_source": source_detail}
        return StepResult(
            step=Step.ANALYZE, status=status,
            total=ok + fail, success=ok, failed=fail,
            duration=time.time() - t0, detail=detail,
        )

    def _should_use_llm(self, rule_result: dict, llm_provider: Any) -> bool:
        if not llm_provider or not self.config.use_llm:
            return False
        rule_changes = rule_result.get("changes", [])
        if len(rule_changes) > 200:
            rule_result["changes"] = []
            return True
        return rule_result.get("confidence", 0.75) < self.config.llm_threshold

    def _llm_analyze(self, provider: Any, md_file: Path, rule_result: dict) -> dict | None:
        from pipeline.model_client import chat_with_retry

        title = rule_result.get("title", md_file.stem)
        doc_id = rule_result.get("doc_id", "")
        doc_type = doc_id.split("-")[1] if "-" in doc_id else ""
        version = rule_result.get("version")
        rule_change_count = len(rule_result.get("changes", []))

        md_content = md_file.read_text(encoding="utf-8", errors="replace")
        clean_content = re.sub(r"<metadata>.*?</metadata>", "", md_content, flags=re.DOTALL)
        max_chars = 12000
        if len(clean_content) > max_chars:
            clean_content = clean_content[:max_chars] + "\n\n...[文档过长已截断]"

        system_prompt = """你是一个证券行业技术文档变更分析专家。
请分析以下文档内容，识别其中的技术变更或规则变更。

输出严格的 JSON 格式（不要包含 markdown 代码块标记）：
{
  "changes": [
    {
      "type": "新增|修改|删除|废止",
      "summary": "20字以内的变更摘要",
      "detail": "50字以内的详细描述",
      "severity": "major|minor|cosmetic"
    }
  ],
  "tags": ["标签1", "标签2"],
  "summary": "30字以内的文档摘要",
  "confidence": 0.95,
  "related_ids": []
}

注意事项：
- type 只能取 "新增"、"修改"、"删除"、"废止" 之一
- severity: major=影响现有系统/流程, minor=新增功能/补充说明, cosmetic=格式/勘误
- 无变更时 changes 返回空数组 []
- tags 包括：数据源(sse/szse/chinaclear)、文档类型、涉及系统(如IS105)、技术主题
- confidence 范围 0.0-1.0
- related_ids：如果本文档明确引用或替代了其他已知文档，填入其 ID，否则留空"""

        user_prompt = f"""文档信息：
- 标题: {title}
- 文档类型: {doc_type}
- 版本: {version or '无'}
- 规则通道已检出 {rule_change_count} 条格式标注变更（来自红色/蓝色文本标注）

请分析以下文档全文，重点关注：
1. 规则通道可能遗漏的变更（无颜色标注的正文变更描述）
2. 对规则通道已检出的变更做 type 纠偏
3. 提取语义标签（不限于预定义关键词库）

文档内容：
{clean_content}"""

        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
            resp = chat_with_retry(provider, messages)
            if resp.degraded:
                logger.warning("  LLM 降级 [%s]", md_file.name)
                return {"degraded": True}
            content = resp.content.strip()
            content = re.sub(r"^```(?:json)?\s*", "", content)
            content = re.sub(r"\s*```$", "", content)
            return json.loads(content)
        except Exception as e:
            logger.warning("  LLM 分析失败 [%s]: %s", md_file.name, e)
            return {"degraded": True}

    def _merge_analysis(self, rule_result: dict, llm_result: dict) -> dict:
        merged = rule_result.copy()

        rule_changes = rule_result.get("changes", [])
        llm_changes = llm_result.get("changes", [])

        type_overrides = {c.get("summary", "")[:40]: c for c in llm_changes if c.get("summary")}
        merged_changes = []
        seen = set()

        for c in rule_changes:
            key = c.get("summary", "")[:40]
            if key in type_overrides:
                llm_c = type_overrides[key]
                c["type"] = llm_c.get("type", c["type"])
                c["summary"] = llm_c.get("summary", c["summary"])
                sevs = {"cosmetic": 0, "minor": 1, "major": 2}
                c_sev = sevs.get(c.get("severity", "minor"), 1)
                l_sev = sevs.get(llm_c.get("severity", "minor"), 1)
                if l_sev > c_sev:
                    c["severity"] = llm_c["severity"]
            merged_changes.append(c)
            seen.add(key)

        for c in llm_changes:
            key = c.get("summary", "")[:40]
            if key not in seen:
                merged_changes.append(c)
                seen.add(key)

        merged["changes"] = merged_changes

        llm_summary = llm_result.get("summary", "")
        if llm_summary and len(llm_summary) > 5:
            merged["summary"] = llm_summary

        merged["tags"] = list(set(rule_result.get("tags", []) + llm_result.get("tags", [])))

        if llm_result.get("related_ids"):
            merged["related_ids"] = llm_result["related_ids"]

        merged["confidence"] = round(max(
            rule_result.get("confidence", 0.75),
            llm_result.get("confidence", 0.75),
        ), 2)

        return merged

    # ---- Step 4: Organize ----

    def _execute_organize(self) -> StepResult:
        t0 = time.time()
        from utils.organize_all import scan_analysis_files, process_analysis_file, build_index

        ok = fail = 0
        source_detail = {}

        for source in self.config.sources:
            analysis_files = scan_analysis_files(source=source)
            if not analysis_files:
                logger.info("  %s: 无待整理的分析文件", source)
                source_detail[source] = {"status": "skipped", "total": 0}
                continue

            # 文件级过滤：将 --files 中提取的关键词用于匹配分析文件
            if self.config.files:
                filter_keys = set()
                for fn in self.config.files:
                    parts = fn.strip("/\\").replace("\\", "/").split("/")
                    for k in parts[-2:]:
                        filter_keys.add(k)
                    base = Path(fn).stem
                    if base:
                        filter_keys.add(base)
                filtered = []
                for af in analysis_files:
                    af_str = str(af).replace("\\", "/")
                    if any(k in af_str for k in filter_keys):
                        filtered.append(af)
                analysis_files = filtered
                if not analysis_files:
                    logger.info("  %s: 无匹配指定文件的分析文件", source)
                    source_detail[source] = {"status": "skipped", "total": 0}
                    continue

            source_ok = source_fail = 0
            entries = []

            for af in analysis_files:
                rel_path = str(af)
                if self.config.incremental and self.state.step_done(rel_path, "organize"):
                    continue

                if self.config.dry_run:
                    logger.info("  [试运行] 整理 %s", af.name)
                    source_ok += 1
                    continue

                try:
                    entry = process_analysis_file(af, dry_run=False)
                    if entry:
                        entries.append(entry)
                        self.state.mark_step_done(rel_path, "organize")
                        source_ok += 1
                    else:
                        source_fail += 1
                except Exception as e:
                    logger.error("  ❌ 整理失败 [%s]: %s", af.name, e)
                    source_fail += 1
                    if self.config.fail_fast:
                        break

            if entries and not self.config.dry_run:
                entries_dir = ARTICLES_DIR / source / "entries"
                entries_dir.mkdir(parents=True, exist_ok=True)
                index = build_index(source, entries)
                index_path = entries_dir / "entries.json"
                index_path.write_text(
                    json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8",
                )
                logger.info("  %s: 索引已更新 (%d 条目)", source, len(entries))

            source_detail[source] = {
                "status": "success",
                "ok": source_ok,
                "fail": source_fail,
                "entries": len(entries),
            }
            ok += source_ok
            fail += source_fail

        if not self.config.dry_run:
            self.state.save()

        status = "success" if fail == 0 else ("partial" if ok > 0 else "failed")
        return StepResult(
            step=Step.ORGANIZE, status=status,
            total=ok + fail, success=ok, failed=fail,
            duration=time.time() - t0, detail=source_detail,
        )

    # ---- Step 5: Save ----

    def _execute_save(self) -> StepResult:
        t0 = time.time()
        from utils.organize_all import perform_version_traceability

        total_entries = 0
        validated = 0
        needs_review = 0
        chains_built = 0
        quality_errors = []
        source_detail = {}

        for source in self.config.sources:
            entries_dir = ARTICLES_DIR / source / "entries"
            if not entries_dir.exists():
                logger.info("  %s: 无条目目录", source)
                source_detail[source] = {"status": "skipped"}
                continue

            entries = []
            for f in sorted(entries_dir.glob("*.json")):
                if f.name == "entries.json":
                    continue
                try:
                    entries.append(json.loads(f.read_text(encoding="utf-8")))
                except (json.JSONDecodeError, OSError) as e:
                    quality_errors.append(f"{f.name}: {e}")

            total_entries += len(entries)

            source_validated = 0
            source_needs_review = 0
            if not self.config.skip_quality:
                try:
                    from hooks.validate_json import validate_entry
                    for entry in entries:
                        errors = validate_entry(entry)
                        if errors:
                            quality_errors.extend(
                                f"{entry.get('id', '?')}: {e}" for e in errors
                            )
                        else:
                            source_validated += 1
                except Exception as e:
                    logger.warning("  质量校验模块加载失败: %s", e)

            for entry in entries:
                if "needs_review" in entry.get("tags", []):
                    source_needs_review += 1

            if not self.config.dry_run:
                try:
                    perform_version_traceability(source)
                    chains_built += 1
                except Exception as e:
                    logger.warning("  %s 版本追溯失败: %s", source, e)

            source_detail[source] = {
                "status": "success",
                "entries": len(entries),
                "validated": source_validated,
                "needs_review": source_needs_review,
            }
            validated += source_validated
            needs_review += source_needs_review

        if not self.config.dry_run:
            self._trigger_notifications()

        status = "success"
        if quality_errors:
            status = "partial"
            for err in quality_errors[:10]:
                logger.warning("  质量: %s", err)

        detail = {
            "total_entries": total_entries,
            "validated": validated,
            "needs_review": needs_review,
            "chains_built": chains_built,
            "quality_errors": len(quality_errors),
            "per_source": source_detail,
        }
        return StepResult(
            step=Step.SAVE, status=status,
            total=total_entries, success=validated,
            duration=time.time() - t0, detail=detail,
        )

    def _trigger_notifications(self):
        pass

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _log_step_result(self, result: StepResult):
        status_icon = {
            "success": "[OK]",
            "partial": "[..]",
            "skipped": "[--]",
            "failed": "[!!]",
        }.get(result.status, "[??]")
        logger.info(
            "  => %s [%s] %d/%d 成功, %.1fs",
            status_icon,
            result.status,
            result.success,
            result.total or result.success,
            result.duration,
        )
        if result.error:
            logger.info("  => 错误: %s", result.error)

    def _build_report(self, total_duration: float) -> PipelineReport:
        statuses = [r.status for r in self.results.values()]
        if all(s == "success" for s in statuses):
            overall = "success"
        elif all(s == "skipped" for s in statuses):
            overall = "skipped"
        elif any(s == "failed" for s in statuses):
            overall = "failed"
        else:
            overall = "partial"
        return PipelineReport(
            status=overall,
            total_duration=total_duration,
            per_step={str(k): v for k, v in self.results.items()},
        )

    def _print_report(self, report: PipelineReport):
        sep = "-" * 52
        status_icon = {"success": "OK", "partial": "..", "failed": "!!", "skipped": "--"}
        icon = status_icon.get(report.status, "??")
        print()
        print(f"+{sep}+")
        print(f"|{'':^50}|")
        print(f"|{'Pipeline - Execution Report':^50}|")
        print(f"|{'':^50}|")
        print(f"+{sep}+")
        print(f"| Status: {icon} {report.status:<10}{'Duration: ' + f'{report.total_duration:.1f}s':>26}|")
        print(f"+{sep}+")

        step_names = {
            "collect": "Collect",
            "parse": "Parse",
            "analyze": "Analyze",
            "organize": "Organize",
            "save": "Save",
        }
        for i, step in enumerate(self.STEPS_ORDER, 1):
            result = self.results.get(step)
            if not result:
                continue
            s_icon = status_icon.get(result.status, "??")
            label = f"Step {i}: {step_names[step.value]}"
            stats = f"{result.success}/{result.total}" if result.total else str(result.success)
            line = f"| {s_icon} {label:<20} {stats:<12} {result.duration:>8.1f}s |"
            print(line)

            if step == Step.ANALYZE:
                llm = result.detail.get("llm_calls", 0)
                if llm:
                    print(f"|{'':^50}|")
                    print(f"|   +- Rule: {result.success - llm}/{result.success}{'':>28}|")
                    print(f"|   +- LLM:  {llm}  triggers (conf<{self.config.llm_threshold}){'':>12}|")
            elif step == Step.SAVE:
                d = result.detail
                print(f"|{'':^50}|")
                print(f"|   +- Valid: {d.get('validated', 0)}{'':>34}|")
                print(f"|   +- Needs review: {d.get('needs_review', 0)}{'':>24}|")
                print(f"|   +- Version chains: {d.get('chains_built', 0)}{'':>22}|")

        # LLM 费用汇总
        llm_cost_cny = tracker.estimated_cost(currency="cny")
        llm_cost_usd = tracker.estimated_cost(currency="usd")
        if llm_cost_cny > 0:
            print(f"|{'':^50}|")
            print(f"|{'LLM Cost':^50}|")
            print(f"|{'CNY ' + f'{llm_cost_cny:.4f}':>27}{'USD ' + f'{llm_cost_usd:.4f}':>23}|")

        print(f"+{sep}+")
        print()


def _parse_args() -> PipelineConfig:
    parser = argparse.ArgumentParser(
        description="知识库自动化流水线 — Collect → Parse → Analyze → Organize → Save",
    )
    parser.add_argument(
        "--sources", default="sse,szse,chinaclear",
        help="数据源列表，逗号分隔（默认: sse,szse,chinaclear）",
    )
    parser.add_argument("--from", dest="from_step", help="起始步骤")
    parser.add_argument("--to", dest="to_step", help="终止步骤")
    parser.add_argument("--step", help="只跑单步")
    parser.add_argument("--limit", type=int, help="每步最多处理文件数（Collect 时=每栏目元数据上限）")
    parser.add_argument("--download-limit", type=int, dest="download_limit", help="Collect 时最多下载文件数（总）")
    parser.add_argument("--per-category-limit", type=int, dest="per_category_limit", help="Collect 时每栏目最多下载文件数")

    parser.add_argument("--incremental", action="store_true", help="增量模式")
    parser.add_argument("--reset", action="store_true", help="重置增量状态")

    parser.add_argument("--use-llm", action="store_true", help="启用 LLM 语义增强")
    parser.add_argument("--llm-provider", default="deepseek", help="LLM 提供商")
    parser.add_argument("--llm-threshold", type=float, default=0.7, help="LLM 触发阈值")

    parser.add_argument("--skip-quality", action="store_true", help="跳过质量门禁")
    parser.add_argument("--fail-fast", action="store_true", help="遇错即停")
    parser.add_argument("--dry-run", action="store_true", help="试运行")
    parser.add_argument("--files", nargs="+", help="指定处理的文件路径（相对于 knowledge/raw/），支持多个，如 szse/发行承销/20260424/t20260424_620191.html")
    parser.add_argument("--verbose", action="store_true", help="详细日志")

    args = parser.parse_args()

    if args.verbose:
        for handler in logging.getLogger().handlers:
            handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)

    if args.reset:
        state = PipelineState()
        state.reset()
        logger.info("增量状态已重置")

    sources = [s.strip() for s in args.sources.split(",") if s.strip()]

    step_map = {s.value: s for s in Step}
    if args.step:
        if args.step not in step_map:
            parser.error(f"无效步骤: {args.step}，可选: {', '.join(step_map)}")
        steps = [step_map[args.step]]
    else:
        from_step = step_map.get(args.from_step, Step.COLLECT)
        to_step = step_map.get(args.to_step, Step.SAVE)
        all_steps = [Step.COLLECT, Step.PARSE, Step.ANALYZE, Step.ORGANIZE, Step.SAVE]
        from_idx = all_steps.index(from_step)
        to_idx = all_steps.index(to_step)
        steps = all_steps[from_idx:to_idx + 1]

    return PipelineConfig(
        sources=sources,
        steps=steps,
        limit=args.limit,
        download_limit=args.download_limit,
        per_category_limit=args.per_category_limit,
        incremental=args.incremental,
        use_llm=args.use_llm,
        llm_provider=args.llm_provider,
        llm_threshold=args.llm_threshold,
        fail_fast=args.fail_fast,
        skip_quality=args.skip_quality,
        dry_run=args.dry_run,
        files=args.files,
    )


def main():
    config = _parse_args()
    runner = PipelineRunner(config)
    report = runner.run()

    if tracker._records:
        tracker.report()
        report_path = Path("log") / f"cost_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        tracker.save_report(str(report_path))

    sys.exit(0 if report.status == "success" else 1)


if __name__ == "__main__":
    main()
