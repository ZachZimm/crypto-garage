import imp
import sys
import io
import random
import logging
from flask import Flask, flash, Response, redirect, request, render_template, url_for, send_from_directory, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, reqparse
import time
import pyfirmata
from api.HelloApiHandler import HelloApiHandler

app = Flask(__name__, static_url_path='',static_folder='frontend/build')
# CORS(app, resources={r"/flask/*": {"origins": "*"}})
CORS(app, origins=["http://127.0.0.1:3000","http://192.168.1.196:3000","http://192.168.1.196:5000","http://localhost:3000","http://127.0.0.1:5000","http://127.0.0.1:5000/flask/hello"])#,"http://192.168.1.196:5000","http://box:3000","http://localhost:3000","http://localhost:5000", "http://192.168.1.212:3000", "http://obsidione:3000/", "http://192.168.1.251"])
#app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('flask-cors').level = logging.DEBUG

# board = pyfirmata.Arduino('/dev/ttyACM0')
api.add_resource(HelloApiHandler, '/flask/hello')

api_v2_cors_config = {
    "origins": ["http://192.168.1.196:3000","http://box:3000","http://localhost:3000","http://localhost:5000", "http://127.0.0.1:5000" "http://192.168.1.212:3000", "http://obsidione:3000/", "http://192.168.1.251"],
    "methods": ["OPTIONS", "GET", "POST"],
    "allow_headers": ["Authorization", "Content-Type"]
    }

@app.route("/",defaults={'path':''}, methods=["GET"])
# @cross_origin(**api_v2_cors_config)
def serve(path):
    # if(request.method == "POST"):
    #     pulse()
    # return render_template("index.html")

    # return "Felix!"
    return send_from_directory(app.static_folder, 'index.html')
    
def pulse():
    print("Pulse!")
    # board.digital[12].write(1)
    # time.sleep(1)
    # board.digital[12].write(0)

if __name__ == "__main__":
    # import webbrowser
    # webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True, host='0.0.0.0')

