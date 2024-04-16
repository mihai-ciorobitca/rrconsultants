from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contability")
def contability():
    return render_template("contability.html")


@app.route("/cookies")
def cookies():
    return render_template("cookies.html")


@app.route("/management")
def management():
    return render_template("management.html")


@app.route("/survey")
def survey():
    return render_template("survey.html")


@app.route("/authority")
def authority():
    return render_template("authority.html")

app.run()
