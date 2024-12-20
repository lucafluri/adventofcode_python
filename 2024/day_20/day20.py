from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 0
expected_output_part_two = 0

def parse_input(input_data):
    grid = input_as_grid(input_data)
    start = find_coordinates(grid, 'S', '.')
    end = find_coordinates(grid, 'E', '.')
        
    counter = Counter(input_data)
    max_length = counter['S'] + counter['E'] + counter['.']
    return grid, max_length, (start, end)    

def find_coordinates(grid, char, replace_char=None):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == char:
                if replace_char:
                    grid[y][x] = replace_char
                return (x, y)
    return (0, 0)
            
def dijkstra(grid, start, end):
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
    
    distances[start] = 0
    return distances

def get_count(input_data, max_cheat=2):
    grid, max_length, (start, end) = parse_input(input_data)
    dists = dijkstra(grid, start, end)
    
    grid_distance = copy.deepcopy(grid)
    
    path_coords = {}
    path_lengths = {}
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '.':
                l = int(max_length - dists[(x, y)] -1)
                grid_distance[y][x] = l
                path_coords[(x, y)] = l
                path_lengths[l] = (x, y)
                
    grid_distance[start[1]][start[0]] = max_length-1
    path_coords[start] = max_length -1
    path_lengths[max_length -1] = start
    
    distances = {} # (x, y): {(a, b): distance}
    for p in path_coords:
        distances[p] = {}
        for q in path_coords:
            d = abs(q[0] - p[0]) + abs(q[1] - p[1]) 
            if(2 <= d <=max_cheat) and path_coords[q] < path_coords[p]: 
                distances[p][q] = d
    
    count = 0
    
    for i in range(max_length-1, -1, -1):
        for cheats in distances[path_lengths[i]]:
            length_cheat = distances[path_lengths[i]][cheats]
            rest = grid_distance[cheats[1]][cheats[0]]
            total = (max_length-1-i) + length_cheat + rest
            saved = max_length-1 - total            

            if(saved >= 100): 
                count += 1

    return count


def solve_part_one(input_data):
    return get_count(input_data, 2)

def solve_part_two(input_data):
    return get_count(input_data, 20)
    
    
def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 20, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 20, solve_part_one, solve_part_two)

