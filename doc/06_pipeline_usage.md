# pipeline/pipeline.py 使用说明

## 一、快速上手

### 全量跑 SSE 分析链路（已有数据，跳过爬取）

```bash
python pipeline/pipeline.py --sources sse --from parse --to save
```

预期：Parse 171 篇已有文件 → Analyze 变更检测 → Organize 生成条目 → Save 质量门禁

### 全量跑 SZSE 分析链路（329 文件已下载，从未分析过）

```bash
python pipeline/pipeline.py --sources szse --from parse --to save
```

### 场景六则

```bash
# 仅爬取下载（每栏目 10 条元数据，只下载 5 个文件）
python pipeline/pipeline.py --step collect --limit 10 --download-limit 5

# SZSE 已下载数据，直接走分析链路（Parse → Analyze → Organize → Save）
python pipeline/pipeline.py --sources szse --from parse --to save

# SSE 已有分析结果，只对新增/变更文件增量更新
python pipeline/pipeline.py --sources sse --from parse --incremental

# 混合：SSE 增量 + SZSE 全量
python pipeline/pipeline.py --sources sse,szse --from parse

# 只做 SZSE 的 Analyze → Organize（Parse 已完成时）
python pipeline/pipeline.py --sources szse --from analyze --to organize
```

### 一次跑所有数据源

```bash
python pipeline/pipeline.py
```

---

## 二、命令参考

### 2.1 基本语法

```bash
python pipeline/pipeline.py [选项]
```

### 2.2 运行控制

| 选项 | 说明 | 默认值 | 示例 |
|------|------|--------|------|
| `--sources` | 数据源列表（逗号分隔） | `sse,szse,chinaclear` | `--sources sse,szse` |
| `--from` | 起始步骤 | `collect` | `--from parse` |
| `--to` | 终止步骤 | `save` | `--to organize` |
| `--step` | 只跑单步 | — | `--step analyze` |
| `--limit` | 每步最多处理文件数（Collect 时=每栏目元数据上限） | 无限制 | `--limit 10` |
| `--download-limit` | Collect 时最多下载文件数 | 无限制 | `--download-limit 20` |

#### --from/--to 的常见组合

| 场景 | 命令 |
|------|------|
| 全量端到端 | 不指定 `--from/--to` |
| 数据已下载，只做分析 | `--from parse` |
| 只爬取 | `--from collect --to collect` 或 `--step collect` |
| Parse 已完成，只做 Analyze | `--from analyze` |
| 只做整理（已有分析结果） | `--from organize --to organize` 或 `--step organize` |
| 只做质量门禁 | `--step save` |

### 2.3 增量模式

| 选项 | 说明 | 默认值 |
|------|------|--------|
| `--incremental` | 按文件 hash + mtime 跳过未变更文件 | 否（全量） |
| `--reset` | 删除增量状态，强制全量 | 否 |

增量状态存储在 `knowledge/.pipeline_state.json`，按文件逐步骤记录完成状态。

文件变更判断：

| 条件 | 动作 |
|------|------|
| 文件 hash/mtime 未变，步骤已完成 | 跳过 |
| 文件 hash/mtime 未变，但步骤未完成 | 从该步骤续跑 |
| 文件 hash/mtime 已变 | 从 Parse 重新处理 |
| 新增文件（state 中不存在） | 全量处理 |

### 2.4 LLM 增强

| 选项 | 说明 | 默认值 |
|------|------|--------|
| `--use-llm` | Analyze 步骤启用 LLM 语义增强 | 否（纯规则） |
| `--llm-provider` | 模型提供商 | `deepseek` |
| `--llm-threshold` | 置信度阈值，低于此值触发 LLM | `0.7` |

#### 三种 LLM 策略

| 策略 | 命令 | 适用场景 | 耗时（SSE 171篇） |
|------|------|---------|-----------------|
| 无 LLM（纯规则） | 不加 `--use-llm` | 常规运行 | ~1 min |
| 低置信度触发 | `--use-llm` | 日常增量，覆盖规则盲区 | ~15 min |
| 全量 LLM | `--use-llm --llm-threshold 1.0` | 首次全量重建，追求最高质量 | ~30 min |

### 2.5 质量与调试

| 选项 | 说明 | 默认值 |
|------|------|--------|
| `--skip-quality` | 跳过 Save 步骤的质量门禁 | 否 |
| `--fail-fast` | 遇错立即停止（默认跳过继续） | 否 |
| `--dry-run` | 试运行，不写任何文件 | 否 |
| `--verbose` | 详细日志输出 | 否 |

---

## 三、按数据源的状态参考

| 数据源 | 爬取状态 | 分析状态 | 推荐命令 |
|--------|---------|---------|----------|
| **SSE** | 545 文件已下载 | 171 篇已有分析结果，可增量更新 | `--sources sse --from parse --incremental` |
| **SZSE** | 329 文件已下载 | 尚未分析 | `--sources szse --from parse` |
| **CSDC** | 仅元数据，无文件 | — | `--sources chinaclear --from collect`（恢复后执行） |

### 3.1 SSE — 增量更新已有结果

```bash
# 检查是否有新文件需要分析
python pipeline/pipeline.py --sources sse --from parse --incremental

# 全量重建（覆盖已有 entries）
python pipeline/pipeline.py --sources sse --from parse
```

### 3.2 SZSE — 从已有原始文件跑全链路

```bash
# Step 1. Parse（将 329 个 raw 文件转为 Markdown + 元数据）
python pipeline/pipeline.py --sources szse --step parse

# Step 2. Analyze（变更检测）
python pipeline/pipeline.py --sources szse --step analyze

# Step 3. Organize + Save（生成条目 + 质量门禁）
python pipeline/pipeline.py --sources szse --from organize --to save

# 或者直接跑到底
python pipeline/pipeline.py --sources szse --from parse --to save
```

### 3.3 CSDC — 先下载再分析

```bash
# Step 1. 爬取（需网站正常，目前劳动节维护中）
python pipeline/pipeline.py --sources chinaclear --step collect

# Step 2-5. 分析链路
python pipeline/pipeline.py --sources chinaclear --from parse --to save
```

---

## 四、执行报告解读

流水线结束后输出汇总报告：

```
╔══════════════════════════════════════════════════╗
║         知识库自动化流水线 — 执行报告              ║
╠══════════════════════════════════════════════════╣
║ 状态: 部分成功                                   ║
║ 总耗时: 187.3s                                   ║
╠══════════════════════════════════════════════════╣
║ Step 1: Collect    ✅  3/3 源            45.2s   ║
║ Step 2: Parse      ✅  171/171           62.1s   ║
║ Step 3: Analyze    ⚠️  169/171           58.4s   ║
║   ├─ 规则通道: 159/159  ✅                        ║
║   ├─ LLM 增强:  12   触发 (置信度<0.7)           ║
║   └─ 合并后:  新增 23 条变更, 78 篇摘要已语义化   ║
║ Step 4: Organize   ✅  169/169           12.3s    ║
║ Step 5: Save       ✅  通过率 98.2%      9.3s     ║
║   ├─ 校验通过: 166                               ║
║   ├─ needs_review: 3                             ║
║   └─ 版本追溯: 8 条链路已建立                     ║
╚══════════════════════════════════════════════════╝
```

状态图标含义：

| 图标 | 含义 |
|------|------|
| ✅ | 全部成功 |
| ⚠️ | 部分成功（有文件失败但继续执行） |
| ❌ | 全部失败 |
| ⏭️ | 跳过 |

---

## 五、日志

所有日志写入 `log/pipeline.log`（追加模式），单步失败详情见对应步骤的独立日志：

| 日志文件 | 内容 |
|----------|------|
| `log/pipeline.log` | Pipeline 编排日志 + 最终报告 |
| `log/parse_all.log` | Parse 步骤详细日志 |
| `log/analyze_all.log` | Analyze 步骤详细日志 |
| `log/organize_all.log` | Organize 步骤详细日志 |

---

## 六、常见问题

### Q: 跑了一半中断了，能续跑吗？

可以。使用 `--from` 指定中断处的步骤即可：

```bash
# 假设 Analyze 跑完 100 篇时中断，续跑
python pipeline/pipeline.py --sources szse --from analyze
```

加上 `--incremental` 还会跳过已完成的文件。

### Q: 如何确认当前各步骤的数据量？

```bash
# 查看 raw 文件数
ls knowledge/raw/szse/**/*.* | wc -l

# 查看 markdown 产出
ls knowledge/articles/szse/markdown/**/*.md | wc -l

# 查看分析产出
ls knowledge/articles/szse/analyzed/**/*.json | wc -l

# 查看最终条目
ls knowledge/articles/szse/entries/*.json | wc -l
```

### Q: CSDC 提示"无文件"怎么办？

CSDC 只有元数据没有实际文件。需要等网站恢复后先执行爬取：

```bash
python pipeline/pipeline.py --sources chinaclear --step collect
```

### Q: LLM 增强太慢怎么办？

- 不加 `--use-llm` 即可回退到纯规则模式（~1 min）
- 或降低 `--llm-threshold` 减少触发量
- 或使用 `--limit 10` 小批量测试

### Q: 试运行能看到结果吗？

```bash
python pipeline/pipeline.py --sources szse --from parse --to save --dry-run
```

`--dry-run` 模式会扫描文件、执行分析逻辑，但不写入任何输出文件，日志会显示"<试运行> 准备写入: xxx"。

### Q: 如何强制全量重建？

```bash
# 方式一：重置增量状态
python pipeline/pipeline.py --reset

# 方式二：不指定 --incremental（默认就是全量）
python pipeline/pipeline.py
```

---

## 七、典型的日常使用流程

### 每周增量更新

```bash
# SSE 增量检查 + LLM 增强
python pipeline/pipeline.py --sources sse --from parse --incremental --use-llm

# SZSE 增量检查 + LLM 增强
python pipeline/pipeline.py --sources szse --from parse --incremental --use-llm

# CSDC（如果网站可用）
python pipeline/pipeline.py --sources chinaclear --from collect --to save
```

### 一次过全量重建

```bash
python pipeline/pipeline.py --reset --from parse --use-llm
```
