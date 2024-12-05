from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = None  

def parse_orderings(l):
    orderDict = {}
    for l, r in (line.split('|') for line in l):
        if int(l) not in orderDict:
            orderDict[int(l)] = []
        orderDict[int(l)].append(int(r))
    return orderDict

def parse_input(input_data):
    o, l = input_data.split('\n\n')
    orderDict = parse_orderings(input_as_lines(o))
    lines = [line.split(',') for line in input_as_lines(l)]
    lines = [[int(x) for x in line] for line in lines]
    return orderDict, lines

def is_valid(line, orderDict):
    seen = set()
    for x in line:
        if x in orderDict and any(y in seen for y in orderDict[x]):
            return False
        seen.add(x)
    return True

def correct_order(line, orderDict):
    for i in range(len(line)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if(line[i] in orderDict and line[j] in orderDict[line[i]]):
                line[i], line[j] = line[j], line[i]
    return line
  
def solve_part_one(input_data):
    orderDict, lines = parse_input(input_data)
    return sum(line[len(line)//2] for line in lines if is_valid(line, orderDict))

def solve_part_two(input_data):
    orderDict, lines = parse_input(input_data)
    return sum(correct_order(line, orderDict)[len(line)//2] for line in lines if not is_valid(line, orderDict))

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 5, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 5, solve_part_one, solve_part_two)

