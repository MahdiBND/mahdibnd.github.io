from bots import Agent, model
from pydantic import BaseModel

from prompts import INSTRUCTIONS

model = model()


class CodeResponse(BaseModel):
    code: str


coder = Agent(
    name="Coding Assistant",
    instructions=INSTRUCTIONS,
    model=model,
    output_type=CodeResponse,
    model_settings={
        "temperature": 0.2,
        "top_p": 0.9,
    },
)

__all__ = ["coder"]
