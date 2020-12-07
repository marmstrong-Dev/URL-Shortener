from flask import render_template, request, redirect, url_for
from data import single_execute, lookup_execute, ShortenedURL


def home():
    init_tables = 'CREATE TABLE IF NOT EXISTS urls (urlID INTEGER PRIMARY KEY AUTOINCREMENT, long TEXT, short TEXT);'
    single_execute(init_tables)

    lookup_query = 'SELECT long, short FROM urls;'
    urls_list = lookup_execute(lookup_query)

    print(urls_list)
    return render_template('index.html', urls=urls_list)


def product(shorturl, longurl):
    return render_template('product.html', short=shorturl, long=longurl)


def addurl():
    candidate = ShortenedURL(request.form['long'], request.form['short'])

    if candidate.long is None and candidate.short is None:
        return redirect(url_for('home'))
    else:
        candidate.add_url()
        return render_template('product.html', short=candidate.short, long=candidate.long)


def delurl():
    candidate = ShortenedURL(request.form['long'], request.form['short'])

    if candidate.check_exists:
        candidate.del_url()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))
