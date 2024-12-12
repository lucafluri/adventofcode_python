from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = 1206  

def parse_input(input_data, part2=False):
    grid = input_as_grid(input_data)
        
    visited = set()
    area = []
    perimeter = []
    sides = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if((x, y) in visited):
                continue
            current = grid[y][x]
            a, p, s = flood_fill(grid, x, y, current, part2=part2)
            visited.update(a)
            area.append(len(a)) 
            perimeter.append(p)        
            sides.append(s)
    
    return grid, area, perimeter, sides


def flood_fill(grid, x, y, value, part2=False):
    to_visit = [(x, y)]
    seen = set()
    perimeter = 0
    corners = 0

    while to_visit:
        px, py = to_visit.pop()
        if (px, py) in seen:
            continue
        seen.add((px, py))
        for dx, dy in DIR4:
            nx, ny = px + dx, py + dy
            if inside_grid(nx, ny, grid) and grid[ny][nx] == value:
                to_visit.append((nx, ny))
            elif not inside_grid(nx, ny, grid):
                perimeter += 1
            elif grid[ny][nx] != value:
                perimeter += 1


   # Count only lowest-right piece of a side.
    if part2: 
        for (x, y) in seen:
            right_out = (x+1, y) not in seen
            bottom_out = (x, y+1) not in seen
            
            # Top Side |- and -|
            if (x, y-1) not in seen and (right_out or (x+1, y-1) in seen):
                corners += 1

            # Bottom Side |- and -|
            if (x, y+1) not in seen and (right_out or (x+1, y+1) in seen):
                corners += 1

            # Left Side
            if (x-1, y) not in seen and (bottom_out or (x-1, y+1) in seen):
                corners += 1

            # Right Side
            if (x+1, y) not in seen and (bottom_out or (x+1, y+1) in seen):
                corners += 1
        
    return seen, perimeter, corners


def solve_part_one(input_data):
    _, area, perimeter, _ = parse_input(input_data)
    return sum([a * p for a, p in zip(area, perimeter)])


def solve_part_two(input_data):
    grid, area, _, sides = parse_input(input_data, part2=True)
    return sum([a * s for a, s in zip(area, sides)])


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 12, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 12, solve_part_one, solve_part_two)
