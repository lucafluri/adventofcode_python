import importlib
import time
import traceback
from aocd import submit
from aocd.models import Puzzle
from input_manager import day_dir, download_and_store_data, get_input_data

GREEN, YELLOW, RED, GREY, BOLD, RESET = "\033[92m", "\033[93m", "\033[91m", "\033[90m", "\033[1m", "\033[0m"
PARTS = (("a", "One"), ("b", "Two"))


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


def load_day(year, day):
    """Return (module, solvers, example inputs, example answers, real input) for a day."""
    module = importlib.import_module(f"{year}.day_{day:02}.day{day:02}")
    download_and_store_data(year, day)
    example_one, example_two, input_data = get_input_data(day_dir(year, day))
    solvers = (module.solve_part_one, module.solve_part_two)
    expected = [getattr(module, "expected_output_part_one", None), getattr(module, "expected_output_part_two", None)]
    if None in expected:
        try:
            example = Puzzle(year=year, day=day).examples[0]
            expected = [e if e is not None else a for e, a in zip(expected, (example.answer_a, example.answer_b))]
        except Exception:
            pass
    return solvers, (example_one, example_two), expected, input_data


def run_day(year, day):
    """Test both parts on the example, then solve the real input and offer to submit."""
    print(f"{BOLD}Year {year}, Day {day}{RESET}")
    solvers, examples, expected, input_data = load_day(year, day)

    for (_, name), solve, example, exp in zip(PARTS, solvers, examples, expected):
        if not example:
            print(f"{YELLOW}No example data, put it in {day_dir(year, day)}/inputs/example.txt{RESET}")
            break
        result, seconds = timed(solve, example)
        if matches(result, exp):
            print(f"{GREEN}{BOLD}Part {name} Example Passed: {result}{RESET} ({seconds:.4f}s)")
        else:
            print(f"{RED}{BOLD}Part {name} Example Failed: expected {exp}, got {result}{RESET} ({seconds:.4f}s)")

    print(f"{GREY}Solving real input...{RESET}")
    puzzle = Puzzle(year=year, day=day)
    for (part, name), solve in zip(PARTS, solvers):
        result, seconds = timed(solve, input_data)
        print(f"{BOLD}Part {name} Result: {result}{RESET} ({seconds:.4f}s)")
        if result is None:
            continue
        if getattr(puzzle, f"answered_{part}"):
            answer = getattr(puzzle, f"answer_{part}")
            print(f"{GREEN}Correct{RESET}" if matches(result, answer) else f"{RED}Wrong, solved answer is {answer}{RESET}")
        elif input(f"Submit Part {name}? (y/n): ").strip().lower() == "y":
            try:
                submit(result, part=part, day=day, year=year)
            except Exception as e:
                print(f"{RED}Submission failed: {e}{RESET}")


def run_day_solutions(year, day):
    """Return ((time, example_ok, input_ok), (time, example_ok, input_ok)) for a day, or None."""
    try:
        solvers, examples, expected, input_data = load_day(year, day)
        puzzle = Puzzle(year=year, day=day)
    except Exception:
        traceback.print_exc()
        return None

    results = []
    for (part, _), solve, example, exp in zip(PARTS, solvers, examples, expected):
        example_result, _ = timed(solve, example)
        input_result, seconds = timed(solve, input_data)
        answer = getattr(puzzle, f"answer_{part}") if getattr(puzzle, f"answered_{part}") else None
        results.append((seconds, matches(example_result, exp), matches(input_result, answer)))
    return tuple(results)
