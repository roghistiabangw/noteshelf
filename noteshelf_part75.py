# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: NoteShelf
def build_validation_report(notes):
    warnings = []
    errors = []
    for idx, note in enumerate(notes):
        if not note.get("title"):
            errors.append(f"note[{idx}]: missing title")
        if not isinstance(note.get("body"), str):
            errors.append(f"note[{idx}]: body must be a string")
        for key in ("folder", "tags", "pinned"):
            value = note.get(key)
            if value is not None and not isinstance(value, list):
                warnings.append(f"note[{idx}]: '{key}' should be a list")
        tags = note.get("tags") or []
        if len(tags) > 50:
            warnings.append(f"note[{idx}]: too many tags ({len(tags)})")
        if note.get("pinned") and not note.get("title"):
            warnings.append(f"note[{idx}]: pinned note has no title")
        if note.get("created_at") and not isinstance(note["created_at"], (int, float)):
            warnings.append(f"note[{idx}]: created_at must be numeric")
    report = {"warnings": warnings, "errors": errors}
    print(f"validation: {len(errors)} error(s), {len(warnings)} warning(s)")
    return report
