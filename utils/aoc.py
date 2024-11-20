import collections, math, re
import itertools as it
import bisect
from input_manager import download_and_store_data
from puzzle_runner import test_with_example, submit_solutions


# Input Parsing
def input_split(string, delimiter="\n") -> list:
    """Return input array split by delimiter"""
    return string.split(delimiter)

def input_as_lines(string) -> list:
    """Return input as lines split by \\n"""
    return input_split(string)

def input_as_ints(string) -> list:
    """Convert each line to int and return list of ints"""
    lines = input_as_lines(string)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))

def input_as_grid(string) -> list:
    """Return input as 2D grid"""
    return [list(line) for line in input_as_lines(string)]


#Functional Utils
def quantify(iterable, pred=bool) -> int:
    """Count number of items in iterable for which pred is true"""
    return sum(map(pred, iterable))

def first(iterable, default=None) -> object:
    """Return first item from iterable or default"""
    return next(iter(iterable), default)

def product(iterable) -> int:
    """Return product of items in iterable"""
    return math.prod(iterable)


# Useful Code

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














# Print Utils
def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print()

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def print_dict(d):
    for k, v in d.items():
        print(f"{k}: {v}")
    print()

def print_list(l):
    for item in l:
        print(item)
    print()

