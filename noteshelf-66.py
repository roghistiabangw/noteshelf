# === Stage 66: Add export of a short status dashboard ===
# Project: NoteShelf
def export_status_dashboard(path, notes, folders):
    total = len(notes)
    pinned = sum(1 for n in notes if n.get("pinned"))
    tagged = sum(1 for n in notes if n.get("tags"))
    folder_count = len(folders)
    lines = []
    lines.append("NoteShelf Status Dashboard")
    lines.append("=" * 30)
    lines.append(f"Total notes:      {total}")
    lines.append(f"Pinned notes:     {pinned}")
    lines.append(f"Folder count:     {folder_count}")
    lines.append(f"Tagged notes:     {tagged}")
    lines.append(f"Unpinned notes:   {total - pinned}")
    lines.append(f"Not tagged:       {total - tagged}")
    lines.append("=" * 30)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return path
