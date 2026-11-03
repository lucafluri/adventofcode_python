from utils.aoc import *

# Set these if aocd can't parse the example answers (None = use aocd's guess)
expected_output_part_one = None
expected_output_part_two = None


def parse_input(input_data):
    return input_as_lines(input_data)


def solve_part_one(input_data):
    data = parse_input(input_data)
    return None


def solve_part_two(input_data):
    data = parse_input(input_data)
    return None


def run():
    test_with_example(__YEAR__, __DAY__, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)
    submit_solutions(__YEAR__, __DAY__, solve_part_one, solve_part_two)
