# === Stage 18: Add an activity log with timestamps and action names ===
# Project: NoteShelf
import time

class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, note_id=None, user=None):
        entry = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "note_id": note_id,
            "user": user,
        }
        self.entries.append(entry)
        print(f"[{entry['timestamp']}] {entry['action']}", end="")
        if note_id is not None:
            print(f" note_id={note_id}", end="")
        if user is not None:
            print(f" user={user}", end="")
        print()

    def get_log(self):
        return self.entries

    def clear_log(self):
        self.entries.clear()
