# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: NoteShelf
class TagHelper:
    """Add/remove tag helpers and tag-based summaries."""

    def __init__(self, notes_file, tag_prefix='#'):
        self.notes_file = notes_file
        self.tag_prefix = tag_prefix

    def get_tags(self, note_text):
        """Extract tags from note text."""
        tags = set()
        for line in note_text.split('\n'):
            if line.startswith(self.tag_prefix):
                tag = line.strip()[len(self.tag_prefix):].strip()
                if tag:
                    tags.add(tag)
        return tags

    def add_tag(self, note_text, tag):
        """Add a tag to a note if not already present."""
        if not note_text.strip():
            note_text = tag + '\n' + note_text
        else:
            note_text = note_text.rstrip() + '\n' + tag + '\n'
        return note_text

    def remove_tag(self, note_text, tag):
        """Remove a tag from a note if present."""
        lines = note_text.split('\n')
        filtered = [line for line in lines if not line.strip().startswith(self.tag_prefix + tag) and not line.strip().startswith(self.tag_prefix + tag + ' ')]
        return '\n'.join(filtered)

    def get_tag_summary(self, tag):
        """Get summary of notes with a specific tag."""
        tag_pattern = self.tag_prefix + tag
        summary = {'tag': tag, 'count': 0, 'notes': []}
        try:
            with open(self.notes_file, 'r') as f:
                notes = f.readlines()
        except FileNotFoundError:
            return summary

        for line in notes:
            if line.strip().startswith(tag_pattern):
                summary['count'] += 1
                summary['notes'].append(line.strip())

        return summary

    def get_all_tags(self):
        """Get all unique tags from notes."""
        tags = set()
        try:
            with open(self.notes_file, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            return tags

        for line in lines:
            if line.strip().startswith(self.tag_prefix):
                tag = line.strip()[len(self.tag_prefix):].strip()
                if tag:
                    tags.add(tag)

        return tags
