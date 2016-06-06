from app import app
from flask import render_template, request, redirect, url_for, session, jsonify
from app.qns_parties_positions import questions, campaigns, experts
from app.translations import translations
from app import ranking
import urlparse
import os


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


@app.route("/")
def index():
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
            trans = translations, 
            fb_share_image = fb_share_image("neutral"))


@app.route("/about")
def about():
    return render_template("about.html", 
            trans = translations, 
            fb_share_image = fb_share_image("neutral"))


def get_quiz_responses():
    if "culm_responses" in session:
        return session["culm_responses"]
    else:
        return []


def update_stored_responses(data):
    # r = [x for x in data if x[0] != "qn_id"]
    r = data
    if "culm_responses" in session:
        session["culm_responses"] += r
    else:
        session["culm_responses"] = r


def clear_response_session_data():
    session.pop("culm_responses", None)


def get_campaign_stance(campaign_id, qn_id, option_id):
    # returns 2 for strong support, 1 for partial/implied support, 
    # 0 for no mention/NA
    e = None
    for x in questions[qn_id]["options"][option_id]["campaign_support"]:
        if x["id"] == campaign_id:
            e = x["position"]
            break
    
    if e == 20:
        return 2
    elif e > 0 and e < 20:
        return 1
    else:
        return 0


@app.route("/quiz/", methods=["POST"])
def quiz():
    qn_id = None
    this_response = request.form.lists()

    # check if request came from front page
    is_first_qn = False
    for r in this_response:
        if r[0] == "front_page":
            is_first_qn = True

    if is_first_qn:
        print "First qn"
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
        print "Not first qn"
        # check the session var for responses to the prev qns
        responses_so_far = get_quiz_responses()

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

    # print "------------------------"
    # print "Prev question", qn_id
    # print "Response", this_response
    # print "All responses so far:", get_quiz_responses()
    # print "------------------------\n"

    return render_template("quiz.html", 
                           question=questions[qn_id],
                           qn_id=qn_id,
                           num_qns=len(questions), 
                           trans=translations, lang="en", 
                           fb_share_image=fb_share_image("neutral"))


# @app.route("/stance/<int:qn_id>/<int:option_num>", methods=["POST"])
@app.route("/_stance/")
def stance():
    # data for campaign stance explanations
    # make 2 lists: stay/leave -> [{campaign name, full/none/halfway}]

    qn_id = request.args.get("qn_id", -1, type=int)
    option_num = request.args.get("option_num", -1, type=int)

    remain = []
    leave = []

    for campaign_id, c in campaigns.iteritems():
        if c["type"] == "remain":
            remain.append(campaign_id)
        elif c["type"] == "leave":
            leave.append(campaign_id)
    
    remain_stances = []
    leave_stances = []

    for campaign_id in remain:
        s = {"campaign_name": campaigns[campaign_id]["name"],
             "stance": get_campaign_stance(campaign_id, qn_id, option_num)
             }
        remain_stances.append(s)

    for campaign_id in leave:
        s = {"campaign_name": campaigns[campaign_id]["name"],
             "stance": get_campaign_stance(campaign_id, qn_id, option_num)
             }
        leave_stances.append(s)

    all_stances = {"remain_stances":remain_stances,
                   "leave_stances":leave_stances}

    return jsonify(all_stances)

@app.route("/results", methods=["POST"])
def results():
    this_response = request.form.lists()
    all_responses = get_quiz_responses() + this_response
    
    print "---------------"
    print "All responses", all_responses
    print "---------------"


    if "culm_responses" not in session:
        print "culm_responses not found"
        return template_500()
    else:
        clear_response_session_data()

    # check if all qn_ids are in the response
    qn_ids = sorted([int(x[1][0]) for x in all_responses if x[0] == "qn_id"])
    correct_qn_ids = questions.keys()
    if correct_qn_ids != qn_ids:
        print "Not all qn_ids present:", qn_ids
        clear_response_session_data()
        return template_500()

    code = ranking.encode(ranking.calculate(all_responses))
    return redirect(url_for("results") + "/" + code)


@app.route("/results/<result_str>", methods=["GET", "POST"])
def results_for_fb(result_str):
    rankings = ranking.decode(result_str)
    remain = []
    leave = []
    
    total_remain_score = 0
    total_leave_score = 0

    for campaign_id, campaign_info in campaigns.iteritems():
        if campaign_info["type"] == "remain":
            remain.append((campaign_id, rankings[campaign_id]))
            total_remain_score += rankings[campaign_id]
        if campaign_info["type"] == "leave":
            leave.append((campaign_id, rankings[campaign_id]))
            total_leave_score += rankings[campaign_id]

    # sort remain and leave
    remain = sorted(remain, key=lambda x: x[1], reverse=True)
    leave = sorted(leave, key=lambda x: x[1], reverse=True)

    average_remain_score = total_remain_score / len(remain)
    average_leave_score = total_leave_score / len(leave)

    image = None
    if abs((average_remain_score - average_leave_score)) <= 10:
        image = "neutral"
    elif average_remain_score < average_leave_score:
        image = "leave"
    else:
        image = "remain"

    r = "My EU referendum quiz results: " +\
                            str(average_remain_score) + "% remain, " +\
                            str(average_leave_score) + "% leave."

    return render_template("results.html", 
                           average_remain_score=average_remain_score,
                           average_leave_score=average_leave_score,
                           remain_scores=remain, 
                           result_share_str=r,
                           leave_scores=leave, 
                           campaigns=campaigns,
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
