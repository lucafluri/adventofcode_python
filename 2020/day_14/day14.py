from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = None


def mask_to_binary(mask):
    #mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    bin_one = 0
    bin_zero = (2**36) - 1
    for i, bit in enumerate(mask):
        if bit == '1':
            bin_one |= (1 << (35 - i))
        elif bit == '0':
            bin_zero &= ~(1 << (35 - i))
    return bin_one, bin_zero

def solve_part_one(input_data):
    data = input_as_lines(input_data)
    mask1, mask0 = (0, 0)
    mem = {}
    
    for line in data:
        if line.startswith('mask'):
            match = re.match('mask = (.*)', line)
            mask1, mask0 = mask_to_binary(match.group(1))
        else:
            match = re.match(r'mem\[(\d+)\] = (\d+)', line)
            mem[int(match.group(1))] = (int(match.group(2)) & mask0) | mask1
    return sum(mem.values())


def solve_part_two(input_data):
    return None

def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 14, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 14, solve_part_one, solve_part_two)

