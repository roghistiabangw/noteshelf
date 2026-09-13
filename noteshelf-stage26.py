# === Stage 26: Add weekly summary calculations ===
# Project: NoteShelf
import json
from datetime import datetime, timedelta

def weekly_summary(notes):
    """Return dict of week_id -> {total_notes, total_chars, avg_length}."""
    week_id = datetime.now().isocalendar()[:2]
    week_notes = [n for n in notes if n.get("week_id") == week_id]
    total = len(week_notes)
    chars = sum(len(n.get("text", "")) for n in week_notes)
    return {
        "week_id": week_id,
        "total_notes": total,
        "total_chars": chars,
        "avg_length": chars / total if total else 0
    }
