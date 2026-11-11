# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: NoteShelf
import os, json, datetime

BASE = "noteshelf"
os.makedirs(BASE, exist_ok=True)
os.makedirs(os.path.join(BASE, "folders"), exist_ok=True)
os.makedirs(os.path.join(BASE, "notes"), exist_ok=True)

NOTES = os.path.join(BASE, "notes", "notes.json")
FOLDERS = os.path.join(BASE, "folders", "folders.json")


def load(path, default):
    if os.path.exists(path):
        try:
            return json.load(open(path))
        except Exception:
            return default
    return default


def save(path, data):
    json.dump(data, open(path, "w"), indent=2)


folders = load(FOLDERS, {"default": {"name": "default", "notes": []}})
notes = load(NOTES, {})
pinned = load(os.path.join(BASE, "pinned.json"), [])
tags = load(os.path.join(BASE, "tags.json"), {})


def add_note(title, body, folder="default", tags=None):
    note_id = str(datetime.datetime.now().timestamp())
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "folder": folder,
        "tags": tags or [],
        "pinned": False,
        "created": datetime.datetime.now().isoformat(),
    }
    notes[note_id] = note
    folder_obj = next((f for f in folders if f["name"] == folder), folders[0])
    if note_id not in folder_obj["notes"]:
        folder_obj["notes"].append(note_id)
    if tags:
        for t in tags:
            tags.setdefault(t, []).append(note_id)
    save(NOTES, notes)
    save(FOLDERS, folders)
    save(os.path.join(BASE, "pinned.json"), pinned)
    save(os.path.join(BASE, "tags.json"), tags)
    return note


def search(term):
    return [n for n in notes.values() if term in n["title"] or term in n["body"]]


def demo():
    n1 = add_note("Groceries", "milk, eggs, bread", folder="home", tags=["shopping"])
    n2 = add_note("Meeting notes", "discuss roadmap", folder="work", tags=["meta"])
    add_note("Pinned idea", "build NoteShelf", folder="default", tags=["project"])
    pinned.append(n2["id"])
    save(os.path.join(BASE, "pinned.json"), pinned)
    results = search("roadmap")
    print("search roadmap:", [r["title"] for r in results])


demo()
