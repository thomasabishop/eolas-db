CREATE_ENTRIES_TABLE = """
CREATE TABLE IF NOT EXISTS entries (
    title TEXT PRIMARY KEY UNIQUE, 
    last_modified STRING, 
    size INTEGER, 
    body TEXT
)
"""

CREATE_TAGS_TABLE = """
CREATE TABLE IF NOT EXISTS tags (
    name TEXT PRIMARY KEY UNIQUE
)
"""

CREATE_BACKLINKS_TABLE = """
CREATE TABLE IF NOT EXISTS backlinks (
    source_entry_title TEXT,
    target_entry_title TEXT,
    FOREIGN KEY (source_entry_title) REFERENCES entries(title),
    FOREIGN KEY (target_entry_title) REFERENCES entries(title),
    PRIMARY KEY (source_entry_title, target_entry_title) 
)
"""


CREATE_ENTRIES_TAGS_TABLE = """
CREATE TABLE IF NOT EXISTS entries_tags (
    entry_title TEXT,
    tag_name TEXT,
    FOREIGN KEY (entry_title) REFERENCES entries(title),
    FOREIGN KEY (tag_name) REFERENCES tags(name),
    PRIMARY KEY (entry_title, tag_name)
)"""

CREATE_BROKEN_LINKS_TABLE = """
CREATE TABLE IF NOT EXISTS broken_links (
    source_entry_title TEXT, broken_link_title TEXT,
    FOREIGN KEY (source_entry_title) REFERENCES entries(title),
    PRIMARY KEY (source_entry_title, broken_link_title)
    )
"""


CREATE_ENTRIES_FTS_TABLE = """
    CREATE VIRTUAL TABLE entries_fts USING fts5(title, body, content=entries, content_rowid=rowid)
"""


tables = [
    {"name": "entries", "create_statement": CREATE_ENTRIES_TABLE},
    {"name": "tags", "create_statement": CREATE_TAGS_TABLE},
    {"name": "backlinks", "create_statement": CREATE_BACKLINKS_TABLE},
    {"name": "entries_tags", "create_statement": CREATE_ENTRIES_TAGS_TABLE},
    {"name": "entries_fts", "create_statement": CREATE_ENTRIES_FTS_TABLE},
    {"name": "broken_links", "create_statement": CREATE_BROKEN_LINKS_TABLE},
]
