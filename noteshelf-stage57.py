# === Stage 57: Add structured result objects for command handlers ===
# Project: NoteShelf
class NoteResult:
    def __init__(self, note, metadata=None):
        self.note = note
        self.metadata = metadata or {}
    
    def to_dict(self):
        d = {
            "id": self.note.id,
            "title": self.note.title,
            "content": self.note.content,
            "folder": self.note.folder,
            "pinned": self.note.pinned,
            "tags": self.note.tags,
            "created": self.note.created,
        }
        if self.metadata:
            d.update(self.metadata)
        return d

class FolderResult:
    def __init__(self, folder, notes=None):
        self.folder = folder
        self.notes = notes or []
    
    def to_dict(self):
        return {
            "name": self.folder.name,
            "path": self.folder.path,
            "note_count": len(self.notes),
            "notes": [n.to_dict() for n in self.notes],
        }

class SearchResult:
    def __init__(self, notes, query, metadata=None):
        self.notes = notes
        self.query = query
        self.metadata = metadata or {"query": query, "total": len(notes)}
    
    def to_dict(self):
        return {
            "query": self.query,
            "total_results": len(self.notes),
            "results": [n.to_dict() for n in self.notes],
        }

class PinnedResult:
    def __init__(self, notes):
        self.notes = notes
    
    def to_dict(self):
        return {
            "pinned_count": len(self.notes),
            "notes": [n.to_dict() for n in self.notes],
        }
