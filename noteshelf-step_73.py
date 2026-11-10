# === Stage 73: Add a lightweight HTML report export ===
# Project: NoteShelf
def export_html_report(notes, folders):
    folders_html = "".join(
        f"<tr><td>{name}</td><td>{len(notes.get(name, []))}</td></tr>" for name in folders
    )
    rows = []
    for note in notes.values():
        tags = ",".join(note["tags"])
        pinned = "★" if note.get("pinned") else ""
        rows.append(
            f"<tr>"
            f"<td>{pinned}</td>"
            f"<td>{note['title']}</td>"
            f"<td>{note['folder']}</td>"
            f"<td>{tags}</td>"
            f"<td>{note['content']}</td>"
            f"</tr>"
        )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>NoteShelf Report</title>
<style>
body {{ font-family: sans-serif; margin: 2rem; }}
h1 {{ color: #2c3e50; }}
table {{ border-collapse: collapse; width: 100%; margin-top: 1rem; }}
th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
th {{ background: #ecf0f1; }}
p {{ color: #7f8c8d; }}
</style>
</head>
<body>
<h1>NoteShelf Report</h1>
<p>Generated: {__import__("datetime").date.today()}</p>
<h2>Folders</h2>
<table>
<thead><tr><th>Folder</th><th>Notes</th></tr></thead>
<tbody>
{folders_html}
</tbody>
</table>
<h2>Notes</h2>
<table>
<thead><tr><th>Pinned</th><th>Title</th><th>Folder</th><th>Tags</th><th>Content</th></tr></thead>
<tbody>
{"".join(rows)}
</tbody>
</table>
</body>
</html>"""
    with open("notes_report.html", "w", encoding="utf-8") as f:
        f.write(html)
