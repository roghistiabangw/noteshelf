# === Stage 13: Add file save support using a configurable path ===
# Project: NoteShelf
import os

SAVE_PATH = os.environ.get("NOTESHelf_SAVE_PATH", "./notes")

def ensure_save_dir():
    os.makedirs(SAVE_PATH, exist_ok=True)
    return SAVE_PATH
