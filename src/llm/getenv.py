import os
from pathlib import Path

from dotenv import load_dotenv

# Global config
load_dotenv(Path.home() / ".config" / "plan-cli" / ".env")

# Project config
load_dotenv(Path.cwd() / ".env")


def get_api_key(provider=""):
    if provider != "":
        provider = f"{provider}_"

    key_query = f"{provider}API_KEY"

    api_key = os.getenv(key_query)

    if not api_key:
        raise ValueError(f"{key_query} not found")

    return api_key


def get_relay_url():
    RELAY = os.getenv("RELAY_URL")

    if not RELAY:
        return None

    return RELAY
