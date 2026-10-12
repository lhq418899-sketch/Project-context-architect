"""Load YAML reminders and render a plain-text digest."""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import yaml


def load_reminders(source_dir: Path) -> list[dict]:
    reminders = []
    for path in sorted(source_dir.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        for item in data.get("reminders", []):
            item["source"] = path.stem
            reminders.append(item)
    return reminders


def render_digest(reminders: list[dict], tz: dt.tzinfo) -> str:
    lines = []
    for item in reminders:
        when = dt.datetime.fromisoformat(item["when"]).astimezone(tz)
        lines.append(f"- {when:%H:%M} {item['text']} ({item['source']})")
    return "\n".join(lines)
