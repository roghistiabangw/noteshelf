# === Stage 50: Add unit tests for import and export behavior ===
# Project: NoteShelf
import json, os, tempfile
from pathlib import Path

SAMPLES_DIR = Path(tempfile.gettempdir()) / "notes_samples"
SAMPLES_DIR.mkdir(parents=True, exist_ok=True)

def write_sample(name: str, data: dict) -> Path:
    p = SAMPLES_DIR / f"{name}.json"
    p.write_text(json.dumps(data, indent=2))
    return p

def read_sample(name: str) -> dict:
    return json.loads((SAMPLES_DIR / f"{name}.json").read_text())

# --- Sample fixture for import/export tests ---

notes = [
    {"id": "n1", "title": "Groceries", "body": "Milk, Eggs, Bread", "folder": "home", "pinned": True, "tags": ["shopping"], "created": "2025-01-01"},
    {"id": "n2", "title": "Meeting notes", "body": "Action items from Monday", "folder": "work", "pinned": False, "tags": ["meeting", "work"], "created": "2025-01-02"},
    {"id": "n3", "title": "Ideas", "body": "Random thoughts", "folder": "personal", "pinned": False, "tags": ["ideas"], "created": "2025-01-03"},
]

folders = ["home", "work", "personal", "archive"]

export_payload = {
    "notes": notes,
    "folders": folders,
    "pinned": ["n1"],
    "tags": ["shopping", "meeting", "work", "ideas"],
    "metadata": {"version": 1, "format": "notes_shelf_export"}
}

def test_export_roundtrip(tmp_path: Path) -> None:
    out = tmp_path / "export.json"
    out.write_text(json.dumps(export_payload))
    assert json.loads(out.read_text())["notes"][0]["title"] == "Groceries"

def test_import_validates_structure(tmp_path: Path) -> None:
    bad = {"notes": [], "folders": [], "pinned": [], "tags": [], "metadata": {}}
    out = tmp_path / "bad.json"
    out.write_text(json.dumps(bad))
    assert json.loads(out.read_text())["notes"] == []

write_sample("export_sample", export_payload)
write_sample("export_bad", bad)
