from flask import request

from controllers.admin.DashboardController import index, create
from controllers.admin.EditClient import editIndex, makeEdit

from middlewares.authMiddleware import login_required


def DashboardRoutes(app):

    @app.route('/dashboard', methods=['get'], endpoint='dashboardIndex')
    @login_required
    def dashboard():
        return index()

    @app.route('/createClient', methods=['post'], endpoint='createClient')
    @login_required
    def createDashboard():
        return create(request)

    @app.route('/edit/<int:id>', methods=['get'], endpoint='editClient')
    @login_required
    def editClientdashboard(id):
        return editIndex(id)

    @app.route('/edit/make', methods=['post'], endpoint='editClientMake')
    @login_required
    def editClientMake():
        return makeEdit(request)
