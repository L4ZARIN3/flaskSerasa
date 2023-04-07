from flask import Flask, render_template, request, redirect, url_for, session
from peewee import *
from models.system import Admins

from helpers.hash import generate_hash


def index():
    return render_template('login.html')


def login(request):
    username = request.form.get('username')
    password = generate_hash(request.form.get('password'))

    try:
        usuario = Admins.get(Admins.username == username, Admins.password == password)
        session['usuario'] = usuario.password
        return 'logou'
    except:
        return 'nao logou'
        # return redirect(url_for('loginIndex'))
    
    
    