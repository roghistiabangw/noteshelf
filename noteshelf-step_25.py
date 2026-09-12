# === Stage 25: Add daily summary calculations ===
# Project: NoteShelf
from datetime import date, timedelta

def daily_summary(notes, date=None):
    if date is None:
        date = date.today()
    day_notes = [n for n in notes if n.get('date') == date]
    return {
        'date': date,
        'note_count': len(day_notes),
        'pinned': sum(1 for n in day_notes if n.get('pinned')),
        'tags': list({t for n in day_notes for t in n.get('tags', [])}),
    }
