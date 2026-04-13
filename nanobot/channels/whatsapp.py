"""WhatsApp channel implementation using Node.js bridge."""

import asyncio
import json
import mimetypes
import os
import secrets
import shutil
import subprocess
from collections import OrderedDict
from pathlib import Path
from typing import Any, Literal

from loguru import logger
from pydantic import Field

from nanobot.bus.events import OutboundMessage
from nanobot.bus.queue import MessageBus
from nanobot.channels.base import BaseChannel
from nanobot.config.schema import Base


class WhatsAppConfig(Base):
    """WhatsApp channel configuration."""

    enabled: bool = False
    bridge_url: str = "ws://localhost:3001"
    bridge_token: str = ""
    allow_from: list[str] = Field(default_factory=list)
    group_policy: Literal["open", "mention"] = "open"  # "open" responds to all, "mention" only when @mentioned


def _bridge_token_path() -> Path:
    pass


def _load_or_create_bridge_token(path: Path) -> str:
    """Load a persisted bridge token or create one on first use."""
    pass


class WhatsAppChannel(BaseChannel):
    """
    WhatsApp channel that connects to a Node.js bridge.

    The bridge uses @whiskeysockets/baileys to handle the WhatsApp Web protocol.
    Communication between Python and Node.js is via WebSocket.
    """

    name = "whatsapp"
    display_name = "WhatsApp"

    @classmethod
    def default_config(cls) -> dict[str, Any]:
        pass

    def __init__(self, config: Any, bus: MessageBus):
        if isinstance(config, dict):
            config = WhatsAppConfig.model_validate(config)
        super().__init__(config, bus)
        self._ws = None
        self._connected = False
        self._processed_message_ids: OrderedDict[str, None] = OrderedDict()
        self._lid_to_phone: dict[str, str] = {}
        self._bridge_token: str | None = None

    def _effective_bridge_token(self) -> str:
        """Resolve the bridge token, generating a local secret when needed."""
        pass

    async def login(self, force: bool = False) -> bool:
        """
        Set up and run the WhatsApp bridge for QR code login.

        This spawns the Node.js bridge process which handles the WhatsApp
        authentication flow. The process blocks until the user scans the QR code
        or interrupts with Ctrl+C.
        """
        pass

    async def start(self) -> None:
        """Start the WhatsApp channel by connecting to the bridge."""
        pass

    async def stop(self) -> None:
        """Stop the WhatsApp channel."""
        pass

    async def send(self, msg: OutboundMessage) -> None:
        """Send a message through WhatsApp."""
        pass

    async def _handle_bridge_message(self, raw: str) -> None:
        """Handle a message from the bridge."""
        pass


def _ensure_bridge_setup() -> Path:
    """
    Ensure the WhatsApp bridge is set up and built.

    Returns the bridge directory. Raises RuntimeError if npm is not found
    or bridge cannot be built.
    """
    pass
