# import flask libraries
from flask import Flask, jsonify, render_template, request, redirect, url_for
app = Flask(__name__)
# flask run -> server runs at http://127.0.0.1:5000 
@app.route("/")
def homepage():
    return render_template("index.html")
@app.route("/selection")
def selection():
    return render_template("selection.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/signup")
def signup():
    return render_template("signup.html")