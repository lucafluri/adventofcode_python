import os
import shutil
import sys
from input_manager import ROOT, day_dir, download_and_store_data


def generate_day(year, day):
    path = day_dir(year, day)
    os.makedirs(path, exist_ok=True)
    download_and_store_data(year, day, path)

    script = os.path.join(path, f"day{day:02}.py")
    if not os.path.exists(script):
        shutil.copy(os.path.join(ROOT, "template.py"), script)
    print(f"Setup for {year} day {day} complete: {script}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python generate_day.py <year> <day>")
    generate_day(int(sys.argv[1]), int(sys.argv[2]))
