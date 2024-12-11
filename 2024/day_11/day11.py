from utils.aoc import *


# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = 65601038650482  

@cache
def stone_rule(s):
    if(s == 0):
        return (1, None)
    elif(len(str(s)) % 2 == 0):
        return (int(str(s)[:len(str(s))//2]), int(str(s)[len(str(s))//2:]))
    return (s*2024, None)
    
@cache
def count_blinks(s, depth):
    l, r = stone_rule(s)
    if(depth == 1):
        return 1 if r is None else 2
    
    left = count_blinks(l, depth-1)
    right = count_blinks(r, depth-1) if r is not None else 0
    return left + right
    
def solve_part_one(input_data):
    stones = ints(input_data)
    return sum(count_blinks(s, 25) for s in stones)

def solve_part_two(input_data):
    stones = ints(input_data)
    return sum(count_blinks(s, 75) for s in stones)

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 11, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 11, solve_part_one, solve_part_two)

