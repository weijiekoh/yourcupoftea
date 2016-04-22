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
            "bn":u"গণতন্ত্র ও ধর্মনিরপেক্ষতার মত নাগরিক অধিকার রক্ষা করা আবশ্যক.",
            "hi":u"",
            "en": "Civil rights, such as democracy and secularism, must be protected.",
            },

        "choices":[ {
            "bn":u"হ্যাঁ",
            "hi":u"",
            "en": "Yes",
            },
            {
                "bn":u"নিরপেক্ষ",
                "hi":u"",
                "en": "Neutral",
                },
            {
                "bn":u"না",
                "hi":u"",
                "en": "No"
                }, ]
            },

    1: {
        "type":"pick_one",
        "text":{
            "bn":"দ্রুত নতুন সড়ক, ফ্লাইওভার ও জনপথ নির্মাণের দ্বারা পশ্চিমবঙ্গের সড়ক অবকাঠামো বিকশিত করা উচিত.",
            "hi":"",
            "en": "The government should rapidly develop West Bengal's road infrastructure by building new roads, flyovers and highways.",
            },

        "choices":[ {
            "bn":u"হ্যাঁ",
            "hi":u"",
            "en": "Yes",
            },
            {
                "bn":u"নিরপেক্ষ",
                "hi":u"",
                "en": "Neutral",
                },
            {
                "bn":u"না",
                "hi":u"",
                "en": "No"
                }, ],
            },
    2: {
            "type":"pick_many",
            "text":{
                "bn":u"সুশাসনের জন্য, শাসক শ্রেণীর মধ্যে দুর্নীতি এই ভাবে কমানো যায়:",
                "hi":u"",
                "en":"For better governance, corruption among the ruling classes needs to be tackled with the following methods:",
                },
            "choices":[ {
                "bn":u"দৃঢ় রাষ্ট্র নীতি দ্বারা দুর্নীতির মোকাবিলা করা উচিত ",
                "hi":u"",
                "en": "Enact strong policy initiaitives to identify and tackle corruption issues",
                },
                {
                    "bn":u"বৃহত্তর জবাবদিহিতার জন্য ই-গভর্নেন্স এবং ডিজিটাল স্বচ্ছতা উন্নত করা উচিত ",
                    "hi":u"",
                    "en": "Implement e-governance and digital transparency for greater accountability",
                    },
                {
                    "bn":u"সরকারি পদের জন্য প্রকাশ্য জবাবদিহিতা খুব জরুরি ",
                    "hi":u"",
                    "en": "Ensure public accountability for government positions",
                    },
                {
                    "bn":u"কালো টাকা এবং কালোবাজারে বাণিজ্য নিয়ন্ত্রণ",
                    "hi":u"",
                    "en": "Track black money and black market trades",
                    },
                {
                    "bn":u"সারদা কেলেঙ্কারির মত আর্থিক কেলেঙ্কারি অবিলম্বে মোকাবিলা করতে হবে",
                    "hi":u"",
                    "en": "Deal with financial scandals such as the Saradha Group scandal as an immediate priority"
                    }, ]
                },

    3: {
            "type":"pick_many",
            "text":{
                "bn":"বাংলার অর্থনৈতিক উন্নয়নের জন্য শিল্প এবং বানিজ্যে জরুরি এবং নিম্নিলিখিত উপায়ে তার বৃদ্ধি হতে পারে:",
                "hi":"",
                "en":"Industrialization is a key driver of economic development for Bengal and can be achieved through the following means:",
                },
            "choices":[ {
                "bn":"বেসরকারী বিনিয়োগ বৃদ্ধি করার চেষ্টা করা উচিত ",
                "hi":"",
                "en": "Encourage private investment",
                },
                {
                    "bn":"বানিজ্যিক এবং শিল্প কেন্দ্র নির্মান করা উচিত, উন্নত পরিকাঠামো আর যোগাযোগ ব্যবস্থা কেন্দ্র করে",
                    "hi":"",
                    "en": "Build industrial parks and centers with a focus on infrastructure and connectivity",
                    },
                {
                    "bn":"আইটির মত বুদ্ধিজীবী শিল্পের বিকাশ খুব জরুরি",
                    "hi":"",
                    "en": "Promote intellectual industries such as IT and services",
                    },
                {
                    "bn":"পশ্চিমবঙ্গে ব্যবসা করার সাধ্যতা কমানোর প্রচেষ্টা করা উচিত",
                    "hi":"",
                    "en": "Increase the ease of doing business in Bengal",
                    }, 
                {
                    "bn":"ব্যবসা ও বানিজ্যের জন্য জমি দখল জরুরি তবে সঠিক বিচার  বিবেচনা করে জমি নেওয়া উচিত",
                    "hi":"",
                    "en": "Land acquisition is important for industry but should be done cautiously",
                    }, ]
                },
    4: {
            "type":"pick_many",
            "text":{
                "bn":"নিম্নলিখিত বিকল্পগুলির সর্বব্যাপী উন্নয়নের জন্য অপরিহার্য:",
                "hi":"",
                "en":"Inclusive development in Bengal should encompass the following:",
                },
            "choices":[ {
                "bn":"ছোট এবং মাঝারি ব্যবসার প্রসারণ ঘটানো দরকার ",
                "hi":"",
                "en": "Empower small industries, medium, small and micro industries",
                },
                {
                    "bn":"গ্রামীন কল্যাণ কেন্দ্র করে গ্রামীন শিল্প ও কলা উন্নত করা উচিত",
                    "hi":"",
                    "en": "Promote rural arts, crafts and artisans with rural welfare as a focal agenda",
                    },
                {
                    "bn":"গুরুত্বপূর্ণ উন্নয়ন প্রকল্পের উপর নজর যেমন আশ্রয়, জল ব্যবস্থা, বিদ্যুত ইত্যাদি ",
                    "hi":"",
                    "en": "Focus on developmental projects such as housing, water, sanitation, and power",
                    },
                {
                    "bn":"খাদ্যের মত মৌলিক মানবাদিখার সব থেকে জরুরি এবং সবার কাছে পৌছে দিতে সার্বজনীন পরিষেবা বিতরণ অনিবার্য",
                    "hi":"",
                    "en": "Enact a universal public-goods distribution system to tackle fundamental issues such as starvation",
                    }, ]
                },
    5: {
            "type":"pick_many",
            "text":{
                "bn":"পশ্চিমবঙ্গের শিক্ষা প্রতিষ্ঠান জোরদার করতে আবশ্যক:",
                "hi":"",
                "en":"Educational institutes in the State must be strengthened through:",
                },
            "choices":[ {
                "bn":"বাক স্বাধীনতা এবং ভিন্নমত প্রকাশের অধিকার রক্ষা করা:",
                "hi":"",
                "en": "Protect free speech and spaces for dissent",
                },
                {
                    "bn":"ভোকেশনাল ট্রেনিং সঙ্গে বৃহত্তর শিল্প সংযোগ স্থাপন",
                    "hi":"",
                    "en": "Establish greater industry linkages with strong vocational training",
                    },
                {
                    "bn":"উচ্চ শিক্ষার ক্ষেত্রে রাজনৈতিক হস্তক্ষেপ কমানো জরুরি",
                    "hi":"",
                    "en": "De-politicize higher education, especially in faculty appointment and college administration",
                    },
                {
                    "bn":"আরও নতুন কলেজ ও বিশ্ববিদ্যালয় প্রতিষ্ঠান জরুরি",
                    "hi":"",
                    "en": "Establish more centers and institutes for higher education",
                    }, ]
                },
    6: {
            "type":"pick_many",
            "text":{
                "bn":"নারীর অধিকার ও নিরাপত্তা নিম্নলিখিত উপায়ে মোকাবিলা করা আবশ্যক:",
                "hi":"",
                "en":"Women's rights and safety must be addressed with the following means:",
                },
            "choices":[ {
                "bn":"সামগ্রিক আইন শৃঙ্খলা পরিস্থিতি উন্নত করা যাতে মহিলারা নির্দিধায় জীবনযাপন করতে পারে ",
                "hi":"",
                "en": "Improve law and order to enable women to access all public spaces",
                },
                {
                    "bn":"নারীশিক্ষা ও আয় নিরাপত্তা কেন্দ্র করা উচিত",
                    "hi":"",
                    "en": "Place a central focus on women's education and income security",
                    },
                {
                    "bn":"পুলিশ কে আরও লিঙ্গ সংবেদনশীল করা এবং মহিলাদের জন্য আলাদা পুলিশ সংস্থা তৈরী করা",
                    "hi":"",
                    "en": "Change the police force to be more responsive and gender-sensitive, and introduce police units dedicated to women",
                    },
                {
                    "bn":"স্কুল ও কলেজ ই লিঙ্গ অধ্যয়ন চালু করা",
                    "hi":"",
                    "en": "Include gender issues in school curricula in schools and colleges to increase awareness",
                    },]
                },

    7: {
            "type":"pick_many",
            "text":{
                "bn":"শ্রমিক দের অধিকার অর্জনের জন্য নিম্নিলিখিত করা কাম্য:",
                "hi":"",
                "en":"Worker's rights can be significantly improved through:",
                },
            "choices":[ {
                "bn":"চুক্তিভিত্তিক এবং দৈনিক মজুরি শ্রমিকদের অধিকার রক্ষা",
                "hi":"",
                "en": "Protect the rights of contractual and daily wage workers",
                },
                {
                    "bn":"বেকার শ্রমিকদের ভর্তুকি ও আয়-ভাতা সুবিধা দেওয়া",
                    "hi":"",
                    "en": "Give unemployed workers subsidies and income allowances",
                    },
                {
                    "bn":"বিমা পেনশন ছুটি এবং অন্যান্য সুবিধে দেওয়া সব ধরনের শ্রমিকদের বিশেষ করে দৈনিক কর্মীদের ",
                    "hi":"",
                    "en": "Provide insurance, pension, benefits and leaves to part time, small, and daily wage workers",
                    },
                {
                    "bn":"মহিলা শ্রমিকদের বিশেষ নজর দেওয়া যেমন সার্বজনীন মাতৃত্ব ছুটি অধিকার এবং অনান্য সুবিধে ",
                    "hi":"",
                    "en": "Provide female workers' rights through maternity leaves, benefits and flexibility",
                    }, ]
                },
    8: {
            "type":"pick_many",
            "text":{
                "bn":"স্বাস্থ্য ব্যবস্থা এইভাবে উন্নত করা যেতে পারে:",
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
