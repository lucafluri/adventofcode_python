from utils.aoc import *


def solve_part_one(input_data):
    earliest, busses = input_data.splitlines()
    earliest = int(earliest)
    busses = [int(b) for b in busses.split(',') if b != 'x']


def solve_part_two(input_data):
    return None


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 13, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    #submit_solutions(2020, 13, solve_part_one, solve_part_two)

