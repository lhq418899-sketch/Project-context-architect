---
name: project-context-architect
description: Establish and maintain a project's smallest authoritative context. Use when bootstrapping handoff docs for a new project, refactoring conflicting or stale project documentation, archiving sprint and review history, or checking whether a fresh session can safely take over. This skill manages project context, not business implementation.
---

# Project Context Architect

Build a **minimum authority**: a small, explicit, current set of repository files that lets a fresh session understand the project without inheriting chat history or reading the entire repository.

Repository authority is the long-term source of truth. An explicit current user decision may supersede stale repository authority; once accepted, codify it in the appropriate authority document. Old chat history is non-authoritative. Current truth and historical explanation live separately. Keep each fact under one authority owner.

## Choose one mode

Honor an explicit mode. Otherwise inspect the project briefly and choose:

- **BOOTSTRAP** — a new or early project lacks a coherent handoff system. Read [references/bootstrap.md](references/bootstrap.md) before changing files.
- **REFACTOR** — an established project has scattered, duplicated, stale, or conflicting context. Read [references/refactor.md](references/refactor.md) before changing files.
- **CHECK** — the user wants a handoff-readiness check, or the project has just crossed a sprint, milestone, or major refactor. Read [references/check.md](references/check.md) before changing files.

If the evidence fits more than one mode, choose the least expansive mode that meets the request and state the choice. A CHECK may recommend REFACTOR; it does not silently expand into one.

## Grounding

Before the first authority write, look once at [examples/bootstrap/](examples/bootstrap/). It is a fictional small project and the **register-and-density target**: your output should feel like those files, not like the bare templates. Never copy its content into a real repository.

[fixtures/messy/](fixtures/messy/) is a deliberately broken reference project. Use it to rehearse a REFACTOR or to regression-test this skill after edits; never treat it as a real project.

## Shared operating contract

1. Read the applicable project instructions and inventory the repository before editing. Use the README as a human-facing entry page, then inspect manifests, configuration, authority candidates, documentation, current entry points, and real run/test definitions as evidence. Read source selectively when it is needed to verify a claim.
2. Separate facts into **verified current truth**, **history**, and **uncertainty**. Verify conflicts with category-appropriate evidence from [references/authority-model.md](references/authority-model.md). Observed implementation is evidence of implementation state, not automatically evidence of intended product truth. Only verified current truth enters authority documents. Ask the user when unresolved alternatives would change product behavior; otherwise report them under `Still Uncertain`.
3. Read [references/authority-model.md](references/authority-model.md) whenever creating, assigning, or consolidating authority documents. Reuse an established equivalent document when it already has a clear owner; filenames are defaults, not a quota.
4. Change only project-context artifacts. Preserve business code and behavior. Preserve valuable history through archival and labeling. Keep unrelated user edits intact.
5. Run the **fresh-session test** using the checklist in [references/fresh-session-test.md](references/fresh-session-test.md): from **L0 Orientation** (the agent convention file, by default `AGENTS.md`, plus `PROJECT_STATE.md` — see the naming rule in [references/authority-model.md](references/authority-model.md)) confirm that a new session can identify the project, current status, current work, main entry point, architecture summary, hard constraints, next step, and which **L1 Task Context** authority document to load on demand. Fix only context defects revealed by this test.
6. Run an **authority delta** check before completion. Update every authority owner affected by verified changes, or leave authority documents untouched and record `Authority impact: none` under `Authority Docs` in the final report. A task with stale affected authority has not passed the completion gate.
7. Reinspect every changed document for one-fact/one-owner compliance, working links, current commands, and unsupported assertions.

Completion requires that every changed fact has one current authority owner, every moved historical artifact remains discoverable, every unresolved material conflict is surfaced rather than guessed away, and the authority delta gate passes.

## Mutation boundaries

- Treat existing root agent convention file instructions (by default `AGENTS.md`) as user-owned constraints. Merge the new-session and authority-maintenance protocols without discarding project-specific rules or copying the root protocol into nested copies of the convention file.
- Treat file moves, labels, and authority rewrites as context work; summarize them before completion. Use recoverable moves and retain history.
- Always establish the agent convention file (by default `AGENTS.md`; reuse a platform equivalent the project already maintains — see the naming rule in [references/authority-model.md](references/authority-model.md)) and `PROJECT_STATE.md` in BOOTSTRAP. Create `ARCHITECTURE.md`, `DECISIONS.md`, and `RUNBOOK.md` only when their authority category has substantive content. Optional authority documents must be justified by stable domain complexity, not by a desire for symmetry.
- Keep `PROJECT_STATE.md` focused on the present and scale it to project size: small single-module projects about 50–150 lines, multi-module projects 100–300 lines; past ~300 lines, move detail to history or a `CURRENT_SPRINT.md` instead of compressing. Keep `New Session Handoff` compact, roughly 30–80 lines, matching the register and density of [examples/bootstrap/](examples/bootstrap/). Condense completed work to short summaries and send detailed narrative to history.
- Keep commands authoritative in `RUNBOOK.md`; elsewhere, point to it.
- Record a decision in `DECISIONS.md` only when future maintainers would benefit from knowing why it was made.

## Report

End with a compact report in this exact field order. Fill any field with no content as `none`; do not omit the field or invent content.

```text
Mode:
BOOTSTRAP / REFACTOR / CHECK

Authority Docs:
...

Conflicts Found:
...

Conflicts Resolved:
...

Archived:
...

Still Uncertain:
...

New Session Read Order:
1. AGENTS.md (or platform equivalent in use)
2. PROJECT_STATE.md
...

Context Health:
GOOD / NEEDS_ATTENTION
```

Use `GOOD` only when the fresh-session test passes and no unresolved material authority conflict remains.
