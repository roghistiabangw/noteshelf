# === Stage 28: Add overdue item detection based on due dates ===
# Project: NoteShelf
def detect_overdue(items, today=None):
    """Return list of items whose due date has passed."""
    if today is None:
        today = datetime.date.today()
    overdue = []
    for item in items:
        due = item.get("due_date")
        if due and due <= today:
            overdue.append(item)
    return overdue
