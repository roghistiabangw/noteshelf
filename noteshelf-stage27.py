# === Stage 27: Add monthly summary calculations ===
# Project: NoteShelf
import json
from datetime import datetime, timedelta
from collections import defaultdict

MONTHLY_STATS = {}


def compute_monthly_summary(notes):
    """Compute monthly summary stats for notes, grouped by folder."""
    global MONTHLY_STATS
    MONTHLY_STATS = defaultdict(lambda: defaultdict(lambda: {"count": 0, "total_chars": 0, "pinned": 0}))
    for note in notes:
        date_str = note.get("date", datetime.now().strftime("%Y-%m"))
        folder = note.get("folder", "default")
        MONTHLY_STATS[date_str][folder]["count"] += 1
        MONTHLY_STATS[date_str][folder]["total_chars"] += len(note.get("content", ""))
        if note.get("pinned", False):
            MONTHLY_STATS[date_str][folder]["pinned"] += 1
    return dict(MONTHLY_STATS)
