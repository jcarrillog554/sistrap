#!flask/bin/python
from flask import Flask, request, jsonify, json, Response
import hashlib
import datetime
import requests
from Autobus import *
from Automovil import *
from Avion import *


app = Flask(__name__)

json_var = {
    "widget":
        {
            "debug": "on",
            "window": {
                "title": "Sample Konfabulator Widget",
                "name": "main_window",
                "width": 500,
                "height": 500
            },
            "image": {
                "src": "Images/Sun.png",
                "name": "sun1",
                "hOffset": 250,
                "vOffset": 250,
                "alignment": "center"
            },
            "text": {
                "data": "Click Here",
                "size": 36,
                "style": "bold",
                "name": "text1",
                "hOffset": 250,
                "vOffset": 100,
                "alignment": "center",
                "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
            }

        }
}

def create_hash(value):
    val = value + datetime.datetime.now().isoformat()
    return hashlib.sha1(val).hexdigest()

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.route('/')
def index():
    json_result = json_var
    js = json.dumps(json_result)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://sistra.com'

    return resp


@app.route('/automovil')
def ruta_automovil():
    param1 = request.args('inicio')
    param2 = request.args('fin')
    js = shortest_pathAutomovil(param1, param2)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://sistra.com'

    return resp

@app.route('/autobus')
def ruta_automovil():
    param1 = request.args('inicio')
    param2 = request.args('fin')
    js = shortest_pathAutobus(param1, param2)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://sistra.com'

    return resp

@app.route('/avion')
def ruta_automovil():
    param1 = request.args('inicio')
    param2 = request.args('fin')
    js = shortest_pathAvion(param1, param2)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://sistra.com'

    return resp


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
