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


# Return all pssible masks by replacing only the X with either 0 or 1
def all_floating_masks(mask):    
    #mask = 0000000000000000000000000000000X00X0
    all_masks = []
    print(2**mask.count('X'))
    for i in range(2**mask.count('X')):
        mask1 = mask
        for j in range(mask.count('X')):
            mask1 = mask1[:j] + str((i >> j) & 1) + mask1[j+1:]
        all_masks.append(mask_to_binary(mask1))
    return all_masks


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
    data = input_as_lines(input_data)
    all_masks = []
    
    mem = {}
    
    for line in data:
        if line.startswith('mask'):
            all_masks = all_floating_masks(line.split(' = ')[1])
            print(all_masks)
        else:
            match = re.match(r'mem\[(\d+)\] = (\d+)', line)
            for mask1, mask0 in all_masks:
                mem[(int(match.group(1)) & mask0) | mask1] = int(match.group(2))
    
    return sum(mem.values())

def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 14, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    # submit_solutions(2020, 14, solve_part_one, solve_part_two)

