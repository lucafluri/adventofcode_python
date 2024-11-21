from utils.aoc import *



def count_diffs(data):
    diff1 = 1
    diff3 = 1
    for i in range(1, len(data)):
         diff = data[i] - data[i-1]
         if(diff == 1): diff1 += 1
         if(diff == 3): diff3 += 1
    return diff1, diff3

def solve_part_one(input_data):
    data = input_as_ints(input_data)
    data.sort()
    diff1, diff3 = count_diffs(data)
    return diff1 * diff3


def solve_part_two(input_data):
    data = input_as_ints(input_data)
    data.sort()
    
    data = [0] + data + [data[-1] + 3]

    ways = {0: 1}
    for adapter in data[1:]:
        ways[adapter] = ways.get(adapter - 1, 0) + ways.get(adapter - 2, 0) + ways.get(adapter - 3, 0)

    return ways[data[-1]]


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 10, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 10, solve_part_one, solve_part_two)
