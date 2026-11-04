# === Stage 63: Add relationships between records where useful ===
# Project: NoteShelf
def build_relationships(notes):
    tags = {}
    for n in notes:
        for t in n.get("tags", []):
            tags.setdefault(t, []).append(n["id"])
    folder_notes = {}
    for n in notes:
        folder_notes.setdefault(n.get("folder_id"), []).append(n["id"])
    pinned = [n["id"] for n in notes if n.get("pinned")]
    for n in notes:
        n.setdefault("related", {})
        n["related"]["tags"] = tags.get(n.get("tag"), [])
        n["related"]["folder"] = folder_notes.get(n.get("folder_id"), [])
        n["related"]["pinned_count"] = len(pinned)
    return tags, folder_notes, pinned
