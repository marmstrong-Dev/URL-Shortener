import sqlite3
from sqlite3 import Error


class DbCon:
    def __init__(self, query):
        self.dataFile = 'urls.db'
        self.query = query

    def single_execute(self):
        conn = sqlite3.connect(self.dataFile)
        cur = conn.cursor()
        cur.execute(self.query)

        conn.commit()
        conn.close()

    def lookup_execute(self, f1, f2):
        results_list = []

        conn = sqlite3.connect(self.dataFile)
        cur = conn.cursor()
        cur.execute(self.query)
        rows = cur.fetchall()

        for row in rows:
            added = {f1: row[0], f2: row[1]}
            results_list.append(added)

        conn.commit()
        conn.close()

        return results_list

    def init_tables(self):
        user_table = 'CREATE TABLE IF NOT EXISTS users (userID INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, password TEXT);'

        urls_table = """CREATE TABLE IF NOT EXISTS urls (
                        urlID INTEGER PRIMARY KEY AUTOINCREMENT, 
                        long TEXT,
                        short TEXT,
                        userID INTEGER,
                        FOREIGN KEY(userID) REFERENCES users(userID));"""

        conn = sqlite3.connect(self.dataFile)
        cur = conn.cursor()

        # Create New Tables if Not Existing
        cur.execute(user_table)
        cur.execute(urls_table)

        conn.commit()
        conn.close()
