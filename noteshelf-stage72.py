# === Stage 72: Add Markdown report export ===
# Project: NoteShelf
def export_markdown(notes):
    lines = ["# NoteShelf Export", ""]
    lines.append("Total: %d notes" % len(notes))
    lines.append("")
    for note in sorted(notes, key=lambda n: (not n.get("pinned", False), n["title"])):
        lines.append("## %s" % note["title"])
        if note.get("pinned"):
            lines.append("> **Pinned**")
        for tag in note.get("tags", []):
            lines.append("### %s" % tag)
        lines.append("")
        lines.append(note.get("content", ""))
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)
