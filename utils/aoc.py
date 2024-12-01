import re
from math import *
from collections import *
import itertools as it
from functools import *
import bisect
from input_manager import download_and_store_data
from puzzle_runner import test_with_example, submit_solutions

# Common Utils

DIR4 = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Left, Right, Up, Down
DIR8 = [
    (-1, 0),  # West
    (1, 0),   # East
    (0, -1),  # North
    (0, 1),   # South
    (-1, -1), # NorthWest
    (-1, 1),  # NorthEast
    (1, -1),  # SouthWest
    (1, 1)    # SouthEast
]


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
    return list(list(line) for line in input_as_lines(string))


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


# Math Utils
# Helper function for Chinese Remainder Theorem
def chinese_remainder(n, a):
    """
    Takes in a list of remainders (a) and a list of moduli (n)
    Solve the equation
        x = a_0 (mod n_0)
        x = a_1 (mod n_1)
        ...
        x = a_{n-1} (mod n_{n-1})
    for x.
    """
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

# Helper function to find modular inverse
def mul_inv(a, b):
    """
    Takes two integers a and b.
    Returns the integer such that (a * x) % b == 1
    """
    
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def lcm_list(nums):
    return reduce(lcm, nums, 1)

def gcd_list(nums):
    return reduce(gcd, nums, nums[0])

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)



# Useful Code

# Graphs
'''
queue = deque()
queue.append((0, 0))
visited = set()
visited.add((0, 0))
while queue:
    x, y = queue.popleft()
    for dx, dy in DIR4:
        nx, ny = x + dx, y + dy
        if (nx, ny) in visited:
            continue
        visited.add((nx, ny))
        queue.append((nx, ny))
'''

'''General DFS
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
'''

'''
# General Karger Alorithm to find minimum cut in a graph
def karger_stein(g):
    while len(g) > 2:
        u, v = random.sample(g.nodes(), 2)
        g.remove_node(u)
        g.remove_node(v)
        g.add_edge(u, v)
    return g
'''

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

