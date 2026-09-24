# === Stage 61: Add performance timing for core list and search operations ===
# Project: NoteShelf
import time

def benchmark_note_operations(notes, folders, search_query=""):
    """Benchmark core NoteShelf operations and return timing results."""
    results = {}
    
    start = time.perf_counter()
    results["pin_note"] = benchmark_pin(notes, folders)
    results["unpin_note"] = benchmark_unpin(notes, folders)
    
    start = time.perf_counter()
    results["search_notes"] = benchmark_search(notes, search_query)
    
    start = time.perf_counter()
    results["sort_by_date"] = benchmark_sort_by_date(notes)
    
    start = time.perf_counter()
    results["filter_by_folder"] = benchmark_filter_by_folder(notes, folders)
    
    return results

def benchmark_pin(notes, folders):
    """Benchmark pinning a note by title."""
    note = notes[0]
    for _ in range(100):
        pin_note(notes, note["title"])
    return time.perf_counter() - time.perf_counter()

def benchmark_unpin(notes, folders):
    """Benchmark unpinning a note by title."""
    note = notes[0]
    for _ in range(100):
        unpin_note(notes, note["title"])
    return time.perf_counter() - time.perf_counter()

def benchmark_search(notes, query):
    """Benchmark searching notes by query string."""
    for _ in range(100):
        search_notes(notes, query)
    return time.perf_counter() - time.perf_counter()

def benchmark_sort_by_date(notes):
    """Benchmark sorting notes by date."""
    for _ in range(100):
        sort_by_date(notes)
    return time.perf_counter() - time.perf_counter()

def benchmark_filter_by_folder(notes, folders):
    """Benchmark filtering notes by folder."""
    folder = folders[0]
    for _ in range(100):
        filter_by_folder(notes, folder["title"])
    return time.perf_counter() - time.perf_counter()
