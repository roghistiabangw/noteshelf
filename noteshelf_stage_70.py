# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: NoteShelf
def clear_state(confirm_required=True):
    if confirm_required:
        ans = input("Are you sure you want to clear all notes? (y/N): ")
        if ans.strip().lower() != "y":
            print("Clear cancelled.")
            return
    for folder in folders:
        folder.notes = []
        folder.pinned = []
        for note in folder.notes:
            note.tags = []
    all_notes.clear()
    pinned_notes.clear()
    tag_index.clear()
    print("NoteShelf cleared.")
