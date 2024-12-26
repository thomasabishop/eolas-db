import argparse

from constants import EOLAS_DIRECTORY
from controllers.controller import Controller
from services.database_service import DatabaseService
from services.parse_file_service import ParseFileService
from services.table_service import TableService

database_service = DatabaseService("eolas")
database_connection = database_service.connect()
table_service = TableService(database_connection)
parse_file_service = ParseFileService(EOLAS_DIRECTORY)
controller = Controller(database_service, table_service, parse_file_service)


def main():
    parser = argparse.ArgumentParser(
        prog="eolas-db", description="Eolas database manager."
    )
    parser.add_argument(
        "command", choices=["populate-database"], help="Command to execute"
    )
    args = parser.parse_args()

    if args.command == "populate-database":
        controller.populate_database()


if __name__ == "__main__":
    main()
