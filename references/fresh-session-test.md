# Fresh-Session Test

Run this checklist whenever a mode or the Authority Maintenance Protocol requires the fresh-session test (BOOTSTRAP, CHECK, REFACTOR, and the completion gate).

## How to run

Role-play a fresh session: you have no chat history, no memory of this project, and you will not read repository source. You may read only the L0 Orientation files (the agent convention file — by default `AGENTS.md`, or the platform equivalent in use — plus `PROJECT_STATE.md`) and whatever L1 authority document a question legitimately names. Answer each question below from those files alone.

## Questions

Ask all of them. A single failure fails the gate.

1. **Identity** — What is this project, in one sentence, and who is it for?
2. **Status** — What is the current status, and what work is in progress right now?
3. **Entry point** — Without opening source, where does execution start? What is the main entry point and start command?
4. **Architecture** — In 3–5 lines, how is the system composed (components, boundaries, main data flow, state ownership)?
5. **Constraints** — What hard constraints, permissions, or non-goals must a fresh session not violate?
6. **Next** — What is the next step, and what is the stop condition for current work?
7. **Task context** — If asked to change the architecture, which L1 document do you load? If asked for an operational command, which one? (Answers must be existing links.)

## Pass / fail

- **Pass** — all seven questions answered from L0 (plus named L1) alone, with no contradiction between files.
- **Fail** — any question requires reading source code, chat history, `docs/history/`, or a document not listed in the read map; or two authority files give conflicting answers.

## Repair discipline

On failure, fix only the defect the failed question exposed. Do not expand the test into a general cleanup. Re-run the full test after any fix.
