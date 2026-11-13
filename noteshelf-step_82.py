# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: NoteShelf
def demo_note_shelf():
    from note_shelf import NoteShelf
    shelf = NoteShelf()
    shelf.create_folder("work")
    shelf.create_folder("personal")
    shelf.add_note("work", "Meeting notes", "urgent")
    shelf.add_note("work", "Project plan", "planning")
    shelf.add_note("personal", "Grocery list", "shopping")
    shelf.pin_note("work", "Meeting notes")
    shelf.tag_note("work", "Meeting notes", "retro")
    print("=== NoteShelf Demo ===")
    print("Folders:", sorted(shelf.list_folders()))
    print("Pinned notes:", [n.title for n in shelf.list_pinned()])
    print("Search 'meeting':", [n.title for n in shelf.search("meeting")])
    print("Tag 'retro':", [n.title for n in shelf.notes_by_tag("retro")])
    print("Folder 'work':", [n.title for n in shelf.notes_in_folder("work")])
    shelf.delete_note("personal", "Grocery list")
    print("After delete Folders:", sorted(shelf.list_folders()))
    print("Done.")
