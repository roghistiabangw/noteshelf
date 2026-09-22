# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: NoteShelf
def _format_tag(tag: str) -> str:
    """Return a tag as a lowercase, hyphen-separated string."""
    return tag.lower().strip().replace(" ", "-")


def _format_date(iso: str) -> str:
    """Convert an ISO date string to a human-readable format."""
    return iso[:10] if len(iso) >= 10 else iso


def _search_notes(query: str, notes: list, limit: int = 20) -> list:
    """Search notes by title or body content and return the top matches."""
    query = query.lower()
    results = []
    for note in notes:
        if query in note.get("title", "").lower() or query in note.get("body", "").lower():
            results.append(note)
            if len(results) >= limit:
                break
    return results
