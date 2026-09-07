# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: NoteShelf
import operator

def sort_notes(notes, key='date'):
    """Sort notes by title, date, priority, or last_update."""
    sort_keys = {
        'title': lambda n: n.get('title', '').lower(),
        'date': lambda n: n.get('date', ''),
        'priority': lambda n: n.get('priority', 0),
        'last_update': lambda n: n.get('last_update', ''),
    }
    if key not in sort_keys:
        key = 'date'
    return sorted(notes, key=sort_keys[key], reverse=(key == 'priority'))
