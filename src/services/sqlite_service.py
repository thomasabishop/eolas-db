import sqlite3
from typing import Optional

from termcolor import colored

from models.entry import Entry
from sql.create_tables import tables


class SqliteService:
    def __init__(self, db_connection):
        self.connection = db_connection
        self.cursor = db_connection.cursor()

    def _query(self, sql, params=None, errorMessage: Optional[str] = None):
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            if errorMessage:
                raise Exception(f"ERROR {errorMessage}: {e}")
            raise
