# Fixtures（回归夹具）

`messy/` 是一个**故意损坏**的参考项目，用于：

- **完整演练 REFACTOR**：在动真实仓库之前先走一遍流程；
- **回归测试本 skill**：修改规则后跑一遍——下方期望产出是固定的，任何破坏流程的改动都会在这里先暴露。

## 使用方式（How to use）

1. 复制 `messy/` 到临时目录——**不要在原位重构**，夹具要保持可复用。
2. 对副本执行 skill 的 REFACTOR 模式。
3. 对照下方期望产出检查，然后运行结构验收脚本：
   `python scripts/verify_refactor.py <临时目录>`（用法见 [scripts/README.md](../scripts/README.md)）。

演练前确认夹具仍处于损坏状态：`python scripts/check_fixture.py`。

## Expected outcomes after a correct REFACTOR

- 根目录只保留 `README.md` 与权威文件（agent 约定文件——`AGENTS.md` 或项目已在用的平台等价文件——以及 `PROJECT_STATE.md`；`ARCHITECTURE.md` / `RUNBOOK.md` / `DECISIONS.md` 仅在确有内容时保留）。
- agent 约定文件恰好包含一份 New Session Protocol 与一份 Authority Maintenance Protocol，并与幸存的项目规则合并。
- `PROJECT_STATE.md` 聚焦当下：CLI 已实现、web 视图是 stub、写明了真实的下一步。
- 所有历史材料（sprint 复盘、旧 TODO、旧 prompt、被取代的架构笔记）位于 `docs/history/` 下，并带非权威标注。
- 业务源文件（`summarize.py`、`app.py`、`tests/`、`requirements.txt`）未被改动。
- fresh-session 测试通过；最终报告以 `Context Health: GOOD` 结尾。
