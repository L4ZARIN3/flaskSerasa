from flask import Flask, request, render_template

from controllers.admin.auth.LoginController import index


def DashboardRoutes(app):

    @app.route('/login', methods=['GET'], endpoint='indexLogin')
    def loginIndex():
       return index()


    @app.route('/login', methods=['POST'], endpoint='makeLogin')
    def login():
       return 