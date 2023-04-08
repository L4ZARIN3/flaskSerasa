from flask import jsonify, request
from functools import wraps
from models.system import Tokens
from datetime import datetime

def client(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        clientToken = request.args.get('token')
        userToken  = Tokens.select().where(Tokens.token == clientToken).get()
        if userToken:
            data = datetime.strptime(userToken.plan, '%Y-%m-%dT%H:%M')
            data_formatada = data.strftime('%Y-%m-%d %H:%M:%S.%f')
            dataObject = datetime.strptime(data_formatada, '%Y-%m-%d %H:%M:%S.%f')
            
            
            if dataObject >= datetime.now():
                return f(*args, **kwargs)
            else:
                return jsonify({'status': False, 'msg': 'plano expirado.', 'plan': data_formatada})    
        else:
            return jsonify({'status': False, 'msg': 'token invalido.'})
    return decorated_function
