from typing import Optional


class SqliteService:
    def __init__(self, db_connection):
        self.connection = db_connection
        self.cursor = db_connection.cursor()

    def _execute(self, sql, params=None, error_message: Optional[str] = None):
        """Use for CREATE, INSERT, UPDATE, DELETE"""
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            if error_message:
                raise Exception(f"ERROR {error_message}: {e}")
            raise

    def _query(self, sql, params=None, error_message: Optional[str] = None):
        """Use for SELECT"""
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            return self.cursor.fetchall()

        except Exception as e:
            if error_message:
                raise Exception(f"ERROR {error_message}: {e}")
            raise
