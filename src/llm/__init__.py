#
#  Base of LLM to use for calls in other parts of this project
#

import openai
from .getenv import get_api_key
from .relay import create_client
from agents import OpenAIChatCompletionsModel

_api_key = get_api_key()

_relay_client = create_client()

_client = openai.AsyncOpenAI(
    api_key=_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    http_client=_relay_client,
)


def model(name="gemini-3.6-flash") -> OpenAIChatCompletionsModel:
    return OpenAIChatCompletionsModel(
        model=name,
        openai_client=_client,
    )
