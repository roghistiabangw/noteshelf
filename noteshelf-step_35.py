# === Stage 35: Add active user switching and user-specific records ===
# Project: NoteShelf
import json
from pathlib import Path

USERS_FILE = Path(__file__).parent / "users.json"

def load_users():
    if not USERS_FILE.exists():
        return [{"id": 0, "name": "default"}]
    with open(USERS_FILE) as f:
        data = json.load(f)
    if not data:
        data = [{"id": 0, "name": "default"}]
    return data

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def current_user():
    users = load_users()
    return users[-1]

def switch_user(name):
    users = load_users()
    if users and users[-1]["name"] == name:
        return users[-1]
    users.append({"id": len(users), "name": name})
    save_users(users)
    return users[-1]
