from flask import session
import sqlite3
from sqlite3 import Error

dataFile = 'urls.db'


def single_execute(query):
    conn = sqlite3.connect(dataFile)

    cur = conn.cursor()
    cur.execute(query)

    conn.commit()
    conn.close()


def lookup_execute(query):
    results_list = []

    conn = sqlite3.connect(dataFile)

    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        added = {"long": row[0], "short": row[1]}
        results_list.append(added)

    conn.close()
    return results_list


class ShortenedURL:
    def __init__(self, long, short):
        self.long = long
        self.short = short

    def check_exists(self):
        check_query = f"SELECT short FROM urls WHERE short = '{self.short}';"
        lookup_results = lookup_execute(check_query)

        if lookup_results.len == 0:
            return False
        else:
            return True

    def add_url(self):
        add_new = f"INSERT INTO urls(long, short) VALUES('{ self.long }', '{ self.short }');"
        single_execute(add_new)

    def del_url(self):
        del_existing = f"DELETE FROM urls WHERE short = '{ self.short }' AND long = '{ self.long }';"
        single_execute(del_existing)
