# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: NoteShelf
import unittest
from note_shelf import NoteShelf, Note

class TestNoteShelfUpdateDelete(unittest.TestCase):
    def setUp(self):
        self.nsf = NoteShelf()

    def test_update_title(self):
        n = self.nsf.add("Original", "Body", "folder1")
        self.assertEqual(n.title, "Original")
        n.update("Updated", "Body")
        self.assertEqual(n.title, "Updated")
        self.assertEqual(n.body, "Body")

    def test_update_preserves_id(self):
        n = self.nsf.add("A", "B", "f")
        pid = n.id
        n.update("C", "D")
        self.assertEqual(n.id, pid)

    def test_delete_existing(self):
        n = self.nsf.add("X", "Y", "f")
        self.assertIn(n.id, self.nsf.notes)
        n.delete()
        self.assertNotIn(n.id, self.nsf.notes)

    def test_delete_nonexistent(self):
        self.nsf.add("X", "Y", "f")
        fake = Note("fake_id", "fake_body", "f")
        with self.assertRaises(ValueError):
            fake.delete()

    def test_update_nonexistent(self):
        fake = Note("fake_id", "fake_body", "f")
        with self.assertRaises(ValueError):
            fake.update("new", "body")

    def test_delete_pinned(self):
        n = self.nsf.add("Pinned", "Body", "f")
        n.pin()
        self.assertTrue(n.pinned)
        n.delete()
        self.assertFalse(n.pinned)
        self.assertNotIn(n.id, self.nsf.notes)

    def test_update_clears_tag(self):
        n = self.nsf.add("T", "Body", "f", tags=["urgent"])
        n.update("T", "Body", tags=[])
        self.assertNotIn("urgent", n.tags)

    def test_delete_removes_tag(self):
        n = self.nsf.add("T", "Body", "f", tags=["urgent"])
        n.delete()
        self.assertNotIn("urgent", self.nsf._tags)
