# === Stage 64: Add validation for relationship references ===
# Project: NoteShelf
def validate_references(self, notes, folders=None, tags=None):
    folder_ids = set(f["id"] for f in (folders or []))
    tag_ids = set(t["id"] for t in (tags or []))
    invalid = []
    for note in notes:
        if note.get("folder_id") is not None and note["folder_id"] not in folder_ids:
            invalid.append(note["id"])
        for tag in note.get("tags", []):
            if tag not in tag_ids:
                invalid.append(tag)
    return invalid
