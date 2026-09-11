# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: NoteShelf
def archive_note(self, note, archive_dir=None):
    if archive_dir is None:
        archive_dir = os.path.join(self.data_dir, "archive")
    os.makedirs(archive_dir, exist_ok=True)
    ext = note.get("type", "text")
    suffix = {
        "text": "txt", "json": "json", "markdown": "md", "html": "html"
    }.get(ext, "txt")
    ts = int(time.time())
    name = f"{note.get('id', '')}_{ts}.{suffix}"
    dest = os.path.join(archive_dir, name)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(note.get("content", ""))
    self._history.append({"action": "archive", "note": note, "dest": dest, "ts": ts})
    return dest
