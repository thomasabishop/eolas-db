from typing import List, TypedDict


class Entry(TypedDict):
    title: str
    last_modified: str
    size: int
    tags: List[str]
    links: List[str]
    body: str
