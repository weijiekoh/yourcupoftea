#!/usr/bin/env python

import argparse
import csv
import pprint
import msgpack
import re


pretty_print = pprint.pprint



def write_msgpack(data, output_file):
    with open(output_file, "w") as msgpack_file:
        msgpack_file.write(msgpack.packb(data))


def extract_campaign_names(row, start, end):
    names = []
    for c in row[start:end]:
        if c != "Impt" and len(c) != 0:
            names.append(c.strip())

    return names


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert question and position data")
    parser.add_argument("-i", "--input", 
            metavar="filename", 
            required=True, 
            type=str, 
            help="Input file")
    parser.add_argument("-o", "--output", 
            metavar="filename", 
            default="master.csv", 
            required=True, 
            type=str, 
            help="Output MessagePack file")

    args = parser.parse_args()
    input_file = args.input
    output_file = args.output

    csv_data = []

    with open(input_file, "rb") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_data.append(row)

    # extract questions and options

    print "Extracting questions..."
    data_to_write = {"questions":{},
                     "campaigns": {},
                     "experts": {},
                     "positions": {}}
    questions = {}
    current_qn_num = None
    for row in csv_data[2:]:
        # question text are on the same rows as the qn nums
        if re.match("\d{1,2}", row[0]):
            current_qn_num =  int(row[0])
            questions[current_qn_num] = {"text":row[1], "options":[]}
        else:
            option = row[2]
            questions[current_qn_num]["options"].append({"text":option, "supporter_ids":[]})


    # extract campaign names
    print "Extracting campaigns..."

    first_stay = None
    first_leave = None
    first_experts = None
    i = 0
    for c in csv_data[0]:
        if c == "Stay":
            first_stay = i
        elif c == "Leave":
            first_leave = i
        elif c == "Experts":
            first_experts = i
        i += 1

    stay_campaigns = []
    leave_campaigns = []
    experts = []

    row_with_names = csv_data[1]    
    stay_campaigns = extract_campaign_names(row_with_names, first_stay, first_leave)
    leave_campaigns = extract_campaign_names(row_with_names, first_leave, first_experts)
    experts = extract_campaign_names(row_with_names, first_experts, len(row_with_names))

    print stay_campaigns
    print leave_campaigns
    print experts

    
    def gen_campaign_entry(c, c_type):
        initials = "".join([x[0].lower() for x in c.split()])
        return {"type":c_type,
                "name":c,
                "initials":initials
                }


    campaigns = {}
    i = 0
    for c in stay_campaigns:
        campaigns[i] = gen_campaign_entry(c, "stay")
        i += 1

    i = len(stay_campaigns) 
    for c in leave_campaigns:
        campaigns[i] = gen_campaign_entry(c, "leave")
        i += 1

    experts = {}

    print "Writing file..."
    data_to_write["questions"] = questions
    data_to_write["campaigns"] = campaigns
    write_msgpack(data_to_write, output_file)

    print "Done."
