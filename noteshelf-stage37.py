# === Stage 37: Add recommendations for the next useful action ===
# Project: NoteShelf
def suggest_next_note():
    """Recommend creating a new note based on recent activity patterns."""
    recent = get_recent_notes(limit=5)
    if not recent:
        print("Tip: Create your first note to get started!")
        return
    tags = [n.get("tags", []) for n in recent]
    all_tags = set()
    for t in tags:
        all_tags.update(t)
    common = [t for t in all_tags if all_tags.count(t) >= 2]
    if common:
        print(f"Tip: Consider using tag '{common[0]}' for new notes to group related ideas.")
    else:
        print("Tip: Start categorizing notes with tags to find them faster later.")
