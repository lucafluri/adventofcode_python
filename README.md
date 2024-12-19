# Advent of Code Solutions

This repository contains my solutions for Advent of Code challenges. The repository is structured to easily manage solutions for different years and days.

## Puzzle Status
Legend: =Completed|=In Progress|=Not Started

|Parts|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|2024-1|||⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|❌|❌|❌|❌|❌|❌|
|2024-2|||⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|🔄|⭐|⭐|⭐|⭐|❌|❌|❌|❌|❌|❌|
|2020-1|||⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|
|2020-2|||⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|⭐|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|
|2015-1|||⭐|⭐|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|
|2015-2|||⭐|⭐|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|❌|

## Setup

1. Create a `.env` file in the root directory with your Advent of Code session token:
```
AOC_SESSION=your_session_token_here
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Scripts

### Generate a New Day
To create a new solution template for a specific day:

```bash
python generate_day.py <year> <day>
```

Example:
```bash
python generate_day.py 2020 7
```

This will:
- Create a new directory for the day
- Generate solution template files
- Download input data from Advent of Code
- Create an example input file

### Run a Specific Day's Solution
To run the solution for a specific day:

```bash
python main.py <year> <day>
```

Example:
```bash
python main.py 2020 6
```

### Run All Days
To run solutions for all available days in a specific year:

```bash
python run_all_days.py <year>
```

Example:
```bash
python run_all_days.py 2020
```

This will:
- Run all available solutions for the specified year
- Display execution times for each part
- Show test results with example data
- Color-code the results (green for correct, yellow for partially correct, red for incorrect)

## Project Structure

```
adventofcode2024/
├── .env                    # Environment variables (AOC session token)
├── requirements.txt        # Python dependencies
├── main.py                # Main runner script
├── run_all_days.py        # Script to run all days
├── generate_day.py        # Script to generate new day
├── puzzle_runner.py       # Utilities for running solutions
├── input_manager.py       # Input data management
└── YYYY/                  # Year directory
    └── day_XX/            # Day directory
        ├── dayXX.py       # Solution file
        └── inputs/        # Input directory
            ├── input.txt  # Puzzle input
            └── example.txt# Example input
```

## Solution Template
Each day's solution file (`dayXX.py`) contains two main functions:
- `solve_part_one(input_data)`: Solution for part 1
- `solve_part_two(input_data)`: Solution for part 2

The template also includes common imports and utility functions.
