from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = None  

ops_cache = {}

def parse_input(input_data):
    return [(i[0], i[1:]) for i in map(ints, input_as_lines(input_data))]

def ops(n, part2=False):
    combinations = []
    if (n, part2) in ops_cache:
        return ops_cache[(n, part2)]
    for c in it.product(['+', '*'] if not part2 else ['+', '*', '|'], repeat=n):
        combinations.append(''.join(c))
    ops_cache[(n, part2)] = combinations
    return combinations

def isValid(n, lasts, part2=False, index=0, current_result=None):
    if current_result is None:
        current_result = lasts[0]

    if index == len(lasts) - 1:
        return current_result == n

    if isValid(n, lasts, part2, index + 1, current_result * lasts[index + 1]):
        return True
    if isValid(n, lasts, part2, index + 1, current_result + lasts[index + 1]):
        return True
    if part2 and isValid(n, lasts, part2, index + 1, int(f"{current_result}{lasts[index + 1]}")):
        return True

    return False

def solve_part_one(input_data):
    return sum(n[0] for n in parse_input(input_data) if isValid(n[0], n[1], False))

def solve_part_two(input_data):
    return sum(n[0] for n in parse_input(input_data) if isValid(n[0], n[1], True))

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 7, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 7, solve_part_one, solve_part_two)
