from flask import session, redirect, url_for
from functools import wraps

def guest(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # se o usuário não estiver logado, redirecione para a página de login
            return f(*args, **kwargs)
        return redirect(url_for('dashboardIndex'))
    return decorated_function
