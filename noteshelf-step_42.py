# === Stage 42: Add CSV export without external dependencies ===
# Project: NoteShelf
def export_to_csv(self):
    import csv
    import os
    if not self.notes:
        return
    file_name = input("Enter filename for CSV export: ").strip()
    if not file_name:
        file_name = "notes_export.csv"
    file_path = os.path.join(self.notes_dir, file_name)
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "content", "created", "modified", "pinned", "tags"])
        for note in self.notes:
            writer.writerow([
                note["id"],
                note["title"],
                note["content"],
                note["created"],
                note["modified"],
                "Yes" if note["pinned"] else "No",
                ", ".join(note["tags"]) if note["tags"] else "",
            ])
    print(f"Notes exported to {file_path}")
