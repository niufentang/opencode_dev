## 1. State 扩展

- [ ] 1.1 向 `KBState` 添加 `sources: list[str]`
- [ ] 1.2 向 `KBState` 添加 `last_crawl_dates: dict[str, str]`
- [ ] 1.3 向 `KBState` 添加 `source_status: dict[str, SourceStatus]`
- [ ] 1.4 向 `KBState` 添加 `workflow_config: dict`（承载 `--use-llm`、`--llm-provider`、`--llm-threshold`、`--skip-quality`、`--dry-run`、`--human-review` 等）
- [ ] 1.5 定义 `SourceStatus` TypedDict，包含 `articles_passed: bool`、`analyze_attempts: int`、`organize_attempts: int`
- [ ] 1.6 定义 `WorkflowConfig` TypedDict，映射所有 CLI 参数到配置字段

## 2. 节点函数

- [ ] 2.1 实现 `collect_source(source)` —— 从 `utils/*_doc_api` 导入爬虫，用 `state.last_crawl_dates` 中的 `since_date` 调用 `fetch_all_categories()`，写入 metadata JSON，更新 `last_crawl_dates[source]`
- [ ] 2.2 实现 `parse_source(source)` —— 导入 `parse_all`，收集原始文件，调用 `parse_file()` 和 `save_output()`，若文件的 Markdown 输出已存在且 SHA256 匹配则跳过
- [ ] 2.3 实现 `analyze_all(state)` —— 导入 `analyze_all.analyze_document()` 走规则通道，通过 `llm_utils.chat_json()` 做 LLM 增强，合并结果，写入 `_analysis.json`，更新 `state.analyses` 和 `state.cost_tracker`；读到 `force_reanalyze` 信号时强制重跑对应源，跑完后清除信号
- [ ] 2.4 实现 `organize_all(state)` —— 导入 `organize_all.process_analysis_file()` 和 `build_index()`，写入条目 JSON，更新 `state.articles`；读到 `force_reorganize` 信号时强制重跑对应源，跑完后清除信号
- [ ] 2.5 实现 `review_router(state)` —— 遍历 `state.source_status` 中的每个源，检查空标题/id 和最小条目数，设置每个源的 `articles_passed`，递增 `analyze_attempts`/`organize_attempts`，设 `force_reanalyze`/`force_reorganize` 信号，更新 `review_feedback` 和 `iteration`
- [ ] 2.6 实现 `save_all(state)` —— 导入 `validate_json.validate_entry()` 和 `organize_all.perform_version_traceability()`，调用 `_trigger_notifications()`（占位），写入 `state.save_report`
- [ ] 2.7 实现 `human_review(state)` —— 将待审数据写入 `knowledge/pending_review/pending-{timestamp}.json`；若配置为 `"interrupt"` 则抛出 `Command` 中断；若为 `"log"` 则设置 `needs_human_review=True` 并结束

## 3. LLM 工具函数

- [ ] 3.1 创建 `workflows/llm_utils.py`，实现 `chat_json(prompt, system, **kwargs) -> (dict|list, usage_dict)` —— 调用 `pipeline.model_client.chat_with_retry()`，自带 3 层 JSON 容错（去 markdown 包裹、直接解析、正则提取最外层 JSON 结构）
- [ ] 3.2 实现 `accumulate_usage(tracker, new_usage) -> dict` —— 累加 token 数、按 DeepSeek 定价估算费用，返回更新后的 cost_tracker

## 4. 路由函数

- [ ] 4.1 实现 `fan_out_sources(state)` —— 返回 `[Send(src, state) for src in active_sources]`，活跃源是尚未通过审查的源（首次运行时为所有源）
- [ ] 4.2 实现 `review_routing(state)` —— 返回字符串字面量表示路由决策：所有源通过返回 `"save"`，有源失败且尝试次数 < 3 返回 `"re_dispatch"`，有源耗尽尝试次数 >= 3 返回 `"human_review"`

## 5. 图构建

- [ ] 5.1 实现 `build_source_subgraph(source: str) -> StateGraph` —— 创建双节点子图：`collect_source` → `parse_source`，作用域限定的源键
- [ ] 5.2 实现 `build_main_graph() -> CompiledGraph` —— 组装完整图：入口 → `fan_out_sources` → `Send()` 到源子图 → 隐式汇合 → `analyze_all` → `organize_all` → `review_router`；条件边：`save` → `save_all` → END，`re_dispatch` → 回到 `fan_out_sources`，`human_review` → `human_review` → END
- [ ] 5.3 接入 checkpointer —— 默认使用 `MemorySaver`，提供 `--checkpoint-path` 时切换为 `SqliteSaver(path)`
- [ ] 5.4 从 `workflows/__init__.py` 导出 `build_main_graph()`

## 6. CLI 入口

- [ ] 6.1 创建 `workflows/__main__.py`，包含 `argparse`，支持参数：`--sources`、`--limit`、`--download-limit`、`--per-category-limit`、`--use-llm`、`--llm-provider`、`--llm-threshold`、`--skip-quality`、`--dry-run`、`--files`、`--verbose`、`--checkpoint-path`、`--human-review`
- [ ] 6.2 实现 `build_config_from_args(args) -> dict` —— 将 CLI 参数映射到 `WorkflowConfig` 字典和初始 `KBState` 字段
- [ ] 6.3 实现 `main()` —— 构建图、构建配置、调用 `graph.invoke(initial_state, config)`、打印执行报告
- [ ] 6.4 编写用法 docstring 和帮助文本，与现有 pipeline 风格一致

## 7. 验证

- [ ] 7.1 运行 `python -m workflows`，带 `--sources sse --dry-run` —— 验证图编译成功且 dry-run 正确执行
- [ ] 7.2 对单个源用小限制运行（`--limit 3`），验证输出与相同数据的 `pipeline/pipeline.py` 一致
- [ ] 7.3 测试审查循环：注入一个产出空条目的源，验证它被重新路由（而非保存）
- [ ] 7.4 测试 checkpointer：运行两次，验证第二次运行使用 checkpoint 中的 `since_date`
- [ ] 7.5 测试 `"log"` 模式下的 human_review：耗尽重试次数，验证最终 state 中 `needs_human_review=True`
