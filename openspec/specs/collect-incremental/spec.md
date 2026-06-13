# collect-incremental

## Purpose

为 Collect 步骤增加基于发布日期的增量爬取能力，支持按 source 独立记录爬取时间戳，以及无时间戳时基于文件存在性的翻页截断。

## Requirements

### Requirement: Fetch 函数 SHALL 接受 since_date 参数实现增量截断

三个数据源的单分类 fetch 函数（`sse_tech_support_doc_api.fetch_category`、`szse_tech_service_doc_api.fetch_category`、`csdc_biz_rule_doc_api.fetch_subcategory`）SHALL 接受可选的 `since_date: date | None` 参数。传入 `None` 时行为不变（全量爬取）。传入日期时，在分页循环中逐页判断：当某页所有文档的 `publish_date` 均早于 `since_date` 时停止翻页。

#### Scenario: 传入 since_date 跳过多余页面
- **WHEN** 调用 `fetch_category(category, since_date=date(2026, 6, 1))`
- **AND** 第 1 页的最小 `publish_date` 为 `2026-06-10`（全部 ≥ since_date）
- **AND** 第 2 页的最小 `publish_date` 为 `2026-05-25`（全部 < since_date）
- **THEN** 函数 SHALL 返回第 1 页的全部文档
- **AND** SHALL NOT 继续请求第 3 页及后续页面

#### Scenario: since_date 为 None 时全量爬取
- **WHEN** 调用 `fetch_category(category, since_date=None)`
- **THEN** 函数 SHALL 遍历所有页面，行为与当前全量模式完全一致

### Requirement: 页内新旧混杂时 SHALL 保留新项并继续翻页

当一页中同时包含 `publish_date >= since_date` 和 `publish_date < since_date` 的文档时，函数 SHALL 保留新项，且 SHALL NOT 停止翻页。只有当一页中所有文档的 `publish_date` 均早于 `since_date` 时，才停止翻页。

#### Scenario: 页内新旧混杂保留新项
- **WHEN** 调用 `fetch_category(category, since_date=date(2026, 6, 1))`
- **AND** 当前页的 publish_date 为 `[06-03, 06-02, 05-28, 05-25]`
- **THEN** 函数 SHALL 返回 `[06-03, 06-02]`
- **AND** SHALL 继续请求下一页

### Requirement: PipelineState SHALL 按 source 存储 last_crawl_date

`PipelineState` SHALL 为每个数据源独立记录 `last_crawl_date` 字段，在 Collect 步骤成功完成后更新为当前日期。`_execute_collect` 在增量模式下 SHALL 读取该字段并传入 fetch 函数。

#### Scenario: 增量模式读取并传入 last_crawl_date
- **WHEN** `--incremental` 启用
- **AND** `PipelineState` 中 `sse.last_crawl_date` 为 `"2026-06-01"`
- **THEN** `_execute_collect` SHALL 以 `since_date=date(2026, 6, 1)` 调用 SSE 的 fetch 函数

#### Scenario: 首次运行无 last_crawl_date 时全量爬取
- **WHEN** `--incremental` 启用
- **AND** `PipelineState` 中 `sse` 尚未记录 `last_crawl_date`
- **THEN** `_execute_collect` SHALL 以 `since_date=None` 调用 fetch 函数（全量）

#### Scenario: Collect 完成后更新 last_crawl_date
- **WHEN** Collect 步骤成功完成（非 dry-run）
- **THEN** `PipelineState` 中对应 source 的 `last_crawl_date` SHALL 更新为当前日期
