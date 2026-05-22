请帮我写一个 MCP Server（mcp_knowledge_server.py），让 AI 工具可以搜索本地知识库：

需求：
1. 读取 knowledge/articles/sse|szse|chinaclear/ 目录下的所有 JSON 文件
2. 提供 3 个 MCP 工具：
   - search_articles(keyword, limit=5): 按关键词搜索文章标题和摘要
   - get_article(article_id): 按 ID 获取文章完整内容
   - knowledge_stats(): 返回统计信息（文章总数、来源分布、热门标签）
3. 使用 JSON-RPC 2.0 over stdio 协议
4. 支持 MCP initialize、tools/list、tools/call 方法
5. 无第三方依赖，只用 Python 标准库

先给出方案和方案评估，不要直接进入编码

[](../doc/mcp_knowledge_server_plan.md)