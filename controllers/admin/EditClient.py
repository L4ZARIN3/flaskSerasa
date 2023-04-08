from flask import render_template, jsonify, redirect, url_for
from peewee import DoesNotExist

from models.system import Tokens

from requests.editClientRequest import editUserRequest

def editIndex(id):
    try:
        client = Tokens.get(Tokens.id == id)
        return render_template('editClient.html', client=client)
    except DoesNotExist:
        return '404'
    
def makeEdit(request):
    form = editUserRequest(request.form)
    if not form.validate():
        return jsonify(form.errors), 400
    
    id = request.form.get('id')
    username = request.form.get('username')
    plan = request.form.get('plan')
    
    client = Tokens.get(Tokens.id == id)
    client.username = username
    client.plan = plan
    client.save()
    
    return editIndex(id) 