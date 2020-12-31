from flask import session
from dbcon import DbCon


def get_urls(id):
    get_url_list = f"SELECT long, short FROM urls WHERE userID = { id };"

    get_con = DbCon(get_url_list)
    urls_list = get_con.lookup_execute("long", "short")

    return urls_list


class ShortenedURL:
    def __init__(self, long, short):
        self.id = 0
        self.long = long
        self.short = short
        self.creator = 0

    def add_url(self):
        add_new = f"INSERT INTO urls(long, short, userID) VALUES('{ self.long }', '{ self.short }, { self.creator }');"

        add_con = DbCon(add_new)
        add_con.single_execute()

    def del_url(self):
        del_existing = f"DELETE FROM urls WHERE short = '{self.short}' AND long = '{self.long}';"

        del_con = DbCon(del_existing)
        del_con.single_execute()
