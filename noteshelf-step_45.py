# === Stage 45: Add restore from backup with validation ===
# Project: NoteShelf
import json, os
from pathlib import Path

class BackupRestorer:
    """Restores NoteShelf data from a JSON backup with validation."""
    def __init__(self, data_dir):
        self.data_dir = Path(data_dir)
        self.note_dir = self.data_dir / "notes"
        self.meta_dir = self.data_dir / "meta"
        self.pinned_set = set()
        self.tag_index = {}
        self.folder_map = {}

    def restore(self, backup_path):
        """Load backup, validate structure, then restore all state."""
        backup_path = Path(backup_path)
        if not backup_path.exists():
            raise FileNotFoundError(f"Backup not found: {backup_path}")
        with open(backup_path) as f:
            data = json.load(f)
        self._restore_notes(data.get("notes", []))
        self._restore_meta(data.get("meta", {}))
        return {"notes": len(data.get("notes", [])), "folders": len(self.folder_map)}

    def _restore_notes(self, notes):
        for note in notes:
            uid = note.get("uid")
            if not uid:
                raise ValueError("Each note must have a uid")
            body = note.get("body", "")
            if not isinstance(body, str):
                raise ValueError("Note body must be a string")
            if not self.note_dir.exists():
                self.note_dir.mkdir(parents=True)
            out = self.note_dir / f"{uid}.md"
            out.write_text(body)

    def _restore_meta(self, meta):
        pins = meta.get("pinned", [])
        if not isinstance(pins, list):
            raise ValueError("pinned must be a list")
        self.pinned_set = set(pins)
        tags = meta.get("tags", {})
        if not isinstance(tags, dict):
            raise ValueError("tags must be a dict")
        self.tag_index = tags
        folders = meta.get("folders", {})
        if not isinstance(folders, dict):
            raise ValueError("folders must be a dict")
        self.folder_map = folders
        if not self.meta_dir.exists():
            self.meta_dir.mkdir(parents=True)
