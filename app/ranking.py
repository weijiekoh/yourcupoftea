"""
Calculates party % points based on their positions and a user's responses
"""

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
            choices = [int(x) for x in response[1]]
            # map(lambda x:int(x), response[1])

            if qn_num in results:
                results[qn_num]["checkbox"] = choices
            else:
                results[qn_num] = {"checkbox": choices}

    return results


def calculate(responses, parties, party_positions, questions):
    """
    Given the form responses from a user, return a dict with the scores for each party.
    e.g. {"0": 90, "1": 28, "3": 59}

    """

    results = {}
    sorted_responses = sort_responses(responses)
    for party_id, party in parties.iteritems():
        results[party_id] = calculate_score(sorted_responses, party_id, party_positions, questions)

    return results


def calculate_score(sorted_responses, party_id, party_positions, questions):
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

    # sorted_responses = fill_in_blank_responses(sorted_responses, questions)

    sorted_responses = remove_empty_answers(sorted_responses)

    if len(sorted_responses) == 0:
        return 0

    max_possible_total_deviation = 0
    for qn_num, positions in party_positions[party_id].iteritems():
        if qn_num in sorted_responses:

            # calculate max dev for this pick-one question
            if type(positions) is int:
                p = positions # for clarity
                max_possible_total_deviation += (abs(p) + 4)

            # calculate max dev for this pick-many question
            elif type(positions) == list:
                for val in positions:
                    if val > 0:
                        max_possible_total_deviation += val

    min_possible_total_deviation = 0

    total_deviation = 0
    # iterate through each response 
    # print "=============="
    # print "Party:", party_id
    for qn_num, response in sorted_responses.iteritems():
        qn_deviation = 0.0
        if "radio" in response:
            answer = 4 * response["radio"] - 4
            party_position = party_positions[party_id][qn_num]
            qn_deviation = abs(party_position - answer)
        elif "checkbox" in response:
            checkbox_score = 0
            for checked_item in response["checkbox"]:
                checkbox_score += party_positions[party_id][qn_num][checked_item]

            max_possible_dev_for_qn = 0
            for val in party_positions[party_id][qn_num]:
                if val > 0:
                    max_possible_dev_for_qn += val

            qn_deviation += max_possible_dev_for_qn - checkbox_score

        total_deviation += (response["importance"] / 5.0) * qn_deviation

    # print "total_dev", total_deviation
    # print "max dev", max_possible_total_deviation
    # print "min dev", min_possible_total_deviation
    # print "=============="

    deviation_difference = max_possible_total_deviation - min_possible_total_deviation
    if deviation_difference == 0:
        return 0

    return 100.0 - 100.0 * (total_deviation / deviation_difference)


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


def remove_empty_answers(responses):
    result = {}
    for qn_num, response in responses.iteritems():
        if "radio" in response or "checkbox" in response:
            result[qn_num] = response

    return result


def fill_in_blank_responses(sorted_responses, questions):
    for qn_num, question in questions.iteritems():
        if not ("radio" in sorted_responses[qn_num] or "checkbox" in sorted_responses[qn_num]):
            if question["type"] == "pick_one":
                sorted_responses[qn_num]["radio"] = 2
            elif question["type"] == "pick_many":
                sorted_responses[qn_num]["checkbox"] = []
    return  sorted_responses
