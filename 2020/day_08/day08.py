from utils.aoc import *

def run_prog(prog):
    acc = 0
    pc = 0
    visited = set()
    visited.clear()
    while 0 <= pc < len(prog):
        if pc in visited: return acc, False
        visited.add(pc)
        op = prog[pc].split(' ')
        if op[0] == 'acc': acc += int(op[1]); pc += 1
        elif op[0] == 'jmp': pc += int(op[1])
        else: pc += 1
    return acc, True

def solve_part_one(input_data):
    prog = input_as_lines(input_data)
    return run_prog(prog)[0]


def solve_part_two(input_data):
    prog = input_as_lines(input_data)
    # iterate from the end and find a jmp or nop
    for i in range(len(prog)-1, -1, -1):
        op = prog[i].split(' ')
        if op[0] == 'jmp': 
            prog[i] = 'nop ' + op[1]
            acc, valid = run_prog(prog)
            if not valid: prog[i] = 'jmp ' + op[1]
        elif op[0] == 'nop': 
            prog[i] = 'jmp ' + op[1]
            acc, valid = run_prog(prog)
            if not valid: prog[i] = 'nop ' + op[1]
        else: continue
        if valid: return acc
    return 0


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 8, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 8, solve_part_one, solve_part_two)

