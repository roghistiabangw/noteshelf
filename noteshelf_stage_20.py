# === Stage 20: Add duplicate detection for newly created records ===
# Project: NoteShelf
def detect_duplicate(record, existing_ids, existing_tags, existing_titles):
    """Return (is_duplicate, collision_type).
    
    collision_type: 'id', 'tag', 'title' or None.
    """
    # 1. Same primary key → exact duplicate
    if record["id"] in existing_ids:
        return True, "id"
    # 2. Same folder + title → likely duplicate
    if record.get("folder") and record.get("title"):
        for e in existing_ids:
            e_rec = _load_record(e)
            if e_rec.get("folder") == record["folder"] and e_rec.get("title") == record["title"]:
                return True, "title"
    # 3. Same title + any tag overlap → high chance duplicate
    if record.get("title"):
        for t in record.get("tags", []):
            for e in existing_ids:
                e_rec = _load_record(e)
                if t in e_rec.get("tags", []):
                    return True, "tag"
    return False, None
