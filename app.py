from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/README")
def readme():
    return "<h1>This will be the README page</h1>"


@app.route("/album")
def album():
    return render_template("album.html")


if __name__ == '__main__':
    app.run(debug=True)