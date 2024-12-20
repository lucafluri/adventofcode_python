import dis
from itertools import count
from os import path
from turtle import st
from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 0
expected_output_part_two = 0

def find_coordinates(grid, char, replace_char=None):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == char:
                if replace_char:
                    grid[y][x] = replace_char
                return (x, y)
    return (0, 0)
            
# Find pattern in both vertical and horizontal direction
def find_patterns(grid):
    possible_cheat_pos = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#' and inside_grid(x+1, y, grid) and grid[y][x+1] == '.' and inside_grid(x-1, y, grid) and grid[y][x-1] == '.':
                possible_cheat_pos.append((x, y))
            elif grid[y][x] == '#' and inside_grid(x, y+1, grid) and grid[y+1][x] == '.' and inside_grid(x, y-1, grid) and grid[y-1][x] == '.':
                possible_cheat_pos.append((x, y))
    return possible_cheat_pos

def parse_input(input_data):
    grid = input_as_grid(input_data)
    start = find_coordinates(grid, 'S', '.')
    end = find_coordinates(grid, 'E', '.')
        
    counter = Counter(input_data)
    max_length = counter['S'] + counter['E'] + counter['.']
    return grid, max_length, (start, end)    
        

def dijkstra(grid, start, end, max_cheat=2):
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
    return None
    grid, max_length, (start, end) = parse_input(input_data)
    # print_grid(grid)
    print(max_length)   
    print(start, end)
    
    print(len(find_patterns(grid)))    
    
    cheats = {}
    
    index = 0
    for cheat in find_patterns(grid):
        if(index % 100 == 0): print(f"{index}/{len(find_patterns(grid))}")
        index += 1
        grid[cheat[1]][cheat[0]] = '.'
        dists = dijkstra(grid, start, end)
        cheats[cheat] = max_length - dists[end] -1
        grid[cheat[1]][cheat[0]] = '#'
        
    # print(cheats)
    
    return sum(1 for k, v in cheats.items() if v >= 100)
    # return 0


def solve_part_two(input_data):
    grid, max_length, (start, end) = parse_input(input_data)
    dists = dijkstra(grid, start, end)
    
    grid_distance = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid_distance[y][x] = grid[y][x]
    
    path_coords = {}
    path_lengths = {}
    
    # print(max_length)
    # pprint(dists)
    
    dists[start] = 0
    
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
            # print(p, q)
            # print(path_coords[p], path_coords[q])
            d = abs(q[0] - p[0]) + abs(q[1] - p[1]) 
            if(2 <= d <=20) and path_coords[q] < path_coords[p]: 
                distances[p][q] = d
    
    # print(distances)
    
                
    # print_grid(grid_distance, 2)
    # pprint(path_coords)
    # pprint(path_lengths)
    count = 0
    all_cheats = {}
    all_cheat_paths = {}
    
    for i in range(max_length-1, -1, -1):
        for cheats in distances[path_lengths[i]]:
            # print(i, cheats, distances[path_lengths[i]][cheats])
            # print(i, path_lengths[i], cheats, grid_distance[cheats[1]][cheats[0]])
            length_cheat = distances[path_lengths[i]][cheats]
            rest = grid_distance[cheats[1]][cheats[0]]
            total = (max_length-1-i) + length_cheat + rest
            saved = max_length-1 - total            
            # print(length_cheat, rest, saved, total)
            
            # if(saved==74):
                # print(i, path_lengths[i], cheats, distances[path_lengths[i]][cheats], grid_distance[cheats[1]][cheats[0]])
            
            # if(saved >= 100):
            #     if saved not in all_cheats:
            #         all_cheats[saved] = 0
            #         all_cheat_paths[saved] = []
            #     all_cheats[saved] += 1
            #     all_cheat_paths[saved].append((path_lengths[i], cheats))
            
            if(saved >= 100): 
                count += 1
                # all_cheats.append((i, cheats))
                
    # pprint(all_cheats)
    
    # pprint(all_cheat_paths[74])
    
    # for i, c in enumerate(all_cheat_paths[74]):
    #     for y in range(len(grid)):
    #         for x in range(len(grid[0])):
    #             if (x, y) == c[0]:
    #                 grid[y][x] = f'X{i}'
    #             if (x, y) == c[1]:
    #                 grid[y][x] = f'Y{i}'
    #             # print(grid[y][x], end='')
    #         # print()
    # print_grid(grid, 2)
    
    # print(all_cheats)
    return count


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 20, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 20, solve_part_one, solve_part_two)

