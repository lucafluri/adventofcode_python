import dis
from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 22
expected_output_part_two = "6, 1" 

def parse_input(input_data):
    coords = []
    for line in input_data.splitlines():
        x, y = ints(line)
        coords.append((x, y))
    return coords

def dijkstra(grid, start, end=None):
    queue = []
    heapq.heappush(queue, (0, start))
    
    distances = { (x, y): float('infinity') for y in range(len(grid)) for x in range(len(grid[0])) }
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        
        if current_vertex == end:
            break
        
        for dx, dy in DIR4:
            nx, ny = current_vertex[0] + dx, current_vertex[1] + dy
            if inside_grid(nx, ny, grid) and grid[ny][nx] != '#':
                distance = current_distance + 1
                if distance < distances[(nx, ny)]:
                    distances[(nx, ny)] = distance
                    heapq.heappush(queue, (distance, (nx, ny)))
        
    return distances


def solve_part_one(input_data):
    coords = parse_input(input_data)
    size = (71, 71)
    max_bytes = 1024
    grid = [['.' for _ in range(size[0])] for _ in range(size[1])]
    
    for y in range(size[1]):
        for x in range(size[0]):
            if (x, y) in coords[:max_bytes]:
                grid[y][x] = '#'
    
    dists = dijkstra(grid, start=(0, 0), end=(size[0]-1, size[1]-1))
    
    return dists[(size[0]-1, size[1]-1)]


def solve_part_two(input_data):
    coords = parse_input(input_data)
    size = (71, 71)
    max_bytes = 1024
    
    grid = [['.' for _ in range(size[0])] for _ in range(size[1])]
        
    for y in range(size[1]):
        for x in range(size[0]):
            if (x, y) in coords[:max_bytes]:
                grid[y][x] = '#'
    
    for i in range(1024, len(coords), 1):
        nx, ny = coords[i][0], coords[i][1]
        grid[ny][nx] = '#'        
                    
        dists = dijkstra(grid, start=(0, 0), end=(size[0]-1, size[1]-1))
        if dists[(size[0]-1, size[1]-1)] == float('infinity'):
            return f"{coords[i][0]},{coords[i][1]}"
    
    return None


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 18, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 18, solve_part_one, solve_part_two)

