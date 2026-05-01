
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

