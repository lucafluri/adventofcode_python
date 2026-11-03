import argparse
import glob
import os
from datetime import datetime
from zoneinfo import ZoneInfo
from input_manager import ROOT, max_day
from generate_day import generate_day
from puzzle_runner import run_day


def default_year_day():
    """Today's puzzle during Advent (AoC unlocks at midnight US Eastern), else the latest solved day."""
    now = datetime.now(ZoneInfo("America/New_York"))
    if now.month == 12 and now.day <= max_day(now.year):
        return now.year, now.day
    latest = max(glob.glob(os.path.join(ROOT, "[0-9]" * 4, "day_[0-9][0-9]")))
    year, day = latest.split(os.sep)[-2:]
    return int(year), int(day[4:])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run (and create if missing) an Advent of Code day.")
    parser.add_argument("year", type=int, nargs="?")
    parser.add_argument("day", type=int, nargs="?")
    args = parser.parse_args()
    year, day = (args.year, args.day) if args.day else default_year_day()

    if not os.path.exists(os.path.join(ROOT, str(year), f"day_{day:02}", f"day{day:02}.py")):
        generate_day(year, day)
    run_day(year, day)
