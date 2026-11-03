from utils.aoc import *



def solve_part_one(input_data):
    ls = input_data.splitlines()
    ls = [int(l) for l in ls]
    for l in ls:
        x = 2020 - int(l)
        if(x in ls): return int(l) * x


def solve_part_two(input_data):
    ls = [int(l) for l in input_data.splitlines()]
    for l in ls:
        t1 = 2020 - int(l)
        for l2 in ls:
            if(t1 == l2): continue
            t2 = 2020 - l2 - l
            if(t2 in ls): return int(l) * l2 * t2
    return 0
