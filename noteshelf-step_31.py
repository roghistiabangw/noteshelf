# === Stage 31: Add compact table rendering for long lists ===
# Project: NoteShelf
def render_compact_table(headers, rows):
    """Render a compact table, wrapping long rows and limiting row count."""
    if not headers:
        return ""
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))
    table = ""
    table += "  |  ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers)) + "  |\n"
    border = "  +  ".join("-" * (w + 2) for w in col_widths) + "+\n"
    table += border
    for row in rows:
        line = "  |  ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)) + "  |\n"
        table += line
    table += border
    if len(rows) > 20:
        table += f"\n  ... and {len(rows) - 20} more rows omitted"
    return table
