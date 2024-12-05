from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = None  

def parse_input(input_data):
    return None

def solve_part_one(input_data):
    total = 0
    for line in input_as_lines(input_data):
        l, w, h = ints(line)
        total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    return total

def solve_part_two(input_data):
    total = 0
    for line in input_as_lines(input_data):
        lenghts = sorted(ints(line))
        l, w, h = lenghts
        total += l*w*h + (lenghts[0]*2 + lenghts[1]*2)
    return total


def run():
    # Use puzzle runner to test with example data
    test_with_example(2015, 2, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2015, 2, solve_part_one, solve_part_two)

