from flask import render_template, request, redirect, url_for, make_response
from auth import RegUser
from data import ShortenedURL, get_urls


user_info = {}


def register():
    new_user = RegUser(request.form['email'], request.form['password'])
    new_user.create_user()
    return redirect(url_for('home'))


def login():
    if request.form['email'] is None or request.form['password'] is None:
        return redirect(url_for('home'))
    else:
        logged_user = RegUser(request.form['email'], request.form['password'])
        logged_user.login_user()

        if logged_user.id > 0:
            user_info['userID'] = logged_user.id
            user_info['userEmail'] = logged_user.email

            resp = make_response(redirect(url_for('dashboard')))
            resp.set_cookie('userEmail', logged_user.email)

            return resp
        else:
            return redirect(url_for('home'))


def home():
    try:
        user_info.pop('userID')
        user_info.pop('userEmail')
    except:
        print('New Login')

    return render_template('auth.html', auth_message='Sign In', action_route='auth/login')


def registration():
    return render_template('auth.html', auth_message='Sign Up', action_route='auth/register')


def dashboard():
    if request.cookies.get('userEmail'):
        urls = get_urls(user_info['userID'])
        return render_template('dashboard.html', user_email=user_info['userEmail'], urls=urls)
    else:
        return redirect(url_for('home'))


def addurl():
    add_candidate = ShortenedURL(request.form['long'], request.form['short'])
    add_candidate.creator = user_info['userID']
    add_candidate.add_url()

    return render_template('product.html', product_banner='Successfully Added URL', is_del=False, candidate=add_candidate)


def delurl():
    del_candidate = ShortenedURL(request.form['long'], request.form['short'])
    del_candidate.del_url()

    return render_template('product.html', product_banner='Deleted URL', is_del=True, candidate=del_candidate)
