# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: NoteShelf
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class NoteStatus(Enum):
    DRAFT = "draft"
    PUBLISHED = "published"


@dataclass
class Tag:
    name: str
    color: Optional[str] = None


@dataclass
class Note:
    title: str
    body: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    status: NoteStatus = NoteStatus.DRAFT
    folder: Optional[str] = None
    tags: list[Tag] = field(default_factory=list)
    pinned: bool = False
    id: str = ""  # filled by the UI or backend


@dataclass
class Folder:
    name: str
    notes: list[Note] = field(default_factory=list)


@dataclass
class SearchQuery:
    q: str
    results: list[Note] = field(default_factory=list)
