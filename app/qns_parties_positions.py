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
msgpack_file = os.path.join(relpath, "data/data.msgpack")

f = open(msgpack_file, "rb")
data = msgpack.unpackb(f.read())
f.close()

questions = collections.OrderedDict()

q = data["questions"]
for qn_num in sorted(q.keys()):
    questions[qn_num - 1] = q[qn_num]

campaigns = data["campaigns"]
experts = data["experts"]

# URLs

campaigns[0]["url"] = "http://www.strongerin.co.uk/"
campaigns[1]["url"] = "http://infacts.org/"
campaigns[2]["url"] = "http://www.britishinfluence.org/"
campaigns[3]["url"] = "http://www.voteleavetakecontrol.org/"
campaigns[4]["url"] = "http://leave.eu/"
campaigns[5]["url"] = "http://www.betteroffout.net/"


if __name__ == "__main__":
    pass
