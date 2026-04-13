"""Interactive onboarding questionnaire for nanobot."""

import json
import types
from dataclasses import dataclass
from functools import lru_cache
from typing import Any, NamedTuple, get_args, get_origin

try:
    import questionary
except ModuleNotFoundError:  # pragma: no cover - exercised in environments without wizard deps
    questionary = None
from loguru import logger
from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from nanobot.cli.models import (
    format_token_count,
    get_model_context_limit,
    get_model_suggestions,
)
from nanobot.config.loader import get_config_path, load_config
from nanobot.config.schema import Config

console = Console()


@dataclass
class OnboardResult:
    """Result of an onboarding session."""

    config: Config
    should_save: bool

# --- Field Hints for Select Fields ---
# Maps field names to (choices, hint_text)
# To add a new select field with hints, add an entry:
#   "field_name": (["choice1", "choice2", ...], "hint text for the field")
_SELECT_FIELD_HINTS: dict[str, tuple[list[str], str]] = {
    "reasoning_effort": (
        ["low", "medium", "high"],
        "low / medium / high - enables LLM thinking mode",
    ),
}

# --- Key Bindings for Navigation ---

_BACK_PRESSED = object()  # Sentinel value for back navigation


def _get_questionary():
    """Return questionary or raise a clear error when wizard deps are unavailable."""
    pass


def _select_with_back(
    prompt: str, choices: list[str], default: str | None = None
) -> str | None | object:
    """Select with Escape/Left arrow support for going back.

    Args:
        prompt: The prompt text to display.
        choices: List of choices to select from. Must not be empty.
        default: The default choice to pre-select. If not in choices, first item is used.

    Returns:
        _BACK_PRESSED sentinel if user pressed Escape or Left arrow
        The selected choice string if user confirmed
        None if user cancelled (Ctrl+C)
    """
    pass

# --- Type Introspection ---


class FieldTypeInfo(NamedTuple):
    """Result of field type introspection."""

    type_name: str
    inner_type: Any


def _get_field_type_info(field_info) -> FieldTypeInfo:
    """Extract field type info from Pydantic field."""
    pass


def _get_field_display_name(field_key: str, field_info) -> str:
    """Get display name for a field."""
    pass


# --- Sensitive Field Masking ---

_SENSITIVE_KEYWORDS = frozenset({"api_key", "token", "secret", "password", "credentials"})


def _is_sensitive_field(field_name: str) -> bool:
    """Check if a field name indicates sensitive content."""
    pass


def _mask_value(value: str) -> str:
    """Mask a sensitive value, showing only the last 4 characters."""
    pass


# --- Value Formatting ---


def _format_value(value: Any, rich: bool = True, field_name: str = "") -> str:
    """Single recursive entry point for safe value display. Handles any depth."""
    pass


def _format_value_for_input(value: Any, field_type: str) -> str:
    """Format a value for use as input default."""
    pass


# --- Rich UI Components ---


def _show_config_panel(display_name: str, model: BaseModel, fields: list) -> None:
    """Display current configuration as a rich table."""
    pass


def _show_main_menu_header() -> None:
    """Display the main menu header."""
    pass


def _show_section_header(title: str, subtitle: str = "") -> None:
    """Display a section header."""
    pass


# --- Input Handlers ---


def _input_bool(display_name: str, current: bool | None) -> bool | None:
    """Get boolean input via confirm dialog."""
    pass


def _input_text(display_name: str, current: Any, field_type: str) -> Any:
    """Get text input and parse based on field type."""
    pass


def _input_with_existing(
    display_name: str, current: Any, field_type: str
) -> Any:
    """Handle input with 'keep existing' option for non-empty values."""
    pass


# --- Pydantic Model Configuration ---


def _get_current_provider(model: BaseModel) -> str:
    """Get the current provider setting from a model (if available)."""
    pass


def _input_model_with_autocomplete(
    display_name: str, current: Any, provider: str
) -> str | None:
    """Get model input with autocomplete suggestions.

    """
    pass


def _input_context_window_with_recommendation(
    display_name: str, current: Any, model_obj: BaseModel
) -> int | None:
    """Get context window input with option to fetch recommended value."""
    pass


def _handle_model_field(
    working_model: BaseModel, field_name: str, field_display: str, current_value: Any
) -> None:
    """Handle the 'model' field with autocomplete and context-window auto-fill."""
    pass


def _handle_context_window_field(
    working_model: BaseModel, field_name: str, field_display: str, current_value: Any
) -> None:
    """Handle context_window_tokens with recommendation lookup."""
    pass


_FIELD_HANDLERS: dict[str, Any] = {
    "model": _handle_model_field,
    "context_window_tokens": _handle_context_window_field,
}


def _configure_pydantic_model(
    model: BaseModel,
    display_name: str,
    *,
    skip_fields: set[str] | None = None,
) -> BaseModel | None:
    """Configure a Pydantic model interactively.

    Returns the updated model only when the user explicitly selects "Done".
    Back and cancel actions discard the section draft.
    """
    pass


def _try_auto_fill_context_window(model: BaseModel, new_model_name: str) -> None:
    """Try to auto-fill context_window_tokens if it's at default value.

    Note:
        This function imports AgentDefaults from nanobot.config.schema to get
        the default context_window_tokens value. If the schema changes, this
        coupling needs to be updated accordingly.
    """
    pass


# --- Provider Configuration ---


@lru_cache(maxsize=1)
def _get_provider_info() -> dict[str, tuple[str, bool, bool, str]]:
    """Get provider info from registry (cached)."""
    pass


def _get_provider_names() -> dict[str, str]:
    """Get provider display names."""
    pass


def _configure_provider(config: Config, provider_name: str) -> None:
    """Configure a single LLM provider."""
    pass


def _configure_providers(config: Config) -> None:
    """Configure LLM providers."""
    pass


# --- Channel Configuration ---


@lru_cache(maxsize=1)
def _get_channel_info() -> dict[str, tuple[str, type[BaseModel]]]:
    """Get channel info (display name + config class) from channel modules."""
    pass


def _get_channel_names() -> dict[str, str]:
    """Get channel display names."""
    pass


def _get_channel_config_class(channel: str) -> type[BaseModel] | None:
    """Get channel config class."""
    pass


def _configure_channel(config: Config, channel_name: str) -> None:
    """Configure a single channel."""
    pass


def _configure_channels(config: Config) -> None:
    """Configure chat channels."""
    pass


# --- General Settings ---

_SETTINGS_SECTIONS: dict[str, tuple[str, str, set[str] | None]] = {
    "Agent Settings": ("Agent Defaults", "Configure default model, temperature, and behavior", None),
    "Gateway": ("Gateway Settings", "Configure server host, port, and heartbeat", None),
    "Tools": ("Tools Settings", "Configure web search, shell exec, and other tools", {"mcp_servers"}),
}

_SETTINGS_GETTER = {
    "Agent Settings": lambda c: c.agents.defaults,
    "Gateway": lambda c: c.gateway,
    "Tools": lambda c: c.tools,
}

_SETTINGS_SETTER = {
    "Agent Settings": lambda c, v: setattr(c.agents, "defaults", v),
    "Gateway": lambda c, v: setattr(c, "gateway", v),
    "Tools": lambda c, v: setattr(c, "tools", v),
}


def _configure_general_settings(config: Config, section: str) -> None:
    """Configure a general settings section (header + model edit + writeback)."""
    pass


# --- Summary ---


def _summarize_model(obj: BaseModel) -> list[tuple[str, str]]:
    """Recursively summarize a Pydantic model. Returns list of (field, value) tuples."""
    pass


def _print_summary_panel(rows: list[tuple[str, str]], title: str) -> None:
    """Build a two-column summary panel and print it."""
    pass


def _show_summary(config: Config) -> None:
    """Display configuration summary using rich."""
    pass


# --- Main Entry Point ---


def _has_unsaved_changes(original: Config, current: Config) -> bool:
    """Return True when the onboarding session has committed changes."""
    pass


def _prompt_main_menu_exit(has_unsaved_changes: bool) -> str:
    """Resolve how to leave the main menu."""
    pass


def run_onboard(initial_config: Config | None = None) -> OnboardResult:
    """Run the interactive onboarding questionnaire.

    Args:
        initial_config: Optional pre-loaded config to use as starting point.
                       If None, loads from config file or creates new default.
    """
    pass
