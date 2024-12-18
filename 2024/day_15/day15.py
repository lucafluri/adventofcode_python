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

# def find_boxes(grid):
#     boxes = []
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if grid[y][x] == 'O':
#                 boxes.append((x, y))
#             elif grid[y][x] == '[':
#                 pass
#     return boxes


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

def move_vertical(grid, pos, move='v'):
    # x, y = pos
    
    return 0, 0
    

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
    print_grid(grid)
    
    startPos = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                startPos = (x, y)
    
    for move in moves:
        grid, startPos = moveRobot(grid, startPos, move, part2=True)
    # print_grid(grid)

    return get_score(grid)


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 15, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    # submit_solutions(2024, 15, solve_part_one, solve_part_two)

