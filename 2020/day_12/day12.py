from utils.aoc import *

NORTH, EAST, SOUTH, WEST, LEFT, RIGHT, FORWARD = 'NESWLRF'
dirs = {'N': 0, 'E': 90, 'S': 180, 'W': 270}

def turn(direction, degrees):
    return next(key for key, value in dirs.items() if value == (dirs[direction] + degrees) % 360)

def rotate(pos, degrees):
    x, y = pos
    degrees = degrees % 360
    if degrees == 90:
        return y, -x
    elif degrees == 180:
        return -x, -y
    elif degrees == 270:
        return -y, x
    return x, y

def solve_part_one(input_data):
    data = input_as_lines(input_data)
    
    east = 0
    north = 0
    direction = EAST
    
    for inst in data:
        action, value = inst[0], int(inst[1:])
        
        if action in dirs:
            if action == NORTH:
                north += value
            elif action == SOUTH:
                north -= value
            elif action == EAST:
                east += value
            elif action == WEST:
                east -= value
        elif action in (LEFT, RIGHT):
            direction = turn(direction, value if action == RIGHT else -value)
        elif action == FORWARD:
            if direction == EAST:
                east += value
            elif direction == WEST:
                east -= value
            elif direction == NORTH:
                north += value
            elif direction == SOUTH:
                north -= value

    return abs(east) + abs(north)


def solve_part_two(input_data):
    data = input_as_lines(input_data)
    
    shipEast = 0
    shipNorth = 0
    waypointEast = 10
    waypointNorth = 1
    
    for inst in data:
        action, value = inst[0], int(inst[1:])
        if action in (NORTH, SOUTH):
            waypointNorth += value if action == NORTH else -value
        elif action in (EAST, WEST):
            waypointEast += value if action == EAST else -value
        elif action in (LEFT, RIGHT):
            waypointEast, waypointNorth = rotate((waypointEast, waypointNorth), value if action == RIGHT else -value)
        elif action == FORWARD:
            shipEast += waypointEast * value
            shipNorth += waypointNorth * value

    return abs(shipEast) + abs(shipNorth)

def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 12, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 12, solve_part_one, solve_part_two)

