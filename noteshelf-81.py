# === Stage 81: Add final README text as a module string with usage examples ===
# Project: NoteShelf
USAGE = r"""
NoteShelf — a personal note shelf with folders, pinned notes, tags, and quick search.

1. Install (no dependencies):
   python -m pip install -r requirements.txt   # empty on purpose

2. Run the app:
   python notes.py

3. Quick start:
   create a folder       ->   add_folder "Work"
   add a note            ->   add_note(folder="Work", title="Ideas", body="Hello")
   pin a note            ->   pin_note(title="Ideas")
   tag a note            ->   tag_note("Ideas", tags=["brainstorm", "quick"])
   search all notes      ->   search("idea")

4. Explore the modules:
   notes.py        core data model and persistence
   folders.py      folder creation and listing
   pins.py         pinning and unpinning notes
   tags.py         tagging and tag listing
   search.py       quick keyword search

5. Example session:
   >>> from notes import NoteShelf
   >>> shelf = NoteShelf()
   >>> shelf.add_folder("Work")
   >>> shelf.add_note(folder="Work", title="Ideas", body="Hello")
   >>> shelf.pin_note("Ideas")
   >>> shelf.tag_note("Ideas", tags=["brainstorm", "quick"])
   >>> for n in shelf.search("idea"):
   ...     print(n.title)
   Ideas

6. Design notes:
   - every addition is self-contained and dependency-free
   - all state is stored as JSON files under the data/ directory
   - keep new features small, readable, and isolated

Happy note-taking!
"""
