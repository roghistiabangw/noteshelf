# === Stage 55: Add a setting to disable colorized output ===
# Project: NoteShelf
import argparse


def add_no_color(args):
    """Disable colorized output when --no-color is passed."""
    parser = argparse.ArgumentParser(description="NoteShelf CLI")
    parser.add_argument("--no-color", action="store_true",
                        help="Disable colored terminal output")
    return parser.parse_args()
