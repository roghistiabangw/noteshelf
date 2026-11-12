# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: NoteShelf
def present_note(title, body, folder="General", pinned=False, tags=()):
    folder = folder or "General"
    tag_line = ", ".join(tags) if tags else ""
    header = title if title else "(untitled)"
    pin = "Pinned" if pinned else "Not pinned"
    print("Note:     ", header)
    print("Folder:   ", folder)
    print("Status:   ", pin)
    if tag_line:
        print("Tags:     ", tag_line)
    print("Body:     ", body if body else "(empty)")
    print("-" * 40)


def show_search_results(query, notes):
    if not query:
        print("No search query provided.")
        return
    match = lambda note: query.lower() in note["title"].lower() or query.lower() in note["body"].lower()
    found = [note for note in notes if match(note)]
    if not found:
        print(f"No notes match '{query}'.")
        return
    print(f"Found {len(found)} note(s) matching '{query}':")
    for note in found:
        present_note(note["title"], note["body"], note["folder"], note.get("pinned", False), note.get("tags", []))


def show_folder(folder, notes):
    if not folder:
        print("Please choose a folder to view.")
        return
    items = [note for note in notes if note["folder"] == folder]
    if not items:
        print(f"The folder '{folder}' is empty.")
        return
    print(f"Notes in folder '{folder}':")
    for note in items:
        present_note(note["title"], note["body"], note["folder"], note.get("pinned", False), note.get("tags", []))


def confirm(title, message, default=False):
    suffix = " (Y/n)?" if default else " (y/N)?"
    choice = input(message + suffix).strip().lower()
    if choice in ("", "y", "yes"):
        return True
    if choice in ("n", "no"):
        return False
    print("Please answer yes or no.")
    return default
