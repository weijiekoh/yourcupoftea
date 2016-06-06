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
            possible_scores.append(
                    option["campaign_support"][campaign_id]["position"]
                    )

        max_score = max(possible_scores)

        total_max_dev += max_score

        # calculate user's deviation
        user_choice = int(r["answer"])
        user_score = int(questions[qn_id]\
                                         ["options"]\
                                         [user_choice]\
                                         ["campaign_support"]\
                                         [campaign_id]\
                                         ["position"])
        if r["importance"] == "off":
            user_score *= 0.75
        qn_dev = max_score - user_score
        total_user_dev += qn_dev

    if total_user_dev == 0:
        return 0

    # Final percentage = 100 - (total deviation / max possible total deviation)
    return int(round(100 - (total_user_dev / total_max_dev * 100)))


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

    # return dict: {campaign_id: score}
    return campaign_scores


if __name__ == "__main__":
    sample_data = [('qn_id', [u'0']), ('radio_0', [u'2']), ('importance_0', [u'on']), 
                   ('qn_id', [u'1']), ('radio_1', [u'1']), 
                   ('qn_id', [u'2']), ('radio_2', [u'1']), ('importance_2', [u'on']), 
                   ('qn_id', [u'3']), ('radio_3', [u'3']),
                   ('qn_id', [u'4']), ('importance_4', [u'on'])]
    
    result = calculate(sample_data)
    print result
    print encode(result)
    print decode(encode(result))
