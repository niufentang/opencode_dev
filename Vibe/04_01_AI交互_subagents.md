
## 步骤 1：确认目录结构

  ```plain
  cd ~/ai-knowledge-base
  ls .opencode/agents/
  # 如果目录不存在则创建
  mkdir -p .opencode/agents
  
  ---
  ```

## 步骤 2：用 AI 编程工具生成采集 Agent

**提示词：**
```plain
请帮我创建 .opencode/agents/collector.md 文件，定义一个知识采集 Agent。

要求：
- 角色：AI 知识库助手的采集 Agent，从上交所、深交所、中国结算爬取技术与规则文档(utils已存在python爬取脚本，请参考，并结合脚本逻辑适当丰富collector.md)  
- 允许权限：Read, Grep, Glob, WebFetch（只看只搜不写）
- 禁止权限：Write, Edit, Bash（并说明为什么禁止）
- 工作职责：搜索采集、提取必要内容（如：文档标题、发布时间、版本、文档类型、一级 / 二级栏目、URL、文件格式（PDF/Word/TXT）、更新时间等）
- 输出格式：metadata.json数组，每条含 title, publish_date，url, category, file_format, file_size，local_path，crawl_time 并保存到 knowledge/raw/ 目录下，同时下载文件保存到 knowledge/raw/sse|szse|chinaclear/ 目录下
- 质量自查清单：文档信息完整、不编造

```

## 步骤 3：用 AI 编程工具生成分析 Agent 和整理 Agent

**提示词：**

```plain
参考 .opencode/agents/collector.md 的格式，帮我创建另外三个 Agent 定义文件：

1. .opencode/agents/parser.md — 解析 Agent
   - 权限同 collector（Read/Grep/Glob/WebFetch，禁止 Write/Edit/Bash）
   - 职责：读取 knowledge/raw/sse|szse|chinaclear/ 的数据，异构文件解析, PDF/Word/ZIP 解析、HTML 结构化提取、全文转 Markdown、元数据抽取，并保存到 knowledge/parser/sse|szse|chinaclear/ 目录下,注意标注出原文技术和规则变更，统一用红颜色标注4

2. .opencode/agents/analyzer.md — 分析 Agent
   - 权限同 collector（Read/Grep/Glob/WebFetch，禁止 Write/Edit/Bash）
   - 职责：读取 knowledge/articles/sse|szse|chinaclear/ 的数据，进行语义分析，做变更分析与关联发现 ，技术变更和规则变更分析、版本差异比对、废止/替代检测、跨站关联发现、标签自动分类 等，并保存到 knowledge/analyzed/sse|szse|chinaclear/ 目录下

3. .opencode/agents/organizer.md — 整理 Agent
   - 权限：允许 Read/Grep/Glob/Write/Edit，禁止 WebFetch/Bash
   - 职责：知识条目结构化, 分析后原始数据去重、过滤、格式化，输出为标准知识条目 JSON，并保存到 knowledge/entries/sse|szse|chinaclear/ 目录下

注意：
1 生成parser.md|analyzer.md|organizer.md  结合主AGENTS.md规划
2 parser.md和analyzer.md对于职能划分， 是否可以直接合并成一个analyzer.md，并给出说明合并和不合并的有缺陷，说重点明合并和拆分的理由

```

