# Architecture notes (draft, 2026-01)

Single-file app: everything in `app.py`. CLI and web share one module; no separation of loading, rendering, serving.

Update planned for sprint 6: split into `summarize.py` (loading + rendering) and `app.py` (serving).
