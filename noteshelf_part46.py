# === Stage 46: Add a schema version field and migration helper ===
# Project: NoteShelf
SCHEMA_VERSION = 2


def migrate_notes_db(db_path: str, version_from: int = 1) -> None:
    """Migrate NoteShelf notes database from version_from to SCHEMA_VERSION.
    
    Adds schema_version column and updates existing notes.
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()
    
    if version_from >= SCHEMA_VERSION:
        cur.execute("SELECT 1")
        return
    
    if version_from < 2:
        cur.execute("ALTER TABLE notes ADD COLUMN schema_version INTEGER DEFAULT 2")
        cur.execute("UPDATE notes SET schema_version = 2 WHERE schema_version IS NULL")
    
    conn.commit()
    conn.close()
