from sql.create_tables import (
    CREATE_BACKLINKS_TABLE,
    CREATE_ENTRIES_TABLE,
    CREATE_ENTRIES_TAGS_TABLE,
    CREATE_TAGS_TABLE,
)


class SqliteService:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def create_tables(self):
        tables = [
            CREATE_ENTRIES_TABLE,
            CREATE_TAGS_TABLE,
            CREATE_BACKLINKS_TABLE,
            CREATE_ENTRIES_TAGS_TABLE,
        ]
        for create_statement in tables:
            self.cursor.execute(create_statement)

        self.connection.commit()

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(self.cursor.fetchall())
