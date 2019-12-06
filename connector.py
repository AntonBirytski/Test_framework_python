import sqlite3

class Connector:
    def __init__(self, database_path):
        connect = sqlite3.connect(database_path)
        self.cursor = connect.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
