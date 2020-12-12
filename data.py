from flask import session
from dbcon import DbCon


class ShortenedURL:
    def __init__(self, long, short):
        self.id = 0
        self.long = long
        self.short = short

    def add_url(self):
        add_new = f"INSERT INTO urls(long, short) VALUES('{ self.long }', '{ self.short }');"

        add_con = DbCon(add_new)
        add_con.single_execute()

    def del_url(self):
        del_existing = f"DELETE FROM urls WHERE short = '{self.short}' AND long = '{self.long}';"

        del_con = DbCon(del_existing)
        del_con.single_execute()
