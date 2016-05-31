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
            "en":u"Leaving the EU would significantly decrease foreign direct investment into the UK.",
            },

        "choices":[ 
            {
                "en":u"Yes",
                },
            {
                "en":u"Yes, because the EU accounts for almost half of foreign investment into the UK.",
                },
            {
                "en":u"Yes, because it will produce a period of uncertainty."
                }, 
            {
                "en":u"Neutral/Not sure."
                }, 
            {
                "en":u"No, because the single market is not the only reason why firms invest in Britain."
                }, 
            {
                "en":u"No, because Britain will remain an attractive place for investment anyway."
                },
            {
                "en":u"No."
                }, 

            ]
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
