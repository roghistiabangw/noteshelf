# === Stage 14: Add file load support with fallback demo data ===
# Project: NoteShelf
def load_data():
    """Load notes from file or return demo data if file is missing."""
    try:
        with open("notes.json", "r") as f:
            return json.load(f)
    except Exception:
        return [
            {"id": 1, "title": "Welcome", "content": "This is a demo note.", "folder": "General", "pinned": True, "tags": ["intro"], "created": "2024-01-01"},
            {"id": 2, "title": "Shopping List", "content": "Milk, Eggs, Bread", "folder": "Personal", "pinned": False, "tags": ["daily"], "created": "2024-01-02"},
            {"id": 3, "title": "Meeting Notes", "content": "Discuss project timeline", "folder": "Work", "pinned": True, "tags": ["work", "meeting"], "created": "2024-01-03"}
        ]
