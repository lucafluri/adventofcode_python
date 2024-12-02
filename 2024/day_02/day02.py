from utils.aoc import *

def parse_input(input_data):
    data = input_as_lines(input_data)
    data = [line.split(' ') for line in data]
    data = [[int(x) for x in line] for line in data]
    return data

def isValid(line, part1=True):
    steps = [1, 2, 3]
    d = 1 if line[1] - line[0] > 0 else -1
    wrongCount = 0
    for i in range(1, len(line)):
        d0 = 1 if line[i] - line[i-1] > 0 else -1
        if abs(line[i] - line[i-1]) not in steps or d0 != d:
            if(part1): return False
            wrongCount += 1
            if wrongCount > 1:
                return False
    return True

def solve_part_one(input_data):
    data = parse_input(input_data)
    valid = list(map(isValid, data))
    return sum(valid)


def solve_part_two(input_data):
    data = parse_input(input_data)
    valid = [isValid(line, False) for line in data]
    return sum(valid)

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 2, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 2, solve_part_one, solve_part_two)

