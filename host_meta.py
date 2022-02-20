from __main__ import app
# from flask import current_app as app
import sys
import io
import random
import logging
import json
from flask import Flask, flash, Response, redirect, request, render_template, url_for
from flask_cors import cross_origin

HEADS_TAILS = True

@app.route("/host/",defaults={'path': ''},methods=["POST","GET"])
@app.route("/host/<path:path>",methods=["POST","GET"])
@cross_origin(origins=["*"])
def meta_route(path):
    filepath = app.static_folder + '/data/'

    if(HEADS_TAILS):
        if(path == ''):
            path = "0"
        if((int(path) + 2) % 2 == 0):
            path = "0"
        else:
            path = "1"

    if(path != ''):
        path = str(int(path))
        filepath = filepath +'id'+path+'.json'
    else:
        filepath = filepath + 'sean_meta.json'
    metadata = open(filepath)
    metadata = json.load(metadata)
    # if(request.method == "GET"): return path
    
    # metadata.header['Access-Control-Allow-Origin'] = '*'
    # metadata.header['Access-Control-Allow-Headers'] = 'Content-Type'
    # metadata.headers.add("Access-Control-Allow-Headers","*")
    # metadata.headers.add("Access-Control-Allow-Origin","127.0.0.1:5000")
    metadata = {"name":"Felix"}

    if(request.method == "GET"): return metadata

    # return render_template("meta.html", meta=metadata)
    
    return metadata
