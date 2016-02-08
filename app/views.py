from app import app
# from app import babel
from flask import render_template, request, g
# from config import LANGUAGES
# from flask.ext.babel import gettext

# @babel.localeselector
# def get_locale():
    # return request.accept_languages.best_match(LANGUAGES.keys())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/survey_bn")
def survey():
    return render_template("survey_bn.html")

@app.route("/survey_hi")
def survey_hi():
    return render_template("survey_hi.html")

@app.route("/survey_en")
def survey_en():
    return render_template("survey_en.html")
