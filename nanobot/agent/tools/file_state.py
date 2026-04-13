"""Track file-read state for read-before-edit warnings and read deduplication."""

from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ReadState:
    mtime: float
    offset: int
    limit: int | None
    content_hash: str | None
    can_dedup: bool


_state: dict[str, ReadState] = {}


def _hash_file(p: str) -> str | None:
    pass


def record_read(path: str | Path, offset: int = 1, limit: int | None = None) -> None:
    """Record that a file was read (called after successful read)."""
    pass


def record_write(path: str | Path) -> None:
    """Record that a file was written (updates mtime in state)."""
    pass


def check_read(path: str | Path) -> str | None:
    """Check if a file has been read and is fresh.

    Returns None if OK, or a warning string.
    When mtime changed but file content is identical (e.g. touch, editor save),
    the check passes to avoid false-positive staleness warnings.
    """
    pass


def is_unchanged(path: str | Path, offset: int = 1, limit: int | None = None) -> bool:
    """Return True if file was previously read with same params and mtime is unchanged."""
    pass


def clear() -> None:
    """Clear all tracked state (useful for testing)."""
    pass
