import sys
import os
from importlib import import_module

# Manually read the .env file and set the AOC_SESSION variable
with open('.env') as f:
    for line in f:
        if line.startswith('AOC_SESSION'):
            AOC_SESSION = line.strip().split('=')[1]
            os.environ['AOC_SESSION'] = AOC_SESSION


if len(sys.argv) != 3:
    print("Usage: python main.py <year> <day>")
    sys.exit(1)

year = sys.argv[1]
day = sys.argv[2]
module_name = f"{year}.day_{day}.day{day}"

try:
    solution = import_module(module_name)
    solution.run()
except ModuleNotFoundError as e:
    print(f"Solution for year {year}, day {day} not found.")
    print(f"Error details: {e}")

except Exception as e:
    print(f"An error occurred while trying to run the solution for year {year}, day {day}.")
    print(f"Error details: {e}")
