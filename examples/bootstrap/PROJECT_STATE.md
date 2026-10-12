> Example artifact from a fictional project (`remindr`). Not part of this skill.

# Project State

Last Updated: 2026-10-11

## Project
`remindr`: internal daily-digest tool for the platform team. Turns YAML reminder sources into a single morning summary, rendered as plain text (CLI) and HTML (web view).

## Current Status
In active development. Core CLI shipped and tested; web view is a stub in progress.

## Current Work
Web view (PR #23): Flask route wraps the CLI digest in HTML. Currently fixing multi-line YAML block rendering.

## Implemented
- YAML source loading with strict schema validation — implemented, tested.
- CLI `remindr digest` producing plain-text digest — implemented, tested.
- Per-source timezone handling — implemented, tested.

## Known Issues
- Web view drops multi-line YAML blocks (open, low priority).
- `remindr digest --from` with a future date silently returns empty.

## Non-goals
- Real notifications (Slack/email) — decided out of scope for 2026 H2 (see DECISIONS.md ADR-003).
- Multi-user accounts and permissions.

## Next
Fix multi-line block rendering, merge PR #23, then flip this file's Current Status to `Web view shipped`.

## New Session Handoff

### Project
Internal daily-digest tool for the platform team: CLI plus a small Flask web view over YAML reminder sources in `reminders/`.

### Current Product State
CLI shipped and tested. Web view in progress; renders markdown digest without auth.

### Current Work
Web view PR #23: Flask route renders digest HTML. Pending: multi-line block fix.

### Current Architecture
`summarize.py` loads and validates YAML, builds the digest. `app.py` wraps that output in Flask. `reminders/*.yaml` is the only data source; no database, state is file-based. See ARCHITECTURE.md.

### Important Constraints
- stdlib + Flask + PyYAML only; no new dependencies without a DECISIONS entry.
- Reminder sources live only under `reminders/` as YAML.
- Tests must run offline.
- No real Slack/email sends from dev branches.

### Next
Merge PR #23 after the multi-line fix; update this file's Current Status.

### Read Next If Needed
- architecture → ARCHITECTURE.md
- rationale → DECISIONS.md
- operation → RUNBOOK.md
