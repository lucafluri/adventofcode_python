from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = None  

def parse_input(input_data):
    adj = {}
    starts, ends = [], []
    
    grid = input_as_grid(input_data)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if(grid[y][x] == '0'): starts.append((x, y))
            if(grid[y][x] == '9'): ends.append((x, y))
            adj[(x, y)] = []    
            for dx, dy in DIR4:
                nx, ny = x + dx, y + dy
                if inside_grid(nx, ny, grid) and int(grid[ny][nx]) == int(grid[y][x]) + 1:
                        adj[(x, y)].append((nx, ny))
    return adj, starts, ends

def DFS(adj, starts, ends, part2=False):
    counts = {}
    for x, y in starts:
        visited = set()
        visited.add((x, y))
        counts[(x, y)] = []
        stack = [(x, y)]
        while stack:
            nx, ny = stack.pop()
            for nx2, ny2 in adj[(nx, ny)]:
                if (nx2, ny2) not in visited:
                    if (nx2, ny2) in ends:
                        counts[(x, y)].append((nx2, ny2))
                    if(not part2): visited.add((nx2, ny2))
                    stack.append((nx2, ny2))
    return counts

def solve_part_one(input_data):
    adj, starts, ends = parse_input(input_data)
    counts = DFS(adj, starts, ends)
    counts = {k: len(v) for k, v in counts.items()}
    return sum(ends for ends in counts.values())


def solve_part_two(input_data):
    adj, starts, ends = parse_input(input_data)
    counts = DFS(adj, starts, ends, part2=True)
    counts = {k: len(v) for k, v in counts.items()}
    return sum(ends for ends in counts.values())


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 10, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 10, solve_part_one, solve_part_two)

