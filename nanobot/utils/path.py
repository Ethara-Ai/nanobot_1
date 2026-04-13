"""Path abbreviation utilities for display."""

from __future__ import annotations

import os
import re
from urllib.parse import urlparse


def abbreviate_path(path: str, max_len: int = 40) -> str:
    """Abbreviate a file path or URL, preserving basename and key directories.

    Strategy:
    1. Return as-is if short enough
    2. Replace home directory with ~/
    3. From right, keep basename + parent dirs until budget exhausted
    4. Prefix with …/
    """
    pass


def _abbreviate_url(url: str, max_len: int = 40) -> str:
    """Abbreviate a URL keeping domain and filename."""
    pass
