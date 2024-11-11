class Controller:
    def __init__(self, database_service, sqlite_service, parse_file_service):
        self.database_service = database_service
        self.sqlite_service = sqlite_service
        self.parse_file_service = parse_file_service

    def populate_database(self):
        try:
            entries = self.parse_file_service.parse_source_directory()
            self.sqlite_service.populate_tables(entries)
        except Exception as e:
            raise Exception(e)

        finally:
            self.database_service.disconnect()
