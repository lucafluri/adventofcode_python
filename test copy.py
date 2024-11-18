import os
import aocd

from aoc_secrets import AOC_COOKIE # Put your session cookie in this variable
os.environ['AOC_SESSION'] = AOC_COOKIE

YEAR = '2020'
day = 3

puzzle = aocd.Puzzle(year=YEAR, day=day)


# s = aocd.get_data(day=day, year=YEAR)

# s = get_input(DAY)
# s = get_example(DAY)

import collections
import math

ans = 569

ls = s.splitlines()
for l in ls:
    print (l)

# submit(DAY, ans)