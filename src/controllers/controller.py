from services.parse_file_service import ParseFileService


class Controller:
    def __init__(self):
        pass

    def parse_entry(self, file_path):
        parse_file_service = ParseFileService(file_path)
        return parse_file_service.parse()
