"""Search tools: grep and glob."""

from __future__ import annotations

import fnmatch
import os
import re
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, TypeVar

from nanobot.agent.tools.filesystem import ListDirTool, _FsTool

_DEFAULT_HEAD_LIMIT = 250
T = TypeVar("T")
_TYPE_GLOB_MAP = {
    "py": ("*.py", "*.pyi"),
    "python": ("*.py", "*.pyi"),
    "js": ("*.js", "*.jsx", "*.mjs", "*.cjs"),
    "ts": ("*.ts", "*.tsx", "*.mts", "*.cts"),
    "tsx": ("*.tsx",),
    "jsx": ("*.jsx",),
    "json": ("*.json",),
    "md": ("*.md", "*.mdx"),
    "markdown": ("*.md", "*.mdx"),
    "go": ("*.go",),
    "rs": ("*.rs",),
    "rust": ("*.rs",),
    "java": ("*.java",),
    "sh": ("*.sh", "*.bash"),
    "yaml": ("*.yaml", "*.yml"),
    "yml": ("*.yaml", "*.yml"),
    "toml": ("*.toml",),
    "sql": ("*.sql",),
    "html": ("*.html", "*.htm"),
    "css": ("*.css", "*.scss", "*.sass"),
}


def _normalize_pattern(pattern: str) -> str:
    pass


def _match_glob(rel_path: str, name: str, pattern: str) -> bool:
    pass


def _is_binary(raw: bytes) -> bool:
    pass


def _paginate(items: list[T], limit: int | None, offset: int) -> tuple[list[T], bool]:
    pass


def _pagination_note(limit: int | None, offset: int, truncated: bool) -> str | None:
    pass


def _matches_type(name: str, file_type: str | None) -> bool:
    pass


class _SearchTool(_FsTool):
    _IGNORE_DIRS = set(ListDirTool._IGNORE_DIRS)

    def _display_path(self, target: Path, root: Path) -> str:
        pass

    def _iter_files(self, root: Path) -> Iterable[Path]:
        pass

    def _iter_entries(
        self,
        root: Path,
        *,
        include_files: bool,
        include_dirs: bool,
    ) -> Iterable[Path]:
        pass


class GlobTool(_SearchTool):
    """Find files matching a glob pattern."""

    @property
    def name(self) -> str:
        pass

    @property
    def description(self) -> str:
        pass

    @property
    def read_only(self) -> bool:
        pass

    @property
    def parameters(self) -> dict[str, Any]:
        pass

    async def execute(
        self,
        pattern: str,
        path: str = ".",
        max_results: int | None = None,
        head_limit: int | None = None,
        offset: int = 0,
        entry_type: str = "files",
        **kwargs: Any,
    ) -> str:
        pass


class GrepTool(_SearchTool):
    """Search file contents using a regex-like pattern."""
    _MAX_RESULT_CHARS = 128_000
    _MAX_FILE_BYTES = 2_000_000

    @property
    def name(self) -> str:
        pass

    @property
    def description(self) -> str:
        pass

    @property
    def read_only(self) -> bool:
        pass

    @property
    def parameters(self) -> dict[str, Any]:
        pass

    @staticmethod
    def _format_block(
        display_path: str,
        lines: list[str],
        match_line: int,
        before: int,
        after: int,
    ) -> str:
        pass

    async def execute(
        self,
        pattern: str,
        path: str = ".",
        glob: str | None = None,
        type: str | None = None,
        case_insensitive: bool = False,
        fixed_strings: bool = False,
        output_mode: str = "files_with_matches",
        context_before: int = 0,
        context_after: int = 0,
        max_matches: int | None = None,
        max_results: int | None = None,
        head_limit: int | None = None,
        offset: int = 0,
        **kwargs: Any,
    ) -> str:
        pass
