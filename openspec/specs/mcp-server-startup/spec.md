# mcp-server-startup

## Purpose

定义 MCP 知识库服务的启动行为，确保在数据加载完成前即可接受并响应 MCP 协议消息。

## Requirements

### Requirement: MCP 服务 SHALL 在启动后立即响应 initialize

MCP 知识库服务 SHALL 在数据加载完成前即开始监听 stdin 上的 JSON-RPC 消息，确保 OpenCode MCP 客户端在 30 秒超时窗口内收到 `initialize` 响应。

#### Scenario: 服务在数据加载完成前响应 initialize
- **WHEN** 服务进程启动
- **THEN** 服务 SHALL 立即开始读取 stdin 上的 MCP 消息
- **AND** 服务 SHALL 在数据加载尚未完成时也能响应 `initialize` 请求

### Requirement: 工具调用 SHALL 等待数据加载完成

当 `ArticleStore` 加载未完成时收到工具调用（search、get_article、get_article_content、knowledge_stats），服务 SHALL 等待加载完成后再处理请求。

#### Scenario: 数据加载期间收到工具调用
- **WHEN** 收到工具调用请求
- **AND** 数据加载仍在进行中
- **THEN** handler SHALL 等待（最长 60 秒）加载完成
- **THEN** handler SHALL 正常处理请求
#### Scenario: 数据加载完成后收到工具调用
- **WHEN** 收到工具调用请求
- **AND** 数据加载已完成
- **THEN** handler SHALL 立即处理请求，无需等待

### Requirement: wait_ready SHALL 返回布尔值表示加载状态

`ArticleStore.wait_ready(timeout)` 方法 SHALL 阻塞直到 `_loaded` 为 True 或超时，加载完成返回 True，超时返回 False。

#### Scenario: 加载在超时前完成
- **WHEN** 调用 `wait_ready(60)`
- **AND** 加载在 60 秒内完成
- **THEN** 方法 SHALL 返回 True
#### Scenario: 超时过期加载仍未完成
- **WHEN** 调用 `wait_ready(5)`
- **AND** 加载在 5 秒内未完成
- **THEN** 方法 SHALL 返回 False
