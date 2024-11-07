from services.parse_file_service import ParseFileService
from services.sqlite_service import SqliteService


class Controller:
    def __init__(self, database_service):
        self.database_service = database_service

    def parse_entry(self, file_path):
        parse_file_service = ParseFileService(file_path)
        return parse_file_service.parse()

    def populate_database(self):
        connection = self.database_service.connect()

        if connection is None:
            raise Exception("Failed to establish database connection")

        sqlite_service = SqliteService(connection)
        sqlite_service.create_tables()
