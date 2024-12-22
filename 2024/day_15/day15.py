from tabnanny import check
from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = None  

def parse_input(input_data, part2=False):
    grid, moves = input_data.split('\n\n')
    moves = moves.replace('\n', '') 
    
    if part2:
        grid = grid.replace('#', '##')
        grid = grid.replace('O', '[]')
        grid = grid.replace('.', '..')
        grid = grid.replace('@', '@.')
    
    grid = input_as_grid(grid)
 
    return grid, moves

def get_delta(move='^'):
    if move == '^': return 0, -1
    if move == '>': return 1, 0
    if move == 'v': return 0, 1
    return -1, 0

def move_horizontal(grid, pos, move='>'):
    x, y = pos
    dx, dy = get_delta(move)
    
    nx, ny = x + dx, y + dy
    blocks = []
    full = True
    index = 0
    index_space = 9999999999
    while inside_grid(nx, ny, grid) and grid[ny][nx] != '#':
        blocks.append(grid[ny][nx])
        if(grid[ny][nx] == '.'): 
            full = False
            index_space = index
            break
        nx, ny = nx + dx, ny + dy
        index += 1
    
    if not full:
        x = x + dx
        y = y + dy
        
        blocks.insert(0, '@')
        blocks.pop()
        for i in range(len(blocks)):
            nx, ny = x + dx * i, y + dy * i
            grid[ny][nx] = blocks[i]
        pos = (x, y)
        grid[y-dy][x-dx] = '.'    
    return grid, pos

def check_vertical(grid, pos, move='v'):    
    x, y = pos
    dx, dy = get_delta(move)
    
    # Check if next position is valid
    next_y = y + dy
    next_x = x + dx
    
    # Base cases
    if not inside_grid(next_x, next_y, grid):
        return False
    if grid[next_y][next_x] == '#':
        return False
    if grid[next_y][next_x] == '.':
        return True
    
    # Handle box cases
    if grid[y][x] == '[':
        # For a box, check both corners
        return check_vertical(grid, (next_x, next_y), move) and check_vertical(grid, (next_x + 1, next_y), move)
    else:
        # For a regular position, check both possible paths
        return check_vertical(grid, (next_x, next_y), move) and check_vertical(grid, (next_x - 1, next_y), move)

def move_recursive(grid, pos, move='v'):
    x, y = pos
    dx, dy = get_delta(move)
    
    before_x = x-dx
    before_y = y-dy    
    next_y = y + dy
    next_x = x + dx
    # Base cases
    if not inside_grid(before_x, before_y, grid) or not inside_grid(next_x, next_y, grid):
        # print('Out of bounds')
        return False
    
    # print(len(grid), len(grid[0]))
    # print(x, y, before_x, before_y, next_x, next_y)
    grid[y][x] = grid[before_y][before_x]
    
    # print_grid(grid, 0)
    
    # Handle box cases
    if grid[y][x] == '[':
        # For a box, check both corners
        return move_recursive(grid, (next_x, next_y), move) and move_recursive(grid, (next_x + 1, next_y), move)
    else:
        # For a regular position, check both possible paths
        return move_recursive(grid, (next_x, next_y), move) and move_recursive(grid, (next_x - 1, next_y), move)
    return grid



def move_vertical(grid, pos, move='v'):
    if not check_vertical(grid, pos, move):
        return grid, pos
    
    x, y = pos
    dx, dy = get_delta(move)
    
    next_y = y + dy
    next_x = x + dx
    
    # move_recursive(grid, (next_x, next_y), move)
    move_recursive(grid, pos, move)
    
    return grid, pos

def moveRobot(grid, pos, move='^', part2=False):
    if not part2: return move_horizontal(grid, pos, move)
    if move in '<>':
        return move_horizontal(grid, pos, move)
    return move_vertical(grid, pos, move)
    
def get_score(grid):
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                score += 100*y + x
                
    return score

def solve_part_one(input_data):
    grid, moves = parse_input(input_data)
    
    startPos = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                startPos = (x, y)
    
    for move in moves:
        grid, startPos = moveRobot(grid, pos=startPos, move=move, part2=False)
    # print_grid(grid)

    return get_score(grid)


def solve_part_two(input_data):
    grid, moves = parse_input(input_data, part2=True)
    print_grid(grid, 0)
    
    startPos = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                startPos = (x, y)
    
    for move in moves:
        grid, startPos = moveRobot(grid, startPos, move, part2=True)
        print('Move: ', move)
        print_grid(grid, 0)
        
        
    print_grid(grid, 0)

    return get_score(grid)


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 15, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    # submit_solutions(2024, 15, solve_part_one, solve_part_two)
