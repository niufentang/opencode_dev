## Why

当前 Collect 步骤每次全量爬取所有分类的所有页面，再靠 `overwrite=False` 跳过已下载的文件。对于每天只有少量新增文档的网站（上交所、深交所、中国结算），大量请求浪费在遍历已抓过的历史页面上，且无法检测文档更新。

## What Changes

- 为三个数据源的 fetch 函数增加 `since_date` 可选参数，传入后逐页爬取时截断：遇到一页中所有文档 `publish_date < since_date` 时停止翻页
- `PipelineState` 按 source 记录 `last_crawl_date`，增量模式传给 fetch 函数
- 保持首次运行（无 `since_date`）行为不变
- 页内新旧混杂时采用"页全旧才停"策略，保证不丢失同一天数据
- 不新增对文档内容更新或删除的检测（增量策略固有局限，可接受）

## Capabilities

### New Capabilities
- `collect-incremental`: 为 Collect 步骤增加基于日期的增量爬取能力

### Modified Capabilities
- （无，仅实现层变更，不涉及 spec 级行为变化）

## Impact

- `pipeline/pipeline.py` — `_execute_collect` 读取 `last_crawl_date` 并传入 fetch 函数
- `utils/sse_tech_support_doc_api.py` — `fetch_category` / `_fetch_paginated` 增加 `since_date` 参数及截断逻辑
- `utils/szse_tech_service_doc_api.py` — `fetch_category` 增加 `since_date` 参数及截断逻辑
- `utils/csdc_biz_rule_doc_api.py` — `fetch_subcategory` / `_fetch_paginated` 增加 `since_date` 参数及截断逻辑
- `pipeline/pipeline.py` — `PipelineState` 增加 `last_crawl_date` 存储
