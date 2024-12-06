from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None
expected_output_part_two = None

dirs = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

def parse_input(input_data):
    grid = input_as_grid(input_data)
    pos_guard = None
    direction = '^'
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in '^>v<':
                pos_guard = (x, y)
                direction = grid[y][x]
                grid[y][x] = '.'
                break
        if pos_guard:
            break
    return grid, pos_guard, direction

def traverse_and_get_path(grid, start_pos, start_direction, detect_loop=False):
    x_temp, y_temp = start_pos
    current_direction = start_direction
    visited = set() 
    path_cells = set()

    while True:
        state = (x_temp, y_temp, current_direction)
        path_cells.add((x_temp, y_temp))

        if detect_loop and state in visited:
            # Loop detected
            return True, path_cells
        visited.add(state)

        dx, dy = dirs[current_direction]
        next_x, next_y = x_temp + dx, y_temp + dy

        if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid):
            if grid[next_y][next_x] == '#':
                current_index = '^>v<'.index(current_direction)
                current_direction = '^>v<'[(current_index + 1) % 4]
            else:
                x_temp, y_temp = next_x, next_y
        else:
            # Outside the grid -> no loop
            return False, path_cells

    return False, path_cells


def solve_part_one(input_data):
    grid, pos_guard, start_direction = parse_input(input_data)
    _, visited_cells = traverse_and_get_path(grid, pos_guard, start_direction)
    return len(visited_cells)


def solve_part_two(input_data):
    grid, pos_guard, start_direction = parse_input(input_data)
    _, visited_cells = traverse_and_get_path(grid, pos_guard, start_direction)

    possible_positions = 0

    for (x, y) in visited_cells:
        if (x, y) == pos_guard:
            continue

        original_value = grid[y][x]
        grid[y][x] = '#'

        loop, _, = traverse_and_get_path(grid, pos_guard, start_direction, detect_loop=True)
        if loop:
            possible_positions += 1

        grid[y][x] = original_value

    return possible_positions

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 6, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 6, solve_part_one, solve_part_two)
