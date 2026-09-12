# === Stage 24: Add grouped summaries by category or status ===
# Project: NoteShelf
def grouped_summaries(notes):
    categories = {
        "pinned": [],
        "folders": [],
        "tags": [],
        "unsorted": [],
    }
    for n in notes:
        if n.get("pinned", False):
            categories["pinned"].append(n)
        if n.get("folder"):
            categories["folders"].append(n)
        if n.get("tags"):
            categories["tags"].append(n)
        else:
            categories["unsorted"].append(n)
    return categories
