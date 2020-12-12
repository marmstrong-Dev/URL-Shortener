from flask import Flask
from dbcon import DbCon
import os.path
import routes


app = Flask(__name__, static_folder='public')
app.secret_key = '#43fivikx'

init_con = DbCon('')
init_con.init_tables()

# Routes
app.add_url_rule('/', view_func=routes.home, methods=['GET'])
app.add_url_rule('/signup', view_func=routes.registration, methods=['GET'])
app.add_url_rule('/dashboard', view_func=routes.dashboard, methods=['GET'])
app.add_url_rule('/auth/register', view_func=routes.register, methods=['POST'])
app.add_url_rule('/auth/login', view_func=routes.login, methods=['POST'])
app.add_url_rule('/product/addurl', view_func=routes.addurl, methods=['POST'])
app.add_url_rule('/product/delurl', view_func=routes.delurl, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
