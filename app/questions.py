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
            "en":u"Civil rights, such as democracy and secularism, must be protected.",
            },

        "choices":[ {
                "bn":u"হ্যাঁ",
                "hi":u"",
                "en":u"Yes",
                },
            {
                "bn":u"নিরপেক্ষ",
                "hi":u"",
                "en":u"Neutral",
                },
            {
                "bn":u"না",
                "hi":u"",
                "en":u"No"
                }, ]
            },

    1: {
        "type":"pick_one",
        "text":{
            "bn":u"দ্রুত নতুন সড়ক, ফ্লাইওভার ও জনপথ নির্মাণের দ্বারা পশ্চিমবঙ্গের সড়ক অবকাঠামো বিকশিত করা উচিত.",
            "hi":"",
            "en":u"The government should rapidly develop West Bengal's road infrastructure by building new roads, flyovers and highways.",
            },

        "choices":[ {
                "bn":u"হ্যাঁ",
                "hi":u"",
                "en":u"Yes",
                },
            {
                "bn":u"নিরপেক্ষ",
                "hi":u"",
                "en":u"Neutral",
                },
            {
                "bn":u"না",
                "hi":u"",
                "en":u"No"
                }, ],
            },
    2: {
            "type":"pick_many",
            "text":{
                "bn":u"নিম্নলিখিত বিকল্পগুলির সর্বব্যাপী উন্নয়নের জন্য অপরিহার্য:",
                "hi":u"",
                "en":"Inclusive development in Bengal should encompass the following:",
                },
            "choices":[ 
                {
                    "bn":u"ছোট এবং মাঝারি ব্যবসার প্রসারণ ঘটানো দরকার ",
                    "hi":u"",
                    "en":u"Empower small industries, medium, small and micro industries",
                },
                {
                    "bn":u"গ্রামীন কল্যাণ কেন্দ্র করে গ্রামীন শিল্প ও কলা উন্নত করা উচিত",
                    "hi":u"",
                    "en":u"Promote rural arts, crafts and artisans with rural welfare as a focal agenda",
                },
                {
                    "bn":u"গুরুত্বপূর্ণ উন্নয়ন প্রকল্পের উপর নজর যেমন আশ্রয়, জল ব্যবস্থা, বিদ্যুত ইত্যাদি ",
                    "hi":u"",
                    "en":u"Focus on developmental projects such as housing, water, sanitation, and power",
                },
                {
                    "bn":u"খাদ্যের মত মৌলিক মানবাদিখার সব থেকে জরুরি এবং সবার কাছে পৌছে দিতে সার্বজনীন পরিষেবা বিতরণ অনিবার্য",
                    "hi":u"",
                    "en":u"Enact a universal public-goods distribution system to tackle fundamental issues such as starvation",
                },]
            },
    3: {
            "type":"pick_many",
            "text":{
                "bn":u"পশ্চিমবঙ্গের শিক্ষা প্রতিষ্ঠান জোরদার করতে আবশ্যক:",
                "hi":u"",
                "en":"Educational institutes in the State must be strengthened through:",
                },
            "choices":[ 
                {
                    "bn":u"বাক স্বাধীনতা এবং ভিন্নমত প্রকাশের অধিকার রক্ষা করা  ",
                    "hi":u"",
                    "en":u"Protect free speech and spaces for dissent",
                },
                {
                    "bn":u"ভোকেশনাল ট্রেনিং সঙ্গে বৃহত্তর শিল্প সংযোগ স্থাপন",
                    "hi":u"",
                    "en":u"Establish greater industry linkages with strong vocational training",
                },
                {
                    "bn":u"উচ্চ শিক্ষার ক্ষেত্রে রাজনৈতিক হস্তক্ষেপ কমানো জরুরি ",
                    "hi":u"",
                    "en":u"De-politicize higher education, especially in faculty appointment and college administration",
                },
                {
                    "bn":u"আরও নতুন কলেজ ও বিশ্ববিদ্যালয় প্রতিষ্ঠান জরুরি ",
                    "hi":u"",
                    "en":u"Establish more centers and institutes for higher education",
                },]
            },
    4: {
            "type":"pick_many",
            "text":{
                "bn":u"নারীর অধিকার ও নিরাপত্তা নিম্নলিখিত উপায়ে মোকাবিলা করা আবশ্যক:",
                "hi":u"",
                "en":"Women's rights and safety must be addressed with the following means:",
                },
            "choices":[ 
                {
                    "bn":u"সামগ্রিক আইন শৃঙ্খলা পরিস্থিতি উন্নত করা যাতে মহিলারা নির্দিধায় জীবনযাপন করতে পারে ",
                    "hi":u"",
                    "en":u"Improve law and order to enable women to access all public spaces",
                },
                {
                    "bn":u"নারীশিক্ষা ও আয় নিরাপত্তা কেন্দ্র করা উচিত ",
                    "hi":u"",
                    "en":u"Place a central focus on women's education and income security",
                },
                {
                    "bn":u"পুলিশ কে আরও লিঙ্গ সংবেদনশীল করা এবং মহিলাদের জন্য আলাদা পুলিশ সংস্থা তৈরী করা",
                    "hi":u"",
                    "en":u"Change the police force to be more responsive and gender-sensitive, and introduce police units dedicated to women",
                },
                {
                    "bn":u"স্কুল ও কলেজ ই লিঙ্গ অধ্যয়ন চালু করা ",
                    "hi":u"",
                    "en":u"Include gender issues in school curricula in schools and colleges to increase awareness",
                },]
            },
   5: {
            "type":"pick_many",
            "text":{
                "bn":u"শ্রমিক দের অধিকার অর্জনের জন্য নিম্নিলিখিত করা কাম্য:",
                "hi":u"",
                "en":"Workers' rights can be significantly improved through:",
                },
            "choices":[ 
                {
                    "bn":u"চুক্তিভিত্তিক এবং দৈনিক মজুরি শ্রমিকদের অধিকার রক্ষা",
                    "hi":u"",
                    "en":u"Protect the rights of contractual and daily wage workers",
                },
                {
                    "bn":u"বেকার শ্রমিকদের ভর্তুকি ও আয়-ভাতা সুবিধা দেওয়া",
                    "hi":u"",
                    "en":u"Give unemployed workers subsidies and income allowances",
                },
                {
                    "bn":u"বিমা পেনশন ছুটি এবং অন্যান্য সুবিধে দেওয়া সব ধরনের শ্রমিকদের বিশেষ করে দৈনিক কর্মীদের",
                    "hi":u"",
                    "en":u"Provide insurance, pension, benefits and leaves to part time, small, and daily wage workers",
                },
                {
                    "bn":u"মহিলা শ্রমিকদের বিশেষ নজর দেওয়া যেমন সার্বজনীন মাতৃত্ব ছুটি অধিকার এবং অনান্য সুবিধে",
                    "hi":u"",
                    "en":u"Provide female workers' rights through maternity leaves, benefits and flexibility",
                },]
            },
    6: {
            "type":"pick_many",
            "text":{
                "bn":u"স্বাস্থ্য ব্যবস্থা এইভাবে উন্নত করা যেতে পারে:",
                "hi":u"",
                "en":"Healthcare in Bengal can be improved through the following means:",
                },
            "choices":[ 
                {
                    "bn":u"নতুন ও উন্নত সুপার স্পেচিয়ালিতী হাসপাতাল    তৈরী করা উচিত ",
                    "hi":u"",
                    "en":u"Facilitate the construction of super-speciality hospitals",
                },
                {
                    "bn":u"শিশু মৃত্যুহার কমানো এবং বিশেষ করে কন্যা শিশুর রক্ষা করা ",
                    "hi":u"",
                    "en":u"Reduce child and infant mortality, with a special focus on the girl child",
                },
                {
                    "bn":u"বর্তমান স্বাস্থ্য পরিকাঠামোর ক্ষমতা বৃদ্ধি",
                    "hi":u"",
                    "en":u"Increase the capacity of current health infrastructure",
                },
                {
                    "bn":u"মহিলা শ্রমিকদের জন্য প্রসবকালীন ছুটি বৃদ্ধি",
                    "hi":u"",
                    "en":u"Increase maternity leave for women employees",
                },]
            },
    7: {
            "type":"pick_many",
            "text":{
                "bn":u"বাংলাদেশ থেকে অবৈধ অনুপ্রবেশ রোধ করতে, নিম্নিলিখিত নীতি আবশ্য়ক:",
                "hi":u"",
                "en":"Immigration and infiltration from Bangladesh poses a challenge for governance in Bengal and it must be dealt through:",
                },
            "choices":[ 
                {
                    "bn":u"বাংলাদেশ থেকে অভিবাসনের উপর কঠোর নিয়ন্ত্রণ পশ্চিমবঙ্গের জনসংখ্যাগত পরিবর্তন রোধ করার জন্য জরুরি ",
                    "hi":u"",
                    "en":u"Tighten immigration from Bangladesh to reduce demographic change in West Bengal",
                },
                {
                    "bn":u"অবৈধ অভিবাসীদের ফেরত পাঠানো জরুরি কিন্তু বৈধ নাগরিকদের অধিকারo রক্ষা করা উচিত ",
                    "hi":u"",
                    "en":u"Deport illegal immigrants but protect Indian citizens",
                },
                {
                    "bn":u"নিপীড়িত  হিন্দু উদ্বাস্তুদের শিক্ষা, কর্ম এবং অর্থনৈতিক সাহায্য কাম্য ",
                    "hi":u"",
                    "en":u"Provide education and job opportunities to persecuted Hindu refugees",
                },
                {
                    "bn":u"সিমান্তরক্ষা বাহিনীর সংখ্যা বৃদ্ধি করা দরকার ",
                    "hi":u"",
                    "en":u"Increase the border security force further",
                },]
            },
    8: {
            "type":"pick_many",
            "text":{
                "bn":u"ধর্মীয় সংখ্যালঘুরা বিশেষ করে মুসলমানেরা এখনো অনুন্নত এবং সেই উন্নয়ন প্রসারিত করতে নিম্নিলিখিত করা উচিত:",
                "hi":u"",
                "en":"Religious minorities, especially Muslims, are underdeveloped in West Bengal right now and their condition can be alleviated through:",
                },
            "choices":[ 
                {
                    "bn":u"ধর্মীয় সংখ্যালঘুদের সামাজিক ও অর্থনৈতিক উন্নয়নের প্রচেষ্টা করতে হবে ",
                    "hi":u"",
                    "en":u"Assist religious minorities with their overall social and economic development",
                },
                {
                    "bn":u"মাদ্রাসা পাঠক্রমের পরিবর্তন দরকার, যার  মাধ্যমে মুসলমান ছাত্র সমাজ সামাজিক ভাবে আরও যুক্ত হতে পারবে ",
                    "hi":u"",
                    "en":u"Change Madrasa curriculums to help Muslim students to integrate with wider society",
                },
                {
                    "bn":u"অনুমোদিত মাদ্রাসা দের সরকারী ভাতা দ্বারা সাহায্য করা উচিত",
                    "hi":u"",
                    "en":u"Provide government grants to approved Madrasas",
                },
                {
                    "bn":u"বিজ্ঞান ও প্রযুক্তির ক্ষেত্রে মাদ্রাসা শিক্ষার্থীদের জন্য সুযোগ উন্নতি",
                    "hi":u"",
                    "en":u"Improve education opportunities for Madrasa students in science and technology",
                },]
            },
    9: {
            "type":"pick_many",
            "text":{
                "bn":u"সুশাসনের জন্য, শাসক শ্রেণীর মধ্যে দুর্নীতি এই ভাবে কমানো যায়",
                "hi":u"",
                "en":"For better governance, corruption among the ruling classes needs to be tackled with the following methods:",
                },
            "choices":[ 
                {
                    "bn":u"দৃঢ় রাষ্ট্র নীতি দ্বারা দুর্নীতির মোকাবিলা করা উচিত ",
                    "hi":u"",
                    "en":u"Enact strong policy initiaitives to identify and tackle corruption issues",
                },
                {
                    "bn":u"বৃহত্তর জবাবদিহিতার জন্য ই-গভর্নেন্স এবং ডিজিটাল স্বচ্ছতা উন্নত করা উচিত ",
                    "hi":u"",
                    "en":u"Implement e-governance and digital transparency for greater accountability",
                },
                {
                    "bn":u"সরকারি পদের জন্য প্রকাশ্য জবাবদিহিতা খুব জরুরি ",
                    "hi":u"",
                    "en":u"Ensure public accountability for government positions",
                },
                {
                    "bn":u"কালো টাকা এবং কালোবাজারে বাণিজ্য নিয়ন্ত্রণ",
                    "hi":u"",
                    "en":u"Track black money and black market trades",
                },
                {
                    "bn":u"সারদা কেলেঙ্কারির মত আর্থিক কেলেঙ্কারি অবিলম্বে মোকাবিলা করতে হবে",
                    "hi":u"",
                    "en":u"Deal with financial scandals such as the Saradha Group scandal as an immediate priority",
                },]
            },
    10: {
            "type":"pick_many",
            "text":{
                "bn":u"বাংলার অর্থনৈতিক উন্নয়নের জন্য শিল্প এবং বানিজ্যে জরুরি এবং নিম্নিলিখিত উপায়ে তার বৃদ্ধি হতে পারে",
                "hi":u"",
                "en":"Industrialization is a key driver of economic development for Bengal and can be achieved through the following means:",
                },
            "choices":[ 
                {
                    "bn":u"বেসরকারী বিনিয়োগ বৃদ্ধি করার চেষ্টা করা উচিত",
                    "hi":u"",
                    "en":u"Encourage private investment",
                },
                {
                    "bn":u"বানিজ্যিক এবং শিল্প কেন্দ্র নির্মান করা উচিত, উন্নত পরিকাঠামো আর যোগাযোগ ব্যবস্থা কেন্দ্র করে",
                    "hi":u"",
                    "en":u"Build industrial parks and centers with a focus on infrastructure and connectivity",
                },
                {
                    "bn":u"আইটির মত বুদ্ধিজীবী শিল্পের বিকাশ খুব জরুরি",
                    "hi":u"",
                    "en":u"Promote intellectual industries such as IT and services",
                },
                {
                    "bn":u"পশ্চিমবঙ্গে ব্যবসা করার সাধ্যতা কমানোর প্রচেষ্টা করা উচিত ",
                    "hi":u"",
                    "en":u"Increase the ease of doing business in Bengal",
                },
                {
                    "bn":u"ব্যবসা ও বানিজ্যের জন্য জমি দখল জরুরি তবে সঠিক বিচার  বিবেচনা করে জমি নেওয়া উচিত",
                    "hi":u"",
                    "en":u"Land acquisition is important for industry but should be done cautiously",
                },]
            }
    })
