# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: NoteShelf
def colorize(text, color):
    codes = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'bold': '\033[1m',
        'reset': '\033[0m',
    }
    code = codes.get(color, '')
    return f"{code}{text}{codes['reset']}" if code else text

def print_colored_notes(notes):
    if not notes:
        print(colorize("No notes found", "red"))
        return
    for note in notes:
        print(colorize(note['title'], 'bold'))
        if 'folder' in note:
            print(colorize(f"  Folder: {note['folder']}", 'cyan'))
        if 'pinned':
            print(colorize("  Pinned: Yes", 'yellow'))
        if 'tags':
            print(colorize(f"  Tags: {', '.join(note['tags'])}", 'magenta'))
        print(colorize(f"  {note['body']}", 'white'))
        print()
