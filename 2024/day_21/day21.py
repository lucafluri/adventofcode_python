from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = None  

numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['#', '0', 'A']
]

dirpad = [
    ['#', '^', 'A'],
    ['<', 'v', '>'],
]

def parse_input(input_data):
    lines = input_as_lines(input_data)
    return lines

def solve_part_one(input_data):
    lines = parse_input(input_data)
    print(lines)
    return None


def solve_part_two(input_data):
    return None


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 21, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    #submit_solutions(2024, 21, solve_part_one, solve_part_two)

