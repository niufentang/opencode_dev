## 工具使用约束与能力说明

## 一、Watt Toolkit（Steam++）
### 定位

开源本地反向代理，用于**合规加速 GitHub、PyPI** 等海外开发资源，**非 VPN、非全局代理**。

### 作用

- 解决 git clone、pip 安装、Playwright 下载超时 / 缓慢
- 定向优选 IP，不影响国内网络
- 替代手动修改 Hosts

### 合规要求

仅用于开发加速，禁止任何违规网络行为。



---

## 二、GitHub CLI (gh)
### 认证规范
统一采用环境变量 `GH_TOKEN` 进行无交互身份认证。

### 常用命令参考
# 登录认证
gh auth login --with-token %GH_TOKEN%

# 仓库操作
gh repo clone <repo>
gh repo create
gh repo view

# Issue 管理
gh issue list
gh issue create
gh issue view <id>

# Pull Request 管理
gh pr list
gh pr create
gh pr checkout <num>
gh pr view <num>
gh pr merge

# 其他常用功能
gh search repos <query>
gh run list
gh alias list

# 全局帮助
gh help

### 使用规则
1. 涉及 GitHub 仓库、PR、Issue、Actions 相关操作，优先使用 gh 命令
2. 执行前确保系统环境变量 GH_TOKEN 已正确配置