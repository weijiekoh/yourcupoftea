from app import app
# from app import babel
from flask import render_template, request, g, redirect, url_for
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
    return redirect(url_for("results") + "/" + smart_share_code(results))
    # return render_template("results.html", 
            # results=results, parties=parties,
            # smart_share_url=request.url + "/" + smart_share_code(results))


base64_regex = "^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$"
@app.route("/results/<base64_result>", methods=["GET", "POST"])
def results_for_fb(base64_result):
    import re
    if re.findall(base64_regex, base64_result):
        import base64
        try:
            import urlparse
            from parties import parties
            u = urlparse.urlparse(request.url)
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=u)
            fb_share_image = domain + "static/img/parties/at.png"
            raw_result_str = base64.decodestring(base64_result)
            sorted_results = smart_share_decode_and_sort(raw_result_str)
            result_share_str = "My top 3 party matches in the 2016 West Bengal Vidhan Sabha Election: " + format_share_str(sorted_results)

            return render_template("results.html", 
                    fb_share_image=fb_share_image,
                    result_share_str=result_share_str,
                   results=sorted_results, parties=parties)
        except (UnicodeDecodeError, AssertionError) as e:
            return render_template("index.html")
    else:
        return render_template("index.html")

def smart_share_decode_and_sort(raw_result_str):
    """
    Converts a result string like "p:xx.x;q:yy.y..." to a dict
    """
    from parties import parties
    import re
    # data verification
    veri_regex = "(?:\d:[\d\.]{2,4},){" + str(len(parties)-1) + "}\d:[\d\.]{2,4}"
    # matches something like 0:74.3,1:70.0,2:88.0,3:67.7, depending on the no. of parties in parties.py
    assert len(re.findall(veri_regex, raw_result_str)) > 0, "Invalid sharer url"
    display = ""
    sorted_parties = sorted([int(x.split(":")[0]) for x in sorted(raw_result_str.split(","))])

    # make sure the input includes all the parties we have and only these parties
    assert sorted_parties == sorted(parties.keys()), "Invalid sharer url"

    # sort by score, not party ID:
    score_sorted_results = []
    for r in raw_result_str.split(","):
        s = r.split(":")
        score_sorted_results.append((int(s[0]), float(s[1])))
    score_sorted_results = sorted(score_sorted_results, key=lambda x:x[1], reverse=True)
    return score_sorted_results


class InvalidShareString: pass

def format_share_str(sorted_results):
    """
    Formats a dict of party_id:score etc to "ABC: xx.x%, ..."
    """
    from parties import parties
    display = ""
    for s in sorted_results[:3]:
        party_id = int(s[0])
        party_score = s[1]
        display += "%s: %s%%, " % (parties[party_id]["initials"], party_score)

    return display[:len(display)-2]


def smart_share_code(results):
    from parties import parties
    import base64
    url = ""
    for party_id, result in results.iteritems():
        url += "%d:%.1f," % (party_id, round(result, 1))

    encoded = base64.encodestring(url[:len(url)-1])
    return encoded[:len(encoded)-1]
