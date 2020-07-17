from flask import Flask, render_template

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/info")
def info():
    return render_template("info.html")