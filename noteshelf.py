# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: NoteShelf
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
NOTES_FILE = PROJECT_ROOT / "notes.json"


def load_notes():
    if NOTES_FILE.exists():
        return json.loads(NOTES_FILE.read_text())
    return []


def save_notes(notes):
    NOTES_FILE.write_text(json.dumps(notes, indent=2))


def new_note(title: str, body: str = "") -> dict:
    return {"id": len(load_notes()) + 1, "title": title, "body": body, "pinned": False, "tags": [], "folders": [], "created": _utc_now()}


def _utc_now() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).isoformat()
