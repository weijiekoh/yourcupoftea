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
import msgpack
import os

relpath = os.path.dirname(__file__)
msgpack_file = os.path.join(relpath, "question_data/data.msgpack")

f = open(msgpack_file, "rb")
unsorted = msgpack.unpackb(f.read())
f.close()

questions = collections.OrderedDict()

for qn_num in sorted(unsorted.keys()):
    questions[qn_num - 1] = unsorted[qn_num]
