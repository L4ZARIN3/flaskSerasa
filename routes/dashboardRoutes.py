from flask import request

from middlewares.authMiddleware import login_required
from controllers.admin.DashboardController import index, create


def DashboardRoutes(app):

    @app.route('/dashboard', methods=['get'], endpoint='dashboardIndex')
    @login_required
    def dashboard():
        return index()

    @app.route('/createClient', methods=['post'], endpoint='createClient')
    @login_required
    def createDashboard():
        return create(request)
