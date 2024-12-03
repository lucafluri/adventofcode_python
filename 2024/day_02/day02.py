from utils.aoc import *

# Define the expected example  outputs for part one and part two
expected_output_part_one = None
expected_output_part_two = 4  

def parse_input(input_data):
    data = input_as_lines(input_data)
    data = [line.split(' ') for line in data]
    data = [[int(x) for x in line] for line in data]
    return data

def isValid(line):
    d = 1 if line[1] - line[0] > 0 else -1
    for i in range(1, len(line)):
        d0 = 1 if line[i] - line[i-1] > 0 else -1
        step = abs(line[i] - line[i-1])
        if(step < 1 or step > 3) or d0 != d:
            return False
    return True

def remove_and_test(line):
    for i in range(len(line)):
        if isValid(line[:i] + line[i+1:]):
            return True
    return False



def solve_part_one(input_data):
    data = parse_input(input_data)
    valid = list(map(isValid, data))
    return sum(valid)


def solve_part_two(input_data):
    data = parse_input(input_data)
    valid = [isValid(line) for line in data]
    
    for index, line in enumerate(data):
        if not valid[index] and remove_and_test(line):
            valid[index] = True
    return sum(valid)

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 2, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 2, solve_part_one, solve_part_two)
