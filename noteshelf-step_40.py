# === Stage 40: Add plain text report export ===
# Project: NoteShelf
def export_to_text(self):
    lines = []
    lines.append(f"# NoteShelf Report — {self._display_name}")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Total notes: {len(self.notes)}")
    lines.append("")
    for note in sorted(self.notes, key=lambda n: (n.pinned, -n._created)):
        lines.append(f"## {note.title}")
        lines.append(f"> {note._created.strftime('%Y-%m-%d %H:%M')}")
        if note.tags:
            lines.append(f"Tags: {', '.join(note.tags)}")
        if note.folder:
            lines.append(f"Folder: {note.folder}")
        lines.append(f"Content: {note.content}")
        lines.append("")
    return "\n".join(lines)
