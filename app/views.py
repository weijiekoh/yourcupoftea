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
    from questions import questions
    return render_template("survey_en.html", questions=questions)

@app.route("/results", methods=["POST"])
def results():
    import ranking
    from questions import questions
    from parties import parties

    import pprint
    pprint.pprint(request.form.lists())

    results = ranking.calculate(request.form.lists(), parties, questions)
    import pprint
    form_data = pprint.pformat(request.form.lists())
    print form_data
    return render_template("results.html", 
            results=results, parties=parties)
