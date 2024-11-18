import os
from aocd.models import Puzzle

def download_and_store_data(year, day, base_dir):
    # Fetch the puzzle for the specified day
    puzzle = Puzzle(year=year, day=day)
    
    # Define file paths
    input_dir = os.path.join(base_dir, "inputs")
    os.makedirs(input_dir, exist_ok=True)
    input_file = os.path.join(input_dir, "input.txt")
    example_file = os.path.join(input_dir, "example.txt")

    # Check and store input data
    if not os.path.exists(input_file):
        with open(input_file, 'w') as f:
            f.write(puzzle.input_data)

    # Check and store example data
    if puzzle.examples and not os.path.exists(example_file):
        with open(example_file, 'w') as f:
            f.write(puzzle.examples[0].input_data)

    print("Data stored locally.")
