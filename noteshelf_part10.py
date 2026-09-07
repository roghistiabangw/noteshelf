# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: NoteShelf
def search_notes(query: str, notes: list, fields: list = None) -> list:
    """Case-insensitive search across specified note fields."""
    if fields is None:
        fields = ['title', 'content', 'tags']
    query_lower = query.lower().strip()
    results = []
    for note in notes:
        for field in fields:
            if field in note and query_lower in str(note[field]).lower():
                results.append(note)
                break
    return results
