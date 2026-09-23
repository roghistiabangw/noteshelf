# === Stage 56: Add compact error classes for domain failures ===
# Project: NoteShelf
class NoteNotFoundError(Exception):
    pass

class FolderNotFoundError(Exception):
    pass

class DuplicateNoteError(Exception):
    pass

class InvalidNoteError(Exception):
    pass

class DuplicateFolderError(Exception):
    pass

class TagNotFoundError(Exception):
    pass

class PinnedNotesLimitExceeded(Exception):
    pass
