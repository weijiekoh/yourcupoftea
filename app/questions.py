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
            "en": "Civil rights, such as democracy and secularism, must be protected.",
            },

        "choices":[ {
            "bn":"",
            "hi":"",
            "en": "Yes",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Neutral",
            },
            {
            "bn":"",
            "hi":"",
            "en": "No"
            }, ]
        },

    1:{
        "type":"pick_one",
        "text":{
            "bn":"",
            "hi":"",
            "en": "The government should rapidly develop West Bengal's road system.",
            },

        "choices":[ {
            "bn":"",
            "hi":"",
            "en": "Yes",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Neutral",
            },
            {
            "bn":"",
            "hi":"",
            "en": "No"
            }, ],
        },

    2: {
        "type":"pick_many",
        "text":{
            "bn":"",
            "hi":"",
            "en":"For better governance, corruption among the ruling classes needs to be tackled with the following methods:",
            },
        "choices":[ {
            "bn":"",
            "hi":"",
            "en": "Enact strong policy initiaitives to identify and tackle corruption issues",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Implement e-governance and digital transparency for greater accountability",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Ensure public accountability for government positions",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Track black money and black market trades",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Deal with financial scandals such as the Saradha Group scandal as an immediate priority"
            }, ]
        },

    3: {
        "type":"pick_many",
        "text":{
            "bn":"",
            "hi":"",
            "en":"Industrialization is a key driver of economic development for Bengal and can be achieved through the following means:",
            },
        "choices":[ {
            "bn":"",
            "hi":"",
            "en": "Encourage private investment",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Build industrial parks and centers with a focus on infrastructure and connectivity",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Promote intellectual industries such as IT and services",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Increase the ease of doing business in Bengal",
            }, 
            {
            "bn":"",
            "hi":"",
            "en": "Land acquisition is important for industry but should be done cautiously",
            }, 
            {
            "bn":"",
            "hi":"",
            "en": "Promote manufacturing, trade, and heavy industries",
            }, ]
        },
    4: {
        "type":"pick_many",
        "text":{
            "bn":"",
            "hi":"",
            "en":"Inclusive development in Bengal should encompass the following:",
            },
        "choices":[ {
            "bn":"",
            "hi":"",
            "en": "Empower small industries, medium, small and micro industries",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Promote rural arts, crafts and artisans with rural welfare as a focal agenda",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Focus on developmental projects such as housing, water, sanitation, and power",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Enact a universal public-goods distribution system to tackle fundamental issues such as starvation",
            }, ]
        },
    5: {
        "type":"pick_many",
        "text":{
            "bn":"",
            "hi":"",
            "en":"Educational institutes in the State must be strengthened through:",
            },
        "choices":[ {
            "bn":"",
            "hi":"",
            "en": "Protect free speech and spaces for dissent",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Establish greater industry linkages with strong vocational training",
            },
            {
            "bn":"",
            "hi":"",
            "en": "De-politicize higher education, especially in faculty appointment and college administration",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Establish more centers and institutes for higher education",
            }, ]
        },
    6: {
        "type":"pick_many",
        "text":{
            "bn":"",
            "hi":"",
            "en":"Women's rights and safety must be addressed with the following means:",
            },
        "choices":[ {
            "bn":"",
            "hi":"",
            "en": "Improve law and order to enable women to access all public spaces",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Place a central focus on women's education and income security",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Change the police force to be more responsive and gender-sensitive, and introduce police units dedicated to women",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Include gender issues in school curricula in schools and colleges to increase awareness",
            },]
        },
    7: {
        "type":"pick_many",
        "text":{
            "bn":"",
            "hi":"",
            "en":"Worker's rights can be significantly improved through:",
            },
        "choices":[ {
            "bn":"",
            "hi":"",
            "en": "Protect the rights of contractual and daily wage workers",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Give workers out of employment subsidies and income allowances",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Provide insurance, pension, benefits and leaves to part time, small, and daily wage workers",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Provide female workers' rights through maternity leaves, benefits and flexibility",
            }, ]
        },
    8: {
        "type":"pick_many",
        "text":{
            "bn":"",
            "hi":"",
            "en":"Healthcare in Bengal can be improved through the following means:",
            },
        "choices":[ {
            "bn":"",
            "hi":"",
            "en": "Set up cutting-edge institutes of medical training",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Facilitate the construction of super-speciality hospitals",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Reduce child and infant mortality, with a special focus on the girl child",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Increase the capacity of current health infrastructure",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Increase maternity leave for women employees"
            }, ]
        },
    9: {
        "type":"pick_many",
        "text":{
            "bn":"",
            "hi":"",
            "en":"Communal violence should be addressed with the following means:",
            },
        "choices":[ {
            "bn":"",
            "hi":"",
            "en": "Assist religious minorities with their overall social and economic development",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Enact a zero-tolerance policy for communal violence",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Increase police presence to improve the overall law and order situation",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Strongly uphold secular ideals",
            }, ]
        },
    10: {
        "type":"pick_many",
        "text":{
            "bn":"",
            "hi":"",
            "en":"The government should adopt the following policies regarding the Muslim population:",
            },
        "choices":[ {
            "bn":"",
            "hi":"",
            "en": "Bring Madrasa curriculums in line with nation-building efforts",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Tighten immigration from East Bengal",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Oppose all forms of communal violence",
            },
            {
            "bn":"",
            "hi":"",
            "en": "Provide special protection to ensure the safety of Muslims and other religious minorities",
            },]
        },
})
