import os
from input_manager import download_and_store_data
from puzzle_runner import test_with_example, submit_solutions
import collections
import math


slopes = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]

def count_trees(grid, slope):
    pos = (0, 0)
    count = 0
    while pos[1] < len(grid):
        if grid[pos[1]][pos[0]] == '#': count += 1
        newPos = ((pos[0] + slope[0]) % len(grid[0]), pos[1] + slope[1])
        pos = newPos
    return count

def solve_part_one(input_data):
    grid = input_data.splitlines()
    return count_trees(grid, slopes[0])


def solve_part_two(input_data):
    prod = 1
    for slope in slopes:
        prod *= count_trees(input_data.splitlines(), slope)
    return prod
        
def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 3, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 3, solve_part_one, solve_part_two)
