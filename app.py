# import flask libraries
from flask import Flask, jsonify, request
app = Flask(__name__)

# flask run -> server runs at http://127.0.0.1:5000 
@app.route("/")
def hello():
    return "Welcome to the home page!"