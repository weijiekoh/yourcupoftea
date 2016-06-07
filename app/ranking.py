"""
Calculates campaigns' % points based on their positions and a user's responses
"""

from qns_parties_positions import campaigns
from qns_parties_positions import questions, campaigns
import ast
import base64

RADIO = "radio_"
IMPORTANCE = "importance_"


def encode(rankings):
    s = str()
    for char in repr(rankings):
        if not char in " {}":
            s += char
    return base64.b64encode(s)


def decode(s):
    return ast.literal_eval("{" + base64.b64decode(s) + "}")


def _calculate_campaign_score(campaign_id, responses):
    """
    Calculates the score for this particular campaign based on the 
    responses given
    """

    # sum deviation for all questions
    total_max_dev = 0
    total_user_dev = 0

    for qn_id, r in responses.iteritems():
        # sum max deviation for all questions
        possible_scores = []
        for option in questions[qn_id]["options"]:
            possible_scores.append(option["campaign_support"][campaign_id]["position"])

        max_score = max(possible_scores)
        min_score = min(possible_scores)
        total_max_dev += max_score - min_score

        # calculate user's deviation
        user_choice = int(r["answer"])
        user_score = int(questions[qn_id]["options"][user_choice]\
                ["campaign_support"][campaign_id]["position"])

        if r["importance"] == "off":
            user_score *= 0.75

        qn_dev = max_score - user_score
        total_user_dev += qn_dev

    # Final percentage = 100 - 100 * (total deviation / max possible total deviation)
    return int(round(100.0 - 100.0 * (total_user_dev / float(total_max_dev))))


def _which_side(qn_id, option_num):
    # return 2 for remain, 1 for leave
    num_remain_support = 0
    num_leave_support = 0
    for campaign_id, c in campaigns.iteritems():
        if c["type"] == "remain":
            position = questions[qn_id]["options"][option_num]\
                    ["campaign_support"][campaign_id]["position"]

            if position > 0:
                num_remain_support += 1

        elif c["type"] == "leave":
            position = questions[qn_id]["options"][option_num]\
                    ["campaign_support"][campaign_id]["position"]

            if position > 0:
                num_leave_support += 1

    if num_remain_support > num_leave_support:
        return 2
    elif num_leave_support > num_remain_support:
        return 1


def _calculate_big_scores(responses):
    num_remain_answers = 0
    num_leave_answers = 0
    num_neutral_answers = 0

    for qn_id, v in responses.iteritems():
        side = _which_side(qn_id, int(v["answer"]))
        if side == 2:
            num_remain_answers += 1
        elif side == 1:
            num_leave_answers += 1

    remain_big_score = int(round(100.0 * (float(num_remain_answers) / float((len(questions))))))
    leave_big_score = int(round(100.0 * (float(num_leave_answers) / float((len(questions))))))

    return remain_big_score, leave_big_score


def calculate(raw_responses):
    # sort into dict:
    # {qn_id: {"answer", "importance"}}

    responses = {}
    for r in raw_responses:
        name = r[0]
        val = r[1][0]

        if name.startswith(RADIO):
            qn_id = int(name[len(RADIO):])
            if not qn_id in responses:
                responses[qn_id] = {"answer": val}
            else:
                responses[qn_id]["answer"] = val
        elif name.startswith(IMPORTANCE):
            qn_id = int(name[len(IMPORTANCE):])
            if not qn_id in responses:
                responses[qn_id] = {"importance": val}
            else:
                responses[qn_id]["importance"] = val

    # remove empty answers. e.g. they don't pick any radio buttons but tick 
    # the importance checkbox

    t = {}
    for qn_id, r in responses.iteritems():
        if "answer" in r:
            t[qn_id] = r

    responses = t

    # fill in missing importance responses.

    for qn_id, r in responses.iteritems():
        if not "importance" in r:
            responses[qn_id]["importance"] = u"off"

    # calculate campaign scores

    campaign_scores = {}
    for campaign_id in campaigns:
        campaign_scores[campaign_id] = \
                _calculate_campaign_score(campaign_id, responses)

    # return dict: {campaign_id: score, rb, lb}
    # rb /lb = remain/leave big score. plain count.

    rb, lb = _calculate_big_scores(responses)
    campaign_scores["rb"] = rb
    campaign_scores["lb"] = lb
    return campaign_scores


if __name__ == "__main__":
    sample_data = [('qn_id', [u'0']), ('radio_0', [u'2']), 
                   ('qn_id', [u'1']), ('radio_1', [u'2']), 
                   ('radio_2', [u'2']), ('qn_id', [u'2'])]

    result = calculate(sample_data)
    print result
