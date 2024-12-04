from utils.aoc import *

# Define the expected example  outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = 31

def parse_data(input_data):
    data = input_as_lines(input_data)
    left, right, rightC = [], [], {}
    
    for line in data:
        l = int(line[:len(line)//2])
        r = int(line[len(line)//2:])
        
        left.append(l)
        right.append(r)
        
        if r in rightC:
            rightC[r] += 1
        else:
            rightC[r] = 1
            
    return left, right, rightC
    

def solve_part_one(input_data):
    left, right, _ = parse_data(input_data)
    left.sort()
    right.sort()
    return sum(abs(l - r) for l, r in zip(left, right))


def solve_part_two(input_data):
    left, right, rightC = parse_data(input_data)
    return sum(num * rightC[num] for num in left if num in rightC)


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 1, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 1, solve_part_one, solve_part_two)

