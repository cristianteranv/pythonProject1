"""A simple flask web app"""
import os
from flask import Flask, request,flash
from flask import render_template
import pandas as pd
from calculator.calculator import Calculator

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route("/")
def index():
    """index  Route Response"""
    return render_template("index.html")

# pylint: disable=consider-using-with
@app.route("/calculate", methods=["GET","POST"])
def calculate():
    """calculation input page"""
    if request.method == "POST":
        value1 = request.form["value1"]
        value2 = request.form["value2"]
        operation = request.form["operation"]
        my_tuple = (value1, value2)
        try:
            getattr(Calculator, operation)(my_tuple)
            last_calc = Calculator.get_last_calculation()
            result = last_calc.get_result()
        except ZeroDivisionError:
            print("ZeroDivisionError")
            result = "ZeroDivisionError"
        cwd = os.getcwd()
        path = os.path.join(cwd, "app/static/csv/web_operations.csv")
        outfile = open(path, "a", encoding="utf-8")
        outfile.write(str(last_calc.values[0]) + "," + str(last_calc.values[1]) +
                   "," +  str(result) + "," + last_calc.operation + "\n")
        return render_template("calculate.html",
                               value1=value1,
                               value2=value2,
                               operation=last_calc.operation,
                               result=result)

    flash("Both values are required.")
    return render_template("calculate.html")

@app.route("/calculation_history")
def history():
    """history"""
    cwd = os.getcwd()
    path = os.path.join(cwd, "app/static/csv/web_operations.csv")
    operations = pd.read_csv(path, header=None)
    rows = operations.values.tolist()
    return render_template("calculation_history.html", rows=rows)

@app.route("/git")
def git():
    """git"""
    return render_template("git.html")

@app.route("/docker")
def docker():
    """docker"""
    return render_template("docker.html")

@app.route("/glossary")
def glossary():
    """glossary"""
    return render_template("glossary.html")

@app.route("/github")
def github():
    """github"""
    return render_template("github.html")

@app.route("/linux")
def linux():
    """linux"""
    return render_template("linux.html")

@app.route("/principles")
def principles():
    """principles"""
    return render_template("principles.html")

@app.route("/solid")
def solid():
    """solid"""
    return render_template("solid.html")

@app.route("/vi")
def vi_page():
    """vi"""
    return render_template("vi.html")

@app.route("/aaa")
def aaa():
    """aaa"""
    return render_template("aaa.html")
