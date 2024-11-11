import sqlite3
from typing import Optional

from sql.create_tables import tables
from src.models.entry import Entry


class SqliteService:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def __query(self, sql, errorMessage: Optional[str] = None):
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except sqlite3.Error as sqliteError:
            raise Exception(f"ERROR SQLite: {sqliteError}")

        except Exception as e:
            if errorMessage:
                raise Exception(f"ERROR {errorMessage}: {e}")
            else:
                raise Exception(f"ERROR Problem with database operation: {e}")

    def create_tables(self):
        for table in tables:
            self.__query(
                table["create_statement"], f"Problem creating table {table['name']}"
            )
        print("INFO Created tables")

    def truncate_tables(self):
        for table in tables:
            self.__query(
                f"DELETE FROM {table['name']}",
                f"Problem truncating table {table['name']}",
            )
        print("INFO Cleared tables")
