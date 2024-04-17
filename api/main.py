from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Set a secret key for session management


# Function to set session language
@app.route("/set_language/<lang>")
def set_language(lang):
    session["language"] = lang
    return redirect(request.referrer or "/")


# Function to get session language
def get_language():
    return session.get("language", "ro")  # Default to English if language is not set


@app.route("/")
def index():
    current_language = get_language()
    return render_template(
        f"/{get_language() }/index.html", current_language=current_language.upper()
    )


# Routes for English pages# Routes for English pages
@app.route("/consultancy-for-operators")
@app.route("/consultancy-for-authorities")
@app.route("/accounting-expertise")
@app.route("/accounting")
@app.route("/about")
@app.route("/cookies")
def english_routes():
    session["language"] = "en"
    return render_template(f"/en/{request.path[1:]}.html")


# Routes for Romanian pages
@app.route("/consultanta-pentru-operatori-economici")
@app.route("/consultanta-autoritati-contractante")
@app.route("/expertiza-contabila")
@app.route("/contabilitate")
@app.route("/despre-noi")
@app.route("/cookieuri")
def romanian_routes():
    session["language"] = "ro"
    return render_template(f"/ro/{request.path[1:]}.html")

 
