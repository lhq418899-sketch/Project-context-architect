# CHECK

Use this mode after a sprint, milestone, or major refactor, or immediately before handing the project to a fresh session.

## Inspect proportionally

Read L0 Orientation (`AGENTS.md` and `PROJECT_STATE.md`) first. Follow their pointers into L1 Task Context only far enough to verify the categories affected by recent work. Use the category-aware verification rules in [authority-model.md](authority-model.md) when a current claim is disputed.

Check for:

- a missing, duplicated, or incomplete authority-maintenance protocol in the root agent convention file (by default `AGENTS.md`);
- authority mappings that name unnecessary or nonexistent project documents;
- maintenance rules that force edits when no authority fact changed;
- a completion rule that permits affected authority to remain stale;
- conflicting authority owners;
- stale current status or current work;
- old designs that still look current;
- an overgrown `PROJECT_STATE.md`;
- root-level sprint, review, fix, migration, or prompt history;
- runtime commands that diverge from scripts or configuration;
- changed architectural entry points or ownership;
- missing links to the appropriate deeper authority;
- a fresh session needing broad history or a repository-wide read to orient.

## Apply narrow repairs

Correct verified stale facts in their owner, replace duplication with links, update affected handoff text, and archive clearly historical artifacts when that action is unambiguous. Narrowly add or repair the root agent convention file's authority-maintenance protocol when its intended owner and wording are clear; preserve existing project rules and avoid copying it into nested copies of the convention file. Preserve sound documents unchanged. If the repair would require a broad taxonomy change, substantial conflict resolution, or uncertain semantic choice, report that REFACTOR is warranted instead of silently expanding scope.

At a sprint or milestone boundary, consider only owners whose truth changed:

- status and next work → `PROJECT_STATE.md`;
- component or data-flow changes → `ARCHITECTURE.md`;
- enduring rationale → `DECISIONS.md`;
- commands and environment → `RUNBOOK.md`;
- stable product invariants → `PRODUCT_RULES.md`.

Archive the detailed review; keep only its current consequences in authority.

## Verify readiness

Run the fresh-session test from [fresh-session-test.md](fresh-session-test.md) and the authority delta gate. CHECK is complete when every inspected category is either healthy, narrowly repaired, or named as a concrete unresolved problem. Return `GOOD` only when the handoff test passes, the root maintenance protocol is coherent, affected authority is current, and material uncertainty is absent; otherwise return `NEEDS_ATTENTION` with the smallest next action.
