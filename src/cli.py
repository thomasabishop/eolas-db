import argparse

from constants import EOLAS_DIRECTORY
from controllers.controller import Controller
from services.database_service import DatabaseService
from services.graph_service import GraphService
from services.parse_file_service import ParseFileService
from services.table_service import TableService
from services.tag_service import TagService

database_service = DatabaseService("eolas")
database_connection = database_service.connect()
table_service = TableService(database_connection)
parse_file_service = ParseFileService(EOLAS_DIRECTORY)
graph_service = GraphService(database_connection)
tag_service = TagService(database_connection)

controller = Controller(
    database_service, table_service, parse_file_service, graph_service, tag_service
)


def main():
    parser = argparse.ArgumentParser(
        prog="eolas-db", description="Eolas database manager."
    )
    parser.add_argument(
        "command",
        choices=["populate-database", "generate-graph", "export-tags"],
        help="Command to execute",
    )
    args = parser.parse_args()

    if args.command == "populate-database":
        controller.execute("populate")

    if args.command == "generate-graph":
        controller.execute("graph")

    if args.command == "export-tags":
        controller.execute("tags")


if __name__ == "__main__":
    main()
