from utils.aoc import *



def solve_part_one(input_data):
    prog = input_as_lines(input_data)
    acc = 0
    pc = 0
    visited = set()
    while 0 <= pc < len(prog):
        if pc in visited: return acc
        visited.add(pc)
        op = prog[pc].split(' ')
        if op[0] == 'acc': acc += int(op[1]); pc += 1
        elif op[0] == 'jmp': pc += int(op[1])
        else: pc += 1
    
    return 0


def solve_part_two(input_data):
    return 0


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 8, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 8, solve_part_one, solve_part_two)

