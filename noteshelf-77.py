# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: NoteShelf
def get_note_by_id(notes: list, note_id: str) -> dict | None:
    for note in notes:
        if note["id"] == note_id:
            return note
    return None


def get_notes_by_tag(notes: list, tag: str) -> list:
    return [note for note in notes if tag in note.get("tags", [])]


def get_pinned_notes(notes: list) -> list:
    return [note for note in notes if note.get("pinned", False)]


def find_note_by_search(notes: list, query: str) -> list:
    query = query.lower()
    results = []
    for note in notes:
        if query in note.get("title", "").lower():
            results.append(note)
        if query in note.get("content", "").lower():
            results.append(note)
        for tag in note.get("tags", []):
            if query in tag.lower():
                results.append(note)
                break
    return results


def get_note_in_folder(notes: list, folder_id: str) -> list:
    return [note for note in notes if note.get("folder_id") == folder_id]


def count_notes_in_folder(notes: list, folder_id: str) -> int:
    return len(get_note_in_folder(notes, folder_id))


def count_notes_by_tag(notes: list, tag: str) -> int:
    return len(get_notes_by_tag(notes, tag))


def count_pinned_notes(notes: list) -> int:
    return len(get_pinned_notes(notes))


def search_notes_in_folder(notes: list, folder_id: str, query: str) -> list:
    return find_note_by_search(get_note_in_folder(notes, folder_id), query)
