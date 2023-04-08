from flask import request, redirect, url_for

from controllers.admin.auth.LoginController import index, login

from middlewares.guestMiddleware import guest


def authRoutes(app):

    @app.route('/', methods=['GET'], endpoint='homeGuest')
    @guest
    def redirectHome():
        return redirect(url_for('indexLogin'))

    @app.route('/login', methods=['GET'], endpoint='indexLogin')
    @guest
    def loginIndex():
        return index()

    @app.route('/login', methods=['POST'], endpoint='makeLogin')
    @guest
    def loginMake():
        return login(request)
