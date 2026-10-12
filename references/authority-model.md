# Authority Model

Use this reference when deciding which document owns a fact, creating a missing authority document, or consolidating conflicting documents.

## Authority set

The set is deliberately small. BOOTSTRAP always establishes the agent convention file (by default `AGENTS.md`; see the naming rule below) and `PROJECT_STATE.md`. Create `ARCHITECTURE.md`, `DECISIONS.md`, and `RUNBOOK.md` only when their category has substantive current content. Existing projects receive only missing categories that are genuinely needed.

| Owner | Question it answers | Owns | Excludes |
|---|---|---|---|
| `AGENTS.md` | How should an AI agent work here? | Development protocol, review expectations, user constraints, prohibited behavior, new-session read protocol, authority-maintenance protocol | Current status, architecture narrative, sprint history |
| `PROJECT_STATE.md` | What is true now? | Overall status, current work, implemented capabilities, known issues, non-goals, next step, handoff capsule | Full history, long design rationale, duplicated commands |
| `ARCHITECTURE.md` | How is the current system composed? | Components, boundaries, dependency direction, state ownership, main data flows, codebase map, important entry points | Former architecture, speculative future design, sprint timeline |
| `DECISIONS.md` | Why do stable choices exist? | Accepted or explicitly superseded ADRs whose rationale matters later | Routine implementation details, status updates |
| `RUNBOOK.md` | How is the project operated? | Environment, variables, start/test/build commands, ports, verification, debug entry points, common operational failures | Product status and duplicated design material |

## Agent convention file naming

The development-protocol owner defaults to `AGENTS.md`, the cross-tool agent convention. Naming is a default, not a quota:

- Reuse a platform equivalent the project already maintains — `CLAUDE.md`, `COPILOT.md`, `GEMINI.md`, or another project-level agent instruction file — instead of creating a parallel `AGENTS.md`. Merge the two root protocols into that file and use its name wherever this skill says `AGENTS.md`.
- When the project has no equivalent, create `AGENTS.md`.
- Never maintain parallel convention files; one fact, one owner applies to protocol files too.
- Reports, read maps, and the fresh-session test name the file actually used.

## `README.md`

`README.md` is the human-facing entry page: explain what the project is, who it is for, and where to go next. It may summarize and link to authority, but it does not own volatile project status, detailed architecture, ADR rationale, or full operational commands.

## Optional authority

Add an optional owner only when the information is stable, substantial, and repeatedly needed:

- `DOMAIN.md` or `CONTEXT.md` owns domain vocabulary and meanings.
- `PRODUCT_RULES.md` owns durable product invariants and permission boundaries.
- `LEARNING_RULES.md` owns durable learning or pedagogical invariants.
- `CURRENT_SPRINT.md` owns a long, frequently changing execution contract only when `PROJECT_STATE.md > Current Work` is genuinely insufficient, such as a multi-person sprint with substantial acceptance criteria.

Prefer one existing filename when a repository already has an equivalent owner. Avoid parallel files such as both `DOMAIN.md` and `CONTEXT.md` unless they have visibly different ownership.

## One fact, one owner

Assign the category before resolving a conflict:

- current sprint, status, next step → `PROJECT_STATE.md`
- current components, boundaries, entry points, data flow → `ARCHITECTURE.md`
- stable product invariant → `PRODUCT_RULES.md`
- runtime and validation commands → `RUNBOOK.md`
- enduring rationale → `DECISIONS.md`
- project working protocol → `AGENTS.md`
- terminology → `DOMAIN.md` or `CONTEXT.md`

Write the complete fact only in its owner. Other documents use a short contextual sentence and a relative link, for example `See [ARCHITECTURE.md](ARCHITECTURE.md).`

## Authority precedence

1. An explicit current user decision may supersede stale repository authority.
2. Once accepted, codify that decision in the appropriate repository owner during the same context-maintenance task.
3. The updated repository authority remains the long-term source of truth.
4. Old chat history, old prompts, and unrecorded prior discussion are non-authoritative.

## Category-aware conflict verification

For each conflict:

1. Identify its authority category.
2. Select evidence appropriate to that category:
   - runtime and configuration facts → current scripts, configuration, task runners, CI definitions, environment examples, or successful execution;
   - implementation state and entry points → current code, tests, and observed runtime behavior;
   - current work and delivery status → maintained project state, verified implementation progress, and explicit current user decisions;
   - architecture as implemented → current code and configuration, reconciled with accepted architectural decisions;
   - product invariants, permissions, and intended behavior → explicit current user decisions and their maintained authority owner; implementation is evidence only of whether the product currently conforms;
   - decision rationale → accepted ADRs or an explicit current user decision, not inference from code shape.
3. Update the owner with verified truth and replace competing current-looking claims with a link, historical label, or explicit supersession marker.
4. Escalate a conflict that changes product meaning, permissions, or user-visible behavior when the evidence cannot settle it.

Observed implementation is evidence of implementation state, not automatically evidence of intended product truth. A buggy implementation that violates a maintained product rule is a defect signal, not permission to rewrite the rule.

Never synthesize incompatible claims into a compromise merely to close the conflict.

## Minimum document shapes

### Agent convention file (defaults to `AGENTS.md`)

Preserve existing project-specific instructions. Put the following protocols once in the project-root agent convention file (by default `AGENTS.md`; reuse the platform equivalent per the naming rule above); nested copies of that file may add local working rules but do not copy the root protocols.

Ensure the root file contains a concise section equivalent to:

```md
## New Session Protocol

L0 Orientation — read first:
1. `AGENTS.md`
2. `PROJECT_STATE.md`

L1 Task Context — then read only what the task requires:
- architecture → `ARCHITECTURE.md`
- rationale → `DECISIONS.md`
- operation → `RUNBOOK.md`
- domain terms → `DOMAIN.md` or `CONTEXT.md`
- stable product rules → `PRODUCT_RULES.md`

List only authority documents that exist and are relevant to this project.
Load history and broad source trees only when the current task provides a reason.
```

Also merge this event-driven write-back contract into the same root file:

```md
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
- Create a missing conditional authority file only when the change gives that category substantive content.
- Mark implementation as `Implemented` only after verification. Plans and work in progress remain identified as such.
- When no authority fact changes, leave authority documents untouched.

### Task Completion Gate

1. Reconcile the authority delta across every affected category.
2. Update only changed `PROJECT_STATE.md` facts, including status, known issues, next step, and handoff pointers.
3. Record an unresolved semantic conflict as an explicit unresolved issue without guessing its answer.
4. Run the L0 fresh-session test checklist in [fresh-session-test.md](fresh-session-test.md).
5. Treat the task as incomplete while any affected authority remains stale.
6. If there was no authority impact, report `Authority impact: none` and make no authority edit.
```

Merge semantically equivalent existing rules instead of appending a duplicate protocol.

### `PROJECT_STATE.md`

Use this compact present-tense structure:

```md
# Project State

Last Updated: YYYY-MM-DD

## Project
## Current Status
## Current Work
## Implemented
## Known Issues
## Non-goals
## Next
## New Session Handoff
```

The handoff must contain:

```md
### Project
### Current Product State
### Current Work
### Current Architecture
### Important Constraints
### Next
### Read Next If Needed
```

Use three to eight truly important constraints. Keep detailed sprint narrative out of current authority.

Keep `New Session Handoff` compact, preferably around 30–80 lines. It is an orientation capsule and pointer map, not a second copy of the authority set.

### `ARCHITECTURE.md`

Describe only deployed or currently implemented architecture. Include a compact map from important directories or modules to responsibilities. Split out a separate codebase map only when repository scale makes the combined file hard to use.

### `DECISIONS.md`

Create this file only when at least one decision has durable rationale worth preserving. For each real ADR use:

```md
## ADR-NNN — Title

Status: Accepted | Superseded
Date: YYYY-MM-DD

### Context
### Decision
### Reason
### Consequence
```

### `RUNBOOK.md`

Use commands verified against scripts, task runners, CI configuration, or a successful local run. Mark any unexecuted command as unverified rather than implying it was tested.

## Historical artifacts

Classify sprint reviews, phase reviews, bug-fix reviews, old prompts, migration plans, and replaced proposals as history when they no longer define current behavior. Place them under a suitable path such as:

```text
docs/history/
  sprints/
  reviews/
  bugfixes/
  superseded/
```

Add a visible header:

```md
> Historical artifact.
> Not authoritative for current project behavior.
```

When replaced, also add:

```md
Status: SUPERSEDED
Superseded by: [current owner or replacement](relative/path.md)
```

Keep root focused on the README and active authority files. Preserve historical artifacts and their useful context rather than deleting them.
