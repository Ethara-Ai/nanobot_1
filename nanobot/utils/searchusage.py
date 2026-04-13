"""Web search provider usage fetchers for /status command."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any


@dataclass
class SearchUsageInfo:
    """Structured usage info returned by a provider fetcher."""

    provider: str
    supported: bool = False          # True if the provider has a usage API
    error: str | None = None         # Set when the API call failed

    # Usage counters (None = not available for this provider)
    used: int | None = None
    limit: int | None = None
    remaining: int | None = None
    reset_date: str | None = None    # ISO date string, e.g. "2026-05-01"

    # Tavily-specific breakdown
    search_used: int | None = None
    extract_used: int | None = None
    crawl_used: int | None = None

    def format(self) -> str:
        """Return a human-readable multi-line string for /status output."""
        pass


async def fetch_search_usage(
    provider: str,
    api_key: str | None = None,
) -> SearchUsageInfo:
    """
    Fetch usage info for the configured web search provider.

    Args:
        provider: Provider name (e.g. "tavily", "brave", "duckduckgo").
        api_key:  API key for the provider (falls back to env vars).

    Returns:
        SearchUsageInfo with populated fields where available.
    """
    pass


# ---------------------------------------------------------------------------
# Tavily
# ---------------------------------------------------------------------------

async def _fetch_tavily_usage(api_key: str | None) -> SearchUsageInfo:
    """Fetch usage from GET https://api.tavily.com/usage."""
    pass


def _parse_tavily_usage(data: dict[str, Any]) -> SearchUsageInfo:
    """
    Parse Tavily /usage response.

    Actual API response shape:
    {
      "account": {
        "current_plan": "Researcher",
        "plan_usage": 20,
        "plan_limit": 1000,
        "search_usage": 20,
        "crawl_usage": 0,
        "extract_usage": 0,
        "map_usage": 0,
        "research_usage": 0,
        "paygo_usage": 0,
        "paygo_limit": null
      }
    }
    """
    pass


