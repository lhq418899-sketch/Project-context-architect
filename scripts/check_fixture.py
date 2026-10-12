"""Verify fixtures/messy is still in its deliberately-broken state.

A correct REFACTOR should NOT have been run on the fixture in place. If someone
ran one (or the fixture got edited), the broken-state preconditions below fail,
so this script doubles as a regression guard.

Checks:
  1. root history files still present (not yet archived)
  2. docs/history/ does not exist yet
  3. README still claims the CLI is deprecated (contradicts the code)
  4. PROJECT_STATE.md still stale (2026-03-01, sprint 5)
  5. business code still intact: app.py is a 501 stub, summarize.py still has
     load_reminders / render_digest, tests parse

Exit code 0 = fixture is still dirty/usable, 1 = fixture was altered.
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

FIXTURE = Path(__file__).resolve().parent.parent / "fixtures" / "messy"

ROOT_HISTORY_FILES = [
    "sprint-review-2026-Q1.md",
    "TODO-old.md",
    "architecture-notes.md",
    "docs/old-prompts/prompt-2026-05.md",
]


def main() -> int:
    failures = []

    for rel in ROOT_HISTORY_FILES:
        if not (FIXTURE / rel).exists():
            failures.append(f"history file already gone from root: {rel}")

    if (FIXTURE / "docs" / "history").exists():
        failures.append("docs/history exists in fixture: it was already refactored")

    readme = (FIXTURE / "README.md").read_text(encoding="utf-8")
    if "deprecated" not in readme.lower():
        failures.append("README no longer claims the CLI is deprecated (contradiction lost)")

    state = (FIXTURE / "PROJECT_STATE.md").read_text(encoding="utf-8")
    if "2026-03-01" not in state or "Sprint 5" not in state:
        failures.append("PROJECT_STATE no longer stale (2026-03-01 / Sprint 5 lost)")

    app = (FIXTURE / "app.py").read_text(encoding="utf-8")
    if "not implemented" not in app.lower():
        failures.append("app.py stub marker lost (web view must stay a 501 stub)")

    summarize = (FIXTURE / "summarize.py").read_text(encoding="utf-8")
    for fn in ("load_reminders", "render_digest"):
        if fn not in summarize:
            failures.append(f"summarize.py lost {fn}")

    for py in ("summarize.py", "app.py", "tests/test_summarize.py"):
        try:
            ast.parse((FIXTURE / py).read_text(encoding="utf-8"))
        except SyntaxError as e:
            failures.append(f"{py} syntax broken: {e}")

    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        print("\nFixture was altered; restore it before rehearsing REFACTOR.")
        return 1
    print("check_fixture: FIXTURE STILL DIRTY AND USABLE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
