import sqlite3
from typing import Optional

from termcolor import colored


class DatabaseService:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_path = "/home/thomas/repos/eolas-db/db"
        self.connection: Optional[sqlite3.Connection] = None

    def connect(self) -> Optional[sqlite3.Connection]:
        if self.connection is not None:
            return self.connection

        try:
            self.connection = sqlite3.connect(f"{self.db_path}/{self.db_name}.db")
            self.connection.execute("PRAGMA foreign_keys = ON")
            print(colored("INFO Database connection established", "light_blue"))
            return self.connection

        except Exception as e:
            raise Exception(f"ERROR Problem connecting to database: {e}")

    def disconnect(self) -> None:
        try:
            if self.connection is not None:
                self.connection.close()
                self.connection = None
        except Exception as e:
            raise Exception(f"ERROR Problem disconnecting from database: {e}")
