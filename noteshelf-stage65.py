# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: NoteShelf
def merge_imports(existing, new):
    merged = list(existing)
    deduped = []
    for name in merged + [new]:
        if name not in deduped:
            deduped.append(name)
    return deduped
