from tabnanny import check
from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 10092 
expected_output_part_two = None  

DIRECTIONS = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0)
}

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
    return DIRECTIONS.get(move, (0, 0))

def move_horizontal(grid, pos, move='>'):
    x, y = pos
    dx, dy = get_delta(move)
    
    nx, ny = x + dx, y + dy
    blocks = []
    full = True
    index = 0
    while inside_grid(nx, ny, grid) and grid[ny][nx] != '#':
        blocks.append(grid[ny][nx])
        if(grid[ny][nx] == '.'): 
            full = False
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
    
    next_y = y + dy
    next_x = x + dx
    
    if not inside_grid(next_x, next_y, grid) or grid[next_y][next_x] == '#':
        return False
    
    if grid[next_y][next_x] == '.':
        return True
    
    # Handle box cases
    if grid[next_y][next_x] == '[':
        return check_vertical(grid, (next_x, next_y), move) and check_vertical(grid, (next_x + 1, next_y), move)
    elif grid[next_y][next_x] == ']':
        return check_vertical(grid, (next_x, next_y), move) and check_vertical(grid, (next_x - 1, next_y), move)
    return True

def move_recursive(grid, pos, move='v'):
    x, y = pos
    dx, dy = get_delta(move)
    
    next_y = y + dy
    next_x = x + dx
    
    if not inside_grid(next_x, next_y, grid) or grid[next_y][next_x] == '#':
        return grid
   
    if grid[next_y][next_x] in '[]':
        direction_offset = 1 if grid[next_y][next_x] == '[' else -1
        grid = move_recursive(grid, (next_x, next_y), move)
        grid = move_recursive(grid, (next_x + direction_offset, next_y), move)
    if grid[y][x] != '@':
        grid[next_y][next_x] = grid[y][x]
        grid[y][x] = '.'
    return grid

def move_vertical(grid, pos, move='v'):
    x, y = pos
    dx, dy = get_delta(move)
    
    next_x = x + dx
    next_y = y + dy
    
    if(grid[next_y][next_x] not in '[].'):
        return grid, pos
    
    if grid[next_y][next_x] in '[]' and check_vertical(grid, (x, y), move) or grid[next_y][next_x] == '.':
        grid = move_recursive(grid, pos, move)
        grid[next_y][next_x] = grid[y][x]
        grid[y][x] = '.'
        pos = (next_x, next_y)
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
            if grid[y][x] == 'O' or grid[y][x] == '[':
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

    return get_score(grid)


def solve_part_two(input_data):
    grid, moves = parse_input(input_data, part2=True)
    
    startPos = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                startPos = (x, y)
    
    for move in moves:
        grid, startPos = moveRobot(grid, startPos, move, part2=True)

    return get_score(grid)


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 15, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 15, solve_part_one, solve_part_two)
