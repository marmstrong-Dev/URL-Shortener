from flask import session
import sqlite3
from sqlite3 import Error

dataFile = 'urls.db'

class DataCon:
    def table_creation():        
        conn = sqlite3.connect(dataFile)

        cur = conn.cursor()
        init_tables = 'CREATE TABLE IF NOT EXISTS urls (urlID INTEGER PRIMARY KEY AUTOINCREMENT, long TEXT, short TEXT);'
        cur.execute(init_tables)
        
        conn.close()
