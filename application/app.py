"""
    This file is the main app.  
    Created as a means of quickly building and testing Flask application.

    Eventually, this file will be removed and the entry point of the application
    will be wsgi.py.  Until then this will remain.
"""
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/info")
def info():
    return render_template("info.html")


if __name__ == '__main__':
    app.run(debug=True)