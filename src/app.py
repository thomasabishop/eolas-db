import argparse

from database_connection import DatabaseConnection
from services.parse_file_service import ParseFileService
from services.table_service import TableService


def main():
    parser = argparse.ArgumentParser(
        prog="eolas-db", description="Eolas database generator."
    )

    parser.add_argument(
        "--source",
        type=str,
        required=True,
        help="Source directory for markdown files",
    )

    parser.add_argument(
        "--target",
        type=str,
        required=True,
        help="Output path for SQLite database file",
    )

    args = parser.parse_args()

    SOURCE_DIRECTORY = args.source
    TARGET_DIRECTORY = args.target

    with DatabaseConnection("eolas", TARGET_DIRECTORY) as conn:
        table_service = TableService(conn)
        parse_file_service = ParseFileService(SOURCE_DIRECTORY)
        entries = parse_file_service.parse_source_directory()
        table_service.populate_tables(entries)


if __name__ == "__main__":
    main()
