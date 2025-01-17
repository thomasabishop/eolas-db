from termcolor import colored


class Controller:
    def __init__(
        self,
        database_service,
        table_service,
        parse_file_service,
        graph_service,
        # tag_service,
    ):
        self.database_service = database_service
        self.table_service = table_service
        self.parse_file_service = parse_file_service
        self.graph_service = graph_service
        # self.tag_service = tag_service

    def execute(self, operation):
        try:
            match operation:
                case "populate":
                    return self.__populate_database()
                case "graph":
                    return self.__generate_graph()
        except Exception as e:
            raise Exception(colored(f"ERROR {e}", "red"))
        finally:
            self.database_service.disconnect()

    def __populate_database(self):
        entries = self.parse_file_service.parse_source_directory()
        self.table_service.populate_tables(entries)
        self.database_service.disconnect()

    def __generate_graph(self):
        self.graph_service.generate_graph()
