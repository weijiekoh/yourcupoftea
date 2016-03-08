"""
Calculates party % points based on their positions and a user's responses
"""

import questions

SLIDER = "slider_"
RADIO = "radio_"
CHECKBOX = "checkbox_"


def sort_responses(responses):
    """
    Converts a flask request.form.lists() data structure to something more 
    sensible.
    """

    results = {}

    for response in responses:
        # handle importance slider results
        if response[0].startswith(SLIDER):
            qn_num = int(response[0][len(SLIDER):])
            importance = int(response[1][0])

            if qn_num in results:
                results[qn_num]["importance"] = importance
            else:
                results[qn_num] = {"importance": importance}

        #handle radio button results
        elif response[0].startswith(RADIO):
            qn_num = int(response[0][len(RADIO):])
            choice = int(response[1][0])

            if qn_num in results:
                results[qn_num]["radio"] = choice
            else:
                results[qn_num] = {"radio": choice}
 
        #handle checkbox results
        elif response[0].startswith(CHECKBOX):
            qn_num = int(response[0][len(CHECKBOX):])
            choices = map(lambda x:int(x), response[1])

            if qn_num in results:
                results[qn_num]["checkbox"] = choices
            else:
                results[qn_num] = {"checkbox": choices}


    return results


def calculate(responses, parties, questions):
    """
    Given the form responses from a user, return a dict with the scores for each party.
    e.g. {"0": 90, "1": 28, "3": 59}

    """

    results = {}
    sorted_responses = sort_responses(responses)
    for party_id, party in parties.iteritems():
        results[party_id] = calculate_score(sorted_responses, party["positions"], questions)

    return results


def calculate_score(sorted_responses, party_positions, questions):
    """
    Calculate the score for this party given its positions and the responses
    from one user.

    Forumla (taken from http://www.electionaire.info/about):

    Total Deviation = Sum of (weight of each question as set by user) * (party
    value - user's value) for all questions 
    Final percentage = 100 - total deviation/(max possible total deviation -
    min possible deviation)

    We assume that if a party has no position on a pick-one question, it is
    neutral. 

    We also assume that if a party has no stated positions on a pick-many
    question, the max deviation is the number of questions.
    min_possible_deviation is 0. This may change.
    """

    sorted_responses = fill_in_blank_responses(sorted_responses, questions)

    min_max_dev_per_qn = min_max_deviations(party_positions, questions)
    min_possible_total_deviation = sum([x[0] for k, x in min_max_dev_per_qn.iteritems()])
    max_possible_total_deviation = sum([x[1] for k, x in min_max_dev_per_qn.iteritems()])

    total_deviation = 0.0

    # iterate through each response 
    for qn_num, response in sorted_responses.iteritems():
        sub_deviation = 0.0

        if "radio" in response:
            sub_deviation = abs(party_positions[qn_num] - response["radio"])
        elif "checkbox" in response:
            sub_deviation = len(set(party_positions[qn_num]).difference(set(response["checkbox"])))

        total_deviation += (response["importance"] / 5.0) * sub_deviation

    return 100 - 100 * (total_deviation / (max_possible_total_deviation - min_possible_total_deviation))



def min_max_deviations(party_positions, questions):
    """
    Return a a dict {qn_num: (min total deviation, max total deviation)}
    """

    result = {}
    for qn_num, position in party_positions.iteritems():
        if type(position) is list:
            max_dev = len(questions[qn_num]["choices"]) - len(position)
            result[qn_num] = (0, max_dev)

        elif type(position) is int:
            result[qn_num] = (0,  abs(2 - position) + 2)

    return result


def fill_in_blank_responses(sorted_responses, questions):
    for qn_num, question in questions.iteritems():
        if not ("radio" in sorted_responses[qn_num] or "checkbox" in sorted_responses[qn_num]):
            if question["type"] == "pick_one":
                sorted_responses[qn_num]["radio"] = 2
            elif question["type"] == "pick_many":
                sorted_responses[qn_num]["checkbox"] = []
    return  sorted_responses
