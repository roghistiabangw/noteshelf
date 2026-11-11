# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: NoteShelf
def _load_notes(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)


def _find_note(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None


def _add_note(notes, note_id):
    notes.append({"id": note_id})
    return notes[-1]


def _remove_note(notes, note_id):
    return [n for n in notes if n["id"] != note_id]


def _is_pinned(notes, note_id):
    return any(n["id"] == note_id and n.get("pinned", False) for n in notes)


def _set_pinned(notes, note_id, pinned):
    for note in notes:
        if note["id"] == note_id:
            note["pinned"] = pinned
            return notes
    return notes


def _add_tag(notes, note_id, tag):
    for note in notes:
        if note["id"] == note_id:
            tags = note.get("tags", [])
            if tag not in tags:
                tags.append(tag)
            note["tags"] = tags
            return notes
    return notes
