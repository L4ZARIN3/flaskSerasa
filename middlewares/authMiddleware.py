from flask import session, redirect, url_for
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # se o usuário não estiver logado, redirecione para a página de login
            return redirect(url_for('indexLogin'))
        return f(*args, **kwargs)
    return decorated_function
