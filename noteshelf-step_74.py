# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: NoteShelf
def snapshot_diff(before, after, key="note"):
    """Compare two states of notes and report additions, deletions, changes."""
    b = {n[key]: n for n in before}
    a = {n[key]: n for n in after}
    added = [n for n in after if n[key] not in b]
    removed = [n for n in before if n[key] not in a]
    changed = []
    for k in b:
        if k in a and b[k] != a[k]:
            changed.append({"key": k, "old": b[k], "new": a[k]})
    return {"added": added, "removed": removed, "changed": changed}
