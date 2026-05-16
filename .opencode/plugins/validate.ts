/**
 * OpenCode Plugin — 写入 knowledge/articles/*.json 时自动触发校验
 *
 * 监听 tool.execute.after 事件，拦截 write / edit 工具，
 * 对 knowledge/articles/ 目录下的 JSON 文件运行 validate_json.py。
 *
 * 基于 OpenCode Plugin API：
 * - 事件: tool.execute.after
 * - Bun Shell: $ 模板字符串（.nothrow() 避免非零退出码抛异常）
 * - 所有 shell 调用被 try/catch 包裹，防止未捕获异常阻塞 Agent
 */

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

        const normalized = filePath.replace(/\\/g, "/")
        if (
          !normalized.includes("knowledge/articles/") ||
          !normalized.endsWith(".json")
        ) {
          return
        }

        // 1) JSON 格式校验
        const result =
          await $`python3 hooks/validate_json.py ${filePath}`.nothrow()

        if (result.exitCode === 0) {
          output.title = `[validate] ✅ ${normalized}`
          output.metadata = { file: normalized, status: "passed" }
        } else {
          const stderr = result.stderr?.toString() ?? ""
          const stdout = result.stdout?.toString() ?? ""
          output.title = `[validate] ❌ ${normalized}`
          output.output = (
            (stdout + "\n" + stderr).trim() ||
            `validate_json.py exited with code ${result.exitCode}`
          )
          output.metadata = { file: normalized, status: "failed", exitCode: result.exitCode }
        }

        // 2) 可选：质量评分
        const quality =
          await $`python3 hooks/check_quality.py ${filePath}`.nothrow()
        if (quality.exitCode !== 0) {
          const msg = (quality.stderr ?? quality.stdout ?? "").toString().trim()
          if (msg) {
            output.output += `\n\n[quality] ⚠️ ${msg}`
          }
        }
      } catch {
        // swallow all errors — uncaught exceptions would block the Agent
      }
    },
  }
}

export default plugin
