from flask import Flask

app = Flask(__name__, static_folder='public')
app.secret_key = '#43fivikx'

from src import router
from src.dbcon import DBCon

# Initial DB and Table Creation
init_con = DBCon('')
init_con.init_tables()

# Routes
app.add_url_rule('/', view_func=router.home, methods=['GET'])
app.add_url_rule('/signup', view_func=router.registration, methods=['GET'])
app.add_url_rule('/dashboard', view_func=router.dashboard, methods=['GET'])
app.add_url_rule('/auth/register', view_func=router.register, methods=['POST'])
app.add_url_rule('/auth/login', view_func=router.login, methods=['POST'])
app.add_url_rule('/product/addurl', view_func=router.addurl, methods=['POST'])
app.add_url_rule('/product/delurl', view_func=router.delurl, methods=['POST'])
