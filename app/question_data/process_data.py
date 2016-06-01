#!/usr/bin/env python

import argparse
import csv
import pprint
import msgpack
import re


def pretty_print(data):
    pprint.pprint(data)


def write_msgpack(questions, output_file):
    data_to_write = msgpack.packb(questions)
    
    print "Writing file..."
    with open(output_file, "w") as msgpack_file:
        msgpack_file.write(data_to_write)


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
    questions = {}
    current_qn_num = None
    for row in csv_data[2:]:
        if re.match("\d{1,2}", row[0]):
            current_qn_num =  int(row[0])
            questions[current_qn_num] = {"text":row[1], "options":[]}
        else:
            option = row[2]
            questions[current_qn_num]["options"].append(option)

    write_msgpack(questions, output_file)

    print "Done."
