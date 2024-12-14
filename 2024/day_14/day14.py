from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = None 
expected_output_part_two = None  

def parse_input(input_data):
    robots = []
    lines = input_as_lines(input_data)
    for line in lines:
        px,py,vx,vy = ints(line)
        robots.append(((px,py),(vx,vy)))
    return robots

def new_pos(height, width, pos, vel, seconds):
    nx = (pos[0] + (vel[0]*seconds)) % width
    ny = (pos[1] + (vel[1]*seconds)) % height

    return (nx, ny)

def safety_score(positions, height, width):
    quadrants = [0,0,0,0]
    for pos in positions:
        if pos[0] == width // 2 or pos[1] == height//2:
            continue


def solve_part_one(input_data):
    robots = parse_input(input_data)
    print(robots)
    return None


def solve_part_two(input_data):
    return None


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 14, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    #submit_solutions(2024, 14, solve_part_one, solve_part_two)

