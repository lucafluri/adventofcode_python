from itertools import count
from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = 16

def parse_input(input_data):
    patterns, towels = input_data.split('\n\n')
    patterns = tuple(patterns.split(', ')) # tuple to be hashable for caching
    towels = input_as_lines(towels)
    return patterns, towels

@cache
def allCombinations(t, patterns):
    if(t == ''): return 1
    return sum(allCombinations(t.removeprefix(p), patterns) for p in patterns if t.startswith(p))

def solve_part_one(input_data):
    patterns, towels = parse_input(input_data)
    allCombs = [allCombinations(towel, patterns) for towel in towels]
    notValid = allCombs.count(0)
    return len(towels) - notValid


def solve_part_two(input_data):
    patterns, towels = parse_input(input_data)
    allCombs = [allCombinations(towel, patterns) for towel in towels]    
    return sum(allCombs)


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 19, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 19, solve_part_one, solve_part_two)
