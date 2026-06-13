# 测试

## 运行机制

```text
python -m pytest <文件路径>
       │           │
       │           └── 文件路径传参 → pytest 直接加载这个文件
       │               无需 conftest.py 或 test discovery
       │
       └── -m 以模块方式启动 pytest（等效于 pytest 命令）
           避免因 PATH 没加进来报 "找不到命令"
```

pytest 拿到文件后的执行流程：

```text
加载 test_xxx.py
  ├─ 扫描 test_ 开头的函数 / Test 开头的类
  │    ├─ TestExample
  │    │   ├─ test_case_1
  │    │   └─ test_case_2
  │    └─ ...
  ├─ 收集到 N 个用例
  └─ 逐个执行（-v 打印每个通过/失败）
```

没有复杂的 discovery 规则，给文件就测文件。

## 运行

```powershell
# 跑所有测试
python -m pytest tests/

# 跑单个测试文件
python -m pytest tests/test_collect_incremental.py -v

# 按测试类/函数名过滤
python -m pytest tests/ -k "PipelineState"
python -m pytest tests/ -k "Szse"
```

## 依赖

```powershell
pip install pytest
```

## 新增测试

- 文件按 `test_*.py` 命名放在 `tests/` 下
- 测试函数以 `test_` 开头，测试类以 `Test` 开头
- 无需注册或配置，pytest 自动发现
