class Controller:
    def __init__(self, database_service, table_service, parse_file_service):
        self.database_service = database_service
        self.table_service = table_service
        self.parse_file_service = parse_file_service

    def populate_database(self):
        try:
            entries = self.parse_file_service.parse_source_directory()
            self.table_service.populate_tables(entries)
        finally:
            self.database_service.disconnect()
