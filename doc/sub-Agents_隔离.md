
**核心特点：隔离**
**上下文隔离**：每个 ~10K Token，信息不会相互干扰
**角色清晰 + 权限安全**: 最小权限原则，越界被阻止
**易于调试**：出问题一查就知道


### 为什么需要角色分工？

- **问题 1：上下文爆炸** — 一个 Agent 干所有事，Token 飙到 50K+，信息丢失
    - 采集 30 条数据 + 逐条分析 + 去重入库 → 后面的指令被遗忘
- **问题 2：角色混乱** — AI 分不清现在该采集还是分析
    - 采集时顺手改了文件，分析时编造了数据
- **问题 3：权限泄漏** — 没有边界，AI 什么都能做
    - 本该只读的操作执行了写入，甚至跑了 rm -rf
- **问题 4：调试困难** — 出了问题不知道是哪个环节
    - 结果不对，是采集错了？分析错了？还是整理错了？


**权限
- 读: Read / Glob / Grep
- 写: Write / Edit
- 执行: Bash (图灵完备的)
- 联网: WebFetch / WebSearch
- 编排: Agent / TodoWrite / Skill

**权限控制
- allow自动执行，无需审批
- ask 暂停，等用户审批后继续
- deny 完全禁止，直接拒绝

**精细粒度控制(以Bash为例)
- allow: ['npm test,'npm run lint"]
- deny: ['rm -rf,'curl | sh','sudo']
* 其余ask(需要用户确认)
* **原则:默认deny，按需allow


**Harness 五大机制**：
① Agentic Loop — while(tool_call) { execute → feed_back → repeat }
② 工具权限图 — allowed-tools 白名单，系统级硬约束
③ 上下文压缩器 — 92% 窗口占用时自动压缩，CLAUDE.md 重新注入
④ Sub-Agent 隔离边界 — 独立 context window + 结果压缩回传
⑤ 实时转向队列 — 用户可在 Agent 执行中途注入新指令

