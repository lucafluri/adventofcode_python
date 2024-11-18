import os
from input_manager import download_and_store_data
from puzzle_runner import test_with_example, submit_solutions
import collections
import math
import parse

Pattern = parse.compile('{min:d}-{max:d} {char}: {pw}')

def solve_part_one(input_data):
    valid = 0
    
    ls = input_data.splitlines()
    for l in ls:
        match = Pattern.parse(l)
        count = 0
        for c in match.named['pw']:
            if c == match.named['char']: count += 1
        if count >= match.named['min'] and count <= match.named['max']: valid += 1
    return valid


def solve_part_two(input_data):
    valid = 0
    
    ls = input_data.splitlines()
    for l in ls:
        match = Pattern.parse(l)
        l1 = match['pw'][match['min']-1]
        l2 = match['pw'][match['max']-1]
        if (l1 == match['char'] and l2 != match['char']) or (l1 != match['char'] and l2 == match['char']): valid += 1
    return valid


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 2, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 2, solve_part_one, solve_part_two)
