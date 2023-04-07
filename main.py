from flask import Flask

from routes.serasaRoutes import SerasaBase
from routes.dashboardRoutes import DashboardRoutes

app = Flask(__name__,template_folder='views')
app.secret_key = 'harryporra'
app.config['JSON_SORT_KEYS'] = False

SerasaBase(app)
DashboardRoutes(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5555', debug=True)
