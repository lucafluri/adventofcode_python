import collections, math, re
import itertools as it
import bisect
from input_manager import download_and_store_data
from puzzle_runner import test_with_example, submit_solutions

def input_split(string, delimiter="\n"):
    """Return input array split by delimiter"""
    return string.split(delimiter)

def input_as_lines(string):
    """Return input as lines split by \\n"""
    return input_split(string)

def input_as_ints(string):
    """Convert each line to int and return list of ints"""
    lines = input_as_lines(string)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))

def input_as_grid(string):
    """Return input as 2D grid"""
    return [list(line) for line in input_as_lines(string)]
