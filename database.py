import sqlite3


class Database:
    def __init__(self):
        self.db_name = 'data.db'
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

    def migrate(self):
        table_entry = """
            CREATE TABLE IF NOT EXISTS [entry]
            (
                [Id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [EntryType] TEXT NOT NULL,
                [Name] TEXT NOT NULL,
                [FileId] TEXT,
                [ParentId] INTEGER,
                [Desc] TEXT,
                [Tags] TEXT 
            )
        """
        self.connection.execute(table_entry)

    def query(self, sql, params):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def query_single(self, sql, params):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()[0]

    def exec(self, command, params):
        self.cursor.execute(command, params)
