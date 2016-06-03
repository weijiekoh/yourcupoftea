#!/usr/bin/env python

import argparse
import csv
import pprint
import msgpack
import re


pretty_print = pprint.pprint

    
def gen_org_entry(c, c_type):
    # Converts "Institute for Fiscal Studies" to "ifs" (not "iffs")
    initials = "".join([x[0].lower() for x in c.split() if x[0].isupper()])
    return {"type":c_type,
            "name":c,
            "initials":initials }


def write_msgpack(data, output_file):
    with open(output_file, "w") as msgpack_file:
        msgpack_file.write(msgpack.packb(data))


def extract_campaign_names(row, start, end):
    names = []
    for c in row[start:end]:
        if c != "Impt" and len(c) != 0:
            names.append(c.strip())

    return names


def get_campaign_id_by_name(campaigns, name):
    for key, val in campaigns.iteritems():
        if val["name"] == name:
            return key


def get_expert_id_by_name(expert_names, name):
    for key, val in expert_names.iteritems():
        if val["name"] == name:
            return key


def extract_pos_score(c):
    # from a string like "Yes (10)", return 10
    # from a string like "Against (-10)", return -10
    # for invalid strings, return 0
    c = c.strip()
    found = re.findall("\((-{0,1}\d+)\)$", c)
    if len(found) == 1:
        return int(found[0])
    else:
        return 0


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

    # Extract questions and options
    print "Extracting questions..."
    data_to_write = {"questions":{},
                     "campaigns": {},
                     "experts": {},
                     "positions": {}}
    questions = {}
    current_qn_num = None
    for row in csv_data[2:]:
        # Question text are on the same rows as the qn nums
        if re.match("\d{1,2}", row[0]):
            current_qn_num =  int(row[0])
            questions[current_qn_num] = {"text":row[1], "options":[]}

        option = row[2]
        questions[current_qn_num]["options"].append({"text":option, 
            "campaign_support": [],
            "expert_views": []})


    # Extract campaign names
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

    campaigns = {}
    expert_names = {}

    i = 0
    for c in stay_campaigns:
        campaigns[i] = gen_org_entry(c, "remain")
        i += 1

    i = len(stay_campaigns) 
    for c in leave_campaigns:
        campaigns[i] = gen_org_entry(c, "leave")
        i += 1

    i = len(leave_campaigns) + len(stay_campaigns) 
    for c in experts:
        expert_names[i] = gen_org_entry(c, "expert")
        i += 1

    # Extract party positions
    print "Extracting party positions"

    current_qn_num = None
    current_option_index = None
    current_campaign_id = None
    org_names_row = csv_data[1]

    for row in csv_data[2:]: # loop through rows
        # Question text are on the same rows as the qn nums
        if re.match("\d{1,2}", row[0]):
            current_qn_num =  int(row[0])
            current_option_index = 0

        option_text = row[2]

        position_score = None
        i = 3
        for c in row[3:]: # loop through each column
            if csv_data[0][i] == "Experts": 
                break

            if i % 2 == 1: # odd cols are position scores
                current_campaign_id = get_campaign_id_by_name(campaigns, org_names_row[i])
                position_score = extract_pos_score(c)
            else:
                importance = None
                if len(c) == 0:
                    importance = 1
                else:
                    importance = int(c)
                questions[current_qn_num]\
                         ["options"]\
                         [current_option_index] \
                         ["campaign_support"].append({
                             "id": current_campaign_id,
                             "position": position_score,
                             "importance": importance
                             })

            i += 1
        
        current_option_index += 1


    # Extract expert views

    print "Extracting expert views"

    i = 0
    for c in csv_data[0]: # loop through each column
        if c == "Experts":
            expert_start_col = i
        i += 1 

    
    i = 0
    current_qn_num = None
    current_option_index = 0
    current_expert_id = None
    for row in csv_data[2:]:
        j = 0
        for c in row[expert_start_col:]:
            if re.match("\d{1,2}", row[0]):
                current_qn_num =  int(row[0])
                current_option_index = 0
                
            current_expert_id = get_expert_id_by_name(expert_names, org_names_row[j])

            questions[current_qn_num]\
                     ["options"]\
                     [current_option_index] \
                     ["expert_views"].append({
                         "id": current_expert_id,
                         "view": c
                         })
            j += 1

        current_option_index += 1
        i += 1



    # Write to output file

    print "Writing file..."
    data_to_write["questions"] = questions
    data_to_write["campaigns"] = campaigns
    data_to_write["experts"] = expert_names
    write_msgpack(data_to_write, output_file)

    print "Done."
