# Skills 说明

## 当前状态：实验性质

`ls-collector` / `ls-parser` / `ls-analyzer` / `ls-organizer` 四个 skill 为早期实验产物，其领域知识（URL 路径、解析策略、变更分类、版本链逻辑等）与 `.opencode/agents/` 中对应的 agent 文档高度重复（约 70-75%）。

## 冗余分析

| 领域 | Skill 独有内容 | Agent 独有内容 | 重复内容 |
|------|---------------|---------------|---------|
| 采集 | — | 工具权限定义、禁止操作列表 | SSE/SZSE/CSDC 的 URL 路径、分页规则、提取方法、输出格式 |
| 解析 | 格式-依赖库映射表 | 工具权限定义、禁止操作列表 | 各格式解析策略、变更标注规则、输出格式 |
| 分析 | 变更分类表、严重程度定义 | 工具权限定义、禁止操作列表 | doc_id 规则、标签分类、跨站关联逻辑、输出格式 |
| 整理 | 数据过滤规则、版本链逻辑 | 工具权限定义 | 去重逻辑、输出格式、索引格式 |

两份文档维护一份知识，每次修改需同步两处，已多次出现不同步（如 SSE 栏目路径在 skill 中错误但 agent 中也未单独更新）。

## 后续计划

Skill 与对应 agent 将合并为单一文档，以 agent 作为唯一参考源。合并后删除 skill 文件。

## 对照实验说明

`parseranalyzer` 是对照实验用的独立 agent（无对应 skill），其设计目的已在 `agents/parseranalyzer.md` 中描述，不受本次合并影响。

## Agent ↔ Skill 关系总览

```markdown
AGENTS.md (项目 Memory · 共享规范)
        │
        ├── collector（采集 Agent）
        │       └── ls-collector（Skill）
        │
        ├── parser（解析 Agent）
        │       └── ls-parser（Skill）
        │
        ├── analyzer（分析 Agent）
        │       └── ls-analyzer（Skill）
        │
        ├── organizer（整理 Agent）
        │       └── ls-organizer（Skill）
        │
        └── parseranalyzer（解析分析合并 Agent · 对照实验）
                └── 无独立 Skill（复用 ls-parser + ls-analyzer 逻辑）
```
