import importlib
import time
import traceback
from aocd import submit
from aocd.models import Puzzle
from input_manager import day_dir, download_and_store_data, get_input_data

GREEN, YELLOW, RED, GREY, BOLD, RESET = "\033[92m", "\033[93m", "\033[91m", "\033[90m", "\033[1m", "\033[0m"


def matches(result, expected):
    return result is not None and expected is not None and str(result) == str(expected)


def timed(solve, data):
    """Return (result, seconds); result is None if solve raised."""
    start = time.perf_counter()
    try:
        result = solve(data)
    except Exception:
        traceback.print_exc()
        result = None
    return result, time.perf_counter() - start


def load_data(year, day):
    download_and_store_data(year, day)
    return get_input_data(day_dir(year, day))


def example_answers(year, day, expected_one=None, expected_two=None):
    """Explicit expected values win; otherwise fall back to aocd's parsed example answers."""
    if expected_one is None or expected_two is None:
        try:
            example = Puzzle(year=year, day=day).examples[0]
            expected_one = expected_one if expected_one is not None else example.answer_a
            expected_two = expected_two if expected_two is not None else example.answer_b
        except Exception:
            pass
    return expected_one, expected_two


def test_with_example(year, day, solve_part_one, solve_part_two, expected_output_part_one=None, expected_output_part_two=None):
    print(f"{BOLD}Year {year}, Day {day}{RESET}")
    example_data, _ = load_data(year, day)
    if not example_data:
        print(f"{YELLOW}No example data, put it in {day_dir(year, day)}/inputs/example.txt{RESET}")
        return
    expected = example_answers(year, day, expected_output_part_one, expected_output_part_two)
    for name, solve, exp in zip(("One", "Two"), (solve_part_one, solve_part_two), expected):
        result, seconds = timed(solve, example_data)
        if matches(result, exp):
            print(f"{GREEN}{BOLD}Part {name} Example Passed: {result}{RESET} ({seconds:.4f}s)")
        else:
            print(f"{RED}{BOLD}Part {name} Example Failed: expected {exp}, got {result}{RESET} ({seconds:.4f}s)")


def submit_solutions(year, day, solve_part_one, solve_part_two):
    print(f"{GREY}Solving real input...{RESET}")
    _, input_data = load_data(year, day)
    puzzle = Puzzle(year=year, day=day)
    for part, name, solve in (("a", "One", solve_part_one), ("b", "Two", solve_part_two)):
        result, seconds = timed(solve, input_data)
        print(f"{BOLD}Part {name} Result: {result}{RESET} ({seconds:.4f}s)")
        if result is None:
            continue
        if getattr(puzzle, f"answered_{part}"):
            answer = getattr(puzzle, f"answer_{part}")
            print(f"{GREEN}Correct{RESET}" if matches(result, answer) else f"{RED}Wrong, solved answer is {answer}{RESET}")
            continue
        if input(f"Submit Part {name}? (y/n): ").strip().lower() == "y":
            try:
                submit(result, part=part, day=day, year=year)
            except Exception as e:
                print(f"{RED}Submission failed: {e}{RESET}")


def run_day_solutions(year, day):
    """Return ((time, example_ok, input_ok), (time, example_ok, input_ok)) for a day, or None."""
    try:
        module = importlib.import_module(f"{year}.day_{day:02}.day{day:02}")
        example_data, input_data = load_data(year, day)
        puzzle = Puzzle(year=year, day=day)
    except Exception:
        traceback.print_exc()
        return None

    expected = example_answers(year, day,
                               getattr(module, "expected_output_part_one", None),
                               getattr(module, "expected_output_part_two", None))
    results = []
    for part, exp in zip("ab", expected):
        solve = getattr(module, f"solve_part_{'one' if part == 'a' else 'two'}")
        example_result, _ = timed(solve, example_data)
        input_result, seconds = timed(solve, input_data)
        answer = getattr(puzzle, f"answer_{part}") if getattr(puzzle, f"answered_{part}") else None
        results.append((seconds, matches(example_result, exp), matches(input_result, answer)))
    return tuple(results)
