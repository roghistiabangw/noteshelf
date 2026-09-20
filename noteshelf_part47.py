# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: NoteShelf
import sys
sys.path.insert(0, '.')
from notebook import Notebook

nb = Notebook()

# Add a few notes with different attributes
nb.add_note("Buy milk", tags=["groceries"], folder="home")
nb.add_note("Code review tomorrow", folder="work", is_pinned=True)
nb.add_note("Read Python docs", tags=["learning"], is_pinned=True)
nb.add_note("Throw away", tags=["trash"], folder="trash")

# Pin a trash note to simulate a mistake
nb.pin_note("Throw away")
nb.unpin_note("Code review tomorrow")

# Tag a note
nb.add_tag("urgent", notes=["Buy milk"])

# Verify the workflow
assert nb.count() == 4
assert nb.find_notes(tags=["groceries"]) == ["Buy milk"]
assert nb.find_notes(folder="work") == ["Code review tomorrow"]
assert nb.find_pinned() == ["Code review tomorrow", "Read Python docs"]
assert nb.find_notes(tags=["trash"]) == ["Throw away"]
assert nb.find_notes(tags=["urgent"]) == ["Buy milk"]
print("All assertions passed.")
