# REFACTOR

Use this mode for an established project whose context is scattered, duplicated, stale, contradictory, or costly for a fresh session to load.

To rehearse or regression-test this mode, run it against the deliberately broken reference project in [fixtures/messy/](../fixtures/messy/); see its README for expected outcomes.

## Audit inventory

Inspect root Markdown, project instructions, README files, `docs/`, status and planning files, reviews, prompts, manifests, runtime configuration, entry points, and recent code needed to verify current behavior. Build a working inventory with one classification per relevant document:

- `CURRENT_AUTHORITY` — presently owns current truth;
- `HISTORICAL` — useful record that no longer governs current behavior;
- `SUPERSEDED` — replaced by an identified authority or later decision;
- `DUPLICATE` — restates a fact owned elsewhere without independent historical value;
- `WORKING_NOTE` — provisional material that is neither authority nor durable history.

This inventory is working analysis; include it in the final response only if the user asks.

Audit the project-root agent convention file (by default `AGENTS.md`; see the naming rule in authority-model.md) for both `New Session Protocol` and `Authority Maintenance Protocol`. Classify overlapping maintenance rules as duplicates to consolidate; do not propagate the root protocols into nested copies of the convention file.

## Detect material conflicts

Compare every current-looking claim about:

- current sprint or task;
- current architecture and state ownership;
- runtime, test, build, ports, and environment;
- product rules and permission boundaries;
- main entry point;
- next step and stop condition.

For each conflict, identify its authority category and use the category-aware verification rules in [authority-model.md](authority-model.md). A conflict is resolved only when the owner holds verified truth and competing current-looking claims no longer masquerade as authority. Treat implementation that violates a maintained product invariant as possible drift or a defect, not automatic evidence that the invariant changed.

## Consolidate authority

Read [authority-model.md](authority-model.md). Reuse sound existing owners. Create only missing authority categories. Consolidate current truth into the owner, replace full duplicate descriptions with links, and keep `PROJECT_STATE.md` present-focused.

An explicit current user decision may resolve stale repository authority; codify the accepted decision in its owner before completion. When an unresolved semantic choice affects behavior or permissions, pause that choice for user review while continuing independent cleanup. Record it under `Still Uncertain`; do not convert uncertainty into an ADR or current-state assertion.

Merge the two root protocols from [authority-model.md](authority-model.md) into the project-root agent convention file with semantically equivalent existing rules. Preserve project-specific constraints, remove duplicate protocol text, and retain the event-driven authority delta completion gate.

## Archive history

Move historical documents from the root into a discoverable `docs/history/` taxonomy appropriate to the repository. Add historical or superseded labels and relative replacement links. Preserve useful provenance. For a pure duplicate with no historical value, prefer reducing it to a redirect note or report it for user-directed removal rather than destroying it silently.

Update links affected by moves when they remain useful. Keep root-level active documents to the README, authority files, and project-required configuration or contribution documents.

## Verify recovery

Run the fresh-session test from [fresh-session-test.md](fresh-session-test.md) using the post-refactor files. Then verify:

- every audited current-looking document is classified;
- every material conflict is resolved or explicitly uncertain;
- each current fact has one owner;
- archived artifacts carry a non-authoritative label and remain reachable;
- root history no longer competes with current authority;
- runtime claims match repository evidence;
- the root agent convention file contains one coherent authority-maintenance protocol, permits no-op tasks to avoid document churn, and blocks completion when affected authority is stale;
- no business source file changed.

REFACTOR is complete only when a fresh session can orient from the minimum authority and no unmarked historical artifact plausibly reads as current truth.
