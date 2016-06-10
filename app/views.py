from app import app
from flask import render_template, request, redirect, url_for, session, jsonify
from app.qns_parties_positions import questions, campaigns, experts
from app.translations import translations
from app import ranking
import urlparse
import os
import base64
import zlib
import uuid
import re



if "FLASK_SECRET_KEY" in os.environ:
    # for deployment
    app.secret_key = os.environ["FLASK_SECRET_KEY"].decode("string_escape")
else:
    # for development only
    app.secret_key = "\x18\x1c\xc2\x18\x95\xfb$\xac\xff\x05\xe6\x91\x04\xd9\x96*\xe3j\xb0_\xb5\x03\xc0\xdd"


def fb_share_image(image):
    u = urlparse.urlparse(request.url)
    domain = "{uri.scheme}://{uri.netloc}/".format(uri=u)
    return domain + "static/img/fb/" + image + ".png"


@app.route("/demo_form_3495740968769879")
def demo():
    log_error_data("test 1", "test 2", "msg")
    return redirect("/")


@app.route("/")
def index():
    clear_response_session_data()
    qn_types = set()
    for qn_id, q in questions.iteritems():
        for t in q["types"]:
            qn_types.add(t)

    qn_types = sorted(list(qn_types))

    half_pt = len(qn_types) / 2 + 1
    qn_types_first_half = qn_types[:half_pt]
    qn_types_second_half = qn_types[half_pt:] + ["All of the above"]

    return render_template("index.html", 
            qn_types_first_half = qn_types_first_half,
            qn_types_second_half = qn_types_second_half,
            fb_share_image=fb_share_image("index"),
            trans = translations)


@app.route("/about")
def about():
    return render_template("about.html", 
            trans = translations, 
            fb_share_image = fb_share_image("neutral"))


def process_expert_view(text, is_non):
    processed = {}
    if is_non:
        pass
    else:
        # matches = re.findall(r, text)
        matches = text.split("\n")
    
        quotes = []
        for match in matches[0:-1]:
            m = match.strip()
            if len(m) > 0:
                if m[0] == "\"" and m[-1] == "\"":
                    m = m[1:-1]
                quotes.append(m)

        processed["url"] = matches[-1]
        processed["quotes"] = quotes

    return processed


def get_expert_views(qn_id):
    # return {name: [views]}
    expert_views = {}
    non = "Non-economic questions"

    for option in questions[qn_id]["options"]: # for each option
        for view in option["expert_views"]: # for each expert view
            view_text = view["view"]

            if not (view_text.strip() == "" or view_text.startswith("No mention")):
                expert_name = experts[view["id"]]["name"]

                if expert_name != non:
                    p = process_expert_view(unicode(view_text, "utf-8"), False)

                    if expert_name in expert_views:
                        expert_views[expert_name].append(p)
                    else:
                        expert_views[expert_name] = [p]
                else:
                    rows = unicode(view_text, "utf-8").split("\n")
                    url = rows[-1]
                    quotes = []
                    expert = None
                    for row in rows[0:-1]:
                        row = row.strip()
                        if len(row) > 0:
                            if row.startswith("\""):
                                r = row
                                if r[0] == "\"" and r[-1] == "\"":
                                    r = r[1:-1]
                                quotes.append(r)
                            elif row.startswith("("):
                                expert = re.findall("\((.+)\)", row)[0]

                    d = {"quotes":quotes, "url":url}
                    if expert in expert_views:
                        expert_views[expert].append(d)
                    else:
                        expert_views[expert] = [d]

    return expert_views


def get_quiz_responses():
    if "culm_responses" in session:
        return session["culm_responses"]
    else:
        return []


def update_stored_responses(data, replacement=[]):
    # r = [x for x in data if x[0] != "qn_id"]
    r = data
    if "culm_responses" in session:
        session["culm_responses"] += replacement + r
    else:
        session["culm_responses"] = replacement + r


def clear_response_session_data():
    session.pop("culm_responses", None)


def get_campaign_agreement(campaign_id, qn_id):
    # returns:
    # 2 for agree
    # 1 for disagree
    # 0 for no mention

    possible_scores = []
    for option in questions[qn_id]["options"]:
        possible_scores.append(option["campaign_support"][campaign_id]["position"])

    max_score = max(possible_scores)

    if max_score == 0:
        return 0

    e = None
    for option in questions[qn_id]["options"]:
        if option["campaign_support"][campaign_id]["position"] == max_score:
            if option["text"].startswith("Yes"):
                return 2
            elif option["text"].startswith("No"):
                return 1


@app.route("/quiz/", methods=["GET", "POST"])
def quiz():
    if request.method == "GET":
        return redirect("/")

    qn_id = None
    responses_so_far = None

    this_response = request.form.lists()

    # check if request came from front page
    is_first_qn = False
    for r in this_response:
        if r[0] == "front_page":
            is_first_qn = True

    if is_first_qn:
        clear_response_session_data()

        # set the importance response var for all qns
        impt_types = []
        for r in this_response:
            if r[0] == "type":
                impt_types = r[1]
                break

        importance = []
        for qn_id, q in questions.iteritems():
            for t in q["types"]:
                if t in impt_types:
                    importance.append(("importance_" + str(qn_id), [u"on"]))

        update_stored_responses(importance)
        qn_id = 0

    else:
        # check the session var for responses to the prev qns
        responses_so_far = get_quiz_responses()

        # determine the current qn_id
        found_qn_id = False
        for x in this_response:
            if x[0] == "qn_id":
                found_qn_id = True
                qn_id = int(x[1][0]) + 1

        if not found_qn_id:
            print "qn_id not found"
            return template_500()

        # store this response to the session var
        update_stored_responses(this_response)

    # debug = True
    debug = False
    if debug:
        print "------------------------"
        print "Prev question", qn_id
        print "Response", this_response
        print "All responses so far:", responses_so_far
        print "------------------------\n"
    

    return render_template("quiz.html", 
                           question=questions[qn_id],
                           qn_id=qn_id,
                           num_qns=len(questions), 
                           fb_share_image=fb_share_image("neutral"))


def agreement(qn_id):
    remain = []
    leave = []

    for campaign_id, c in campaigns.iteritems():
        if c["type"] == "remain":
            remain.append(campaign_id)
        elif c["type"] == "leave":
            leave.append(campaign_id)
    
    remain_agreement = []
    leave_agreement = []

    for campaign_id in remain:
        s = {"campaign_name": campaigns[campaign_id]["name"],
             "agreement": get_campaign_agreement(campaign_id, qn_id)
             }
        remain_agreement.append(s)

    for campaign_id in leave:
        s = {"campaign_name": campaigns[campaign_id]["name"],
             "agreement": get_campaign_agreement(campaign_id, qn_id)
             }
        leave_agreement.append(s)

    all_agreement = {"remain":remain_agreement,
                   "leave":leave_agreement}

    return all_agreement


def log_error_data(this_response, all_responses, error_msg):
    u = None
    if "uid" in session:
        u = session["uid"]

    d = {
        "error_msg": error_msg,
        "this_response": this_response,
        "all_responses": all_responses,
        "uid": u
        }
    print "ERROR:", base64.b64encode(zlib.compress(str(d)))
    
  
@app.route("/results", methods=["POST"])
def results():
    this_response = request.form.lists()
    all_responses = get_quiz_responses() + this_response

    if "culm_responses" not in session:
        print "culm_responses not found"
        log_error_data(this_response, all_responses, "culm_responses not found")
        return template_500()
    else:
        clear_response_session_data()

    # check if all qn_ids are in the response
    qn_ids = sorted([int(x[1][0]) for x in all_responses if x[0] == "qn_id"])
    correct_qn_ids = questions.keys()

    if len(correct_qn_ids) > len(qn_ids):
        print "not all qns answered:", qn_ids
        clear_response_session_data()
        log_error_data(this_response, all_responses, "not all qns answered")
        return template_500()
    elif len(correct_qn_ids) < len(qn_ids):
        all_responses = remove_duplicates(all_responses)

    # debug = True
    debug = False
    if debug:
        print "---------------"
        print "Results"
        print "All responses", all_responses
        print "---------------"

    session["demo_quiz_data"] = base64.b64encode(zlib.compress(str(all_responses)))

    # keep track of the number of times this user has taken the quiz
    if "uid" not in session:
        session["uid"] = uuid.uuid4()

    tt = "times_taken"
    if tt in session:
        session[tt] += 1
    else:
        session[tt] = 1
 
    c = ranking.calculate(all_responses)
    code = ranking.encode(c)
    return redirect(url_for("results") + "/" + code)


@app.route("/results/<result_str>", methods=["GET", "POST"])
def results_for_fb(result_str):
    rankings = ranking.decode(result_str)
    remain = []
    leave = []
    
    for campaign_id, campaign_info in campaigns.iteritems():
        if campaign_info["type"] == "remain":
            remain.append((campaign_id, rankings[campaign_id]))
        if campaign_info["type"] == "leave":
            leave.append((campaign_id, rankings[campaign_id]))

    # sort remain and leave
    remain = sorted(remain, key=lambda x: x[1], reverse=True)
    leave = sorted(leave, key=lambda x: x[1], reverse=True)

    remain_big_score = rankings["rb"]
    leave_big_score = rankings["lb"]

    image = None
    if abs((remain_big_score - leave_big_score)) <= 10:
        image = "neutral"
    elif remain_big_score < leave_big_score:
        image = "leave"
    else:
        image = "remain"

    demo_quiz_data = None
    if "demo_quiz_data" in session:
        demo_quiz_data = session["demo_quiz_data"]
    session.pop("demo_quiz_data", None)

    tt = "times_taken"
    if not tt in session:
        session[tt] = -1

    if not "uid" in session:
        session["uid"] = -1

    a = {}
    e = {}
    for qn_id in questions:
        a[qn_id] = agreement(qn_id)
        e[qn_id] = get_expert_views(qn_id)


    result_share_str = "My Remain vs Leave quiz results: " +\
                            str(remain_big_score) + "% remain, " +\
                            str(leave_big_score) + "% leave."


    return render_template("results.html", 
                           demo_quiz_data=demo_quiz_data,
                           agreement=a,
                           expert_views=e,
                           remain_big_score=remain_big_score,
                           leave_big_score=leave_big_score,
                           remain_scores=remain, 
                           result_share_str=result_share_str,
                           leave_scores=leave, 
                           campaigns=campaigns,
                           questions=questions,
                           experts=experts,
                           times_taken=session[tt],
                           uid=session["uid"],
                           image=image,
                           fb_share_image=fb_share_image(image),
                           trans=translations)



@app.errorhandler(404)
def error_404(e):
    return render_template("404.html", trans=translations), 404


@app.errorhandler(405)
def error_405(e):
    return render_template("404.html", trans=translations), 405


def template_500():
    return render_template("500.html", trans=translations), 500

@app.errorhandler(500)
def error_500(e):
    return template_500()


def remove_duplicates(all_responses):
    fixed = []
    r = "radio_"
    for qn_id in reversed(questions.keys()):
        for n, v in reversed(all_responses):
            if n == "qn_id" and int(v[0]) == qn_id:
                fixed.append((n,v))
                break

    for qn_id in reversed(questions.keys()):
        for n, v in reversed(all_responses):
            if n.startswith(r):
                if int(n[len(r):]) == qn_id:
                    fixed.append((n,v))
                    break

    fixed.reverse()
    return fixed
