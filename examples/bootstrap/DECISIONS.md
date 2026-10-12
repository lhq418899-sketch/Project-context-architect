> Example artifact from a fictional project (`remindr`). Not part of this skill.

# Decisions

## ADR-001 — CLI owns digest rendering; web view wraps it

Status: Accepted
Date: 2026-08-14

### Context
The web view and CLI initially each rendered digests with their own templates, producing subtly different output.

### Decision
`summarize.py` owns digest construction; `app.py` only wraps CLI output in HTML.

### Reason
One rendering path means one format to test and no drift between surfaces.

### Consequence
Web changes that need new rendering must go through the CLI layer first. Simpler tests, slightly less flexible HTML.
