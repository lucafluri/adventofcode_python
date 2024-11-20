from utils.aoc import *


def solve_part_one(input_data):
    # lines = input_data.splitlines()
    lines = input_as_lines(input_data)
    for line in lines:
        print(line)
        re.match(r'(.+) bags contain ((\d+) (.+) bag[s]?[,.])+', line)
    return 0


def solve_part_two(input_data):
    return 0


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 7, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    #submit_solutions(2020, 7, solve_part_one, solve_part_two)


# Graphs
'''
import networkx as nx
G = nx.Graph()
# G.add_edge(3, 1)
nx.shortest_path(G, -1, 5)
'''

# Assembler interpreter
'''
prog = s.splitlines()
pc = 0
regs = []
while 0 <= pc < len(prog):
    op = prog[pc]
    if op == 1:
        ...
    elif op == 2:
        ...
    else:
        assert False
    pc += 1
'''
