class Controller:
    def __init__(
        self,
        database_service,
        table_service,
        parse_file_service,
    ):
        self.database_service = database_service
        self.table_service = table_service
        self.parse_file_service = parse_file_service

    def execute(self, operation):
        try:
            match operation:
                case "populate":
                    return self.__populate_database()
        except Exception as e:
            raise Exception(f"ERROR {e}")
        finally:
            self.database_service.disconnect()

    def __populate_database(self):
        entries = self.parse_file_service.parse_source_directory()
        self.table_service.populate_tables(entries)
        self.database_service.disconnect()
