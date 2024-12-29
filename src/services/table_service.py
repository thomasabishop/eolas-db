from termcolor import colored

from models.entry import IEntry
from services.sqlite_service import SqliteService
from sql.create_tables import tables


class TableService(SqliteService):
    def __init__(self, db_connection):
        super().__init__(db_connection)

    def __create_tables(self):
        for table in tables:
            self._execute(
                table["create_statement"],
                error_message=f"Problem creating table {table['name']}",
            )
        print(colored("INFO Created tables", "blue"))

    def __drop_tables(self):
        # Reverse the order of `tables` list to avoid foreign key violation when
        # deleting
        for table in reversed(tables):
            self._execute(
                f"DROP TABLE IF EXISTS {table['name']}",
                error_message=f"Problem truncating table {table['name']}",
            )
        print(colored("INFO Cleared tables", "blue"))

    def __entry_exists(self, title) -> bool:
        self._execute("SELECT 1 FROM entries WHERE title = :title", {"title": title})
        result = self.cursor.fetchone()
        return result is not None

    def __populate_base_tables(self, entries: list[IEntry]):
        for entry in entries:
            self._execute(
                "INSERT INTO entries (title, last_modified, size, body) VALUES (:title, :last_modified, :size, :body)",
                entry,
                error_message=f"The following entry could not be added to `entries` table: {entry}",
            )
            tags = entry.get("tags")
            if tags:
                for tag in tags:
                    self._execute(
                        "INSERT OR IGNORE INTO tags (name) VALUES (:tag_name)",
                        {"tag_name": tag},
                    )

        print(colored("INFO Base tables populated", "blue"))

    def __populate_junction_tables(self, entries: list[IEntry]):
        for entry in entries:
            tags = entry.get("tags")
            links = entry.get("links")
            if tags:
                for tag in tags:
                    self._execute(
                        "INSERT INTO entries_tags (entry_title, tag_name) VALUES (:entry_title, :tag_name)",
                        {"entry_title": entry.get("title"), "tag_name": tag},
                    )
            if links:
                for link in links:
                    if self.__entry_exists(link):
                        self._execute(
                            "INSERT OR IGNORE INTO backlinks (source_entry_title, target_entry_title) VALUES (:source_entry_title, :target_entry_title)",
                            {
                                "source_entry_title": entry.get("title"),
                                "target_entry_title": link,
                            },
                        )

        print(colored("INFO Junction tables populated", "blue"))

    def populate_tables(self, entries: list[IEntry]):
        self.__drop_tables()
        self.__create_tables()
        self.__populate_base_tables(entries)
        self.__populate_junction_tables(entries)
