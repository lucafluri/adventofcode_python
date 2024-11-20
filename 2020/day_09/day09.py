from utils.aoc import *

def isValid(n, lasts):
    # ordered = sorted(lasts)
    for i in range(len(lasts)):
        if n-lasts[i] in lasts[i+1:]:
            # print(n, lasts[i], n-lasts[i], lasts[i+1:])
            return True
    return False   

def solve_part_one(input_data):
    data =input_as_ints(input_data)
    preamble = 5 if len(data) < 25 else 25
    for i in range(preamble, len(data)):
        if not isValid(data[i], data[i-preamble:i]):
            return data[i]
    return 0


def solve_part_two(input_data):
    target = solve_part_one(input_data)
    data =input_as_ints(input_data)
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if sum(data[i:j]) == target:
                return min(data[i:j]) + max(data[i:j])
    return 0


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 9, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 9, solve_part_one, solve_part_two)

