from flask import Flask
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from dbcon import DbCon


class RegUser:
    def __init__(self, email, password):
        self.id = 0
        self.email = email
        self.password = password

    def create_user(self):
        self.password = generate_password_hash(self.password, method='sha256')
        register_query = f"INSERT INTO users (email, password) VALUES ('{ self.email }', '{ self.password }');"

        register_con = DbCon(register_query)
        register_con.single_execute()

    def login_user(self):
        login_query = f"SELECT userID, password FROM users WHERE email = '{ self.email }';"

        login_con = DbCon(login_query)
        user_data = login_con.lookup_execute('userID', 'password')

        if len(user_data) == 0:
            return
        else:
            if check_password_hash(user_data[0]['password'], self.password):
                self.id = user_data[0]['userID']
                return
            else:
                return

