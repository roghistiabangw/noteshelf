# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: NoteShelf
def test_create_note():
    note = create_note("Hello World", "2024-01-01", "folder1", "tag1", "tag2")
    assert note["title"] == "Hello World"
    assert note["created"] == "2024-01-01"
    assert note["folder"] == "folder1"
    assert note["tags"] == ["tag1", "tag2"]
    assert note["pinned"] is False

def test_create_note_defaults():
    note = create_note("Quick Note", "2024-01-02")
    assert note["created"] == "2024-01-02"
    assert note["folder"] == "inbox"
    assert note["tags"] == []
    assert note["pinned"] is False

def test_create_note_invalid_date():
    try:
        create_note("Bad Date", "not-a-date", "inbox")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

def test_create_note_empty_title():
    try:
        create_note("", "2024-01-03", "inbox")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

def test_validate_note():
    note = create_note("Test", "2024-01-04")
    assert validate_note(note) is True

def test_validate_note_missing_title():
    note = {"created": "2024-01-05", "folder": "inbox", "tags": [], "pinned": False}
    assert validate_note(note) is False

def test_validate_note_missing_date():
    note = {"title": "Test", "folder": "inbox", "tags": [], "pinned": False}
    assert validate_note(note) is False
