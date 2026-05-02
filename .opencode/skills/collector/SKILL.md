---
name: collector
description: "Use this skill when the task involves crawling or scraping documents from the SSE (上交所) trading tech support portal, SZSE (深交所) technical service site, or ChinaClear (中国结算) business rules page. Triggers include: @collector, mentions of crawling/采集/爬取/抓取, references to the three exchange data sources, or requests to download PDF/Word documents from these websites. Also use when checking for new or updated documents from these sources, performing incremental crawling with dedup, or downloading technical documents for the knowledge base. Do NOT use for general web scraping unrelated to these three specific sources, or for modifying already-crawled data."
allowed-tools: [Read, Grep, Glob, WebFetch]
---

# 采集技能 (Collector Skill)

## 使用场景

从上交所交易技术支持专区、深交所技术服务、中国结算业务规则三大数据源自动爬取技术与规则文档，提取结构化元数据并下载原始文件。

## 输入

- `--max-pages N`：每栏目最大爬取页数（默认全部）
- `--source sse|szse|chinaclear`：限定数据源
- `--no-download`：仅采集元数据，不下载文件

## 执行步骤

### Step 1: 去重检查

采集前先检查 `knowledge/raw/crawl_metadata.json` 或各源 `metadata.json` 中已有的记录，以 `url` + `title` 联合作为唯一标识跳过已采集条目。

使用 `Glob` 查找已有元数据文件，使用 `Read` 读取内容比对。

### Step 2: 上交所采集

**目标 URL：** `https://www.sse.com.cn/services/tradingtech/home/`

**8 个栏目：** 技术通知、服务指引、技术接口、技术指南、软件下载、测试文档、技术杂志、历史资料

**分页 URL 模式：**
- 第 1 页：`{category_path}/s_list.shtml`
- 第 N 页：`{category_path}/s_list_{N}.shtml`

**提取方法：** 用 `WebFetch` 获取列表页 HTML，从 `<dl><dd>` 中解析 `<a>`（title 属性）和 `<span>` 文本。

**提取字段：** title, publish_date（YYYY-MM-DD）, url（绝对路径）, category, file_format（从 URL 扩展名推断）

### Step 3: 深交所采集

**目标 URL：** `https://www.szse.cn/marketServices/technicalservice/index.html`

**5 个栏目：** 技术公告、交易系统介绍、服务指引、数据接口、技术指南

**分页 URL 模式：**
- 第 1 页：`{path}/`
- 第 N 页：`{path}/index_{N-1}.html`

**提取方法：**
- 技术公告：全量 DOM 渲染（JS 分页），从 `<ul class="newslist date-right">` 下的 `<li>` 提取 `<a>` 和 `<span class="time">`
- 其他栏目：静态列表页，直接提取下载链接

### Step 4: 中国结算采集

**目标 URL：** `http://www.chinaclear.cn/zdjs/fywgz/law_flist.shtml`

**12 个子栏目：** 账户管理、登记与存管、清算与交收、证券发行、债券业务、股票期权、融资融券与转融通、基金与资产管理业务、涉外与跨境业务、协助执法、其他、已废止业务规则

**分页 URL 模式（iframe 内容页）：**
- 第 1 页：`{sub_path}/code_1.shtml`
- 第 N 页：`{sub_path}/code_1_{N}.shtml`

**提取方法：** 从 `<li class="item">` 中提取 `<a>` 和 `<span class="date">`

### Step 5: 文件下载

对于可下载的文件类型（pdf/doc/docx/xls/xlsx/zip/rar/txt），下载至 `knowledge/raw/{source}/{category}/`。

**命名规则：** `{YYYYMMDD}_{安全标题前80字符}.{ext}`

### Step 6: 输出 crawl_metadata.json

合并三个数据源的采集结果，输出扁平 JSON 数组：

```json
[
  {
    "title": "关于xx接口规范V3.2发布的通知",
    "publish_date": "2025-04-28",
    "url": "https://www.sse.com.cn/...",
    "category": "技术通知",
    "sub_category": null,
    "file_format": "pdf",
    "file_size": 245760,
    "local_path": "knowledge/raw/sse/技术通知/20250428_xxx.pdf",
    "crawl_time": "2025-04-28T10:30:00+00:00"
  }
]
```

## 注意事项

- **请求间隔：** 每个页面之间至少间隔 1 秒，批量分页间隔不低于 0.5 秒
- **增量策略：** 以 `url` + `title` 联合去重，仅当 `publish_date` 或 `url` 变化才重采
- **中国结算维护期：** 每年劳动节（5/1-5/4）官网暂停服务，返回 302 跳转
- **禁止高频请求** — 遵守项目红线
- **文件名安全：** 替换 `<>:"/\|?*` 为 `_`
- **crawl_time 格式：** ISO 8601 含 UTC 时区

## 输出

- `knowledge/raw/crawl_metadata.json` — 本次采集总表
- `knowledge/raw/{source}/metadata.json` — 各源单独元数据
- `knowledge/raw/{source}/{category}/{file}` — 实际下载的文件

## 质量检查

- [ ] 每条约目的 title 非空且有实际意义
- [ ] publish_date 格式为 YYYY-MM-DD
- [ ] url 为完整 URL（含协议和域名）
- [ ] category 匹配对应数据源的栏目定义
- [ ] file_format 使用已知格式集合
- [ ] 已检查与已有 crawl_metadata.json 的去重逻辑

## 参考脚本

实际批量采集可调用：
- `utils/sse_tech_support_doc_api.py`
- `utils/szse_tech_service_doc_api.py`
- `utils/csdc_biz_rule_doc_api.py`

以及测试脚本：
- `test/test_sse.py`
- `test/test_szse.py`
- `test/test_csdc.py`
