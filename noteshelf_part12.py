# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: NoteShelf
import json

def load_notes(path):
    """Load notes from a JSON file with friendly error handling."""
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Note file not found: {path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Malformed JSON in {path}: {e}")
        return []
    if not isinstance(data, list):
        print("Expected a JSON array of notes")
        return []
    return data
