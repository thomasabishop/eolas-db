import os
from datetime import datetime
from typing import List, TypedDict

from hurry.filesize import size

from services.parse_markdown_service import ParseMarkdownService


class Entry(TypedDict):
    title: str
    tags: List[str]
    body: str
    last_modified: str
    size: int


class ParseFileService:
    def __init__(self, file):
        self.eolas_file = file
        self.info = os.stat(file)
        self.parse_markdown_service = ParseMarkdownService(file)

    def __get_title(self):
        return os.path.basename(self.eolas_file)

    def parse(self) -> Entry:
        markdown_data = self.parse_markdown_service.parse()
        return {
            "title": self.__get_title(),
            "last_modified": datetime.fromtimestamp(self.info.st_mtime).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "size": size(self.info.st_size),
            "tags": markdown_data.get("tags", []),
            "body": markdown_data.get("body", []),
        }
