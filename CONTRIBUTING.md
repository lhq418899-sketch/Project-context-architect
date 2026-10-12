# 贡献指南（Contributing）

欢迎提交 Issue、PR 或文档改进。本项目是一个 **agent skill**——贡献的本质是改进"代理如何维护项目上下文"这套协议。

## 本地开发

无需安装任何依赖，Python 3.x 即可（脚本为纯标准库）：

```bash
python scripts/lint_skill.py          # 结构自检：必需文件、链接、编码、契约措辞
python scripts/check_fixture.py       # 确认演练夹具仍处于"故意损坏"状态
```

## 修改纪律

1. **先读再改**：改动涉及权威模型 / 三模式时，先读 [SKILL.md](SKILL.md) 与 [references/authority-model.md](references/authority-model.md)，保持概念一致性（一事实一主、当前真相与历史分离、权威完成门）。
2. **脚本只做结构断言**：`scripts/` 只检查确定性结构；语义级验收（fresh-session 7 问、冲突消解质量、报告字段）由 agent 在对话中完成。新增结构性约束时，请同步更新 `lint_skill.py` 的 `REQUIRED_FILES` / `KEY_PHRASES`。
3. **夹具勿在原位重构**：演练 REFACTOR 时先复制 `fixtures/messy/` 到临时目录，验证后删除。
4. **发布文件属于仓库**：`README.md`、`LICENSE`、`CHANGELOG.md` 等发布配套是仓库一部分，删除或改名需在 PR 中说明理由。

## 提 PR

1. 先在 [Issues](https://github.com/lhq418899-sketch/Project-context-architect/issues) 说明意图（改动类型、影响面），避免重复劳动。
2. 分支命名建议：`fix/`、`feat/`、`docs/` 前缀。
3. 提交前本地跑通上述脚本 + `verify_refactor.py` 对演练副本的验收。
4. PR 描述写清：改了什么、为什么、验证方式。

## 语言约定

- 面向人的分发与贡献文档：**中文为主**（可中英混合）。
- 核心执行文件（`SKILL.md`、`references/`、`examples/`）：保持**英文**，以保证各平台 agent 触发与执行一致。
- 新增关键词/概念请中英并注，便于全球贡献者对齐术语。

## 许可证

贡献即表示你同意你的内容按 [MIT](LICENSE) 授权。
