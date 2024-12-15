from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = None  

def parse_input(input_data):
    grid, moves = input_data.split('\n\n')
    moves = moves.replace('\n', '') 
    
    grid = input_as_grid(grid)
    
    return grid, moves

def get_delta(move='^'):
    if move == '^': return 0, -1
    if move == '>': return 1, 0
    if move == 'v': return 0, 1
    return -1, 0
    

def moveRobot(grid, pos, move='^'):
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
        
    # print(blocks, full, index_space)
    
    if not full:
        x = x + dx
        y = y + dy
        
        blocks.insert(0, '@')
        blocks.pop()
        # print(blocks)
        for i in range(len(blocks)):
            nx, ny = x + dx * i, y + dy * i
            grid[ny][nx] = blocks[i]
        
        
        # for i in range(index_space+1, 1, -1):
            # nx, ny = x + dx * i, y + dy * i
            # nnx, nny = x + dx * (i-1), y + dy * (i-1)
            # print(grid[nny][nnx], grid[ny][nx])
            # grid[ny][nx] = grid[nny][nnx]
        pos = (x, y)
        grid[y-dy][x-dx] = '.'
        # grid[y][x] = '@'
    
    
    return grid, pos
    
    
def get_score(grid):
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                score += 100*y + x
                
    return score

def solve_part_one(input_data):
    grid, moves = parse_input(input_data)
    # print_grid(grid)
    # print(moves)
    
    startPos = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                startPos = (x, y)
    
    for move in moves:
        grid, startPos = moveRobot(grid, pos=startPos, move=move)
        # print(f"Move: {move}, Pos: {startPos}")
    print_grid(grid)
    
    
    
    
    return get_score(grid)


def solve_part_two(input_data):
    return None


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 15, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 15, solve_part_one, solve_part_two)

