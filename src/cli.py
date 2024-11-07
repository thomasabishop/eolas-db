import argparse
import importlib

from controllers.controller import Controller
from services.database_service import DatabaseService

importlib.invalidate_caches()
file_path = "/home/thomas/repos/eolas-db/dev-data/Turing_completeness.md"


def main():
    parser = argparse.ArgumentParser(
        prog="eolas-db", description="Eolas database manager."
    )
    parser.add_argument(
        "command", choices=["parse", "populate"], help="Command to execute"
    )
    args = parser.parse_args()

    database_service = DatabaseService("eolas")
    controller = Controller(database_service)

    if args.command == "parse":
        parsed_entry = controller.parse_entry(file_path)
        print(parsed_entry)

    if args.command == "populate":
        controller.populate_database()


if __name__ == "__main__":
    main()
