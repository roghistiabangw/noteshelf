# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: NoteShelf
def build_changelog(entries):
    if not entries:
        return "No activity recorded yet."

    entries = sorted(entries, key=lambda e: e["ts"], reverse=True)

    lines = ["Changelog", "=" * 40]
    for e in entries:
        date = e["ts"][:10]
        kind = e["action"]
        text = e["text"]
        lines.append(f"- [{date}] {kind}: {text}")

    return "\n".join(lines)
