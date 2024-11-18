import os
import aocd
from puzzle_runner import run_day_solutions
from tabulate import tabulate
import argparse


def run_all_days(year):
    """
    Run all available days in the given year and display execution timings for all parts.

    Args:
        year (int): The year to run the solutions for.
    """
    year_directory = str(year)
    results = []

    # Iterate through all days from 1 to 25
    for day_number in range(1, 26):
        day_path = os.path.join(year_directory, f'day_{day_number:02}')
        if os.path.isdir(day_path):
            timings = run_day_solutions(year, day_number)
            if timings:
                (part_one_time, part_one_correct_example, part_one_correct_input), (part_two_time, part_two_correct_example, part_two_correct_input) = timings

                # Determine color based on correctness
                part_one_color = "\033[92m" if part_one_correct_example and part_one_correct_input else ("\033[93m" if part_one_correct_example else "\033[91m")
                part_two_color = "\033[92m" if part_two_correct_example and part_two_correct_input else ("\033[93m" if part_two_correct_example else "\033[91m")

                results.append([
                    f"\033[1mDay {day_number:02}\033[0m",
                    f"{part_one_color}{part_one_time:.5f} seconds\033[0m",
                    f"{part_two_color}{part_two_time:.5f} seconds\033[0m",
                    f"{part_one_color if part_one_correct_example and part_one_correct_input else part_two_color}{part_one_time + part_two_time:.4f} seconds\033[0m"
                ])
            else:
                results.append([f"\033[1mDay {day_number:02}\033[0m", "N/A", "N/A", "N/A"])
        else:
            results.append([f"\033[1mDay {day_number:02}\033[0m", "N/A", "N/A", "N/A"])

    # Display the results in a table with bold headers
    headers = ["\033[1mDay\033[0m", "\033[1mPart One Time\033[0m", "\033[1mPart Two Time\033[0m", "\033[1mTotal Time\033[0m"]
    print(tabulate(results, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run all available days in a given year and display execution timings.")
    parser.add_argument("year", type=int, help="The year to run the solutions for.")
    args = parser.parse_args()
    run_all_days(args.year)
