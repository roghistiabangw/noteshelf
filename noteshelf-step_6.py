# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: NoteShelf
def delete_note(self, note_id: str, confirm: bool = False) -> bool:
    """Delete a note by ID. When confirm is False, returns silently; when True, asks the user."""
    note = self._find_note(note_id)
    if note is None:
        return False
    if confirm:
        if not input(f"Delete note '{note.title}'? [y/N] ").lower().startswith("y"):
            return False
    self._notes.remove(note)
    self._save()
    return True
