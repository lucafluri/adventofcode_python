import os
from aocd.models import Puzzle

ROOT = os.path.dirname(os.path.abspath(__file__))


def load_env():
    """Load AOC_SESSION from .env (optional; aocd also reads ~/.config/aocd/token)."""
    path = os.path.join(ROOT, ".env")
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                key, _, value = line.strip().partition("=")
                if key == "AOC_SESSION":
                    os.environ["AOC_SESSION"] = value.strip().strip('"\'')


load_env()


def max_day(year):
    return 12 if int(year) >= 2025 else 25


def day_dir(year, day):
    return os.path.join(ROOT, str(year), f"day_{int(day):02}")


def download_and_store_data(year, day, base_dir=None):
    input_dir = os.path.join(base_dir or day_dir(year, day), "inputs")
    os.makedirs(input_dir, exist_ok=True)
    input_file = os.path.join(input_dir, "input.txt")
    example_file = os.path.join(input_dir, "example.txt")
    if os.path.exists(input_file) and os.path.exists(example_file):
        return

    puzzle = Puzzle(year=int(year), day=int(day))
    if not os.path.exists(input_file):
        with open(input_file, "w") as f:
            f.write(puzzle.input_data)
    if not os.path.exists(example_file):
        with open(example_file, "w") as f:
            f.write(puzzle.examples[0].input_data if puzzle.examples else "")


def get_input_data(base_dir):
    """Return (example, example_part_two, input) from base_dir/inputs.
    example2.txt is optional for when part two uses a different example."""
    def read(name):
        path = os.path.join(base_dir, "inputs", name)
        if not os.path.exists(path):
            return ""
        with open(path) as f:
            return f.read().rstrip("\n")
    example = read("example.txt")
    return example, read("example2.txt") or example, read("input.txt")
