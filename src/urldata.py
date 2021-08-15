from flask import session
from .dbcon import DBCon


# Get List of URLs for User
def get_urls(id):
    get_url_list = f"SELECT long, short FROM urls WHERE userID = { id };"

    get_con = DBCon(get_url_list)
    urls_list = get_con.lookup_execute("long", "short")

    return urls_list


# Class for URL Data
class ShortenedURL:
    def __init__(self, long, short):
        self.id = 0
        self.long = long
        self.short = short
        self.creator = 0

    # Add New URL
    def add_url(self):
        add_new = f"INSERT INTO urls(long, short, userID) VALUES('{self.long}', '{self.short}', {self.creator});"

        add_con = DBCon(add_new)
        add_con.single_execute()

    # Delete Existing URL
    def del_url(self):
        del_existing = f"DELETE FROM urls WHERE short = '{self.short}' AND long = '{self.long}';"

        del_con = DBCon(del_existing)
        del_con.single_execute()
