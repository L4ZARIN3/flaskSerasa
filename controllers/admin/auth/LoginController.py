from flask import render_template, session, redirect, url_for
from peewee import *
from models.system import Admins

from helpers.hash import generate_hash


def index():
    return render_template('auth/login.html')


def login(request):
    username = request.form.get('username')
    password = generate_hash(request.form.get('password'))

    try:
        usuario = Admins.get(Admins.username == username,
                             Admins.password == password)
        session['user_id'] = usuario.id
        return redirect(url_for('dashboardIndex'))
    except:
        return 'nao logou'
        # return redirect(url_for('loginIndex'))
