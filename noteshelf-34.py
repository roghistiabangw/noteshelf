# === Stage 34: Add support for multiple local user profiles ===
# Project: NoteShelf
import json, os, uuid

class UserProfiles:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.profiles_dir = os.path.join(base_dir, "profiles")
        self._ensure_profiles_dir()

    def _ensure_profiles_dir(self):
        os.makedirs(self.profiles_dir, exist_ok=True)

    def list_profiles(self):
        return [f.replace(".json", "") for f in os.listdir(self.profiles_dir) if f.endswith(".json")]

    def get_profile(self, name):
        path = os.path.join(self.profiles_dir, f"{name}.json")
        if not os.path.exists(path):
            raise FileNotFoundError(f"Profile '{name}' not found")
        with open(path, "r") as f:
            return json.load(f)

    def create_profile(self, name, default_folder=None):
        if name in self.list_profiles():
            raise ValueError(f"Profile '{name}' already exists")
        profile = {
            "name": name,
            "id": uuid.uuid4().hex[:8],
            "default_folder": default_folder or "Inbox",
            "pinned_ids": [],
            "tags": {},
            "notes": {},
        }
        with open(os.path.join(self.profiles_dir, f"{name}.json"), "w") as f:
            json.dump(profile, f, indent=2)
        return profile

    def delete_profile(self, name):
        if len(self.list_profiles()) <= 1:
            raise ValueError("Cannot delete the last profile")
        os.remove(os.path.join(self.profiles_dir, f"{name}.json"))
