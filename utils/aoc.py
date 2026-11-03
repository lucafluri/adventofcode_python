import sys
import re
from math import *
from collections import *
import itertools as it
from functools import *
from fractions import Fraction
import bisect
import heapq
import copy
from pprint import pprint
from builtins import pow  # undo math.pow shadowing (float-only, no modulus)

sys.setrecursionlimit(100000)

# Directions as (dx, dy), y grows downwards: grid[y][x]
DIR4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Left, Right, Up, Down
DIR8 = DIR4 + [
    (-1, -1),  # NorthWest
    (1, -1),   # NorthEast
    (-1, 1),   # SouthWest
    (1, 1),    # SouthEast
]


# Input parsing
def input_split(string, delimiter="\n") -> list:
    return string.split(delimiter)

def input_as_lines(string) -> list:
    return string.splitlines()

def paragraphs(string) -> list:
    """Blocks separated by blank lines."""
    return string.split("\n\n")

def input_as_ints(string) -> list:
    return lmap(int, input_as_lines(string))

def input_as_grid(string) -> list:
    """2D list, access as grid[y][x]."""
    return [list(line) for line in input_as_lines(string)]

def grid_dict(string) -> dict:
    """{(x, y): char}; avoids bounds checks: `if p in grid`."""
    return {(x, y): c for y, line in enumerate(input_as_lines(string)) for x, c in enumerate(line)}

def find(grid: dict, char):
    """First position of char in a grid_dict."""
    return next(p for p, c in grid.items() if c == char)

def get_diagonals_from_lines(lines):
    """Diagonals in both directions (top-left→bottom-right and bottom-left→top-right)."""
    diagonals = []
    rows, cols = len(lines), len(lines[0])
    for d in range(rows + cols - 1):
        diagonals.append(''.join(lines[i][d - i] for i in range(rows) if 0 <= d - i < cols))
        diagonals.append(''.join(lines[i][i - d + cols - 1] for i in range(rows) if 0 <= i - d + cols - 1 < cols))
    return diagonals

def get_columns_from_lines(lines):
    return [''.join(col) for col in zip(*lines)]

def lmap(func, *iterables) -> list:
    return list(map(func, *iterables))

def ints(s: str) -> list:
    return lmap(int, re.findall(r"-?\d+", s))

def positive_ints(s: str) -> list:
    return lmap(int, re.findall(r"\d+", s))

def floats(s: str) -> list:
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))

def positive_floats(s: str) -> list:
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))

def words(s: str) -> list:
    return re.findall(r"[a-zA-Z]+", s)


# Iterables
def flatten(l):
    return [i for x in l for i in x]

def quantify(iterable, pred=bool) -> int:
    """Count items for which pred is true."""
    return sum(map(pred, iterable))

def first(iterable, default=None):
    return next(iter(iterable), default)

def product(iterable):
    return prod(iterable)


# Grids & graphs
def neighbors(p, dirs=DIR4):
    x, y = p
    return [(x + dx, y + dy) for dx, dy in dirs]

def inside_grid(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def bfs(start, next_states):
    """Distances from start to every reachable state. next_states(state) -> iterable of states."""
    dist = {start: 0}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        for nxt in next_states(state):
            if nxt not in dist:
                dist[nxt] = dist[state] + 1
                queue.append(nxt)
    return dist

def dijkstra(start, next_states):
    """Shortest costs from start. next_states(state) -> iterable of (cost, state)."""
    dist = {start: 0}
    queue = [(0, start)]
    while queue:
        d, state = heapq.heappop(queue)
        if d > dist[state]:
            continue
        for cost, nxt in next_states(state):
            if d + cost < dist.get(nxt, inf):
                dist[nxt] = d + cost
                heapq.heappush(queue, (d + cost, nxt))
    return dist


# Math
def chinese_remainder(n, a):
    """Smallest x with x ≡ a_i (mod n_i) for coprime moduli n."""
    N = prod(n)
    return sum(a_i * (N // n_i) * pow(N // n_i, -1, n_i) for n_i, a_i in zip(n, a)) % N

def solve_equations(coefficients, constants):
    """Exact solution of a linear system (Gaussian elimination with Fractions).
    Ints where the solution is integral. Raises ValueError if there is no unique solution.

    >>> solve_equations([[1, 2], [3, 4]], [5, 6])  # x + 2y = 5, 3x + 4y = 6
    [-4, Fraction(9, 2)]
    """
    n = len(coefficients)
    m = [[Fraction(v) for v in row] + [Fraction(c)] for row, c in zip(coefficients, constants)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col]), None)
        if pivot is None:
            raise ValueError("The system has no unique solution")
        m[col], m[pivot] = m[pivot], m[col]
        for r in range(n):
            if r != col and m[r][col]:
                factor = m[r][col] / m[col][col]
                m[r] = [a - factor * b for a, b in zip(m[r], m[col])]
    solutions = [m[i][n] / m[i][i] for i in range(n)]
    return [int(s) if s.denominator == 1 else s for s in solutions]

def lcm_list(nums):
    return lcm(*nums)

def gcd_list(nums):
    return gcd(*nums)


# Printing
def print_grid(grid, spacing=1):
    for row in grid:
        if spacing == 0:
            print(''.join(row))
        else:
            print(' '.join(f'{cell:>{spacing}}' for cell in row))
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
