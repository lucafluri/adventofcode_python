from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = None  

def parse_input(input_data):
    data = input_data.split("\n")
    groups = []
    locks, keys = [], []
    lockN, keyN = [], []
    for k, g in it.groupby(data, lambda x: x != ''):
        if k:
            groups.append(list(g))

    for g in groups:
        topRow = g[0]
        heights = []
        cols =get_columns_from_lines(g)
        for c in cols:
            heights.append(c.count('#')-1)
        
        if(all(x == '#' for x in topRow)):
            locks.append(g)
            lockN.append(heights)
        else:
            keys.append(g)
            keyN.append(heights)
    return lockN, keyN

def fitting_key(lock, key):
    for l, k in zip(lock, key):
        if((l + k) > 5):
            return False
    return True

def solve_part_one(input_data):
    locks, keys = parse_input(input_data)
    
    return sum(1 for l, k in it.product(locks, keys) if fitting_key(l, k))



def solve_part_two(input_data):
    return None
