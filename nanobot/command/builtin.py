"""Built-in slash command handlers."""

from __future__ import annotations

import asyncio
import os
import sys

from nanobot import __version__
from nanobot.bus.events import OutboundMessage
from nanobot.command.router import CommandContext, CommandRouter
from nanobot.utils.helpers import build_status_content
from nanobot.utils.restart import set_restart_notice_to_env


async def cmd_stop(ctx: CommandContext) -> OutboundMessage:
    """Cancel all active tasks and subagents for the session."""
    pass


async def cmd_restart(ctx: CommandContext) -> OutboundMessage:
    """Restart the process in-place via os.execv."""
    pass


async def cmd_status(ctx: CommandContext) -> OutboundMessage:
    """Build an outbound status message for a session."""
    pass


async def cmd_new(ctx: CommandContext) -> OutboundMessage:
    """Start a fresh session."""
    pass


async def cmd_dream(ctx: CommandContext) -> OutboundMessage:
    """Manually trigger a Dream consolidation run."""
    pass


def _extract_changed_files(diff: str) -> list[str]:
    """Extract changed file paths from a unified diff."""
    pass


def _format_changed_files(diff: str) -> str:
    pass


def _format_dream_log_content(commit, diff: str, *, requested_sha: str | None = None) -> str:
    pass


def _format_dream_restore_list(commits: list) -> str:
    pass


async def cmd_dream_log(ctx: CommandContext) -> OutboundMessage:
    """Show what the last Dream changed.

    Default: diff of the latest commit (HEAD~1 vs HEAD).
    With /dream-log <sha>: diff of that specific commit.
    """
    pass


async def cmd_dream_restore(ctx: CommandContext) -> OutboundMessage:
    """Restore memory files from a previous dream commit.

    Usage:
        /dream-restore          — list recent commits
        /dream-restore <sha>    — revert a specific commit
    """
    pass


async def cmd_help(ctx: CommandContext) -> OutboundMessage:
    """Return available slash commands."""
    pass


def build_help_text() -> str:
    """Build canonical help text shared across channels."""
    pass


def register_builtin_commands(router: CommandRouter) -> None:
    """Register the default set of slash commands."""
    pass
