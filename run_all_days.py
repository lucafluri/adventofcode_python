import argparse
from tabulate import tabulate
from input_manager import day_dir, max_day
from puzzle_runner import run_day_solutions, GREEN, YELLOW, RED, BOLD, RESET
import os


def colored(seconds, example_ok, input_ok):
    color = GREEN if input_ok else YELLOW if example_ok else RED
    return f"{color}{seconds:.4f}s{RESET}"


def run_all_days(year):
    """Green: real answer correct, yellow: only example correct, red: both wrong."""
    rows = []
    for day in range(1, max_day(year) + 1):
        timings = run_day_solutions(year, day) if os.path.isdir(day_dir(year, day)) else None
        if timings:
            (t1, *ok1), (t2, *ok2) = timings
            rows.append([f"Day {day:02}", colored(t1, *ok1), colored(t2, *ok2), f"{t1 + t2:.4f}s"])
        else:
            rows.append([f"Day {day:02}", "N/A", "N/A", "N/A"])
    print(tabulate(rows, headers=[f"{BOLD}{h}{RESET}" for h in ("Day", "Part One", "Part Two", "Total")], tablefmt="grid"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run all days of a year and show timings.")
    parser.add_argument("year", type=int)
    run_all_days(parser.parse_args().year)
