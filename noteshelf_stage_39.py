# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: NoteShelf
def repair_notes():
    import json, os
    data_file = "notes.json"
    if not os.path.exists(data_file):
        return
    with open(data_file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
    if not isinstance(data, dict):
        data = {}
    if "notes" not in data:
        data["notes"] = []
    if "folders" not in data:
        data["folders"] = []
    if "pinned" not in data:
        data["pinned"] = []
    if "tags" not in data:
        data["tags"] = []
    if "metadata" not in data:
        data["metadata"] = {"version": 1, "created": None, "last_modified": None}
    for note in data["notes"]:
        if not isinstance(note, dict):
            note = {}
        if "id" not in note:
            note["id"] = str(hash(note.get("title", "")) % 10**8)
        if "content" not in note:
            note["content"] = ""
        if "folder" not in note:
            note["folder"] = "default"
        if "tags" not in note:
            note["tags"] = []
        if "pinned" not in note:
            note["pinned"] = False
        if "created" not in note:
            note["created"] = data["metadata"].get("created")
        if "last_modified" not in note:
            note["last_modified"] = data["metadata"].get("last_modified")
    for folder in data["folders"]:
        if not isinstance(folder, dict):
            folder = {}
        if "name" not in folder:
            folder["name"] = "default"
    for tag in data["tags"]:
        if not isinstance(tag, dict):
            tag = {}
        if "name" not in tag:
            tag["name"] = ""
    for tag in data["tags"]:
        tag["count"] = sum(1 for n in data["notes"] if tag["name"] in n.get("tags", []))
    if data["metadata"]["created"] is None:
        data["metadata"]["created"] = data["metadata"].get("last_modified")
    data["metadata"]["last_modified"] = data["metadata"].get("created")
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
