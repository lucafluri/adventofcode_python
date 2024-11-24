from utils.aoc import *
import copy

floor, empty, occupied = '.L#'
crowdedLimit = 4
distance = 1

def firstSeen(grid, x, y, dx, dy):
    for i in range(0, distance):
        x += dx
        y += dy
        if (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            if grid[y][x] != floor:
                return grid[y][x]
        else:
            break
    return False

# Check all 8 adjacent seats if all empty return true
def emptyToOccupied(grid, x, y):
    for (dx, dy) in DIR8:
        if not (0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid)):
            continue
        if firstSeen(grid, x, y, dx, dy) == occupied:
            return False
    return True

# If four or more adjacent seats are occupied, return true
def occupiedToEmpty(grid, x, y):
    count = 0
    for (dx, dy) in DIR8:
        if not (0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid)):
            continue
        if firstSeen(grid, x, y, dx, dy) == occupied:
            count += 1
        if count >= crowdedLimit:
            return True
    return False


def run_round(ref):
    mutated = copy.deepcopy(ref)
    for y in range(len(ref)):
        for x in range(len(ref[0])):
            if ref[y][x] == empty and emptyToOccupied(ref, x, y):
                    mutated[y][x] = occupied
            elif ref[y][x] == occupied and occupiedToEmpty(ref, x, y):
                    mutated[y][x] = empty
    # print_grid(mutated)
    return mutated


def solve_part_one(input_data):
    grid = input_as_grid(input_data)
    crowdedLimit = 4
    distance = 1
    old = grid
    while True:
        new_grid = run_round(old)
        if new_grid == old:
            return sum([row.count(occupied) for row in new_grid])
        old = new_grid
        
    
    return None


def solve_part_two(input_data):
    grid = input_as_grid(input_data)
    global crowdedLimit, distance
    crowdedLimit = 5
    distance = 999999
    
    old = grid
    while True:
        new_grid = run_round(old)
        if new_grid == old:
            return sum([row.count(occupied) for row in new_grid])
        old = new_grid

    return None


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 11, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 11, solve_part_one, solve_part_two)
