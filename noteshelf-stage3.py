# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: NoteShelf
import re

def validate_id(value):
    if not value or not re.match(r'^[a-zA-Z0-9_-]+$', value):
        raise ValueError("Invalid identifier format.")
    return value

def validate_short_text(value, max_length=200):
    if not value:
        raise ValueError("Text cannot be empty.")
    if len(value) > max_length:
        raise ValueError(f"Text exceeds {max_length} characters.")
    return value.strip()

def validate_required(value, field_name="Field"):
    if not value:
        raise ValueError(f"{field_name} is required.")
    return value
