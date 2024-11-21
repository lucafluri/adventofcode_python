from utils.aoc import *

# Check all 8 adjacent seats if all empty return true
def emptyToOccupied(grid, y, x):
    for (dy, dx) in DIR8:
        if x+dx < 0 or x+dx >= len(grid[0]) or y+dy < 0 or y+dy >= len(grid):
            continue
        if grid[y+dy][x+dx] == '#':
            return False
    return True

# If four or more adjacent seats are occupied, return true
def occupiedToEmpty(grid, y, x):
    count = 0
    for (dy, dx) in DIR8:
        if x+dx < 0 or x+dx >= len(grid[0]) or y+dy < 0 or y+dy >= len(grid):
            continue
        if grid[y+dy][x+dx] == '#':
            count += 1
    if count >= 4:
        return True
    return False


def run_round(ref):
    mutated = ref.copy()
    for y in range(len(ref)):
        for x in range(len(ref[0])):
            if ref[y][x] == 'L':
                if emptyToOccupied(ref, y, x):
                    mutated[y][x] = '#'
            elif ref[y][x] == '#':
                if occupiedToEmpty(ref, y, x):
                    mutated[y][x] = 'L'
    print_grid(mutated)
    return mutated


def solve_part_one(input_data):
    grid = input_as_grid(input_data)
    grid2 = input_as_grid(input_data)

    print_grid(grid)
    # grid2 = run_round(grid)
    # grid2 = grid.copy()
    # grid = run_round(grid)
    # grid2 = grid.copy()
    
    while True:
        grid = run_round(grid)
        if grid == grid2:
            # print_grid(grid)
            return sum([row.count('#') for row in grid])
        grid2 = grid.copy()
    
    
    return 0


def solve_part_two(input_data):
    return 0


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 11, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    #submit_solutions(2020, 11, solve_part_one, solve_part_two)


