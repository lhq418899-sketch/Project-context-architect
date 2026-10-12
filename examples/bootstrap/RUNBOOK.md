> Example artifact from a fictional project (`remindr`). Not part of this skill.

# RUNBOOK

Commands verified against a clean checkout on 2026-10-09 unless marked unverified.

## Setup
- `python -m venv .venv` then activate — verified on Windows and macOS.
- `pip install -r requirements.txt` — verified.

## Run
- `python summarize.py digest reminders/ --out digest.txt` — verified.
- `python app.py --port 8080` — verified (local only).

## Test
- `python -m pytest tests/` — verified, 34 passing.
- (unverified) `python -m pytest --cov=summarize` — coverage plugin not yet installed.

## Common failures
- YAML parse error: source file uses tabs; convert to spaces (see ADR-002 in DECISIONS.md).
- Port 8080 busy: pass `--port`; do not edit `app.py` for a local run.
