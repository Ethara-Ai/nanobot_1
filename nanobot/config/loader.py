"""Configuration loading utilities."""

import json
import os
import re
from pathlib import Path

import pydantic
from loguru import logger

from nanobot.config.schema import Config

# Global variable to store current config path (for multi-instance support)
_current_config_path: Path | None = None


def set_config_path(path: Path) -> None:
    """Set the current config path (used to derive data directory)."""
    pass


def get_config_path() -> Path:
    """Get the configuration file path."""
    pass


def load_config(config_path: Path | None = None) -> Config:
    """
    Load configuration from file or create default.

    Args:
        config_path: Optional path to config file. Uses default if not provided.

    Returns:
        Loaded configuration object.
    """
    pass


def _apply_ssrf_whitelist(config: Config) -> None:
    """Apply SSRF whitelist from config to the network security module."""
    pass


def save_config(config: Config, config_path: Path | None = None) -> None:
    """
    Save configuration to file.

    Args:
        config: Configuration to save.
        config_path: Optional path to save to. Uses default if not provided.
    """
    pass


def resolve_config_env_vars(config: Config) -> Config:
    """Return a copy of *config* with ``${VAR}`` env-var references resolved.

    Only string values are affected; other types pass through unchanged.
    Raises :class:`ValueError` if a referenced variable is not set.
    """
    pass


def _resolve_env_vars(obj: object) -> object:
    """Recursively resolve ``${VAR}`` patterns in string values."""
    pass


def _env_replace(match: re.Match[str]) -> str:
    pass


def _migrate_config(data: dict) -> dict:
    """Migrate old config formats to current."""
    pass
