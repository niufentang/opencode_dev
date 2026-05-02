# `hooks/check_quality.py` — 5 维度质量评分标准

## 一、定位

对整理 Agent（Organizer）产出的标准知识条目 JSON 进行 **5 维度质量评分**，输出等级 A/B/C，作为质量门禁与持续改进的依据。

核心目标：确保障券交易所技术文档知识条目的**变更可追溯、元数据规范、检索可发现、内容无冗余**。

---

## 二、输入与触发方式

### 2.1 直接从文件读入

```bash
# 单文件
python hooks/check_quality.py knowledge/articles/sse/entries/sse-iface-20250328-140.json

# 通配符批量
python hooks/check_quality.py knowledge/articles/sse/entries/*.json

# 禁用颜色（终端不支持时）
python hooks/check_quality.py knowledge/articles/sse/entries/*.json --no-color

# 紧凑模式（一行输出，无进度条）
python hooks/check_quality.py knowledge/articles/sse/entries/*.json --compact
```

### 2.2 通过 OpenCode 自定义工具调用

`.opencode/tools/check-quality.ts` 负责封装调用：

```ts
import { tool } from "@opencode-ai/plugin"
import path from "path"
import { $ } from "bun"

export default tool({
  description: "对知识条目做 5 维度质量评分",
  args: {
    files: tool.schema.string()
      .describe("JSON 文件路径（支持通配符）")
      .optional(),
    compact: tool.schema.boolean()
      .describe("紧凑模式")
      .optional()
      .default(false),
    verbose: tool.schema.boolean()
      .describe("输出详细信息")
      .optional()
      .default(false),
  },
  async execute(args, context) {
    const script = path.join(context.worktree, "hooks/check_quality.py")
    let cmd = `python ${script}`
    if (args.files) cmd += ` ${args.files}`
    if (args.verbose) cmd += ` --verbose`
    if (args.compact) cmd += ` --compact`
    cmd += ` --no-color`
    const result = await $`${cmd}`.text()
    return result.trim()
  },
})
```

### 2.3 流水线自动触发

整理 Agent 写文件 → 自动调用本工具评分 → 存在 C 级条目则告警或阻止入库。

---

## 三、等级标准

| 等级 | 总分范围 | 含义 | 退出码 |
|------|----------|------|--------|
| **A（绿色）** | >= 80 | 高质量，可直接入库 | 0 |
| **B（黄色）** | >= 60 | 合格，建议改进薄弱维度 | 0 |
| **C（红色）** | < 60 | 需改进，阻止入库 | 1 |

等级颜色仅在支持 ANSI 的终端中显示（Windows Terminal / VS Code / Linux / macOS），终端不支持时自动降级为纯文本。

---

## 四、维度总览

总分 **100 分**，分 5 个维度加权评分：

| 维度 | 满分 | 核心评估内容 |
|------|------|--------------|
| **摘要变更精度** | 25 | summary 是否准确捕获变更要点 |
| **变更完整性** | 25 | 版本链 + 状态一致性 + 实质内容 |
| **元数据规范** | 20 | 必填元数据字段合规性 |
| **可检索性** | 15 | 标签覆盖面 + title 标识性 |
| **信息密度** | 15 | 无模板套话 + 无冗余 + 有效内容占比 |

---

## 五、评分细则

### 5.1 摘要变更精度（25 分）

评估 `summary` 字段是否准确捕获了文档的变更要点。

#### 评分规则

| 条件 | 得分 | 说明 |
|------|------|------|
| `summary` 缺失或为空 | **0** | 无摘要内容 |
| 仅含"初始版本"类标记 | **12** | 新文档无变更历史，属有效元数据而非缺陷 |
| 普通摘要（无变更关键词） | **15** | 信息完整但未描述具体变更内容 |
| 含接口编号 `IS\d+` | **+5** | 如"IS101 接口 V3.2 发布" |
| 含版本号 `v\d+(\.\d+)+` | **+3** | 如"接口规范 V3.2" |
| 含具体字段/协议名 | **+3** | 如"调整了订单字段长度限制" |
| **上限** | **25** | — |

**示例：**

| 摘要内容 | 得分 | 理由 |
|----------|------|------|
| `初始版本，暂无历史变更` | **12** | 有效初始标记 |
| `本次更新主要调整了交易系统接口规范` | **15** | 普通，无具体编号/字段 |
| `IS101 接口 V3.2 发布，调整了订单字段长度，新增了撤单协议` | **23** | 接口号+版本号+字段名全命中 |
| `IS124 接口 V2.1 发布，本次调整了债券质押式回购行情字段的精度` | **23** | 同上 |

#### 占位摘要检测

以下模式视为占位摘要，得 **0 分**：

```
暂无.*摘要|无.*内容|待补充|placeholder
```

> 注意：`初始版本` 不在此列，属于有效元数据，得 12 分。

---

### 5.2 变更完整性（25 分）

评估版本链、状态一致性、变更内容的实质价值——这是知识库**核心价值的直接度量**。

#### 评分规则概览

| 子项 | 满分 | 核心逻辑 |
|------|------|----------|
| **版本链完整** | 8 | `previous_version` 或 `superseded_by` 是否正确填写 |
| **状态一致性** | 7 | deprecated → 有 `deprecated_date`；superseded → 有 `superseded_by` |
| **变更内容实质** | 5 | content_markdown 包含表格/代码/列表等结构化技术内容 |
| **has_changes 准确** | 5 | 有变更的条目正确标注 `has_changes` 标签 |

#### 版本链完整（8 分）细则

| 条件 | 得分 | 场景 |
|------|------|------|
| `previous_version` 或 `superseded_by` 任一正确填写 | **8** | 有明确的版本追溯信息 |
| 两者均为 null 且 status=active | **6** | 首次发布，无历史版本，合理 |
| 两者均为 null 且 status≠active | **0** | 异常：已废弃/替代但不标记来源 |
| 填写了但值为空字符串 `""` | **2** | 字段存在但无实际内容 |

#### 状态一致性（7 分）细则

| 条件 | 得分 | 说明 |
|------|------|------|
| status=active，无额外字段要求 | **7** | 活跃状态无需补充字段 |
| status=superseded 且有 `superseded_by` | **7** | 正确标记了替代条目 |
| status=deprecated 且有 `deprecated_date` | **7** | 正确标记了废止日期 |
| deprecated 缺少 `deprecated_date` | **0** | 典型扣分场景（实测 26/26 缺失） |
| superseded 缺少 `superseded_by` | **0** | 替代关系断裂 |

#### 变更内容实质（5 分）细则

扫描 `content_markdown` 中的结构化技术内容，检测该条目是否包含**有实质价值的技术描述**：

| 检测项 | 加分 | 说明 |
|--------|------|------|
| 包含 `\|` 表格 | +2 | 接口字段表、参数说明表等 |
| 包含 ``` 代码块 | +2 | XML 报文样例、JSON 示例、协议编码示例 |
| 技术术语密度 >= 5 种 | +1 | 如"接口+T+协议+STEP+规范" |
| **上限** | **5** | — |

> 设计意图：单纯的大段公告模板文本（如"根据相关规定……"）无法获得分数，而包含表格/代码的技术文档可获得满分。

#### has_changes 准确（5 分）细则

| 条件 | 得分 | 说明 |
|------|------|------|
| 有版本历史 + 有 `has_changes` 标签 | **5** | 正确标注 |
| 无版本历史 + 无 `has_changes` 标签 | **5** | 首次发布，无变更，正确 |
| **误标**：无变更但有 `has_changes` | **0** | 引起下游误判 |
| **漏标**：有变更但无 `has_changes` | **0** | 变更无法被检索发现 |

> "有版本历史" 判定条件：`version > "1"` 或 `status` 为 `deprecated/superseded` 或有 `previous_version/superseded_by`。

---

### 5.3 元数据规范（20 分）

评估必填元数据字段的合规性与一致性。

#### 评分规则

| 子项 | 满分 | 扣分条件 |
|------|------|----------|
| **id 格式** | 4 | 不匹配正则 `^(sse\|szse\|chinaclear)-(tech\|iface\|rule\|guide\|soft\|test\|mag)-\d{8}-\d{3}$` |
| **title 非空** | 4 | 缺失、非字符串、或纯空白 |
| **source_url** | 3 | 缺失或空字符串 |
| **status + 版本链一致性** | 5 | status 是否合法 + 条件字段是否存在 |
| **时间戳** | 4 | `public_date` (3) + `crawl_date` (1) |

#### id 格式正则

```
^(sse|szse|chinaclear)-(tech|iface|rule|guide|soft|test|mag)-\d{8}-\d{3}$
```

| 段 | 说明 | 示例 |
|----|------|------|
| source | 数据源 | `sse`, `szse`, `chinaclear` |
| type_abbr | 类型缩写 | `tech`, `iface`, `rule`, `guide`, `soft`, `test`, `mag` |
| date | 发布日期 | `20250428` |
| seq | 序号 | `001` |

#### status + 版本链一致性（5 分）细则

| 条件 | 得分 |
|------|------|
| status 在 `{active, deprecated, superseded}` 中 | **4**（否则 0） |
| status=deprecated 且 `deprecated_date` 存在 | **+1** |
| status=superseded 且 `superseded_by` 存在 | **+1** |
| **上限** | **5** |

#### 时间戳（4 分）细则

| 条件 | 得分 | 说明 |
|------|------|------|
| `public_date` 存在且格式 YYYY-MM-DD | **3** | 发布日期，用户检索的核心维度 |
| `crawl_date` 存在且格式 ISO 8601 | **1** | 采集时间，辅助追溯 |
| **上限** | **4** | — |

---

### 5.4 可检索性（15 分）

评估条目被搜索定位的能力。**5 个子项各 3 分**，独立计分。

| 子项 | 满分 | 评估逻辑 |
|------|------|----------|
| **数据源标签** | 3 | tags 包含 `{sse, szse, chinaclear}` 之一 |
| **文档类型标签** | 3 | tags 包含与 `type` 字段对应的类型标签 |
| **接口/系统标签** | 3 | tags 包含 `IS\d+` 编号或 `STEP`/`BINARY`等系统名 |
| **业务领域标签** | 3 | tags 包含业务领域标签（债券/股权/期权等） |
| **title 含关键标识** | 3 | title 包含接口编号 `IS\d+` 或版本号 `v\d+` |

> 设计意图：可检索性是知识库的"发现能力"指标。一个拥有丰富标签和明确标识的条目，用户在搜索时更容易命中，无论数据多"深"或多"浅"。

#### 标准标签分类参考

| 分类 | 标签列表 |
|------|----------|
| **数据源** | `sse`, `szse`, `chinaclear` |
| **文档类型** | `technical_notice`, `interface_spec`, `business_rule`, `guide`, `software`, `test_doc`, `magazine` |
| **接口编号** | `IS101`, `IS124`, `IS118`, `IS105`, `IS120`, `IS111`, `IS122`, `IS117`, `IS109`, `IS113`, `IS104`, `IS419` 等 IS\d+ 模式 |
| **系统/平台** | `STEP`, `BINARY`, `EzOES`, `EzSTEP`, `EzDA`, `EzTrans`, `EzSR`, `TDGW`, `MDGW`, `EzNTP`, `UniTrans`, `ITCS` |
| **业务领域** | `债券`, `股权`, `期权`, `基金`, `融资融券`, `固收`, `IOPV`, `REITs`, `ETF`, `ETF申购赎回`, `ETF定义文件`, `港股通`, `转融通`, `优先股`, `可转债` |

---

### 5.5 信息密度（15 分）

评估条目内容的质量：是否包含冗余套话、标题和摘要是否过度重复、正文的结构化内容占比。

#### 评分规则

| 子项 | 满分 | 评估逻辑 |
|------|------|----------|
| **无公告模板套话** | 5 | 正文不含公文模板套话 |
| **title/summary 不冗余** | 5 | title 和 summary 不高度重复 |
| **正文有效内容占比** | 5 | 表格/代码/列表等有效内容行数占比 |

#### 公告模板套话黑名单

证券交易所技术文档中常见的低信息密度模式：

```
特此通知
请遵照执行
请各.*(?:单位|会员|参与人).*遵照执行
有关事项通知如下
具体事项通知如下:
为进一步.*(?:加强|规范|完善)
根据.*(?:相关|有关).*规定
附件[:：]
特此通告
```

> **扣分规则**：每命中 1 个模式扣 **2 分**，上限扣至 **0 分**。

#### title/summary 冗余检测

检测标题和摘要是否高度重复（如 title="关于发布 IS101 接口规范的通知"，summary="关于发布 IS101 接口规范的通知的详细内容"）：

| 条件 | 得分 |
|------|------|
| title 与 summary 文本重复度 < 50% | **5** |
| title 与 summary 文本重复度 >= 50% | **0** |
| summary 为空 | **0** |

> 实现方式：扫描 title 中连续 5 字以上的片段是否出现在 summary 中。

#### 正文有效内容占比

扫描 `content_markdown`，计算**结构化内容行数**（表格行 `|`、代码块行 ` ``` `、列表项 `-`/`*`/`1.`）占总行数的比例：

| 占比 | 得分 | 文档特征 |
|------|------|----------|
| >= 30% | **5** | 高密度技术文档，含大量接口表、代码样例 |
| >= 15% | **3** | 中等密度，含部分结构化内容 |
| >= 5% | **1** | 少量结构化内容 |
| < 5% | **0** | 纯文本段落，无结构化描述 |

---

## 六、输出格式

### 6.1 默认模式（维度进度条）

每条条目输出一个带进度条的评分块：

```
文件：sse-iface-20250328-140.json#1
────────────────────────────────────────
  [■] 摘要变更精度   [████████████──────] 18/25
  [■] 变更完整性     [████████████████──] 23/25
  [■] 元数据规范     [█████████████████─] 19/20
  [■] 可检索性       [██████████████████] 15/15
  [■] 信息密度       [████████████──────] 10/15
────────────────────────────────────────
  总分：85，等级：A
```

- 分隔线为暗灰色 `\033[90m`
- "文件：" 为青色 `\033[96m`
- 进度条填充 `█`（实心）与 `─`（空心），包裹在 `[...]` 内
- 维度名按视觉宽度对齐（CJK 字符算 2 列）
- 状态指示 `[■]` 颜色对应：绿色 `>=80%`、黄色 `>=60%`、红色 `<60%`
- 多条目之间以双分隔线间隔

### 6.2 紧凑模式（`--compact`）

```
[B] sse-guide-00000000-007.json#1  73/100  摘要变更精度=15/25 | 变更完整性=20/25 | 元数据规范=16/20 | 可检索性=12/15 | 信息密度=10/15
```

### 6.3 汇总

```
────────────────────────────────────────
  质量评估汇总  171 个条目
────────────────────────────────────────
  A (>= 80): 43 条  高质量
  B (>= 60): 125 条  合格
  C (>= 0): 3 条  需改进
────────────────────────────────────────
```

---

## 七、选项

```
usage: check_quality.py [-h] [-v] [--compact] [--no-color] [file ...]

positional arguments:
  file              JSON 文件路径（支持 glob 通配符）

options:
  -h, --help        显示帮助
  -v, --verbose     输出调试日志
  --compact         使用单行摘要输出（不显示维度进度条）
  --no-color        禁用 ANSI 颜色输出
```

---

## 八、文件结构

```
hooks/
  check_quality.py       # 主脚本（单文件，~930 行）
```

内部模块划分：

```
check_quality.py
├── 常量区        — 模板套话黑名单、标签分类、正则模式、满分配置
├── 颜色支持      — ANSI 颜色初始化（colorama/Win32 API 两路降级）、颜色函数
├── 视觉对齐      — _display_width / _visual_ljust（CJK 宽度计算）
├── 数据结构      — DimensionScore / QualityReport dataclass
├── 评分函数核心  — 5 个维度各一个独立评分函数（score_*）
├── 报告生成      — build_report() 将 5 个维度评分聚合为 QualityReport
├── 文件读取      — read_entries() → list[dict]（支持 3 种顶层结构）
└── CLI           — 参数解析、文件解析展开、循环评分、退出码
```

---

## 九、编码约束

遵循项目 AGENTS.md 规范：

- **Google 风格 docstring** — 所有公开函数必须有 Args/Returns 说明
- **`logging` 替代 `print`** — 调试信息使用 logging，评分结果使用 print
- **自定义 dataclass 严格类型** — DimensionScore / QualityReport 使用 @dataclass
- **文件编码 UTF-8** — 统一 `utf-8-sig` 读取，`utf-8` 写入
- **禁止硬编码路径/URL** — 路径通过 CLI 参数传入
- **单文件 ≤ 500 行** — 当前约 860 行，保持单文件便于部署，行数超出为可接受偏差
- **无第三方库依赖** — 标准库仅依赖；colorama 为可选（安装后启用颜色，不装不影响功能）

---

## 十、实现依赖

### 强制依赖（标准库，Python 3.12+）

| 模块 | 用途 |
|------|------|
| `json` | 解析 JSON 条目文件 |
| `re` | 正则校验（ID/日期/模板套话/技术关键词/CJK 宽度） |
| `sys` | stdout 编码重配、退出码 |
| `argparse` | CLI 参数解析 |
| `logging` | 调试日志输出 |
| `pathlib` | 跨平台路径处理 |
| `dataclasses` | 数据结构 DimensionScore / QualityReport |

### 可选依赖（增强颜色显示）

| 模块 | 用途 | 安装方式 |
|------|------|----------|
| `colorama` | Windows ANSI 颜色翻译（终端不支持时自动降级） | `pip install colorama` |

> 不安装 `colorama` 不影响评分功能，仅颜色输出在 Windows 终端不可见。
