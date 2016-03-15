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
        "text":{
            "bn":"",
            "hi":"",
            "en": "Are tapoica balls essential to bubble tea?",
            },

        "choices":[
            {
            "bn":"",
            "hi":"",
            "en": "Yes",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Yes, but I like the tea too",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Neutral",
            },
            {
            "bn":"",
            "hi":"",
            "en": "No, but I don't mind chewing them",
            },
            {
            "bn":"",
            "hi":"",
            "en": "No"
            },
            ]

        },

    1: {
        "type":"pick_many",
        "text":{
            "bn":"",
            "hi":"",
            "en":"What would you like in your bubble tea?", 
            },
        "choices":[
            {
            "bn":"",
            "hi":"",
            "en": "Extra sugar",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Tapoica pearls",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Ai-yu jelly",
            },
            {
            "bn":"",
            "hi":"",
            "en": "White pearls",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Less sugar"
            },
            ]
        },

    2:{
        "type":"pick_one",
        "text":{
            "bn":"",
            "hi":"",
            "en":"Should Koi Bubble Tea expand overseas?",
            },
        "choices":[
            {
            "bn":"",
            "hi":"",
            "en": "Yes",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Yes, but only if Gong Cha overseas is successful",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Neutral",
            },
            {
            "bn":"",
            "hi":"",
            "en": "No, but cater to an international audience",
            },
            {
            "bn":"",
            "hi":"",
            "en": "No"
            },
            ]

        },

    3:{
        "type":"pick_many",
        "text":{
            "bn":"",
            "hi":"",
            "en":"Which flavours do you like?",
            },
        "choices":[
            {
            "bn":"",
            "hi":"",
            "en": "Regular milk tea",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Mango",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Green tea",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Passionfruit",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Oolong"
            },
            ]

        },

    4:{
        "type":"pick_one",
        "text":{
            "bn":"",
            "hi":"",
            "en":"Is coffee a legitimate bubble tea flavour?",
            },
        "choices":[
            {
            "bn":"",
            "hi":"",
            "en": "Yes",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Yes, but only if it contains milk and sugar",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Neutral",
            },
            {
            "bn":"",
            "hi":"",
            "en": "No, but that's because I don't like coffee anyway",
            },
            {
            "bn":"",
            "hi":"",
            "en": "No"
            },
            ]

        }
})
