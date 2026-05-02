
### Step 1 初始化插件环境

```bash
cd ~/opencode_dev
mkdir -p .opencode/plugins
cd .opencode
# npm init -y
npm install @opencode-ai/plugin
```

![1](./pictures/07_2.png)

### Step 2 向 AI 编程助手提需求，让 AI 编写插件

```
请帮我编写一个 OpenCode TypeScript 插件 .opencode/plugins/validate.ts：

需求：
1. 监听 tool.execute.after 事件
2. 当 Agent 使用 write 或 edit 工具写入 knowledge/articles/*.json 时触发
3. 触发时先调用 python3 hooks/validate_json.py <file_path> 做格式校验
4. 校验通过后调用 python3 hooks/check_quality.py <file_path> 做质量评分
5. 使用 Bun Shell API（$ 模板字符串）执行命令
5. 必须使用 .nothrow() 而非 .quiet()（.quiet() 会导致 OpenCode 卡死）
6. 必须用 try/catch 包裹所有 shell 调用（未捕获异常会阻塞 Agent）

关键 API：
- import type { Plugin } from "@opencode-ai/plugin"
- 插件入参解构 { $ } 得到 Bun Shell
- input.tool 是工具名（如 "write"、"edit"），建议用 .toLowerCase()
- input.args.file_path 或 input.args.filePath 取文件路径
- output 参数可设置 title / output / metadata 展示到 UI
- 结合 .nothrow() 后检查 result.exitCode 区分成功/失败
- check_quality.py 作为格式校验通过后的补充评分步骤
```

### Step 3 实际产出 — validate.ts 关键模式

```typescript
import type { Plugin } from "@opencode-ai/plugin"

const VALID_TOOLS = new Set(["write", "edit"])

const plugin: Plugin = async ({ $ }) => {
  return {
    "tool.execute.after": async (input, output) => {
      try {
        const tool = input.tool?.toLowerCase() ?? ""
        if (!VALID_TOOLS.has(tool)) return

        const filePath: string | undefined =
          input.args?.file_path ?? input.args?.filePath
        if (!filePath) return

        // normalize Windows backslashes
        const normalized = filePath.replace(/\\/g, "/")
        if (!normalized.includes("knowledge/articles/") || !normalized.endsWith(".json")) return

        // use .nothrow() to prevent non-zero exit from throwing
        const result = await $`python3 hooks/validate_json.py ${filePath}`.nothrow()

        if (result.exitCode === 0) {
          output.title = `[validate] ✅ ${normalized}`
          output.output = ""
          output.metadata = { file: normalized, status: "passed" }
        } else {
          output.title = `[validate] ❌ ${normalized}`
          output.output = (result.stdout + "\n" + result.stderr).trim()
          output.metadata = { file: normalized, status: "failed", exitCode: result.exitCode }
          return  // 格式未通过，不继续质量评分
        }

        // quality check (only if format passed)
        const quality = await $`python3 hooks/check_quality.py ${filePath}`.nothrow()
        if (quality.exitCode !== 0) {
          const msg = (quality.stderr ?? quality.stdout ?? "").toString().trim()
          if (msg) {
            output.output = output.output
              ? output.output + `\n\n[quality] ⚠️ ${msg}`
              : `[quality] ⚠️ ${msg}`
          }
        }
      } catch {
        // swallow — unhandled exceptions would block Agent
      }
    },
  }
}

export default plugin
```

### Step 4 临时关闭 hooks 的三种方案

**方案 A：重命名插件文件（最直接，需重启 OpenCode）**

```powershell
# 关闭
Rename-Item .opencode/plugins/validate.ts validate.ts.bak

# 恢复
Rename-Item .opencode/plugins/validate.ts.bak validate.ts
```

**方案 B：环境变量守卫（无需改文件名，新建会话生效）**

在 `validate.ts` 开头加入：

```typescript
const plugin: Plugin = async ({ $, directory }) => {
  // 环境变量 OPENCODE_NO_VALIDATE=1 时跳过所有校验
  if (process.env.OPENCODE_NO_VALIDATE) return {}
  // ... 原有逻辑
}
```

```powershell
# 关闭（新会话生效）
$env:OPENCODE_NO_VALIDATE = 1

# 恢复
Remove-Item Env:OPENCODE_NO_VALIDATE
```

**方案 C：文件标记守卫（当前会话立即生效）**

在 `validate.ts` 开头加入：

```typescript
import { existsSync } from "fs"
import { join } from "path"

const plugin: Plugin = async ({ $, directory }) => {
  const guardFile = join(directory, ".nohooks")
  if (existsSync(guardFile)) return {}
  // ... 原有逻辑
}
```

```powershell
# 关闭
New-Item .nohooks -ItemType File

# 恢复
Remove-Item .nohooks
```

注意：方案 B/C 需要先改造插件代码再加入守卫逻辑。
