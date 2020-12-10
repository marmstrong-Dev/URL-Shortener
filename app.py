from flask import Flask
import json
import os.path
import routes

app = Flask(__name__, static_folder='public')
app.secret_key = '#43fivikx'

# Routes
app.add_url_rule('/', view_func=routes.home)
app.add_url_rule('/product', view_func=routes.product)
app.add_url_rule('/product/addurl', view_func=routes.addurl, methods=['POST'])
app.add_url_rule('/product/delurl', view_func=routes.delurl, methods=['POST'])


if __name__ == '__main__':
   app.run(debug = True)
