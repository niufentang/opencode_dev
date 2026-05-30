## 1. 索引缓存

- [x] 1.1 实现 `_cache_path(knowledge_dir)` 返回 `knowledge/.cache/.index_cache.json.gz` 路径
- [x] 1.2 实现 `_build_manifest(knowledge_dir)` 扫描 entries/*.json（跳过 entries.json）构建 {filepath → mtime} 映射
- [x] 1.3 `_load_cache` 单次遍历：`_build_manifest` 调用一次，manifest 集合比对 + mtime 上限校验合并
- [x] 1.4 移除独立的 `_cache_is_fresh` 方法，逻辑内联到 `_load_cache`
- [x] 1.5 实现 `_save_cache()` 使用 gzip + JSON 序列化 entries + inverted_index + manifest（synonym_map 不缓存，始终实时构建）
- [x] 1.6 `_save_cache` 原子写入：先写 `.tmp` 再 `os.replace()`，失败时清理残骸
- [x] 1.7 `_load_cache` 读取失败时删除残骸，阻断重试循环
- [x] 1.8 缓存未命中/过期/manifest 变更时返回 False，触发完整重建
- [x] 1.9 添加 `CACHE_VERSION` 常量，缓存 data 包含版本标记，加载时校验
- [x] 1.10 缓存加载后调用 `_auto_discover_synonyms()`，保证同义词映射与当前代码版本一致
- [x] 1.11 在 `load()` 中添加缓存加载逻辑：优先加载缓存，重建后保存缓存

## 2. stdio 协议优化

- [x] 2.1 将 `_make_error` / `_make_result` 的返回值从 str 改为 bytes
- [x] 2.2 新增 `_write_response(data: bytes)` 方法，写入 sys.stdout.buffer 并 flush
- [x] 2.3 主循环从 `sys.stdin` 改为 `sys.stdin.buffer`，读取后 decode("utf-8")
- [x] 2.4 `_handle_message` 的返回值从 str 改为 bytes
- [x] 2.5 所有写 stdout 的位置替换为 `_write_response()`

## 3. 搜索调试信息

- [x] 3.1 搜索无结果时先检查 `logger.isEnabledFor(logging.DEBUG)`，避免不必要的 jieba.lcut
- [x] 3.2 构造 debug_info 字符串（keyword → tokens → index_hits → index_size）
- [x] 3.3 DEBUG 级别下无结果时 debug_info 拼接到结果文本前；INFO 级别仅日志一行

## 4. 可观测性提升

- [x] 4.1 `get_stats` 新增倒排索引词条数统计
- [x] 4.2 `main()` 包入 try/except，异常时 logger.exception + sys.exit(1)
- [x] 4.3 信号注册兼容处理：SIGTERM/SIGINT try/except 降级 + Windows SIGBREAK 支持

## 5. 验证

- [x] 5.1 人工验证：启动 Server，首次启动完整构建索引，二次启动加载缓存
- [x] 5.2 人工验证：搜索无结果时返回调试信息
- [x] 5.3 人工验证：knowledge_stats 返回倒排索引词条数
- [x] 5.4 自动验证：已有单元测试全部通过
- [x] 5.5 自动验证：已有集成测试全部通过
