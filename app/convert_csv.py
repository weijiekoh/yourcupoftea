#!/usr/bin/env python

import csv
import ast
import argparse

from qns_parties_positions import questions
from parties import parties
from qns_parties_positions import party_positions
import ranking

parser = argparse.ArgumentParser(description="Convert Electionance data")
parser.add_argument("-i", "--input",  metavar="filename", required=True, type=str, help="Input filename")
parser.add_argument("-o", "--output",  metavar="filename", required=True, type=str, help="Output filename")

args = parser.parse_args()

input_file = args.input 
output_file = args.output 

party_initial_order = parties.keys()

def repr_dblq(x):
    return "\"" + str(x) + "\""

with open(input_file, "rb") as csvfile:
    with open(output_file, "wb") as writefile:
        reader = csv.reader(csvfile)
        writer = csv.writer(writefile)
        i = 0
        for row in reader:
            if i == 0:
                writer.writerow(row + [parties[x]["initials"] for x in party_initial_order])
                # for item in row + [parties[x]["initials"] for x in party_initial_order]:
                    # print repr_dblq(item) + ",",
                # print
            else:
                if row[4][0] == "-":
                    writer.writerow(row + ["999" for party_id in party_initial_order])
                else:
                    data = ast.literal_eval(row[4])
                    rankings = ranking.calculate(data, parties, party_positions, questions)
                    writer.writerow(row + [rankings[party_id] for party_id in party_initial_order])
            
            i += 1
