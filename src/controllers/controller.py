from termcolor import colored

class Controller:
    def __init__(
        self, database_service, table_service, parse_file_service, graph_service
    ):
        self.database_service = database_service
        self.table_service = table_service
        self.parse_file_service = parse_file_service
        self.graph_service = graph_service

    def populate_database(self):
        try:
            entries = self.parse_file_service.parse_source_directory()
            self.table_service.populate_tables(entries)
            print(colored("SUCCESS Database populated", "green"))
        except Exception as e:
            raise Exception(colored(f"ERROR {e}", "red"))  
        finally:
            self.database_service.disconnect()
            print(colored("INFO Database connection closed", "blue"))
    def generate_graph(self):
        try:
            self.graph_service.generate_graph()
            print(colored("SUCCESS Graph generated", "green"))
        except Exception as e:
            raise Exception(colored(f"ERROR {e}"), "red")
        finally:
            self.database_service.disconnect()
            print(colored("INFO Database connection closed", "blue"))
