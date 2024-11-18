from aocd import submit
from aocd.models import Puzzle
import os
import time


def test_with_example(year, day, solve_part_one, solve_part_two):
    # Fetch the puzzle for the specified day
    puzzle = Puzzle(year=year, day=day)

    # Read example data
    example_data = puzzle.examples[0].input_data

    # Test part one with timing
    start_time = time.perf_counter_ns()
    example_part_one_result = solve_part_one(example_data)
    example_part_one_time = (time.perf_counter_ns() - start_time) / 1e9
    if example_part_one_result == int(puzzle.examples[0].answer_a):
        print(f"\033[1;92mPart One Example Test Passed!: {example_part_one_result}\033[0m")
    else:
        print(f"\033[1;91mPart One Example Test Failed: Expected {puzzle.examples[0].answer_a}, Got {example_part_one_result}\033[0m")
    print(f"Part One Example Time: {example_part_one_time:.9f} seconds")

    # Test part two with timing
    if(puzzle.examples[0].answer_b is None):  # Skip if there is no part two
        return
    start_time = time.perf_counter_ns()
    example_part_two_result = solve_part_two(example_data)
    example_part_two_time = (time.perf_counter_ns() - start_time) / 1e9
    if example_part_two_result == int(puzzle.examples[0].answer_b):
        print("\033[1;92mPart Two Example Test Passed!\033[0m")
    else:
        print(f"\033[1;91mPart Two Example Test Failed: Expected {puzzle.examples[0].answer_b}, Got {example_part_two_result}\033[0m")
    print(f"Part Two Example Time: {example_part_two_time:.9f} seconds")


def submit_solutions(year, day, solve_part_one, solve_part_two):
    print("\033[90mSubmitting solutions...\n=======================\033[0m")
    # Determine base directory for inputs
    base_dir = os.path.join(os.path.dirname(__file__), str(year), f'day_{day:02}')

    # Read input data
    input_file = os.path.join(base_dir, "inputs", "input.txt")
    with open(input_file, 'r') as f:
        input_data = f.read()

    # Solve part one with timing
    start_time = time.perf_counter_ns()
    part_one_result = solve_part_one(input_data)
    part_one_time = (time.perf_counter_ns() - start_time) / 1e9
    print(f"\033[1mPart One Result: {part_one_result}\033[0m")
    print(f"Part One Time: {part_one_time:.9f} seconds")

    # Solve part two with timing
    start_time = time.perf_counter_ns()
    part_two_result = solve_part_two(input_data)
    part_two_time = (time.perf_counter_ns() - start_time) / 1e9
    print(f"\033[1mPart Two Result: {part_two_result}\033[0m")
    print(f"Part Two Time: {part_two_time:.9f} seconds")

    # Ask for confirmation before submitting part one result
    confirm = input("Submit Part One result? (y/n): ").strip().lower()
    if confirm == 'y':
        try:
            submit(part_one_result, part="a", day=day, year=year)
            print("\033[1;92mPart One Submission Successful!\033[0m")
        except Exception as e:
            print(f"\033[1;91mPart One Submission Failed: {e}\033[0m")

    # Ask for confirmation before submitting part two result
    confirm = input("Submit Part Two result? (y/n): ").strip().lower()
    if confirm == 'y':
        try:
            submit(part_two_result, part="b", day=day, year=year)
            print("\033[1;92mPart Two Submission Successful!\033[0m")
        except Exception as e:
            print(f"\033[1;91mPart Two Submission Failed: {e}\033[0m")
