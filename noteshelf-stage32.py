# === Stage 32: Add pagination helpers for long console output ===
# Project: NoteShelf
def paginate(lines, page_size=10):
    """Yield chunks of lines for long console output."""
    for start in range(0, len(lines), page_size):
        end = min(start + page_size, len(lines))
        chunk = '\n'.join(lines[start:end])
        print(chunk)
        if start + page_size >= len(lines):
            break
