from app import app
from flask import render_template, request, redirect, url_for
from app.questions import questions
from app.translations import translations
from app.parties import parties
from app.party_positions import party_positions
# from config import LANGUAGES

@app.route("/")
def index():
    return render_template("index.html", trans=translations)


@app.route("/about")
def about():
    return render_template("about.html")


# Bengali survey
@app.route("/survey_bn")
def survey():
    return render_template("survey.html", questions=questions,
            trans=translations, lang="bn")


# Hindi survey
@app.route("/survey_hi")
def survey_hi():
    return render_template("survey.html", questions=questions,
            trans=translations, lang="hi")


# English survey
@app.route("/survey_en")
def survey_en():
    # import random
    # shuffled_qns = sorted(questions.items(), key=lambda x: random.random())

    # return render_template("survey.html", questions=shuffled_qns,
            # trans=translations, lang="en")
    return render_template("survey.html", questions=questions,
            trans=translations, lang="en")


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html', trans=translations), 404


@app.errorhandler(405)
def error_405(e):
    return render_template('404.html', trans=translations), 405


@app.errorhandler(500)
def error_500(e):
    return render_template('500.html', trans=translations), 500


@app.route("/results", methods=["POST"])
def results():
    import app.ranking
    rankings = app.ranking.calculate(request.form.lists(), parties, party_positions, questions)
    return redirect(url_for("results") + "/" + smart_share_code(rankings))


@app.route("/results/<base64_result>", methods=["GET", "POST"])
def results_for_fb(base64_result):
    import re
    base64_regex = \
            "^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$"
    if re.findall(base64_regex, base64_result):
        import base64
        try:
            import urlparse

            u = urlparse.urlparse(request.url)
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=u)
            fb_share_image = domain + "static/img/combined_logos.png"

            raw_result_str = base64.decodestring(base64_result)
            sorted_results = smart_share_decode_and_sort(raw_result_str)

            from app.translations import DEFAULT_LANG
            lang = DEFAULT_LANG

            if "Referer" in request.headers:
                referrer = request.headers["Referer"]
                if referrer:
                    path = urlparse.urlparse(referrer).path
                    if path == "/survey_en":
                        lang = "en"
                    elif path == "/survey_hi":
                        lang = "hi"
                    elif path == "/survey_bn":
                        lang = "bn"

            result_share_str = translations["results"]["share_str"][lang] + \
                    format_share_str(sorted_results)

            whatsapp_share_str = translations["results"]["share_str"][lang] + "\n\n" + \
                    format_share_str(sorted_results, whatsapp=True)
                    
            return render_template("results.html", 
                    fb_share_image=fb_share_image,
                    result_share_str=result_share_str,
                    whatsapp_share_str=whatsapp_share_str,
                    parties=parties,
                    lang=lang, 
                    trans=translations,
                    results=sorted_results)

            # else:
                # return render_template("index.html")

        except (UnicodeDecodeError, AssertionError) as e:
            print e
            return render_template("index.html", trans=translations)
    else:
        return render_template("index.html")


def smart_share_decode_and_sort(raw_result_str):
    """
    Converts a result string like "p:xx.x;q:yy.y..." to a dict
    """
    import re
    # data verification
    veri_regex = "(?:\d:[\d\.]{2,4},|\d:100.0,){" + str(len(parties)-1) + \
            "}\d:[\d\.]{2,4}|\d:100.0"
    # matches something like 0:74.3,1:70.0,2:88.0,3:67.7, depending on the no.
    # of parties in parties.py
    found = re.findall(veri_regex, raw_result_str)
    # print "=============="
    # print veri_regex
    print raw_result_str
    # print found
    # print "=============="

    # throw an exeception if the url is invalid to prevent abuse
    assert len(found) > 0, "Invalid sharer url: no parties given in string"

    sorted_parties = sorted([int(x.split(":")[0]) for x in \
        sorted(found[0].split(","))])

    # make sure the input includes all the parties we have and only these
    # parties
    assert sorted_parties == sorted(parties.keys()), "Invalid sharer url: wrong number of parties"

    # sort by score, not party ID:
    score_sorted_results = []
    for r in found[0].split(","):
        s = r.split(":")
        score_sorted_results.append((int(s[0]), float(s[1])))
    score_sorted_results = sorted(score_sorted_results, key=lambda x: x[1],
            reverse=True)
    return score_sorted_results


class InvalidShareString: pass


def format_share_str(sorted_results, whatsapp=False):
    """
    Formats a dict of party_id:score etc to "ABC: xx.x%, ..."
    """
    display = ""
    for s in sorted_results[:3]:
        party_id = int(s[0])
        party_score = s[1]
        if whatsapp:
            display += "%s: %s%% \n" % (parties[party_id]["initials"], party_score)
        else:
            display += "%s: %s%%, " % (parties[party_id]["initials"], party_score)

    return display[:len(display)-2]


def smart_share_code(results):
    import base64
    url = ""
    for party_id, result in results.iteritems():
        url += "%d:%.1f," % (party_id, round(result, 1))

    encoded = base64.encodestring(url[:len(url)-1])
    return encoded[:len(encoded)-1]
