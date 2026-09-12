import asyncio
from bots import planner
from agents import Runner

questions = ["i need a simple python name teller, my name is mahdi"]


async def main() -> None:
    result = await Runner.run(planner, questions[0])
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
