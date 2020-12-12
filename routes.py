from flask import render_template, request, redirect, url_for, make_response
from auth import RegUser
from data import ShortenedURL


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
            resp = make_response(redirect(url_for('dashboard')))
            resp.set_cookie('userEmail', logged_user.email)
            return resp
        else:
            return redirect(url_for('home'))


def logout():
    return redirect(url_for('home'))


def home():
    return render_template('auth.html', auth_message='Sign In', action_route='auth/login')


def registration():
    return render_template('auth.html', auth_message='Sign Up', action_route='auth/register')


def dashboard():
    return render_template('dashboard.html', user_email=request.cookies.get('userEmail'))


def addurl():
    add_candidate = ShortenedURL(request.form['long'], request.form['short'])


def delurl():
    del_candidate = ShortenedURL(request.form['long'], request.form['short'])
