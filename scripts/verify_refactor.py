"""Structural acceptance check for a REFACTOR run against fixtures/messy.

Usage: python scripts/verify_refactor.py <refactored-project-dir>

Checks the deterministic expectations from fixtures/README.md:
  1. root keeps README.md plus authority files only
  2. exactly one agent convention file exists (AGENTS.md / CLAUDE.md / COPILOT.md)
  3. that convention file contains New Session Protocol and Authority Maintenance
     Protocol, each exactly once
  4. PROJECT_STATE.md is present with the full present-tense section set
  5. root no longer carries history files; history lives under docs/history/
     with a non-authoritative marker
  6. business source files were not broken (app.py stub marker, summarize.py
     functions, requirements.txt)

Semantic acceptance (fresh-session 7 questions, conflict resolution quality,
final report fields) cannot be machine-checked and is left to the agent.

Exit code 0 = all structural checks pass, 1 = any failure.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

CONVENTION_CANDIDATES = ["AGENTS.md", "CLAUDE.md", "COPILOT.md"]

ROOT_HISTORY_FILES = [
    "sprint-review-2026-Q1.md",
    "TODO-old.md",
    "architecture-notes.md",
]

STATE_SECTIONS = [
    "Last Updated",
    "## Current Status",
    "## Current Work",
    "## Implemented",
    "## Next",
    "## New Session Handoff",
]

NON_AUTHORITATIVE_MARKERS = ("historical", "not authoritative")

OPTIONAL_AUTHORITY = ["ARCHITECTURE.md", "RUNBOOK.md", "DECISIONS.md"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Structural acceptance for a REFACTOR result")
    parser.add_argument("dir", help="path to the refactored project directory")
    args = parser.parse_args()

    root = Path(args.dir).resolve()
    failures = []

    if not root.is_dir():
        print(f"FAIL: not a directory: {root}")
        return 1

    # 1. root entry point
    if not (root / "README.md").exists():
        failures.append("README.md missing from root")

    # 2. exactly one convention file
    present = [c for c in CONVENTION_CANDIDATES if (root / c).exists()]
    if len(present) == 0:
        failures.append("no agent convention file (AGENTS.md / CLAUDE.md / COPILOT.md)")
    elif len(present) > 1:
        failures.append(f"parallel convention files forbidden, found: {', '.join(present)}")
    else:
        conv = present[0]
        text = (root / conv).read_text(encoding="utf-8")
        for proto in ("New Session Protocol", "Authority Maintenance Protocol"):
            count = text.count(proto)
            if count != 1:
                failures.append(f"{conv}: '{proto}' appears {count} times (expected exactly 1)")

    # 3. PROJECT_STATE sections
    state = root / "PROJECT_STATE.md"
    if state.exists():
        stext = state.read_text(encoding="utf-8")
        for sec in STATE_SECTIONS:
            if sec not in stext:
                failures.append(f"PROJECT_STATE.md missing section: {sec}")
    else:
        failures.append("PROJECT_STATE.md missing")

    # 4. root history must be gone; history archived under docs/history
    for rel in ROOT_HISTORY_FILES:
        if (root / rel).exists():
            failures.append(f"history still at root: {rel}")

    hist_dir = root / "docs" / "history"
    archived = []
    for pattern in ("sprint-review-2026-Q1.md", "TODO-old.md", "architecture-notes.md"):
        hits = list(hist_dir.rglob(pattern)) + list(hist_dir.rglob("**/prompt-2026-05.md"))
        archived += hits
    if not archived:
        failures.append("no archived history found under docs/history/")
    else:
        for h in archived:
            try:
                htext = h.read_text(encoding="utf-8")
            except Exception:
                htext = ""
            if not any(marker in htext.lower() for marker in NON_AUTHORITATIVE_MARKERS):
                failures.append(f"archived artifact lacks non-authoritative marker: {h.relative_to(root)}")

    # 5. business code not broken
    app = root / "app.py"
    if app.exists():
        if "not implemented" not in app.read_text(encoding="utf-8").lower():
            failures.append("app.py stub marker lost (business code was modified)")
    else:
        failures.append("app.py missing (business code was removed)")
    for fn in ("load_reminders", "render_digest"):
        sm = root / "summarize.py"
        if sm.exists():
            if fn not in sm.read_text(encoding="utf-8"):
                failures.append(f"summarize.py lost {fn} (business code was modified)")
        else:
            failures.append("summarize.py missing (business code was removed)")
    if not (root / "requirements.txt").exists():
        failures.append("requirements.txt missing")

    # 6. optional authority files are non-empty if present
    for name in OPTIONAL_AUTHORITY:
        p = root / name
        if p.exists() and p.stat().st_size == 0:
            failures.append(f"{name} exists but is empty")

    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        print("\nStructural acceptance failed. Semantic acceptance (fresh-session test,"
              " conflict quality, report fields) still needs agent review.")
        return 1
    print("verify_refactor: STRUCTURAL ACCEPTANCE PASS")
    print("Reminder: run the fresh-session 7-question checklist and confirm the final"
          " report before declaring Context Health: GOOD.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
