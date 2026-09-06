# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: NoteShelf
def format_note(n, max_title=40):
    title = (n["title"] or "")[:max_title].ljust(max_title)
    body = (n.get("body") or "")[:100].replace("\n", " ")
    return f"[{title}]\n  {body}"

def format_note_list(notes, max_show=6):
    lines = []
    for i, n in enumerate(notes[:max_show]):
        lines.append(f"  {i+1:2d}. {n['title'] or '(untitled)'}")
    if len(notes) > max_show:
        lines.append(f"  ... and {len(notes)-max_show} more")
    return "\n".join(lines)

def format_note_detail(n, max_body=500):
    body = (n.get("body") or "")[:max_body].replace("\n", " ")
    return f"Title: {n['title']}\nBody: {body}"

def format_folder(f):
    return f"Folder: {f['name']} (notes: {len(f.get('notes', []))})"

def format_tag(t):
    return f"Tag: {t['name']} (notes: {len(t.get('notes', []))})"
