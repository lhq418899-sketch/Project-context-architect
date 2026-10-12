# Project Context Architect（项目上下文架构师）

> 维护一个项目**最小的权威上下文**：让任何全新会话无需继承聊天历史、也无需通读整个仓库，就能安全接管项目。
> Build and maintain a project's smallest authoritative context: handoff docs, authority refactor, and fresh-session readiness checks.

<!-- 仓库公开后在此添加徽章：CI 状态、license、stars（如 [![CI](https://github.com/lhq418899-sketch/Project-context-architect/actions/workflows/ci.yml/badge.svg)](...)） -->

## 这是什么

AI 代理在长项目中最常见的问题是**上下文碎片化**：事实散落在聊天记录、过期的设计文档、被推翻的决策和"看起来还活着"的旧笔记里。本项目提出一个治理层——**minimum authority**（最小权威集）：

- 少数几个有明确职责的仓库文件，作为当前真相的唯一拥有者；
- **一事实一主**：每条当前事实只归一个权威文档所有，其余文档只能链接；
- **当前真相与历史分离**：历史归档并标注"非权威"，不参与接管判断；
- **分类感知的冲突验证**：用与类别匹配的证据核对冲突，而不是凭实现猜产品意图；
- **权威完成门**：受影响的权威未更新，任务不算完成。

它管理的是**项目上下文**，不是业务实现。

## 三种模式

| 模式 | 何时用 | 产出 |
|---|---|---|
| **BOOTSTRAP** | 新项目 / 早期项目没有交接体系 | 最小权威集（`AGENTS.md` + `PROJECT_STATE.md`，按需加 `ARCHITECTURE.md` / `DECISIONS.md` / `RUNBOOK.md`） |
| **REFACTOR** | 既有项目上下文散乱、重复、过期、互相矛盾 | 单一权威归属 + 历史归档 + 收敛后的交接文档 |
| **CHECK** | 冲刺/里程碑之后，或交接给全新会话前 | 健康度报告 + `GOOD` / `NEEDS_ATTENTION` |

模式选择规则：能小则小。CHECK 可以建议 REFACTOR，但不会悄悄扩大成它。

## 快速开始

### 本地安装（当前推荐）

把本目录放入你的 agent skill 目录（如 Claude Code / Codex 的 skills 或 plugins 目录），然后在项目里使用：

- 新项目：让 agent 执行 **BOOTSTRAP**
- 混乱的既有项目：**REFACTOR**
- 交接前：**CHECK**

接入分发（官方目录 / 自建 marketplace / 本地插件）见 [PLUGIN.md](PLUGIN.md)。仓库公开后支持 `claude plugin install project-context-architect@...` 一键安装。

### 概念与执行细则

- 权威模型、文件命名与一事实一主：见 [references/authority-model.md](references/authority-model.md)
- 三模式执行细则：见 [references/bootstrap.md](references/bootstrap.md)、[references/refactor.md](references/refactor.md)、[references/check.md](references/check.md)
- 交接就绪测试（7 问）：见 [references/fresh-session-test.md](references/fresh-session-test.md)
- 金标准示例（虚构项目）：见 [examples/bootstrap/](examples/bootstrap/)
- 故意损坏的演练项目：见 [fixtures/messy/](fixtures/messy/)

## 仓库结构

```
project-context-architect/
├── SKILL.md                    # 主 skill（三模式入口 + 共享操作契约）
├── references/                 # 权威模型 / 三模式细则 / 交接测试
├── examples/bootstrap/         # 金标准示例（虚构项目，勿照抄）
├── fixtures/messy/             # 故意损坏的演练项目（回归夹具）
├── scripts/                    # 确定性回归脚本（纯 stdlib）
├── agents/openai.yaml          # Codex 侧接口配置
├── .claude-plugin/plugin.json  # Claude 插件元数据
├── marketplace.json            # 仓库级 marketplace 清单
└── PLUGIN.md                   # 插件分发指南
```

## 回归测试

每次修改 skill 后运行（无需安装任何依赖）：

```bash
python scripts/lint_skill.py        # 结构自检：必需文件、链接、编码、契约措辞
python scripts/check_fixture.py     # 确认演练夹具仍处于"故意损坏"状态
python scripts/verify_refactor.py <dir>  # 对 REFACTOR 结果做结构级验收
```

详见 [scripts/README.md](scripts/README.md)。CI 已接入：每次 push / PR 自动运行前两个脚本（见 [.github/workflows/ci.yml](.github/workflows/ci.yml)）。

## 语言约定

文档采用**中英混合、中文为主**。核心执行文件（`SKILL.md`、`references/`、`examples/`）保持英文，以保证各平台 agent 的触发与执行一致性；面向人的分发与贡献文档以中文为主。欢迎补充其他语言的 README。

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

[MIT](LICENSE) © 2026 lhq418899-sketch
