from typing import List, TypedDict

from services.file_service import FileService
from services.markdown_parse_service import MarkdownParseService


class Entry(TypedDict):
    title: str
    tags: List[str]
    body: str
    last_modified: int
    size: int


class Controller:
    def __init__(self):
        pass

    def parse_entry(self, file_path) -> Entry:
        markdown_parser_service = MarkdownParseService(file_path)
        file_parser_service = FileService(file_path)

        markdown_metadata = markdown_parser_service.parse()
        file_data = file_parser_service.get_info()

        entry_metadata: Entry = {
            "title": file_data.get("title", ""),
            "last_modified": file_data.get("last_modified", 0),
            "size": file_data.get("size", 0),
            "tags": markdown_metadata.get("tags", []),
            "body": markdown_metadata.get("body", ""),
        }

        return entry_metadata
