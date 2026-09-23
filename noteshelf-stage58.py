# === Stage 58: Add bulk update behavior for selected records ===
# Project: NoteShelf
def bulk_update(self, records: list[dict]) -> int:
        """Update multiple notes in one call; returns the number of records actually changed."""
        if not records:
            return 0
        count = 0
        for note in records:
            note_id = note.pop("id", None)
            if note_id is None:
                continue
            if note_id in self._notes:
                self._notes[note_id].update(note)
                self._notes[note_id]["updated_at"] = datetime.now(UTC)
                if "text" in note:
                    self._reindex(note_id)
                self._persist()
                count += 1
            else:
                self.log.warning("bulk_update: id %s not found", note_id)
        return count
