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

tables = [
    {"name": "entries", "create_statement": CREATE_ENTRIES_TABLE},
    {"name": "tags", "create_statement": CREATE_TAGS_TABLE},
    {"name": "backlinks", "create_statement": CREATE_BACKLINKS_TABLE},
    {"name": "entries_tags", "create_statement": CREATE_ENTRIES_TAGS_TABLE},
]
