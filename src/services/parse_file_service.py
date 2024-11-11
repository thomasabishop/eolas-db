import os
from datetime import datetime
from pathlib import Path

from hurry.filesize import size

from models.entry import Entry
from services.parse_markdown_service import ParseMarkdownService


class ParseFileService:
    def __init__(self, source_directory):
        self.source_directory = source_directory
        self.parse_markdown_service = ParseMarkdownService()

    def __get_title(self, file):
        return os.path.basename(file)

    def __parse_file(self, file) -> Entry:
        markdown_data = self.parse_markdown_service.parse(file)
        return {
            "title": self.__get_title(file),
            "last_modified": datetime.fromtimestamp(os.stat(file).st_mtime).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "size": os.stat(file).st_size,
            "tags": markdown_data.get("tags", []),
            "links": markdown_data.get("links", []),
            "body": markdown_data.get("body", []),
        }

    def parse_source_directory(self):
        print("INFO Indexing entries in source directory")
        parsed_entries = []
        with os.scandir(self.source_directory) as dir:
            for file in dir:
                if Path(file).suffix == ".md":
                    parsed = self.__parse_file(file)
                    parsed_entries.append(parsed)
        return parsed_entries
