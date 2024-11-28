from utils.aoc import *


def solve_part_one(input_data):
    earliest, busses = input_data.splitlines()
    earliest = int(earliest)
    busses = [int(b) for b in busses.split(',') if b != 'x']
    min_wait_time = float('inf')
    best_bus_id = None
    for bus_id in busses:
        wait_time = bus_id - (earliest % bus_id)
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            best_bus_id = bus_id
    return min_wait_time * best_bus_id


def solve_part_two(input_data):
    return None


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 13, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 13, solve_part_one, solve_part_two)
