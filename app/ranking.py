"""
Calculates campaigns' % points based on their positions and a user's responses
"""

RADIO = "radio_"
IMPORTANCE = "checkbox_"


def calculate(raw_responses):
    # sort into dict:
    # {qn_id: {"answer", "importance"}}

    # calculate campaign score

    # return dict: {qn_id: answer}




if __name__ == "__main__":
    sample_data = [('qn_id', [u'0']), ('radio_0', [u'0']), ('importance_0', [u'on']), 
                   ('qn_id', [u'1']), ('radio_1', [u'7']), 
                   ('qn_id', [u'2']), ('radio_2', [u'1']), ('importance_2', [u'on']), 
                   ('qn_id', [u'3']), ('radio_3', [u'3'])]
    
    print calculate(sample_data)
