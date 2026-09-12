import os
from dotenv import load_dotenv

load_dotenv()


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
        raise ValueError("RELAY_URL is not set in environment or .env file")

    return RELAY
