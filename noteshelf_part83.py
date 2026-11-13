# === Stage 83: Add regression tests for the final demo workflow ===
# Project: NoteShelf
def test_demo_workflow_end_to_end():
    from noteshef import Shelf, Note, Folder
    shelf = Shelf()
    folder = Folder("journal")
    shelf.add_folder(folder)
    n1 = Note("buy milk", folder, ["grocery"], pinned=True)
    n2 = Note("read chapter 3", folder, ["study"])
    shelf.add_note(n1)
    shelf.add_note(n2)
    assert len(shelf) == 2
    assert n1.is_pinned and not n2.is_pinned
    assert shelf.search("milk")[0] is n1
    assert shelf.search("chapter")[0] is n2
    assert folder.list_tags() == ["grocery", "study"]
    assert shelf.search("grocery", tag_only=True)[0] is n1
    n1.pin()
    assert shelf.search("pinned")[0] is n1
    assert shelf.search("milk", folder_only="journal")[0] is n1
    assert shelf.search("milk")[0] is None
    assert shelf.search("milk", folder_only="other")[0] is None
    assert shelf.search("milk", tag_only=["study"])[0] is None
    assert shelf.search("milk", tag_only=["grocery"])[0] is n1
    assert shelf.search("milk", tags=["grocery", "study"])[0] is n1
    assert shelf.search("milk", tags=["grocery", "none"])[0] is None
    assert shelf.search("milk")[0] is n1
