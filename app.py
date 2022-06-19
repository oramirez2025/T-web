# import flask libraries
from flask import Flask, jsonify, render_template, request, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
app = Flask(__name__)
app.secret_key = "3.1415"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
class userInfo(db.Model):
    #Unique identifcation (as an int) for each object in the model 
    _id = db.Column("id", db.Integer, primary_key=True)
    #Store the user's email and password
    email = db.Column("email", db.String(100))
    password = db.Column("password",db.String(100))
    def __init__(self, email, password):
        self.email = email
        self.password = password

# flask run -> server runs at http://127.0.0.1:5000 
@app.route("/")
def homepage():
    return render_template("index.html")
@app.route("/selection")
def selection():
    return render_template("selection.html")
@app.route("/log-in")
def login():
    return render_template("log-in.html")

@app.route("/sign-up",methods=["POST","GET"])
def signup():
    if request.method == "GET":
        return render_template("sign-up.html")
    #request.method == "POST"
    else: 
        email = request.form["email"]
        #Finds the user in the database
        found_user = userInfo.query.filter_by(email=email).first()
        if found_user:
            flash("This account has already been made!")
            flash("Navigate to the log-in page to log in")
            return render_template("sign-up.html")
        else:
            #Store the email and password into the database
            user = userInfo(email,request.form["password"])
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("homepage"))
db.create_all()
        