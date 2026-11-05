# === Stage 67: Add a function that returns key project metrics ===
# Project: NoteShelf
def get_project_metrics(notes, folders=None):
    folders = folders or []
    total = len(notes)
    pinned = sum(1 for n in notes if n.get("pinned"))
    tagged = sum(1 for n in notes if n.get("tags"))
    with_tags = sum(1 for n in notes if n.get("tags"))
    folder_notes = sum(1 for f in folders for n in notes if n.get("folder") == f)
    return {
        "total_notes": total,
        "pinned_notes": pinned,
        "notes_with_tags": with_tags,
        "total_tags": tagged,
        "folders": len(folders),
        "notes_in_folders": folder_notes,
    }
