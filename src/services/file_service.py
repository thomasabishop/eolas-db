import os


class FileService:
    def __init__(self, eolas_file):
        self.eolas_file = eolas_file
        self.info = os.stat(eolas_file)

    def __extract_title(self):
        return os.path.basename(self.eolas_file)

    def get_info(self):
        return {
            "title": self.__extract_title(),
            "last_modified": self.info.st_mtime,
            "size": self.info.st_size,
        }
