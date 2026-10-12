> Example artifact from a fictional project (`remindr`). Not part of this skill.

# AGENTS.md

Project-specific working rules for the remindr repository, plus the standard orientation and maintenance protocols.

## Project rules (user-owned, do not edit casually)

- Python 3.11+; dependencies limited to stdlib plus Flask and PyYAML.
- All reminder sources live under `reminders/` as YAML. Never introduce a new source format without a `DECISIONS.md` entry.
- Tests must run offline; no network calls in fixtures.
- Do not send real Slack/email messages from development branches.

## New Session Protocol

L0 Orientation — read first:
1. `AGENTS.md`
2. `PROJECT_STATE.md`

L1 Task Context — then read only what the task requires:
- architecture → `ARCHITECTURE.md`
- rationale → `DECISIONS.md`
- operation → `RUNBOOK.md`
- stable product rules → `PRODUCT_RULES.md`

List only authority documents that exist and are relevant to this project. Load history and broad source trees only when the current task provides a reason.

## Authority Maintenance Protocol

Apply this protocol to tasks that change project facts. Read-only analysis, explanation, and review require no authority edit unless they produce an accepted decision.

### Task Start

1. Read L0 Orientation: `AGENTS.md` and `PROJECT_STATE.md`.
2. Identify which authority categories the task may affect and load only their L1 documents.
3. Update `PROJECT_STATE.md > Current Work` before implementation only when this task becomes the project's main tracked work, changes `Next`, or replaces the current task.

### Authority Checkpoints

- Codify an accepted explicit user decision in its owner before later work depends on it.
- When verified work changes an authority fact, update its owner in the same task:
  - status, current work, issues, or next step → `PROJECT_STATE.md`
  - implemented components, boundaries, entry points, or data flow → `ARCHITECTURE.md`
  - durable decision and rationale → `DECISIONS.md`
  - environment, start, test, build, validation, or debugging → `RUNBOOK.md`
  - product invariant or permission boundary → `PRODUCT_RULES.md`
- Mark implementation as `Implemented` only after verification. Plans and work in progress remain identified as such.
- When no authority fact changes, leave authority documents untouched.

### Task Completion Gate

1. Reconcile the authority delta across every affected category.
2. Update only changed `PROJECT_STATE.md` facts, including status, known issues, next step, and handoff pointers.
3. Record an unresolved semantic conflict as an explicit unresolved issue without guessing its answer.
4. Run the L0 fresh-session test checklist.
5. Treat the task as incomplete while any affected authority remains stale.
6. If there was no authority impact, report `Authority impact: none` and make no authority edit.
