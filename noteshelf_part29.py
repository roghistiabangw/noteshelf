# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: NoteShelf
def upcoming_reminders():
    """Return notes whose scheduled date is in the future, sorted by date."""
    now = datetime.now()
    items = []
    for note in _notes_store.values():
        if note.get("scheduled"):
            try:
                sched = datetime.fromisoformat(note["scheduled"])
                if sched > now:
                    items.append((sched, note))
            except (ValueError, TypeError):
                continue
    items.sort(key=lambda x: x[0])
    return [n for _, n in items]
