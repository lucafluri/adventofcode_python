import os
from input_manager import download_and_store_data
from puzzle_runner import test_with_example, submit_solutions
import collections
import math



def getLower(t):
    return (t[0], int((t[1]-t[0])/2)+t[0])

def getUpper(t):
    return (int((t[1]-t[0])/2 + t[0])+1, t[1])

def calcRow(p):
    row = (0, 127)
    
    rc = p[:-3]
    # print(p, rc)

    for c in rc:
        if(c=='F'):
            row = getLower(row)
        if(c=='B'):
            row = getUpper(row)
        # print(row)

    return row[0]

def calcCol(p):
    col = (0, 7)
    rc = p[7:]
    # print(p, rc)
    for c in rc:
        if(c=='L'):
            col = getLower(col)
        if(c=='R'):
            col = getUpper(col)
        # print(col)

    return col[0]

            

def solve_part_one(input_data):
    passes = []
    passes.clear()
    passes = input_data.splitlines()
    
    maxID = 0
    
    for p in passes:
        r = calcRow(p)
        c = calcCol(p)
        id = r*8 + c
        if(id>maxID):
            maxID = id
        
        # print(r, c, id)
    return maxID


def solve_part_two(input_data):
    return 0


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 5, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 5, solve_part_one, solve_part_two)


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
