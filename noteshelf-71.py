# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: NoteShelf
def seed_demo_data(path):
    folders = {
        "Personal": ["notes/personal.json"],
        "Work": ["notes/work.json"],
        "Ideas": ["notes/ideas.json"],
    }
    tags = ["important", "todo", "project", "finance", "health", "random"]
    titles = [
        "Grocery list", "Meeting notes", "App idea", "Budget plan",
        "Workout routine", "Book recommendations", "Travel plans", "Todo",
    ]
    bodies = [
        "Milk, eggs, bread, coffee, avocados.",
        "Discussed roadmap and next sprint priorities.",
        "A simple task tracker with a local database.",
        "Track expenses monthly and review weekly.",
        "Three sets of push-ups, squats, and planks.",
        "Atomic Habits, Deep Work, The Pragmatic Programmer.",
        "Visit family in spring, book a cabin for summer.",
        "Finish the demo data helper and ship it.",
    ]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pinned = {}
    for folder, files in folders.items():
        records = []
        for i, title in enumerate(titles):
            tag = tags[(i * 3) % len(tags)]
            records.append({
                "id": f"{folder}-{i:03d}",
                "title": title,
                "body": bodies[i],
                "folder": folder,
                "tags": [tag],
                "pinned": i < 2,
                "created_at": 1700000000 + i * 3600,
            })
        with open(files, "w", encoding="utf-8") as fh:
            json.dump({"folders": [folder], "tags": [tag], "notes": records}, fh, indent=2)
    return folders
