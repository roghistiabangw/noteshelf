# === Stage 51: Add unit tests for search and filter behavior ===
# Project: NoteShelf
import unittest
from NoteShelf import NoteShelf
from NoteShelf.note import Note

class TestSearchFilter(unittest.TestCase):
    def setUp(self):
        self.ns = NoteShelf()
        self.ns.add_note(Note("Pinned! Important", "pinned", "important"))
        self.ns.add_note(Note("A note about Python", "python", "python"))
        self.ns.add_note(Note("A note about Java", "java", "java"))
        self.ns.add_note(Note("A note about C++", "cpp", "cpp"))

    def test_search_by_title(self):
        notes = self.ns.search(title="Python")
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].title, "A note about Python")

    def test_search_by_tag(self):
        notes = self.ns.search(tag="java")
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].tag, "java")

    def test_search_by_folder(self):
        notes = self.ns.search(folder="python")
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].title, "A note about Python")

    def test_search_empty(self):
        notes = self.ns.search(title="Nonexistent")
        self.assertEqual(len(notes), 0)

    def test_search_multiple_matches(self):
        notes = self.ns.search()
        self.assertEqual(len(notes), 4)

if __name__ == "__main__":
    unittest.main()
