import random
import pprint
import math
from qns_parties_positions import questions

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

if __name__ == "__main__":
    rows = []
    for i in range(0, 1000):
        responses = []
        for qn_id, qn in questions.iteritems():
            qn_text = qn["text"]["en"]
            num_one_choices = len(qn["choices"])

            weight = ("slider_" + str(qn_id), [str(random.randint(1, 5))])


            if qn["type"] == "pick_one":
                r = random.randint(0, num_one_choices - 1)
                entry = ("radio_" + str(qn_id), [str(r)])
                responses.append(entry)
            elif qn["type"] == "pick_many":
                num_two_choices = nCr(num_one_choices, 2)

                r = random.randint(0, num_one_choices + num_two_choices - 1)

                selected = []
                if r <= num_one_choices:
                    selected = random.sample(range(0, num_one_choices -1), 1)
                else:
                    selected = random.sample(range(0, num_one_choices), 2)

                entry = ("checkbox_" + str(qn_id), [str(x) for x in selected])

                responses.append(entry)

            responses.append(weight)
        rows.append(responses)

    print '"Timestamp","Gender","Age","District","Data","Allegiance"'
    for row in rows:
        print '"4/23/2016 19:24:17","Other","18-25","Kolkata","' + repr(row) + '",'
