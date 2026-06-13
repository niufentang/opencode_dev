## 1. PipelineState: last_crawl_date 存储

- [x] 1.1 在 `PipelineState.data` 中增加 `last_crawl_date: dict[str, str]` 字段
- [x] 1.2 新增 `get_last_crawl_date(source: str) -> date | None` 方法
- [x] 1.3 新增 `set_last_crawl_date(source: str, crawl_date: date)` 方法，调用后立即保存
- [x] 1.4 `reset()` 方法清空 `last_crawl_date`

## 2. SSE fetch_category: since_date 参数

- [x] 2.1 `fetch_category` 增加 `since_date: date | None = None` 参数，透传给 `_fetch_paginated`
- [x] 2.2 `_fetch_paginated` 增加 `since_date` 参数，在 page 循环顶注入截断逻辑（页全旧才停）

## 3. SZSE fetch_category: since_date 参数

- [x] 3.1 `fetch_category` 增加 `since_date: str | None = None` 参数
- [x] 3.2 在分页循环中注入截断逻辑（页全旧才停）

## 4. ChinaClear fetch_subcategory: since_date 参数

- [x] 4.1 `fetch_subcategory` 增加 `since_date: str | None = None` 参数，透传给 `_fetch_paginated`
- [x] 4.2 `_fetch_paginated` 增加 `since_date` 参数，在 page 循环顶注入截断逻辑（页全旧才停）

## 5. Pipeline _execute_collect 适配

- [x] 5.1 增量模式下读取 `state.get_last_crawl_date(source)`，传入 fetch 函数
- [x] 5.2 每个 source 抓取成功后调用 `state.set_last_crawl_date(source, today)` 并保存
- [x] 5.3 非增量模式或首次运行（无 last_crawl_date）传入 `since_date=None`

## 6. 基于文件存在性的翻页截断（D8）

- [x] 6.1 在 fetch 函数中增加 `check_file_exists` 回退模式：当 `since_date=None` 且 `--incremental` 启用时，对每页 items 检查本地文件是否存在
- [x] 6.2 HTML 等非文件类文档不参与检查
- [x] 6.3 页内所有可检查的文件均存在时停止翻页
