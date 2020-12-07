from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
import routes

app = Flask(__name__, static_folder='public')
app.secret_key = '#43fivikx'

#Routes
app.add_url_rule('/', view_func=routes.home)
app.add_url_rule('/product', view_func=routes.product)


#@app.route('/product', methods=['GET', 'POST'])
#def product():
#    if request.method == 'POST':
#        urls = {}
#
#        #If urls.json exists add to existing file, otherwise creates new urls.json
#        if os.path.exists('urls.json'):
#            with open('urls.json') as urls_file:
#                urls = json.load(urls_file)
#
#        #Checks if name already exists in urls.json. If so, error message is displayed
#        if request.form['short'] in urls.keys():
#            flash('That name is already registered')
#            return redirect(url_for('home'))
#
#        urls[request.form['short']] = {'long':request.form['long']}
#        with open('urls.json', 'w') as url_file:
#            json.dump(urls, url_file)
#        return render_template('product.html', short=request.form['short'])
#    else:
#        return redirect(url_for('home'))


if __name__ == '__main__':
   app.run(debug = True)
