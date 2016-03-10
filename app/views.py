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

    results = ranking.calculate(request.form.lists(), parties, questions)
    import pprint
    form_data = pprint.pformat(request.form.lists())
    print form_data
    return render_template("results.html", 
            results=results, parties=parties,
            smart_share_url=smart_share_url(results))


base64_regex = "^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$"
@app.route("/results/<base64_result>", methods=["GET"])
def results_for_fb(base64_result):
    import re
    if re.findall(base64_regex, base64_result):
        import base64
        try:
            return render_template("result_fb_share.html", 
                    result_fb_str=result_fb_str(base64.decodestring(base64_result)))
        except (UnicodeDecodeError, AssertionError) as e:
            return render_template("index.html")
    else:
        return render_template("index.html")


class InvalidShareString: pass

def result_fb_str(result_str):
    # TODO: input verification
    from parties import parties
    import re
    # data verification
    veri_regex = "(?:\d:[\d\.]{2,4},){" + str(len(parties)-1) + "}\d:[\d\.]{2,4}"
    # matches something like 0:74.3,1:70.0,2:88.0,3:67.7, depending on the no. of parties in parties.py
    assert len(re.findall(veri_regex, result_str)) > 0, "Invalid sharer url"
    display = ""
    sorted_parties = sorted([int(x.split(":")[0]) for x in sorted(result_str.split(","))])

    # make sure the input includes all the parties we have and only these parties
    assert sorted_parties == sorted(parties.keys()), "Invalid sharer url"

    for party in sorted(result_str.split(",")):
        s = party.split(":")
        party_id = int(s[0])
        party_score = s[1]
        display += "%s: %s%%, " % (parties[party_id]["initials"], party_score)

    return display[:len(display)-2]


def smart_share_url(results):
    from parties import parties
    import base64
    url = ""
    for party_id, result in results.iteritems():
        url += "%d:%.1f," % (party_id, round(result, 1))

    encoded = base64.encodestring(url[:len(url)-1])
    return encoded[:len(encoded)-1]
