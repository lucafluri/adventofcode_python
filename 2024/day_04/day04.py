from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 18    
expected_output_part_two = 9

def parse_input(input_data):
    rows = input_as_lines(input_data)
    cols = get_columns_from_lines(rows)
    diags = get_diagonals_from_lines(rows)
    return rows, cols, diags

def is_XMAS(x, y, grid):
    if grid[y][x] != 'A':
        return False

    corner_patterns = [
        ('M', 'S', 'M', 'S'),
        ('S', 'M', 'S', 'M'),
        ('M', 'M', 'S', 'S'),
        ('S', 'S', 'M', 'M')
    ]
    
    corners = [
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y + 1)
    ]
    
    for pattern in corner_patterns:
        if all(grid[cy][cx] == p for (cx, cy), p in zip(corners, pattern)):
            return True
    
    return False

def solve_part_one(input_data):
    rows, cols, diags = parse_input(input_data)
    c = 0
    for line in rows + cols + diags:
        m1 = re.findall(r'XMAS', line)
        m2 = re.findall(r'SAMX', line)
        c += len(m1) + len(m2)
    
    return c

def solve_part_two(input_data):
    grid = input_as_grid(input_data)
    c = 0
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            if is_XMAS(x, y, grid):
                c += 1
    return c


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 4, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 4, solve_part_one, solve_part_two)
