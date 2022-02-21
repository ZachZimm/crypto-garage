import logging
from flask import Flask, flash, Response, redirect, request, render_template, url_for, send_from_directory, jsonify
from wsgiref.simple_server import make_server
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, reqparse
import time
import pyfirmata

# from api.HelloApiHandler import HelloApiHandler

app = Flask(__name__, static_url_path='',static_folder='frontend/build')

# CORS(app, resources={r'/pulse/*': {"origins": "*"}})
CORS(app, 
    origins=["*"],
    methods=["OPTIONS", "GET", "POST"],
    allow_headers=["Content-Type"])
#app.config['CORS_HEADERS'] = 'Content-Type'
# api = Api(app)
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('flask-cors').level = logging.DEBUG
board = pyfirmata.Arduino('/dev/ttyACM0')
# api.add_resource(HelloApiHandler, '/flask/hello')

@app.route("/api/",defaults={'path': ''},methods=["POST","GET"])
@app.route("/api/<path:path>",methods=["POST","GET"])
@cross_origin(origins=["*"])
def serve(path):
    # if(request.method == "POST"):
    #     pulse()
    data = {"name":"Sean"}
    if(request.method == "GET"): return data
    return render_template(app.static_folder + '/index.html', data=data)

@app.route("/post/",defaults={'path':''}, methods=["GET","POST"])
@app.route("/post/<path:path>",methods=["POST","GET"])    
@cross_origin(origins=["*"])
def post(path):
    content = request.json['name']
    print(content)
    return request.json
    
@app.route("/pulse/",defaults={'path':''}, methods=["GET", "POST"])
@app.route("/pulse/<path:path>",methods=["POST","GET"])    
@cross_origin(origins=["*"])
def pulse(path):
    print(".pulse")
    if(request.method == "POST"):
        print("Pulse!")
        board.digital[12].write(1)
        time.sleep(1)
        board.digital[12].write(0)

    return {"name":"Pulse!"}




if __name__ == "__main__":
    import host_meta
    app.run(debug=True, host='0.0.0.0')
    


