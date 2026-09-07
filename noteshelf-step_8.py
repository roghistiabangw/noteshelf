# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: NoteShelf
def filter_notes(self, notes, status=None, category=None, owner=None, tag=None):
    for n in notes:
        if status is not None and n.get("status") != status:
            continue
        if category is not None and n.get("category") != category:
            continue
        if owner is not None and n.get("owner") != owner:
            continue
        if tag is not None and tag not in n.get("tags", []):
            continue
        yield n
