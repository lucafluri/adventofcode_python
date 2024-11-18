import os
import shutil
from aocd.models import Puzzle
from input_manager import download_and_store_data

YEAR = 2020

def generate_day(year, day):
    # Define the base directory
    base_dir = os.path.dirname(__file__)

    # Manually read the .env file and set the AOC_SESSION variable
    with open('.env') as f:
        for line in f:
            if line.startswith('AOC_SESSION'):
                AOC_SESSION = line.strip().split('=')[1]
                os.environ['AOC_SESSION'] = AOC_SESSION

    day_dir = os.path.join(base_dir, str(year), f"day_{day:02}")
    os.makedirs(day_dir, exist_ok=True)

    # Use input manager to download and store input and example data
    download_and_store_data(year, day, day_dir)

    # Copy template script
    template_script = os.path.join(base_dir, "template.py")
    day_script = os.path.join(day_dir, f"day{day:02}.py")
    if not os.path.exists(day_script):
        shutil.copy(template_script, day_script)

        # Update YEAR and DAY in the copied script
        with open(day_script, 'r') as file:
            script_content = file.read()

        script_content = script_content.replace('YEAR = 2020', f'YEAR = {year}')
        script_content = script_content.replace('DAY = 3', f'DAY = {day}')

        with open(day_script, 'w') as file:
            file.write(script_content)

    print(f"Setup for Day {day} complete.")


def main():
    year = int(input("Enter the year to generate: "))
    day = int(input("Enter the day to generate: "))
    generate_day(year, day)


if __name__ == "__main__":
    main()
