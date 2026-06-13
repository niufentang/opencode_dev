## Context

当前 Collect 步骤在增量模式下仅靠检查 `crawl_metadata.json` 是否存在来决定是否跳过整个步骤。一旦跑过，后续永远不会重新抓取。对于每天只新增少量文档的场景，全量翻页造成大量无效请求。

三个数据源（SSE、SZSE、ChinaClear）的列表页均按发布时间倒序排列，但 API 均不支持服务端按日期过滤。因此增量方案必须客户端实现——在分页循环中根据文档发布时间截断。

## Goals / Non-Goals

**Goals:**
- 为三个数据源的 fetch 函数增加 `since_date` 可选参数，实现基于发布日期的翻页截断
- `PipelineState` 按 source 独立记录 `last_crawl_date`，增量模式自动传入 fetch 函数
- 页内新旧混杂时保留新项并继续翻页，保证不丢失数据
- `--reset` 时清空 `last_crawl_date`，确保重置语义完整
- 无 `last_crawl_date` 时基于文件存在性做翻页截断，避免首次全量超时后重复爬取

**Non-Goals:**
- 检测文档内容更新（日期不变的内容变更无法覆盖）
- 检测文档被删除（需定期全量对比）
- 重构三个数据源的分页循环为统一模式
- 跨 source 协调爬取时间

## Decisions

### D1: 三个 fetch 函数各自独立修改，不做统一重构

**决策**：SSE/CC 共享 `_fetch_paginated` 模式，SZSE 内联分页循环。各自在循环顶注入截断逻辑，不重构 SZSE 的结构。

**理由**：总改动量 ~17 行，不值得为一次增量优化做架构重构。改动点一致——在每页解析后判断 `all(item.publish_date < since_date for item in items)` 并 `break`。

### D2: "页全旧才停"策略

**决策**：不因页内出现旧项而停止翻页。只有当一页中所有文档的 `publish_date` 均早于 `since_date` 时才停止。

**理由**：同一天发布的文档可能跨多页分布。严格按 `publish_date < since_date` 截断会漏掉同一天的数据。"多翻 1 页"的开销（仅列表页 HTML，~KB 级别）可接受。

### D3: --reset 时清空 last_crawl_date

**决策**：`--reset` 重置 PipelineState 时，将 `last_crawl_date` 一并清空。下次运行 Collect 走全量。

**理由**：reset 语义是"回到初始状态"。保留 `last_crawl_date` 会导致元数据 JSON 不完整（只含最近几页）而磁盘上有历史文件，状态不一致。

### D4: 每个 source 完成后立即保存 state

**决策**：在 Collect 的 source 循环中，每个 source 抓取成功后立即更新 `last_crawl_date` 并保存 `PipelineState`。

**理由**：避免一个 source 失败导致前面成功的 source 状态丢失。某 source 失败不影响已成功的 source，下次增量运行时成功的 source 不会重复抓取。

### D5: 截断逻辑实现方式

在每个 page 循环中，对解析后的 items 列表做判断：

```python
if since_date is not None:
    all_old = True
    for item in items:
        if item.publish_date and item.publish_date >= since_date:
            all_old = False
            break
    if all_old:
        logger.info("增量模式: %s 后无更新，停止翻页", since_date)
        break
```

空日期的文档不参与截断判断。如果所有文档都缺日期，不会触发截断（保证至少全量跑一次）。

**不修改** `_parse_list_html` 等解析函数的签名——在调用方做后处理过滤，保持解析函数纯净。

### D6: since_date 类型 — 函数签名用 date，内部用字符串比较

**决策**：`fetch_category` / `fetch_subcategory` 的 `since_date` 参数类型为 `date | None`，入口处用 `.isoformat()` 转为字符串，传入 `_fetch_paginated` 及截断逻辑使用字符串比较。

**理由**：调用方类型安全；`publish_date` 保持 `str` 不变，不需迁移 DocItem 数据模型；`YYYY-MM-DD` 格式字符串比较等价于日期比较，零解析开销。

### D7: 按 source 独立判断增量，去掉全局 crawl_metadata.json 跳过

**决策**：拆除现有 `if meta_path.exists() and incremental: 跳过全部 Collect` 的粗粒度逻辑。改为 per-source 判断：`last_crawl_date` 存在的 source 走增量爬取，不存在的 source 自动全量爬取。

**理由**：加新数据源时不会因为已有 `crawl_metadata.json` 而被错误跳过；状态完全由 `PipelineState` 统一管理，消除隐式文件状态依赖。

```json
{
  "version": 1,
  "last_run": "2026-06-14T...",
  "last_crawl_date": {
    "sse": "2026-06-14",
    "szse": "2026-06-14",
    "chinaclear": "2026-06-13"
  },
  "files": {}
}
```

`last_crawl_date` 按 source 存储，值格式 `YYYY-MM-DD`（与 API 的 `publish_date` 格式一致）。首次运行该字段不存在，等价于全量。

### D8: 无 last_crawl_date 时的"文件存在即停止"回退

**决策**：当 `--incremental` 启用但某 source 无 `last_crawl_date`（首次运行或 reset 后），不直接退化为全量爬取。改为：逐页翻取元数据列表，对每页的文档项检查本地文件是否已存在。当某页**所有文档对应的文件**均已存在于磁盘上时，停止翻页。

**理由**：首次全量爬取通常超时中断，导致 `last_crawl_date` 从未保存。此时再次增量运行仍会全量翻页，浪费大量请求。"文件存在即停止"利用已下载的文件作为隐式标记，即使没有 `last_crawl_date` 也能实现增量效果。

**边界规则**：
- 文件存在性检查基于 `item.local_path` 或通过 `category + publish_date + title` 构造的预期路径
- 非文件类（HTML 页面等）不参与检查，不影响停止判断
- 若某页因文件存在而停止，该页之前的文件已被下载，同页中更新文档可能漏掉（但可通过下一次带 `since_date` 的增量补充）

```python
def _all_files_exist(items: list, storage_dir: Path) -> bool:
    for item in items:
        if getattr(item, "file_format", "") == "html":
            continue  # HTML 不参与判断
        local_path = getattr(item, "local_path", None)
        if local_path and not Path(local_path).exists():
            return False
    return True
```

## Risks / Trade-offs

| 风险 | 缓解措施 |
|------|----------|
| 文档内容更新但日期不变，增量无法检测 | 已知局限，接受。可定期全量运行 |
| 文档被删除，增量无法感知 | 同上 |
| 同一天多页分布，多翻 1 页开销 | 仅列表页 HTML ~KB 级别，可忽略 |
| 无 last_crawl_date 时文件检查截断可能漏掉同页后半段的新文档 | 下一次带 `since_date` 的增量会自动补充，不永久丢失 |
| 数据源改变排列顺序（非倒序） | 按"页全旧才停"策略，仍能保证至少全量一次 |
