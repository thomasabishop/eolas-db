import argparse
import importlib

from controllers.controller import Controller

importlib.invalidate_caches()

file_path = "/home/thomas/repos/eolas-db/dev-data/Turing_completeness.md"


def main():
    parser = argparse.ArgumentParser(
        prog="eolas-db", description="Eolas database manager."
    )
    parser.add_argument("command", choices=["parse"], help="Command to execute")
    args = parser.parse_args()

    controller = Controller()

    if args.command == "parse":
        parsed_entry = controller.parse_entry(file_path)
        print(parsed_entry)


if __name__ == "__main__":
    main()
