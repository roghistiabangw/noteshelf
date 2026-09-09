# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: NoteShelf
import re

# Simple command dispatcher for text commands
COMMANDS = {
    "help": lambda: print("Available commands: help, list, add, pin, tag, search, quit"),
    "list": lambda: print("Listing notes..."),
    "add": lambda: print("Add command: add <title> <content>"),
    "pin": lambda: print("Pin command: pin <title>"),
    "tag": lambda: print("Tag command: tag <title> <tag>"),
    "search": lambda: print("Search command: search <query>"),
    "quit": lambda: print("Exiting..."),
}

def dispatch(command):
    cmd = command.strip().lower()
    if cmd in COMMANDS:
        COMMANDS[cmd]()
    else:
        print(f"Unknown command: {command}")
