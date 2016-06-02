from app import app
from flask import render_template, request, redirect, url_for, session
from app.qns_parties_positions import questions
from app.translations import translations
from app.parties import parties
from app.qns_parties_positions import party_positions
import urlparse
import os


if "FLASK_SECRET_KEY" in os.environ:
    # for deployment
    app.secret_key = os.environ["FLASK_SECRET_KEY"].decode("string_escape")
else:
    # for development only
    app.secret_key = "\x18\x1c\xc2\x18\x95\xfb$\xac\xff\x05\xe6\x91\x04\xd9\x96*\xe3j\xb0_\xb5\x03\xc0\xdd"


def fb_share_image():
    u = urlparse.urlparse(request.url)
    domain = "{uri.scheme}://{uri.netloc}/".format(uri=u)
    return domain + "static/img/fb_share_logo.png"


@app.route("/")
def index():
    return render_template("index.html", trans=translations, fb_share_image=fb_share_image())


@app.route("/about")
def about():
    return render_template("about.html", trans=translations, fb_share_image=fb_share_image())


@app.route("/quiz/<int:qn_id>", methods=["POST"])
def quiz_n(qn_id):
    #TODO: assert code

    this_response = request.form.lists()

    if not "culm_responses" in session:
        session["culm_responses"] = []

    session["culm_responses"] += this_response

    print "------------------------"
    print "Question", qn_id
    print "This response", this_response
    print "All responses so far:", session["culm_responses"]
    print "------------------------\n"
    
    return render_template("quiz.html", 
                           question=questions[qn_id], 
                           qn_id=qn_id,
                           num_qns=len(questions), 
                           trans=translations, lang="en", 
                           fb_share_image=fb_share_image())


@app.route("/quiz")
def quiz():
    return quiz_n(0)


@app.route("/results", methods=["POST"])
def results():
    import app.ranking
    data_str = str(request.form.lists())
    session["demo_data"] = data_str

    if "culm_responses" not in session:
        return render_template("500.html", trans=translations), 500


    this_response = request.form.lists()
    all_responses = session["culm_responses"] + this_response
    session.pop("culm_responses", None)
            

    print "------------------------"
    print "Results"
    print "This response", this_response
    print "All responses so far:", all_responses
    print "------------------------\n"

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
            raw_result_str = base64.decodestring(base64_result)
            sorted_results = smart_share_decode_and_sort(raw_result_str)

            from app.translations import DEFAULT_LANG
            lang = DEFAULT_LANG

            result_share_str = translations["results"]["share_str"][lang] + \
                    format_share_str(sorted_results)

            whatsapp_share_str = translations["results"]["share_str"][lang] + "\n\n" + \
                    format_share_str(sorted_results, whatsapp=True)
            
            demo_data = None
            if "demo_data" in session:
                demo_data = session["demo_data"]
            session.pop("demo_data", None)

            return render_template("results.html", 
                    fb_share_image=fb_share_image(),
                    result_share_str=result_share_str,
                    whatsapp_share_str=whatsapp_share_str,
                    parties=parties,
                    lang=lang, 
                    trans=translations,
                    demo_data=demo_data,
                    results=sorted_results)

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


@app.errorhandler(404)
def error_404(e):
    return render_template("404.html", trans=translations), 404


@app.errorhandler(405)
def error_405(e):
    return render_template("404.html", trans=translations), 405


@app.errorhandler(500)
def error_500(e):
    return render_template("500.html", trans=translations), 500


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
