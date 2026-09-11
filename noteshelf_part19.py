# === Stage 19: Add undo support for the last simple mutation ===
# Project: NoteShelf
def undo_last_mutation(self):
    """Undo the last simple mutation (add_note, remove_note, update_note)."""
    if self._undo_stack:
        note_id, action = self._undo_stack.pop()
        if action == "add":
            self.notes[note_id] = {}
            self._undo_stack.append((note_id, "add"))
        elif action == "remove":
            self.notes[note_id] = {}
            self._undo_stack.append((note_id, "remove"))
        elif action == "update":
            self.notes[note_id] = self._snapshot[note_id]
            self._undo_stack.append((note_id, "update"))
        self._current_snapshot = self._snapshot.copy()
    return self
