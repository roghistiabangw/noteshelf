# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: NoteShelf
def score_note(note, query):
    text = (note.get("content", "") + " " + " ".join(note.get("tags", []))).lower()
    if note.get("pinned", False):
        score = 100
    else:
        score = 0
    query = (query or "").lower()
    if query:
        if query in text:
            score += 100
        for word in query.split():
            if word in text:
                score += 50
            if word in note.get("title", "").lower():
                score += 20
    score += len(note.get("tags", [])) * 3
    score += len(note.get("content", "")) * 0.1
    return round(score, 1)


def rank_notes(notes, query):
    scored = [(score_note(note, query), note) for note in notes]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [note for _, note in scored]


def top_recommendations(notes, query, limit=5):
    ranked = rank_notes(notes, query)
    if query:
        return ranked[:limit]
    return ranked
