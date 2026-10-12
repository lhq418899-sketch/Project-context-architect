# 插件市场接入（Plugin Distribution）

本 skill 已按 Claude Code 插件规范补齐市场接入资产。根目录 `SKILL.md` 即插件主 skill（`skills: ["."]` 指向仓库根）。

## 接入方式

### 1. 官方目录（推荐，面向大众分发）

提交到 [Anthropic 官方插件目录](https://github.com/anthropics/claude-plugins-official) 的 `external_plugins/`：

1. 将仓库公开到 GitHub，许可证选 MIT（本 skill 默认声明 MIT）；
2. 确认 `marketplace.json` 与 `.claude-plugin/plugin.json` 中的账号信息为 `lhq418899-sketch`；
3. 通过官方[插件目录提交表单](https://clau.de/plugin-directory-submission)提交，附仓库 URL；
4. 审核通过后，用户可 `claude plugin install project-context-architect@claude-plugins-official` 安装。

### 2. 自建 marketplace（面向团队内部）

仓库本身就是 marketplace：

```bash
claude plugin marketplace add lhq418899-sketch/Project-context-architect
claude plugin install project-context-architect@project-context-architect-marketplace
```

### 3. 本地安装（面向自己）

```bash
claude plugin install C:\path\to\project-context-architect
```

### 4. Codex 用户接入（面向 OpenAI Codex / ChatGPT）

本 skill 采用跨平台通用 skill 格式（`SKILL.md` + 资源子目录），Codex 与 Claude Code 均原生兼容。`agents/openai.yaml` 即 Codex 侧接口配置（`display_name` / `short_description` / `default_prompt` / `allow_implicit_invocation`）。

方式 A（推荐，官方 skill-installer，从 GitHub 安装到 `$CODEX_HOME/skills`）：

```text
在 Codex 中执行：
/use skill-installer "Install the project-context-architect skill from https://github.com/lhq418899-sketch/Project-context-architect"
```

方式 B（手动复制）：把整个 `project-context-architect/` 目录（含 `SKILL.md` 及 `references/`、`examples/`、`fixtures/`、`scripts/` 子目录）复制到 `~/.codex/skills/`（即 `$CODEX_HOME/skills`），目录名保持不变。

方式 C（界面）：ChatGPT / Codex 的 Plugins 入口中安装（视账号可用性）。

Codex 侧无需 Claude 的 marketplace 命令；两套分发互不干扰。

## 结构映射（Claude 插件规范）

| 本仓库路径 | 插件规范对应 |
|---|---|
| `SKILL.md`（根） | `skills/` 主 skill，经 `skills: ["."]` 声明 |
| `references/` `examples/` `fixtures/` `scripts/` | skill 资源目录，随仓库分发 |
| `agents/openai.yaml` | Codex 侧接口配置，与 Claude 插件互不干扰 |
| `.claude-plugin/plugin.json` | 插件元数据（必需） |

## 发布前 Checklist

- [ ] 仓库已公开，含 LICENSE（MIT）
- [ ] `marketplace.json` / `.claude-plugin/plugin.json` 占位已替换
- [ ] 已运行 `python scripts/lint_skill.py`（结构自检）
- [ ] 已运行 `python scripts/check_fixture.py`（夹具前提完好）
- [ ] README 写明用法（BOOTSTRAP / REFACTOR / CHECK 三模式）
