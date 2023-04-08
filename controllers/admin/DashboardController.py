from flask import render_template, jsonify, session, redirect, url_for
from models.system import Tokens
import uuid

from requests.createClient import createUserRequest

def index():
    clients = Tokens.select()
    return render_template('dashboard.html', clients=clients)

def create(request):
    form = createUserRequest(request.form)
    if not form.validate():
        return jsonify(form.errors), 400
    
    username = request.form.get('username')
    plan = request.form.get('plan')
    
    client = Tokens(admin_id=session['user_id'], username=username, token=uuid.uuid4(), plan=plan)
    client.save()

    return redirect(url_for('dashboardIndex'))  
    