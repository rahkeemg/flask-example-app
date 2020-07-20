from flask import render_template, url_for
from application import app


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/info")
def info():
    return render_template("info.html")
