from utils.aoc import *
import copy

floor, empty, occupied = '.L#'

def precompute_visibility(grid, max_distance):
    visibility_map = {}
    rows, cols = len(grid), len(grid[0])
    for y in range(rows):
        for x in range(cols):
            visibility_map[(x, y)] = []
            for dx, dy in DIR8:
                nx, ny = x, y
                distance = 0
                while distance < max_distance:
                    nx += dx
                    ny += dy
                    distance += 1
                    if not (0 <= nx < cols and 0 <= ny < rows):
                        break
                    if grid[ny][nx] != floor:
                        visibility_map[(x, y)].append((nx, ny))
                        break
    return visibility_map


def run_round(ref, visibility_map, crowdedLimit=4):
    mutated = [row[:] for row in ref]
    changed = False

    for y in range(len(ref)):
        for x in range(len(ref[0])):
            occupied_count = sum(ref[ny][nx] == occupied for nx, ny in visibility_map[(x, y)])
            if ref[y][x] == empty and occupied_count == 0:
                mutated[y][x] = occupied
                changed = True
            elif ref[y][x] == occupied and occupied_count >= crowdedLimit:
                mutated[y][x] = empty
                changed = True

    return mutated, changed


def solve_part_one(input_data):
    grid = input_as_grid(input_data)
    visibility_map = precompute_visibility(grid, max_distance=1)
    distance = 1

    old = grid
    while True:
        new_grid, changed = run_round(old, visibility_map)
        if not changed:
            return sum(row.count(occupied) for row in new_grid)
        old = new_grid

    return None


def solve_part_two(input_data):
    grid = input_as_grid(input_data)
    visibility_map = precompute_visibility(grid, max_distance=9999)
    global crowdedLimit, distance
    
    old = grid
    while True:
        new_grid, changed = run_round(old, visibility_map, crowdedLimit=5)
        if not changed:
            return sum(row.count(occupied) for row in new_grid)
        old = new_grid

    return None


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 11, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 11, solve_part_one, solve_part_two)
