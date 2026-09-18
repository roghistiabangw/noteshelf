# === Stage 41: Add plain text import for a simple line-based format ===
# Project: NoteShelf
def import_plain_text(text, default_tags=None):
    """Import notes from a plain text file format.
    
    Each line is a note. Lines starting with '#' are skipped.
    Notes can be tagged with #tag format.
    """
    notes = []
    for line in text.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        tags = set()
        if default_tags:
            tags.update(default_tags)
        for tag in line.split('#'):
            tag = tag.strip()
            if tag:
                tags.add(tag)
        notes.append(Note(line, tags=tags))
    return notes
