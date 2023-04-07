from flask import Flask, request

from controllers.admin.auth.LoginController import index, login


def DashboardRoutes(app):

    @app.route('/login', methods=['GET'], endpoint='indexLogin')
    def loginIndex():
        return index()

    @app.route('/login', methods=['POST'], endpoint='makeLogin')
    def loginMake():
        return login(request)
