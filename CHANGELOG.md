# Changelog

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 与语义化版本（[SemVer](https://semver.org/lang/zh-CN/)）。

## [Unreleased]

- 计划提交 [Anthropic 官方插件目录](https://github.com/anthropics/claude-plugins-official)（仓库公开后走提交表单）。

## [0.1.0] - 2026-10-11

### Added

- 三种模式：**BOOTSTRAP**（最小权威集建立）、**REFACTOR**（上下文收敛与历史归档）、**CHECK**（交接就绪检查）。
- 权威模型：一事实一主、当前真相与历史分离、分类感知冲突验证、权威完成门。
- Agent 约定文件命名通用化：默认 `AGENTS.md`，可复用平台等价文件（`CLAUDE.md` / `COPILOT.md` / `GEMINI.md` 等），禁止并行约定文件。
- 交接就绪测试：`references/fresh-session-test.md` 7 问清单。
- 金标准示例：`examples/bootstrap/`（虚构 remindr 项目）。
- 回归夹具：`fixtures/messy/` 故意损坏参考项目 + `scripts/` 确定性验收脚本（`lint_skill.py` / `check_fixture.py` / `verify_refactor.py`）。
- 插件分发资产：`.claude-plugin/plugin.json`、`marketplace.json`、`PLUGIN.md`（官方目录 / 自建 marketplace / 本地安装三种接入）。
- 发布配套：README（中英混合、中文为主）、MIT LICENSE、CHANGELOG、CONTRIBUTING、CI workflow。

### Fixed

- `lint_skill.py` 对 `references/authority-model.md` 中指向目标项目根目录的模板示例链接加入显式豁免。
