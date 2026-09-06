# === Stage 4: Implement create operations for the primary records ===
# Project: NoteShelf
def create_note(self, title="", body="", tags=None, pinned=False, folder_id=None):
    if tags is None:
        tags = []
    note_id = self._next_id("note")
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "tags": tags,
        "pinned": pinned,
        "folder_id": folder_id,
        "created_at": time.time(),
        "updated_at": time.time(),
    }
    self._notes[note_id] = note
    if pinned:
        self._pinned_notes.append(note_id)
    if folder_id is not None:
        self._notes_in_folder[folder_id].append(note_id)
    return note_id
