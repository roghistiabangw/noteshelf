# === Stage 11: Add JSON export for the current application state ===
# Project: NoteShelf
def export_state(self):
    state = {
        "notes": [
            {
                "id": n["id"],
                "title": n["title"],
                "content": n["content"],
                "folder": n["folder"],
                "tags": n["tags"],
                "pinned": n["pinned"],
                "created": n["created"],
                "modified": n["modified"],
            }
            for n in self.notes
        ],
        "folders": list(self.folders),
        "tags": list(self.tags),
        "current_folder": self.current_folder,
        "current_search": self.current_search,
        "current_view": self.current_view,
        "current_note": self.current_note,
    }
    with open("notes.shelf.json", "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    print(f"[NoteShelf] State exported to notes.shelf.json ({len(self.notes)} notes)")
