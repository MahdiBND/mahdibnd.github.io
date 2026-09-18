import sys
from agents import Runner
from bots.coder import coder


async def generate_code(request: str) -> str:
    result = Runner.run_sync(coder, request)
    return result.final_output.code


def main():
    # Read the full request from stdin
    request = sys.stdin.read().strip()

    if not request:
        print("No request provided", file=sys.stderr)
        sys.exit(1)

    try:
        code = generate_code(request)
        # IMPORTANT: only print the code to stdout
        print(code, end="")
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
