from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 51   
expected_output_part_two = 208

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

# Return all possible masks by replacing only the X with either 0 or 1
def all_floating_masks(mask, floating_indices):    
    #mask = 0000000000000000000000000000000X00X0    
    all_masks = []
    
    for bits in it.product('01', repeat=len(floating_indices)):
        new_mask = list(mask)
        for i, bit in zip(floating_indices, bits):
            new_mask[i] = bit
        all_masks.append(int(''.join(new_mask), 2))
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
            addr, val = ints(line)
            mem[addr] = (val & mask0) | mask1
    return sum(mem.values())

def solve_part_two(input_data):
    data = input_as_lines(input_data)
    floating_indices = None
    mask = None
    mask1 = 0
    mem = {}
    
    for line in data:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
            floating_indices = [i for i, bit in enumerate(mask) if bit == 'X']
            mask1, mask0 = mask_to_binary(mask)
        else:
            addr, val = ints(line)
            masked_addr = addr | mask1
            all_addrs = all_floating_masks(list(f'{masked_addr:036b}'), floating_indices)
            for a in all_addrs:
                mem[a] = val
    
    return sum(mem.values())

def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 14, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 14, solve_part_one, solve_part_two)
