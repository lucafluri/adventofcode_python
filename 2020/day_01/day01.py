import os
from input_manager import download_and_store_data
from puzzle_runner import test_with_example, submit_solutions
import collections
import math

YEAR = 2020
DAY = 1


def solve_part_one(input_data):
    ls = input_data.splitlines()
    ls = [int(l) for l in ls]
    for l in ls:
        x = 2020 - int(l)
        if(x in ls): return int(l) * x


def solve_part_two(input_data):
    ls = [int(l) for l in input_data.splitlines()]
    for l in ls:
        t1 = 2020 - int(l)
        for l2 in ls:
            if(t1 == l2): continue
            t2 = 2020 - l2 - l
            if(t2 in ls): return int(l) * l2 * t2
    return 0


def run():
    # Use puzzle runner to test with example data
    test_with_example(YEAR, DAY, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(YEAR, DAY, solve_part_one, solve_part_two)
