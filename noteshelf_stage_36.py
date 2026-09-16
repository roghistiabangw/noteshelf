# === Stage 36: Add templates for quickly creating common records ===
# Project: NoteShelf
TEMPLATES = {
    "todo": f"""# {datetime.now().strftime('%Y-%m-%d %H:%M')}
- [ ] TODO: {{task}}
- [ ] TODO: {{task}}
- [ ] TODO: {{task}}
Tags: {{tag}}
""",
    "meeting": f"""# {datetime.now().strftime('%Y-%m-%d %H:%M')}
## Meeting Notes
### Attendees
- {{name}}
### Agenda
1. {{topic}}
2. {{topic}}
### Action Items
- [ ] {{item}}
Tags: {{tag}}
""",
    "diary": f"""# {datetime.now().strftime('%Y-%m-%d %H:%M')}
## Day {{day}}
{{entry}}
Tags: {{tag}}
""",
    "recipe": f"""# {{name}}
## Ingredients
- {{ingredient}}
- {{ingredient}}
## Instructions
1. {{step}}
2. {{step}}
Tags: {{tag}}
""",
    "budget": f"""# {datetime.now().strftime('%Y-%m-%d %H:%M')}
## Expenses
| Category | Amount |
| -------- | ------ |
| {{category}} | ${{amount}} |
Tags: {{tag}}
""",
}
