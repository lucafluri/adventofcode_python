from utils.aoc import *

# Define the expected example  outputs for part one and part two
expected_output_part_one = None
expected_output_part_two = 4  

def isValid(line):
    d = (line[1] > line[0]) - (line[1] < line[0])
    return all(1 <= abs(line[i] - line[i-1]) <= 3 and 
            (line[i] > line[i-1]) - (line[i] < line[i-1]) == d 
            for i in range(1, len(line)))

def remove_and_test(line):
    return any(isValid(line[:i] + line[i+1:]) for i in range(len(line)))

def solve_part_one(input_data):
    data = [ints(line) for line in input_as_lines(input_data)]
    return sum(map(isValid, data))

def solve_part_two(input_data):
    data = [ints(line) for line in input_as_lines(input_data)]
    valid = [isValid(line) for line in data]
    return sum([v or remove_and_test(line) for v, line in zip(valid, data)])

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 2, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 2, solve_part_one, solve_part_two)
