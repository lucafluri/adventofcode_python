from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = None  

def parse_input(input_data):
    disk = []
    for i in range(len(input_data)):
        size = int(input_data[i])
        if i % 2 == 0 and size > 0:
            disk.append((i // 2, size))
        elif size > 0:
            disk.append((None, size))
    return disk

def solve_part_one(input_data):
    disk = parse_input(input_data)
    unpacked = []
    
    for index, size in disk:
        unpacked.extend([index if index is not None else -1] * size)
    
    l, r = 0, len(unpacked) - 1
    while l < r:
        while unpacked[l] != -1:
            l += 1
        while unpacked[r] == -1:
            r -= 1
        unpacked[l], unpacked[r] = unpacked[r], unpacked[l]
        l += 1
        r -= 1

    unpacked = [i for i in unpacked if i != -1]
    return sum(value * i for i, value in enumerate(unpacked))


def solve_part_two(input_data):
    disk = parse_input(input_data)
    
    for i in range(1, len(disk)):
        num, size = disk[-i]
        if num is None:
            continue
        
        for j, (n, s) in enumerate(disk[:-i]):
            if n is None and s >= size:
                disk[j] = (num, s) if s == size else (None, s - size)
                if s > size:
                    disk.insert(j, (num, size))
                disk[-i] = (None, size)
                break
    checksum = 0
    i = 0
    for num, size in disk:
        if num is not None:
            for offset in range(size):
                checksum += num * (i + offset)
        i += size
    return int(checksum)

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 9, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 9, solve_part_one, solve_part_two)
