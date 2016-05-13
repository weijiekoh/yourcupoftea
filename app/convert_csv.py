#!/usr/bin/env python

import csv
import ast
import argparse

from questions import questions
from parties import parties
from party_positions import party_positions
import ranking

parser = argparse.ArgumentParser(description="Convert Electionance data")
parser.add_argument("-i", "--input",  metavar="filename", required=True, type=str, help="Input filename")

args = parser.parse_args()

input_file = args.input 

party_initial_order = parties.keys()

with open(input_file, "rb") as csvfile:
    reader = csv.reader(csvfile)
    i = 0
    for row in reader:
        if i == 0:
            for item in row + [parties[x]["initials"] for x in party_initial_order]:
                print repr(item) + ",",
            print
        else:
            if row[4][0] == "-":
                continue

            data = ast.literal_eval(row[4])

            rankings = ranking.calculate(data, parties, party_positions, questions)

            for item in row:
                print repr(item), ",",
            for party_id in party_initial_order:
                print repr(rankings[party_id]), ",",
            print
        
        i += 1
