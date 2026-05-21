# entries.json 去除方案评估

> 编写日期：2026-05-14
> 状态：方案备选，待评审

---

## 一、背景

`entries.json` 是 `knowledge/articles/{source}/entries/` 目录下的汇总索引文件，包含该数据源所有知识条目的精简摘要（id、title、type、status、tags）。其与单条目 JSON 文件（`{doc_id}.json`）存在数据冗余。

本方案客观评估去除 entries.json 的影响及具体调整步骤。

---

## 二、现状：全量依赖清单

### 2.1 写入侧（4 处）

| 位置 | 代码片段 | 作用 |
|------|---------|------|
| `utils/organize_all.py:301-319` | `build_index()` 函数 | 从 entries 列表构建索引字典 |
| `pipeline/pipeline.py:662-666` | `index = build_index(...)` → 写入 | 流水线整理的 Step 末尾写入索引 |
| `utils/organize_all.py:580-584` | `build_index()` + 写入 | `main()` 标准模式 |
| `utils/organize_all.py:547-551` | `build_index()` + 写入 | `--trace-only` 模式版本追溯后重建索引 |
| `utils/organize_all.py:599-...` | `build_index()` + 写入 | 版本追溯后重新读取并重建索引 |

### 2.2 校验侧（1 处）

| 位置 | 校验逻辑 |
|------|---------|
| `utils/check_entries_quality.py:75-84` | 检查 entries.json 存在性 + `total_entries` 与实际文件数一致 |

### 2.3 跳过侧（7 处）

所有遍历 entries 目录的场景均需跳过 entries.json 自身：

| 位置 | 代码 |
|------|------|
| `pipeline/pipeline.py:710` | `if f.name == "entries.json": continue` |
| `utils/organize_all.py:438` | 同上 |
| `utils/organize_all.py:541` | 同上 |
| `utils/organize_all.py:592` | 同上 |
| `utils/entry_stats.py:13` | 同上 |
| `utils/check_szse_versions.py:6` | 同上 |
| `utils/check_entries_quality.py:17` | 同上 |

### 2.4 文档 & Agent 配置侧（6 处）

| 文件 | 内容 |
|------|------|
| `.opencode/agents/organizer.md:31` | "去重逻辑读取 entries.json 中已有条目" |
| `.opencode/agents/organizer.md:82` | "维护 entries.json 索引文件" |
| `.opencode/agents/organizer.md:120` | 目录结构树中包含 entries.json |
| `.opencode/agents/organizer.md:130-155` | `### entries.json` 专节说明 |
| `.opencode/skills/ls-organizer/SKILL.md` | 技能描述及目录结构 |
| `doc/06_pipeline_design.md:244,253` | 产出物及索引重建说明 |
| `doc/validate-json-hook-requirements.md` | 校验示例包含 entries.json |

### 2.5 其他（1 处）

| 位置 | 说明 |
|------|------|
| `hooks/validate_json.py:5,7` | 作为示例参数被引用，非逻辑依赖 |

---

## 三、去除方案（分 5 步）

### Step 1：删除写入侧

**`utils/organize_all.py` 改动：**

```diff
- def build_index(source: str, entries: list[dict]) -> dict:
-     """构建 entries.json 索引文件。"""
-     ...
```

- 删除 `build_index()` 整函数（:301-319）
- `main()` 中删除 3 处 `build_index()` 调用块（:547-551, :580-584, :599-...）

**`pipeline/pipeline.py` 改动：**

```diff
  from utils.organize_all import scan_analysis_files, process_analysis_file
- from utils.organize_all import scan_analysis_files, process_analysis_file, build_index
```

```diff
- index = build_index(source, entries)
- index_path = entries_dir / "entries.json"
- index_path.write_text(
-     json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8",
- )
- logger.info("  %s: 索引已更新 (%d 条目)", source, len(entries))
```

### Step 2：删除校验侧

**`utils/check_entries_quality.py:75-84`：**

```diff
-     # Verify index
-     index_path = entries_dir / "entries.json"
-     if index_path.exists():
-         index = json.loads(index_path.read_text(encoding="utf-8"))
-         if index["total_entries"] != entry_count:
-             errors.append(...)
-         if len(index["entries"]) != entry_count:
-             errors.append(...)
-     else:
-         errors.append("entries.json index file missing")
```

### Step 3：清理跳过逻辑（7 处）

所有 `if f.name == "entries.json": continue` 行可安全删除。

涉及文件：
- `pipeline/pipeline.py:710`
- `utils/organize_all.py:438, 541, 592`
- `utils/entry_stats.py:13`
- `utils/check_szse_versions.py:6`
- `utils/check_entries_quality.py:17`

### Step 4：更新文档 & Agent 配置

**`.opencode/agents/organizer.md`：**
- :31 — 去重描述改为"遍历目录读取已有 {doc_id}.json 文件比对"
- :82 — 删除"维护 entries.json 索引"整节（可替换为"条目文件自动构成目录索引"）
- :120 — 从目录树移除 entries.json
- :130-155 — 删除 `### entries.json` 专节

**`.opencode/skills/ls-organizer/SKILL.md`：**
- skill 描述中去掉 "generate entries.json index"
- 目录树中移除 entries.json

**`doc/06_pipeline_design.md`：**
- :244 — 产出物改为 `articles/{source}/entries/{doc_id}.json`
- :253 — "索引重建"描述改为"目录自动反映条目状态"

### Step 5：清理产物

```bash
rm knowledge/articles/sse/entries/entries.json
```

（szse 和 chinaclear 尚无 entries.json，无需操作）

---

## 四、方案遗漏评估

### 已覆盖
- ✅ 写入侧 4 处
- ✅ 校验侧 1 处
- ✅ 跳过侧 7 处
- ✅ 文档/Agent 配置 6 处
- ✅ 产物文件清理

### 需补充确认
- ⚠️ **CI/CD 配置**：需检查 `.github/` 或其他 CI 目录下是否有直接引用 `entries.json` 路径的配置（当前项目未发现此类配置）
- ⚠️ **外部依赖方**：如有其他系统（如搜索索引、通知分发）通过 URL 或固定路径读取 entries.json，需同步调整
- ⚠️ **`opencode.json`**：当前未直接引用 entries.json，但确认无误

### 去重逻辑的影响
organizer.md 描述"读取 entries.json 去重"，但**实际代码中此逻辑尚未实现**。去除 entries.json 后，未来如需实现去重，改由 `Get-ChildItem *.json` 替代即可。

---

## 五、保留 entries.json 的好处

| 维度 | 优势 |
|------|------|
| **查询性能** | 读取 entries.json 是 O(1) 单次 IO；遍历目录是所有条目数量的 O(n) + 磁盘 IO |
| **轻量摘要** | entries.json 仅含 5 个摘要字段，不加载 content_markdown（单条目可能 >100KB） |
| **原子快照** | 目录遍历时若有并发写入，可能读到不一致状态；entries.json 是原子快照 |
| **去重基座** | 保留 entries.json 后，未来去重可直接读索引 → O(1) 判重，无需遍历全部单条目文件 |
| **外部集成** | 下游系统（搜索索引、Dashboard、通知分发）只需拉一个 entries.json 即可获取条目清单 |
| **校验便利** | 现有 `check_entries_quality.py` 已建立"索引 vs 实际文件数"的交叉验证，去除后失去这层门禁 |

---

## 六、决策建议

| 时间窗口 | 建议 |
|---------|------|
| **短期（无外部消费方）** | 可去除，精简项目结构，7 处代码改动 + 文档更新，约 1 人日工作量 |
| **中期（计划接入搜索/分发）** | 建议保留，entries.json 作为轻量摘要索引对下游系统价值大 |
| **长期（条目数 > 500）** | 强烈建议保留或重构升级为更完善的索引机制 |

**折中方案**：保留 entries.json 但将其纳入质量门禁，确保 `total_entries` 始终与实际文件数一致，避免"写索引却无人消费"的纯粹冗余。

---

## 七、索引机制重构升级方案

若选择保留并升级索引机制（而非简单去除），以下为 5 种可选方案，按复杂度递增排列。

---

### 方案 A：自愈式索引（最小改动）

当前 entries.json 是"手工维护"，核心问题在于**写入后无人验证一致性**。

改进：
- 将 entries.json **降级为缓存**：每次读取时先比较 `mtime(entries.json)` 与目录最新文件的 `mtime`，若过期则自动重建
- 或：在 `pipeline.py` 的 Save Step 末尾触发一次 `check_entries_quality.py`，不一致则告警 + 自动重建

```
读取流程：请求索引 → 校验缓存时效 → 过期则重建 → 返回
```

| 优点 | 缺点 |
|------|------|
| 改动极小（~10 行校验逻辑） | 仍仅提供摘要列表，功能无实质增强 |
| 消除"索引与实际不一致"风险 | |

---

### 方案 B：全局统一索引（跨源检索）

当前每个 source 各自维护 entries.json。升级为**一个全局索引文件**：

`knowledge/articles/global_index.json`

```json
{
  "last_updated": "2026-05-14T00:00:00+00:00",
  "total_entries": 200,
  "by_source": { "sse": 171, "szse": 29, "chinaclear": 0 },
  "by_type": { "guide": 50, "interface_spec": 80, ... },
  "entries": [
    {
      "id": "sse-guide-00000000-007", "source": "sse",
      "title": "...", "type": "guide", "status": "superseded",
      "public_date": null, "tags": [...]
    }
  ],
  "version_chains": [
    {
      "series": "IS101",
      "versions": [
        { "id": "sse-guide-00000000-007", "ver": "1" },
        { "id": "sse-guide-00000000-051", "ver": "2" }
      ]
    }
  ]
}
```

| 优点 | 缺点 |
|------|------|
| 跨 source 搜索无需遍历 3 个目录 | 单文件可能较大（~500KB for 500 entries） |
| version_chains 可快速回答"某接口的版本演进" | 写入时需要合并 3 个 source 数据 |
| 便于外部消费者一次性获取全量清单 | |

---

### 方案 C：分层索引（按查询模式组织）

不再只有一个 entries.json，而是按查询需求拆分多个索引文件：

```
knowledge/articles/
├── global_index.json              ← 总览（仅 id + title，极轻量）
├── by_type/
│   ├── guide.json
│   ├── interface_spec.json
│   └── technical_notice.json
├── by_status/
│   ├── active.json
│   ├── superseded.json
│   └── deprecated.json
└── version_chains.json            ← 完整的版本追溯图
```

每个索引文件仅含该维度下的摘要字段，总数据量不变但**查询可按需加载**。

| 优点 | 缺点 |
|------|------|
| 按需读取，适合不同场景 | 索引文件数量增多，写入复杂度上升 |
| 快速回答"当前生效有哪些"等高频问题 | 部分索引可实时计算（如 type 分组），未必需要持久化 |

---

### 方案 D：SQLite 嵌入式数据库

用 SQLite 替代 JSON 文件作为索引引擎：

`knowledge/articles/index.db`

```sql
CREATE TABLE entries (
    id TEXT PRIMARY KEY,
    title TEXT,
    type TEXT,
    source TEXT,
    status TEXT,
    version TEXT,
    previous_version TEXT,
    superseded_by TEXT,
    public_date TEXT,
    tags TEXT,              -- JSON array
    file_path TEXT,         -- 指向 {doc_id}.json
    summary TEXT
);

CREATE INDEX idx_source ON entries(source);
CREATE INDEX idx_type ON entries(type);
CREATE INDEX idx_status ON entries(status);
CREATE INDEX idx_public_date ON entries(public_date);
```

| 优点 | 缺点 |
|------|------|
| 原生 SQL 查询，任意维度组合过滤 | 项目新增 sqlite3 依赖 |
| 索引实时一致（INSERT 时同步更新） | 二进制文件无法直接 diff / manual review |
| 支持全文检索（FTS5） | Git 不擅长追踪二进制变更 |
| 适合下游系统直接读取 | 与现有纯 JSON 工具链风格不一致 |

---

### 方案 E：混合架构（JSON + SQLite，推荐）

兼顾人类可读与机器查询：

```
knowledge/articles/
├── entries/                       ← 单条目 JSON（不变）
│   ├── {doc_id}.json
│   └── .gitkeep
├── index.json                     ← 轻量人类可读摘要（仅 id + title + status）
└── index.db                       ← SQLite 全量可查询索引（自动从 JSON 构建）
```

- `index.json`：极简，50 行以内，供人眼快速浏览、git diff
- `index.db`：CI 或 pipeline 中自动构建，供搜索 / Dashboard 等下游使用

构建命令：
```bash
python utils/rebuild_index.py   # 扫描 entries/ → 生成 index.json + index.db
```

| 优点 | 缺点 |
|------|------|
| `index.json` 保持人类可读、git diff-able | 维护 2 套索引有一定复杂度 |
| `index.db` 支持复杂查询 | 需在 CI 或 pipeline 中编排重建 |
| **增删改全量由 `rebuild_index.py` 单点负责，消除不一致** | |

---

### 方案对比总览

| 维度 | A 自愈式 | B 全局索引 | C 分层索引 | D SQLite | E 混合 |
|------|----------|-----------|-----------|----------|--------|
| 改动量 | 极小 | 中 | 中 | 大 | 大 |
| 消除不一致 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 跨源检索 | ❌ | ✅ | 需聚合 | ✅ | ✅ |
| 版本追溯查询 | ❌ | ✅ | ✅ | ✅ | ✅ |
| 人类可读 | ✅ | ✅ | ✅ | ❌ | ✅ (index.json) |
| 下游集成友好 | ❌ | 中 | 中 | ✅ | ✅ |
| 与现有 JSON 工具链兼容 | ✅ | ✅ | ✅ | ❌ | ✅ |

**推荐演进路径**：先做 **A（自愈式）** 解决一致性问题，后续按需演进至 **B（全局索引）** 或 **E（混合架构）**。
