"""Structural self-check for the project-context-architect skill.

Checks (deterministic only):
  1. required files exist
  2. all relative Markdown links resolve (examples/bootstrap/ excluded: it points into a fictional project)
  3. every .md/.py/.yaml/.json file is strict UTF-8 without BOM
  4. SKILL.md still carries the key contract phrases

Exit code 0 = all pass, 1 = any failure. Pure stdlib, no dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "SKILL.md",
    "references/authority-model.md",
    "references/bootstrap.md",
    "references/check.md",
    "references/refactor.md",
    "references/fresh-session-test.md",
    "examples/README.md",
    "examples/bootstrap/AGENTS.md",
    "examples/bootstrap/PROJECT_STATE.md",
    "examples/bootstrap/DECISIONS.md",
    "examples/bootstrap/RUNBOOK.md",
    "fixtures/README.md",
    "fixtures/messy/README.md",
    "fixtures/messy/AGENTS.md",
    "fixtures/messy/PROJECT_STATE.md",
    "fixtures/messy/summarize.py",
    "fixtures/messy/app.py",
    "fixtures/messy/requirements.txt",
    "fixtures/messy/tests/test_summarize.py",
    "agents/openai.yaml",
    ".claude-plugin/plugin.json",
    "marketplace.json",
    "PLUGIN.md",
    "scripts/README.md",
    # 发布配套
    "README.md",
    "README.en.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    ".gitignore",
    ".github/workflows/ci.yml",
]

KEY_PHRASES = [
    ("SKILL.md", "Fill any field with no content as `none`"),
    ("SKILL.md", "see the naming rule in [references/authority-model.md](references/authority-model.md)"),
    ("SKILL.md", "[references/fresh-session-test.md](references/fresh-session-test.md)"),
    ("SKILL.md", "[examples/bootstrap/](examples/bootstrap/)"),
    ("SKILL.md", "[fixtures/messy/](fixtures/messy/)"),
    ("references/authority-model.md", "## Agent convention file naming"),
    ("fixtures/README.md", "Expected outcomes after a correct REFACTOR"),
    ("README.md", "中英混合、中文为主"),
    ("README.md", "[MIT](LICENSE)"),
    ("CHANGELOG.md", "## [0.1.0]"),
    ("README.en.md", "## Three modes"),
    ("PLUGIN.md", "Codex 用户接入"),
    ("README.md", "OpenAI Codex"),
    ("README.en.md", "OpenAI Codex"),
]

LINK_RE = re.compile(r"\]\(([^)#]+?)\)")

# Template examples inside authority-model.md point into the TARGET project root
# (e.g. `See [ARCHITECTURE.md](ARCHITECTURE.md)`), not into this skill. They are
# intentional illustrations, so they are exempt from link resolution.
EXEMPT = {
    "references/authority-model.md": {"ARCHITECTURE.md", "relative/path.md"},
}


def check_required() -> list[str]:
    return [f"missing required file: {p}" for p in REQUIRED_FILES if not (ROOT / p).exists()]


def check_links() -> list[str]:
    problems = []
    files = sorted((ROOT / "references").glob("*.md")) + [
        ROOT / "SKILL.md",
        ROOT / "examples" / "README.md",
        ROOT / "fixtures" / "README.md",
        ROOT / "PLUGIN.md",
        ROOT / "README.md",
        ROOT / "README.en.md",
        ROOT / "CONTRIBUTING.md",
    ]
    for md in files:
        text = md.read_text(encoding="utf-8")
        text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)  # HTML comments are not document links
        base = md.parent
        exempt = EXEMPT.get(md.relative_to(ROOT).as_posix(), set())
        for m in LINK_RE.finditer(text):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target in exempt:
                continue
            if not (base / target).resolve().exists():
                problems.append(f"{md.relative_to(ROOT)} -> broken link: {target}")
    return problems


def check_encoding() -> list[str]:
    problems = []
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file():
            continue
        if p.suffix.lower() not in {".md", ".py", ".yaml", ".yml", ".json", ".txt"}:
            continue
        raw = p.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            problems.append(f"{p.relative_to(ROOT)}: BOM present (expected no BOM)")
            continue
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError as e:
            problems.append(f"{p.relative_to(ROOT)}: not UTF-8 ({e})")
    return problems


def check_key_phrases() -> list[str]:
    problems = []
    for rel, phrase in KEY_PHRASES:
        p = ROOT / rel
        if not p.exists():
            problems.append(f"{rel}: missing (cannot check phrase)")
            continue
        if phrase not in p.read_text(encoding="utf-8"):
            problems.append(f"{rel}: missing contract phrase -> {phrase}")
    return problems


def main() -> int:
    failures = check_required() + check_links() + check_encoding() + check_key_phrases()
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        print(f"\n{len(failures)} problem(s) found.")
        return 1
    print("lint_skill: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
