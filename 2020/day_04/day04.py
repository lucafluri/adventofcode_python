import os
from input_manager import download_and_store_data
from puzzle_runner import test_with_example, submit_solutions
import collections
import math
import re

# Required passport fields
REQUIRED_PASSPORT_FIELDS = {
    'byr': None,  # Birth Year
    'iyr': None,  # Issue Year
    'eyr': None,  # Expiration Year
    'hgt': None,  # Height
    'hcl': None,  # Hair Color
    'ecl': None,  # Eye Color
    'pid': None,  # Passport ID
    #'cid': None   # Country ID
}

passports = []


def solve_part_one(input_data):
    linesPassports = input_data.split("\n\n")
    valid = 0
    for passport in linesPassports:
        matches = re.findall(r'(\w+):(\S+[cm|in]?)', passport)
        passportDict = {}
        for match in matches:
            passportDict[match[0]] = match[1]        
        if all(field in passportDict for field in REQUIRED_PASSPORT_FIELDS):
            valid += 1
            passports.append(passportDict)
            print("Valid: " + str(passportDict))

    print(len(passports))
    print(valid)
    return valid


def solve_part_two(input_data):
    print(len(passports))
    valid = len(passports)
    for passport in passports:
        for key in passport.keys():
            if key == 'byr':
                if not re.match(r'^(19[2-9][0-9]|200[0-2])$', passport[key]):
                    valid -= 1
                    break
            elif key == 'iyr':
                if not re.match(r'^20(1[0-9]|20)$', passport[key]):
                    valid -= 1
                    break
            elif key == 'eyr':
                if not re.match(r'^20(2[0-9]|30)$', passport[key]):
                    valid -= 1
                    break
            elif key == 'hgt':
                height_match = re.match(r'^(1[5-8][0-9]|19[0-3])cm$|^(59|6[0-9]|7[0-6])in$', passport[key])
                if not height_match:
                    valid -= 1
                    break
            elif key == 'hcl':
                if not re.match(r'^#[0-9a-f]{6}$', passport[key].lower()):
                    valid -= 1
                    break
            elif key == 'ecl':
                if not re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', passport[key]):
                    valid -= 1
                    break
            elif key == 'pid':
                if not re.match(r'^[0-9]{9}$', passport[key]):
                    valid -= 1
                    break
    # print(len(passports))
    print(valid)
    return valid


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 4, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 4, solve_part_one, solve_part_two)


# Graphs
'''
import networkx as nx
G = nx.Graph()
# G.add_edge(3, 1)
nx.shortest_path(G, -1, 5)
'''

# Assembler interpreter
'''
prog = s.splitlines()
pc = 0
regs = []
while 0 <= pc < len(prog):
    op = prog[pc]
    if op == 1:
        ...
    elif op == 2:
        ...
    else:
        assert False
    pc += 1
'''
