# === Stage 22: Add favorite records and quick favorite listing ===
# Project: NoteShelf
def toggle_favorite(self, note):
    if note.is_favorite:
        note.unfavorite()
        self._favorites.remove(note)
    else:
        note.favorite()
        self._favorites.append(note)
    self._save()

def get_favorite_notes(self):
    return sorted(self._favorites, key=lambda n: n.timestamp, reverse=True)
