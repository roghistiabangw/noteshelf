# === Stage 43: Add CSV import for the primary record type ===
# Project: NoteShelf
def import_csv(filepath, sep=",", encoding="utf-8-sig"):
    """Import notes from a CSV file.
    Expected columns (any order): title, content, created, tags, folder, pinned, priority.
    Returns (count, error_message) tuple.
    """
    try:
        with open(filepath, encoding=encoding, newline="") as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                title = (row.get("title") or "").strip()
                if not title:
                    continue
                tags_str = (row.get("tags") or "").strip()
                tags = [t.strip() for t in tags_str.split(",") if t.strip()] if tags_str else []
                folder = (row.get("folder") or "").strip()
                pinned = row.get("pinned", "").strip().lower() in ("true", "1", "yes")
                priority = int(row.get("priority", 0))
                record = NoteRecord(
                    title=title,
                    content=(row.get("content") or "").strip(),
                    created=(row.get("created") or datetime.now()).isoformat(),
                    tags=tags,
                    folder=folder,
                    pinned=pinned,
                    priority=priority,
                )
                NoteShelf.add_record(record)
                count += 1
        return count, None
    except Exception as e:
        return 0, str(e)
