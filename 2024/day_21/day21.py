from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = 154115708116294  

numpad = ["789", "456", "123", "#0A"]
dirpad = ["#^A", "<v>"]
delta = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}

def parse_input(input_data):
    lines = input_as_lines(input_data)
    return lines

def isNumpad(a, b):
    return a.isdigit() or b.isdigit()

def get_pos(char, num=True):
    pad = numpad if num else dirpad
    for y in range(len(pad)):
        for x in range(len(pad[0])):
            if pad[y][x] == char:
                return x, y

def get_delta(a, b):
    if(a == b): return (0, 0)
    apos = get_pos(a, isNumpad(a, b))
    bpos = get_pos(b, isNumpad(a, b))
    return (bpos[0] - apos[0], bpos[1] - apos[1])

def is_valid_move(a, b, moves):
    pad = numpad if isNumpad(a, b) else dirpad
    apos = get_pos(a, pad is numpad)

    for m in moves:
        newpos = (apos[0] + delta[m][0], apos[1] + delta[m][1])
        if(pad[newpos[1]][newpos[0]] == '#'):
            return False
        apos = newpos
    return True

def get_all_paths(a, b):
    dx, dy = get_delta(a, b)
    chary = '^' if dy < 0 else 'v'
    charx = '<' if dx < 0 else '>'
    allmoves = chary * abs(dy) + charx * abs(dx)
    possible = set()
    for p in it.permutations(allmoves): # ABC => ABC, BCA, CBA...
        if is_valid_move(a, b, p): 
            possible.add(''.join(p) + 'A')
    return possible

@cache
def get_shortest_path(code, depth):
    min_length = 0
    for a, b in  it.pairwise('A' + code): # ABC => AB, BC
        moves = get_all_paths(a, b)
        min_length += min(len(p) if depth == 0 else get_shortest_path(p, depth-1) for p in moves)
    return min_length

def solve_part_one(input_data):
    return sum(get_shortest_path(line, 2) * int(line.replace('A', '')) for line in parse_input(input_data))

def solve_part_two(input_data):
    return sum(get_shortest_path(line, 25) * int(line.replace('A', '')) for line in parse_input(input_data))

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 21, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 21, solve_part_one, solve_part_two)

