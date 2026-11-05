# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: NoteShelf
def reset_demo_data(db, reset_id=1):
    if "notes" in db:
        db.execute("DELETE FROM notes WHERE 1=1")
    if "folders" in db:
        db.execute("DELETE FROM folders WHERE 1=1")
    if "tags" in db:
        db.execute("DELETE FROM tags WHERE 1=1")
    if "note_tags" in db:
        db.execute("DELETE FROM note_tags WHERE 1=1")
    if "note_folders" in db:
        db.execute("DELETE FROM note_folders WHERE 1=1")
    if "pinned" in db:
        db.execute("DELETE FROM pinned WHERE 1=1")

    db.execute("INSERT INTO folders (name) VALUES (?)", ("Work",))
    db.execute("INSERT INTO folders (name) VALUES (?)", ("Personal",))
    db.execute("INSERT INTO folders (name) VALUES (?)", ("Archive",))

    db.execute("INSERT INTO tags (name) VALUES (?)", ("todo",))
    db.execute("INSERT INTO tags (name) VALUES (?)", ("urgent",))
    db.execute("INSERT INTO tags (name) VALUES (?)", ("idea",))

    db.execute("INSERT INTO notes (title, body, folder_id, tag_ids, pinned) VALUES (?, ?, ?, ?, ?)",
               ("Welcome to NoteShelf", "This is a demo note.", 1, "1", 1))
    db.execute("INSERT INTO notes (title, body, folder_id, tag_ids, pinned) VALUES (?, ?, ?, ?, ?)",
               ("Groceries", "Milk, eggs, bread.", 2, "3", 0))
    db.execute("INSERT INTO notes (title, body, folder_id, tag_ids, pinned) VALUES (?, ?, ?, ?, ?)",
               ("Project Plan", "Phase 1: research. Phase 2: build.", 1, "1", 0))

    db.execute("INSERT INTO pinned (note_id) VALUES (1)")
    db.execute("INSERT INTO pinned (note_id) VALUES (2)")

    db.commit()
