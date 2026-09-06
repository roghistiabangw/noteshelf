# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: NoteShelf
def update_note(self, note_id, updates):
    """Update a note's fields; returns the updated note or None if not found."""
    try:
        note = next(n for n in self.notes if n["id"] == note_id)
    except StopIteration:
        return None
    for key, value in updates.items():
        if key not in note:
            return None
        note[key] = value
    self.save()
    return note
