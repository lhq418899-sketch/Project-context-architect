# 回归脚本

确定性检查脚本，全部纯 Python 标准库，Windows / macOS / Linux 均可运行，无需安装依赖。

| 脚本 | 作用 | 何时运行 |
|---|---|---|
| `lint_skill.py` | 自检 skill 本体：必需文件、相对链接、UTF-8 编码、关键契约措辞 | 每次修改 skill 后 |
| `check_fixture.py` | 验证 `fixtures/messy/` 仍处于"故意损坏"状态（前提未被意外修好） | 修改 skill 或 fixture 后 |
| `verify_refactor.py <dir>` | 对 REFACTOR 后的目录做结构级验收（对照 fixtures/README.md 期望产出） | 用 fixture 演练 REFACTOR 后 |

## 用法

```bash
python scripts/lint_skill.py
python scripts/check_fixture.py

# 演练 REFACTOR（先复制夹具，勿在原位改）
copy /Y fixtures\messy C:\scratch\messy-test   # Windows
# cp -r fixtures/messy /tmp/messy-test          # macOS/Linux
# 对副本执行 skill 的 REFACTOR 模式……
python scripts/verify_refactor.py C:\scratch\messy-test
```

## 边界（脚本查什么、不查什么）

- 脚本只做**确定性结构断言**（文件存在、链接、章节、标记、编码）。
- **语义级验收**（fresh-session 7 问能否答出、报告字段是否 `GOOD`、冲突消解是否正确）必须由 agent 在对话中完成，脚本不做、也不替代。
- 所有脚本退出码：0 = 全部通过；1 = 存在失败项。
