# `hooks/validate_json.py` — OpenCode 知识条目 JSON 校验工具

## 一、定位

作为 OpenCode **自定义工具**（Custom Tool），被整理 Agent（Organizer）在产出最终 `entries.json` 后自动调用，或在流水线 CI 中独立触发。核心使命：确保知识条目 JSON 的**结构完整性、字段合法性、数据一致性**。

---

## 二、输入与触发方式

### 2.1 直接从文件读入

```bash
python hooks/validate_json.py knowledge/articles/sse/entries/entries.json
python hooks/validate_json.py knowledge/articles/**/entries/*.json
```

### 2.2 通过 OpenCode 自定义工具调用

`.opencode/tools/validate-entries.ts` 负责封装调用：

```ts
import { tool } from "@opencode-ai/plugin"
import path from "path"
import { $ } from "bun"

export default tool({
  description: "验证知识条目 JSON 文件的字段完整性和合法性",
  args: {
    source: tool.schema.string()
      .describe("数据源: sse / szse / chinaclear")
      .optional(),
    file: tool.schema.string()
      .describe("指定 JSON 文件路径")
      .optional(),
    fix: tool.schema.boolean()
      .describe("自动修复小问题")
      .optional()
      .default(false),
  },
  async execute(args, context) {
    const script = path.join(context.worktree, "hooks/validate_json.py")
    let cmd = `python ${script}`
    if (args.source) cmd += ` --source ${args.source}`
    if (args.file) cmd += ` ${args.file}`
    if (args.fix) cmd += ` --fix`
    const result = await $`${cmd}`.text()
    return result.trim()
  },
})
```

### 2.3 流水线自动触发

整理 Agent 写文件 → 自动调用本工具 → 失败则回滚并报错。

---

## 三、完整校验规则

### 3.1 字段存在性（error）

检查 JSON 对象是否包含以下 19 个必填字段：

```
id, type, title, source, source_url, summary, tags, status,
version, previous_version, public_date, crawl_date, effective_date,
deprecated_date, superseded_by, related_ids, file_format, file_hash,
content_markdown
```

### 3.2 枚举值校验（error）

| 字段 | 允许值 |
|------|--------|
| `type` | `technical_notice`, `interface_spec`, `business_rule`, `guide`, `software`, `test_doc`, `magazine` |
| `source` | `sse`, `szse`, `chinaclear` |
| `status` | `active`, `deprecated`, `superseded` |
| `file_format` | `html`, `pdf`, `doc`, `docx`, `zip` |

### 3.3 格式校验（error）

| 字段 | 规则 | 示例 |
|------|------|------|
| `id` | 正则 `^(sse\|szse\|chinaclear)-(tech\|iface\|rule\|guide\|soft\|test\|mag)-\d{8}-\d{3}$` | `sse-tech-20250428-001` |
| `public_date` | `YYYY-MM-DD`，`datetime.strptime` 严格校验 | `2025-04-28` |
| `crawl_date` | ISO 8601：`YYYY-MM-DDTHH:MM:SS` 或含时区 | `2025-04-28T10:30:00` |
| `effective_date` | 同 public_date 格式，可为 null | `2025-05-15` |
| `deprecated_date` | 同 public_date 格式，可为 null | `2025-12-31` |

### 3.4 类型校验（error）

| 字段 | 预期类型 | 补充 |
|------|----------|------|
| `title` | `str` | 非空 |
| `summary` | `str` | 可为空串 |
| `tags` | `list[str]` | 元素不允许空串 |
| `related_ids` | `list[str]` | 元素格式同 `id` 规则 |
| `version` | `str` | 可为空串 |
| `previous_version` | `str \| None` | — |
| `superseded_by` | `str \| None` | — |
| `file_hash` | `str` | 须以 `sha256:` 开头 |
| `content_markdown` | `str` | 非空 |

### 3.5 条件必填（error）

| 条件 | 必填字段 |
|------|----------|
| `status = "deprecated"` | `deprecated_date` 不能为 null |
| `status = "superseded"` | `superseded_by` 不能为 null |

### 3.6 一致性校验（warning）

| 规则 | 说明 |
|------|------|
| `id` 的 source 段与 `source` 字段一致 | `sse-tech-...` 中的 `sse` == `source: "sse"` |
| `id` 的 type 段与 `type` 字段一致 | `sse-tech-...` 中的 `tech` → `technical_notice` |
| `id` 的日期段与 `public_date` 一致 | `sse-tech-20250428-001` → `public_date: "2025-04-28"` |

`id` 中 `type` 缩写的映射表：

| `type` 枚举值 | id 缩写 |
|---|---|
| `technical_notice` | `tech` |
| `interface_spec` | `iface` |
| `business_rule` | `rule` |
| `guide` | `guide` |
| `software` | `soft` |
| `test_doc` | `test` |
| `magazine` | `mag` |

### 3.7 跨条目校验（`--full` 模式）

| 规则 | 级别 |
|------|------|
| `id` 在同文件中不重复 | error |
| `superseded_by` 引用的 id 在同文件中存在 | warning |
| 同 `id` 的旧/新条目版本链不矛盾 | warning |

---

## 四、输出格式

每条问题一行，格式：

```
{file}:{行号} {级别} {字段}: {描述}
```

示例：

```
entries.json:3 ERROR source: 值 "ssse" 不在允许范围内 [sse, szse, chinaclear]
entries.json:12 WARNING id: id 中的 source 段 "szse" 与 source 字段 "sse" 不一致
entries.json:18 ERROR deprecated_date: status 为 "deprecated" 时 deprecated_date 不能为空
```

行号 = JSON 对象在文件中的起始行。

---

## 五、退出码

| 退出码 | 含义 |
|--------|------|
| `0` | 全部通过 |
| `1` | 存在 error |

---

## 六、选项

```
usage: validate_json.py [-h] [--fix] [--source {sse,szse,chinaclear}] [--full] [file ...]

positional arguments:
  file                  JSON 文件路径（支持通配符）

options:
  -h, --help            显示帮助
  --fix                 自动修补小问题（日期格式标准化等）
  --source              限定校验特定数据源
  --full                启用跨条目一致性校验（性能开销较大）
```

---

## 七、文件结构

```
hooks/
  validate_json.py     # 主脚本（单文件，~250 行）
```

内部模块划分：

```
validate_json.py
├── 常量区     — SCHEMA（枚举、必填列表、id 缩写映射）
├── 校验器核心  — validate_entry() → list[dict]
├── 跨条目校验  — validate_cross_entry()（--full 模式）
├── 修复器     — fix_entry()（--fix 模式）
├── 文件读取   — read_json_file() → list[dict]
└── main       — 参数解析、循环校验、退出码
```

---

## 八、编码约束

遵循项目 AGENTS.md 规范：

- Google 风格 docstring（所有公开函数）
- `logging` 替代 `print`
- 自定义异常 `ValidationError`
- 文件编码 UTF-8
- 禁止硬编码路径/URL
- 单文件 ≤ 500 行

---

## 九、实现依赖

仅标准库：

| 模块 | 用途 |
|------|------|
| `json` | 解析 JSON |
| `re` | id 格式正则校验 |
| `datetime` | 日期格式严格校验 |
| `sys` | 退出码 |
| `argparse` | CLI 参数 |
| `logging` | 日志输出 |
| `pathlib` | 路径处理 |

无第三方库依赖。
