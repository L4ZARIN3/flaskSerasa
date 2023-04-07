from flask import Flask, request, jsonify, Response, stream_with_context

from routes import route

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

route(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5555', debug=True)
