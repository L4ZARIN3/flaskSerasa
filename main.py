from flask import Flask

from routes.serasaRoutes import SerasaBase
from routes.dashboardRoutes import DashboardRoutes
from routes.authRoutes import authRoutes


app = Flask(__name__,template_folder='views')
app.secret_key = 'harryporra'
app.config['JSON_SORT_KEYS'] = False

SerasaBase(app)
DashboardRoutes(app)
authRoutes(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8091', debug=True)
