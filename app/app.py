"""A simple flask web app"""
from flask import Flask, request,flash
from flask import render_template
import pandas
from calculator.calculator import Calculator

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route("/")
def index():
    """index  Route Response"""
    flash("flash test")
    return render_template("index.html")

@app.route("/calculate", methods=["GET","POST"])
def calculate():
    """calculation input page"""
    if request.method == "POST":
        print("this was a post")
        return render_template("calculate.html")
    else:
        return render_template("calculate.html")