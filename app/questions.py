# -*- coding: utf-8 -*-
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
    0: {
        "type":"pick_one",
        "text":{
            "en":u"Civil rights, such as democracy and secularism, must be protected.",
            },

        "choices":[ {
            "en":u"Yes",
            },
            {
                "en":u"Neutral",
                },
            {
                "en":u"No"
                }, ]
            },

    1: {
        "type":"pick_many",
        "text":{
            "en":"Inclusive development in Bengal should encompass the following:",
            },
        "choices":[ 
            {
                "en":u"Empower small industries, medium, small and micro industries",
                },
            {
                "en":u"Promote rural arts, crafts and artisans with rural welfare as a focal agenda",
                },
            {
                "en":u"Focus on developmental projects such as housing, water, sanitation, and power",
                },
            {
                "en":u"Enact a universal public-goods distribution system to tackle fundamental issues such as starvation",
                },]
            },
    })
