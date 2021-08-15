from flask_login import LoginManager
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash
from .dbcon import DBCon


# Class for Registered User
class RegUser:
    def __init__(self, email, password):
        self.id = 0
        self.email = email
        self.password = password

    # New User Creation Method
    def create_user(self):
        if self.email and self.password:
            self.password = generate_password_hash(self.password, method='sha256')
            register_query = f"INSERT INTO users (email, password) VALUES ('{self.email}', '{self.password}');"

            register_con = DBCon(register_query)
            register_con.single_execute()
        else:
            return

    # Login User Function
    def login_user(self):
        login_query = f"SELECT userID, password FROM users WHERE email = '{self.email}';"
        login_con = DBCon(login_query)
        user_data = login_con.lookup_execute('userID', 'password')

        if len(user_data) == 0:
            return
        else:
            if check_password_hash(user_data[0]['password'], self.password):
                self.id = user_data[0]['userID']
                return
            else:
                return
