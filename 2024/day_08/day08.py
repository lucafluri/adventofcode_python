from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = 34

def parse_input(input_data):
    grid = input_as_grid(input_data)
    antennas = {}
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '.':
                if grid[y][x] not in antennas:
                    antennas[grid[y][x]] = []
                    antennas[grid[y][x]].append((x, y))
                else:
                    antennas[grid[y][x]].append((x, y))
    return grid, antennas

def get_antinodes(input_data, part2=False):
    grid, antennas = parse_input(input_data)
    antinodes = set()
        
    for k, v in antennas.items():
        if len(v) > 1:
            for pairs in it.combinations(v, 2):
                x1, y1 = pairs[0]
                x2, y2 = pairs[1]
                d = ((x1 - x2), (y1 - y2))
                an1 = x1 + d[0], y1 + d[1]
                while inside_grid(an1[0], an1[1], grid):
                    antinodes.add((an1[0], an1[1]))
                    an1 = (an1[0] + d[0], an1[1] + d[1])
                    if(not part2): break
                
                an2 = x2 - d[0], y2 - d[1]
                while inside_grid(an2[0], an2[1], grid):
                    antinodes.add((an2[0], an2[1]))
                    an2 = (an2[0] - d[0], an2[1] - d[1])
                    if(not part2): break
    if(part2):                 
        for t in antennas.values():
            for a in t:
                antinodes.add(a)
    return antinodes

def solve_part_one(input_data):
    return len(get_antinodes(input_data))

def solve_part_two(input_data):
    return len(get_antinodes(input_data, part2=True))

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 8, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 8, solve_part_one, solve_part_two)

