# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: NoteShelf
def _dedupe_notes(notes):
    seen = set()
    result = []
    for note in notes:
        key = (note['id'], note['content'], note['folder'], tuple(sorted(note.get('tags', []))))
        if key not in seen:
            seen.add(key)
            result.append(note)
    return result


def _normalize_note(note):
    note = dict(note)
    note.setdefault('folder', None)
    note.setdefault('pinned', False)
    note.setdefault('tags', [])
    if isinstance(note['tags'], str):
        note['tags'] = [t.strip() for t in note['tags'].split(',') if t.strip()]
    note['tags'] = [t.lower() for t in note['tags']]
    note['content'] = note.get('content', '')
    return note


def _sanitize_notes(notes):
    if not isinstance(notes, list):
        return []
    return _dedupe_notes([_normalize_note(n) for n in notes])


def _search_notes(notes, query):
    query = query.lower().strip()
    return [n for n in notes if query in n['content'].lower() or query in n.get('folder', '').lower() or any(query in tag for tag in n.get('tags', []))]


def _export_notes(notes, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)
        f.write('\n')


def _import_notes(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return _sanitize_notes(json.load(f))
