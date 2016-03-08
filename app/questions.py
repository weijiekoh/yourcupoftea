"""
Defines the questions in the quiz.

Radio options:
0 = No
1 = Qualified no
2 = Neutral
3 = Qualified yes
4 = Yes
"""

import collections

questions = collections.OrderedDict({
    0:{
        "type":"pick_one",
        "text":"Are tapoica balls essential to bubble tea?",
        "choices":[
            "Yes",
            "Yes, but I like the tea too",
            "Neutral",
            "No, but I don't mind chewing them",
            "No"
            ]

        },

    1: {
        "type":"pick_many",
        "text":"What would you like in your bubble tea?",
        "choices":[
            "Extra sugar",
            "Tapoica pearls",
            "Ai-yu jelly",
            "White pearls",
            "Less sugar"
            ]
        },

    2:{
        "type":"pick_one",
        "text":"Should Koi Bubble Tea expand overseas?",
        "choices":[
            "Yes",
            "Yes, but only if Gong Cha overseas is successful",
            "Neutral",
            "No, but cater to an international audience",
            "No"
            ]

        },

    3:{
        "type":"pick_many",
        "text":"Which flavours do you like?",
        "choices":[
            "Regular milk tea",
            "Mango",
            "Green tea",
            "Passionfruit",
            "Oolong"
            ]

        },

    4:{
        "type":"pick_one",
        "text":"Is coffee a legitimate bubble tea flavour?",
        "choices":[
            "Yes",
            "Yes, but only if it contains milk and sugar",
            "Neutral",
            "No, but that's because I don't like coffee anyway",
            "No"
            ]

        }
})
