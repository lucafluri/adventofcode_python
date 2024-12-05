from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 0 
expected_output_part_two = None  

def solve_part_one(input_data):
    c = Counter(input_data)
    return c['('] - c[')']


def solve_part_two(input_data):
    floor = 0
    for i, c in enumerate(input_data, 1):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return i
    return None


def run():
    # Use puzzle runner to test with example data
    test_with_example(2015, 1, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2015, 1, solve_part_one, solve_part_two)

