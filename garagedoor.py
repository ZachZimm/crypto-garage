import sys
import io
import random
import logging
from flask import Flask, flash, Response, redirect, request, render_template, url_for
import time
import pyfirmata

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

board = pyfirmata.Arduino('/dev/ttyACM0')

@app.route("/",methods=["POST","GET"])
def index():
    if(request.method == "POST"):
        pulse()
    return render_template("index.html")

def pulse():
    board.digital[12].write(1)
    time.sleep(1)
    board.digital[12].write(0)

if __name__ == "__main__":
    # import webbrowser
    # webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True, host='0.0.0.0')
    app.debug = True
