"""
Defines the parties and their policy positions in the quiz.

Radio options:
0 = No
1 = Qualified no
2 = Neutral
3 = Qualified yes
4 = Yes

We assume that if a party has no position on a pick-one question, it is
neutral (2). 

We also assume that if a party has no stated positions on a pick-many
question, the max deviation is the number of questions.
min_possible_deviation is 0. So just give it an empty list.
"""

parties = \
{
    0:{
        "name": "Anything but Tapoica",
        "logo": "at.png",
        "positions": {
            0: 0,
            1:[0,2,3,4],
            2: 2,
            3:[],
            4: 2
        }
    },

    1:{
        "name": "Pro-sugar",
        "logo": "ps.png",
        "positions": {
            0: 2,
            1:[0],
            2: 2,
            3:[0, 1, 2, 3],
            4: 3
        }
    },

    2:{
        "name": "Global SunBucks",
        "logo": "sb.png",
        "positions": {
            0: 2,
            1:[],
            2: 4,
            3:[],
            4: 4
        }
    },

    3:{
        "name": "Toppings R Great",
        "logo": "trg.png",
        "positions": {
            0: 4,
            1:[0,1,2,3,4],
            2: 2,
            3:[],
            4: 2
        }
    },
}
