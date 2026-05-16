# Hooks 事件驱动 — 学习笔记

---

## 一、OpenCode Plugin Hook 体系总览

OpenCode 提供 **5 种核心 Hook 类型**，贯穿 Agent 执行全生命周期：

| Hook 类型 | 触发时机 | 典型用途 | 返回值控制 |
|-----------|----------|----------|-----------|
| `tool.execute.before` | 工具执行前 | 权限拦截、参数检查 | 可阻止执行 |
| `tool.execute.after` | 工具执行后 | 格式校验、日志记录 | 可触发修正 |
| `Notification` | Agent 发送通知时 | 消息推送、状态记录 | 仅观察 |
| `UserPromptSubmit` | 用户提交 prompt 时 | 输入预处理、安全审查、最终质量门、完整性检查 | 可修改输入 |
| `Stop` | Agent 停止前 | — | 可阻止停止 |

---

## 二、真实 API 与 Plugin 签名

- **插件位置**：`.opencode/plugins/*.ts`（TypeScript 文件，自动加载）
- **包名**：`@opencode-ai/plugin`（注意不是 `@opencode/plugin`）

### 核心 Hook 事件（实际支持的）

- `tool.execute.before` — 工具执行前触发（可拦截）
- `tool.execute.after` — 工具执行后触发（可校验产出）
- `chat.message` — 收到消息时触发
- `command.execute.before` — 命令执行前触发
- `shell.env` — 注入环境变量

### Plugin 签名（真实 API）

```typescript
export const MyHook: Plugin = async ({ $ }) => {
  return {
    "tool.execute.after": async (input) => { ... }
  }
}
```

> 注意：不是 `definePlugin()`，是直接导出 `Plugin` 类型的函数。

---

## 三、对比：OpenCode Hook vs Claude Code Hook

| 维度 | OpenCode Plugin Hook | Claude Code Hook |
|------|---------------------|------------------|
| 配置方式 | TypeScript 代码 | JSON 声明式 |
| 文件位置 | `.opencode/plugins/*.ts` | `.claude/settings.json` |
| 语言 | TypeScript + Bun Shell | Shell 脚本 |
| 事件名 | `tool.execute.before/after` | `PreToolUse / PostToolUse` |
| 加载 | 启动时自动发现 | 读取 JSON 配置 |
| 优势 | 代码灵活，可调用任意程序 | 声明式，不需要写代码 |
| 劣势 | 需要 TypeScript 基础 | 只能跑 Shell 脚本 |

---

## 四、反馈驱动循环 — 完整运行图

```
                   ┌─────────────┐
                   │   Gather    │
                   │  (采集信息)  │
                   └──────┬──────┘
                          │
                          ▼
                   ┌─────────────┐
                   │    Act      │
                   │  (执行操作)  │
                   │ (Hook 触发)  │
                   └──────┬──────┘
                          │
                          ▼
                   ┌─────────────┐
              ┌───│   Verify    │
              │   │  (校验结果)  │
              │   └──────┬──────┘
              │          │
              │     ┌────┴────┐
              │     │         │
              │   通过      不通过
              │     │         │
              │     ▼         ▼
              │  入库完成  ┌─────────┐
              │           │ 反馈给   │
              │           │ Agent    │
              │           └────┬────┘
              │                │
              └── 再次校验 ← 自动修正
```

---

## 五、对比：有 Hook vs 无 Hook

| 维度 | 无 Hook = 开环系统 | 有 Hook = 闭环系统 |
|------|--------------------|--------------------|
| 流程 | Agent 执行 → 直接输出 → 结束 | Agent 执行 → Hook 校验 → 反馈 → 修正 → 再校验 |
| 问题发现 | 靠人工检查（经常忘记） | 自动（Hook 触发） |
| 修正方式 | 手动重新跑 | Agent 自动修正 |
| 质量保证 | 无 | 持续 |

**类比：**

| 场景 | 无 Hook | 有 Hook |
|------|---------|---------|
| 工厂 | 没有质检 → 次品流到客户 | 有质检 → 次品被拦截 |
| 开发 | 写代码没有测试 → bug 上线 | 有 CI/CD → 测试不过不上线 |
| 驾驶 | 没有仪表盘 → 不知道速度 | 有仪表盘 → 超速自动报警 |

**结果：**

| 无 Hook | 有 Hook |
|---------|---------|
| 产出质量不稳定 | 产出质量稳定一致 |
| 好的时候很好，差的时候很差 | 不依赖人的注意力 |
| 取决于人的注意力和记忆力 | 7x24 自动运行，质量有底线 |

---

## 六、关键要点总结

1. Hook 是 Agent 执行流程中的 **事件拦截点**，可在关键节点注入自定义逻辑
2. 5 种 Hook 类型覆盖了 **执行前、执行后、输入、输出、停止** 全生命周期
3. OpenCode Hook **代码灵活但需 TypeScript 基础**；Claude Code **声明式简单但只能跑 Shell**
4. 有 Hook 的系统是 **闭环系统**，能自动发现并修正问题，质量有保障
5. 反馈驱动循环（Gather → Act → Verify）是 Hook 的核心运行模式
