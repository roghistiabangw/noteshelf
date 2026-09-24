# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: NoteShelf
def bulk_delete_notes(self, note_ids, confirmed=False):
    if not confirmed:
        raise ValueError("Bulk delete requires user confirmation")
    for nid in note_ids:
        if nid in self.notes:
            del self.notes[nid]
    return list(note_ids)
