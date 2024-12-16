import heapq
from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 7036 
expected_output_part_two = 45  # Adjust if necessary based on new requirements

def parse_input(input_data):
    raw_grid = input_as_grid(input_data)
    nodes = {}
    
    start = None
    end = None
    
    for y in range(len(raw_grid)):
        for x in range(len(raw_grid[0])):
            cell = raw_grid[y][x]
            if cell == 'S':
                start = (x, y)
            if cell == 'E':
                end = (x, y)
            if cell == '#':
                continue
            for dx, dy in DIR4:
                nx, ny = x + dx, y + dy
                if inside_grid(nx, ny, raw_grid) and raw_grid[ny][nx] != '#':
                    if (x, y) not in nodes:
                        nodes[(x, y)] = []
                    nodes[(x, y)].append((nx, ny))
   
    return raw_grid, nodes, start, end

def dijkstra(graph, start, end=None):
    queue = []
    heapq.heappush(queue, (0, start, (1, 0)))
    
    # Initialize distances and predecessors
    distances = { (vertex, direction): float('infinity') for vertex in graph for direction in DIR4 }
    
    prev = { (vertex, direction): [] for vertex in graph for direction in DIR4 }
    
    while queue:
        current_distance, current_vertex, current_direction = heapq.heappop(queue)
        
        if current_vertex == end:
            break
        
        for neighbor in graph[current_vertex]:
            dx = neighbor[0] - current_vertex[0]
            dy = neighbor[1] - current_vertex[1]
            diff = (dx, dy)
            
            weight = 1 if diff == current_direction else 1001
            distance = current_distance + weight
            
            if distance < distances[(neighbor, diff)]:
                distances[(neighbor, diff)] = distance
                prev[(neighbor, diff)] = [(current_vertex, current_direction)]
                heapq.heappush(queue, (distance, neighbor, diff))
            elif distance == distances[(neighbor, diff)]:
                if (current_vertex, current_direction) not in prev[(neighbor, diff)]:
                    prev[(neighbor, diff)].append((current_vertex, current_direction))
                    heapq.heappush(queue, (distance, neighbor, diff))
    
    return distances, prev

def get_all_shortest_paths(prev, start, end):
    paths = []
    end_states = [ (end, direction) for direction in DIR4 ]
    
    def backtrack(current_state, path):
        current_vertex, _ = current_state
        path.append(current_vertex)
        if current_vertex == start:
            paths.append(path[::-1].copy())
        else:
            for predecessor in prev[current_state]:
                backtrack(predecessor, path)
        path.pop()
    
    for state in end_states:
        if prev[state]:  # Only proceed if the state has predecessors
            backtrack(state, [])
    
    return paths

def print_path(grid, path):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in path:
                print('X', end='')
            else:
                print(grid[y][x], end='')
        print()

def solve_part_one(input_data):
    grid, nodes, start, end = parse_input(input_data)
    distances, prev = dijkstra(nodes, start, end)
        
    return min([ distances.get((end, direction), float('infinity')) for direction in DIR4 ])

    # return distances[end]

def solve_part_two(input_data):
    grid, nodes, start, end = parse_input(input_data)
    distances, prev = dijkstra(nodes, start, end)
    
    paths = get_all_shortest_paths(prev, start, end)

    distinct_cells = set()
    for path in paths:
        distinct_cells.update(path)
        
    return len(distinct_cells)

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 16, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 16, solve_part_one, solve_part_two)
