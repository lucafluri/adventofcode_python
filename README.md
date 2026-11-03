# Advent of Code Solutions

## Setup

```bash
pip install -r requirements.txt
echo "AOC_SESSION=your_session_cookie" > .env
```

The session cookie is the `session` cookie from adventofcode.com (browser dev tools).

## Usage

```bash
python main.py              # during December: today's puzzle, otherwise the latest existing day
python main.py 2025 3       # a specific day
python run_all_days.py 2024 # timings + correctness table for a year
```

`main.py` creates the day from `template.py` and downloads input + example if it doesn't exist yet
(`python generate_day.py <year> <day>` does only that).

Running a day:
1. Runs both parts on the example and compares against the expected answers
   (`expected_output_part_one/two` in the day file, otherwise aocd's parsed example answers).
2. Runs both parts on the real input, then asks to submit unsolved parts (`None` results are skipped).
   Already-solved parts are just checked against your accepted answer.

Inputs are cached in `YYYY/day_XX/inputs/` (gitignored). If aocd picks the wrong example,
edit `example.txt` and set the expected outputs in the day file.

Note: from 2025 on, Advent of Code has 12 days instead of 25.

## Structure

```
main.py           # run/create a day
generate_day.py   # create a day from template.py
run_all_days.py   # run a whole year
puzzle_runner.py  # example testing, submitting, timing
input_manager.py  # .env loading, input download/cache
utils/aoc.py      # helpers imported by every day (`from utils.aoc import *`)
YYYY/day_XX/dayXX.py
```
