import datetime as dt
from pathlib import Path

from summarize import load_reminders, render_digest


def test_load_reminders(tmp_path: Path) -> None:
    (tmp_path / "team.yaml").write_text(
        "reminders:\n  - when: '2026-10-12T09:00:00'\n    text: standup\n",
        encoding="utf-8",
    )
    reminders = load_reminders(tmp_path)
    assert reminders[0]["source"] == "team"


def test_render_digest() -> None:
    reminders = [{"when": "2026-10-12T09:00:00", "text": "standup", "source": "team"}]
    out = render_digest(reminders, dt.timezone.utc)
    assert "standup" in out
    assert "(team)" in out
