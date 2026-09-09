# === Stage 16: Add argparse support for the most common commands ===
# Project: NoteShelf
import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="NoteShelf - Personal Note Manager")
    sub = parser.add_subparsers(dest="command", required=True)
    
    add = sub.add_parser("add", help="Add a new note")
    add.add_argument("title", help="Note title")
    add.add_argument("content", help="Note content")
    add.add_argument("-p", "--pin", action="store_true", help="Pin the note")
    add.add_argument("-t", "--tag", help="Add a tag")
    
    show = sub.add_parser("show", help="Show a note by ID")
    show.add_argument("note_id", help="Note ID to display")
    
    list_ = sub.add_parser("list", help="List notes with optional filters")
    list_.add_argument("-f", "--folder", help="Filter by folder")
    list_.add_argument("-p", "--pinned", action="store_true", help="Show only pinned notes")
    list_.add_argument("-t", "--tag", help="Filter by tag")
    
    search = sub.add_parser("search", help="Quick search across all notes")
    search.add_argument("query", help="Search string")
    
    return parser
