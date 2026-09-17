# === Stage 38: Add data integrity checks for broken references ===
# Project: NoteShelf
def check_integrity(notes_dir, folders_dir):
    """Validate that all note and folder references are intact."""
    errors = []
    for note_path in pathlib.Path(notes_dir).glob("*"):
        if not note_path.is_file():
            errors.append(f"Missing note file: {note_path}")
            continue
        try:
            with open(note_path, "r", encoding="utf-8") as f:
                content = f.read()
            if "title:" not in content:
                errors.append(f"Note {note_path} missing title:")
            if "content:" not in content:
                errors.append(f"Note {note_path} missing content:")
        except Exception as e:
            errors.append(f"Cannot read {note_path}: {e}")
    for folder_path in pathlib.Path(folders_dir).glob("*"):
        if not folder_path.is_dir():
            errors.append(f"Broken folder reference: {folder_path}")
    return errors
