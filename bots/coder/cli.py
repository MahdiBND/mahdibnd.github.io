import sys
from agents import Runner
from bots.coder import coder


def generate_code(request: str) -> str:
    result = Runner.run_sync(coder, request)
    return result.final_output.code


def main():
    if len(sys.argv) < 2:
        print("No request provided", file=sys.stderr)
        sys.exit(1)

    # Join all arguments after the script name
    request = " ".join(sys.argv[1:]).strip()

    if not request:
        print("No request provided", file=sys.stderr)
        sys.exit(1)

    try:
        code = generate_code(request)
        print(code, end="")
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
