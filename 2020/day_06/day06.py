from utils.aoc import *

def solve_part_one(input_data):
    groups = input_data.split("\n\n")
    count = 0
    
    for group in groups:
        charSet = set()
        group = group.replace("\n", "")
        for char in group:
            charSet.add(char)
        count += len(charSet)
    return count


def solve_part_two(input_data):
    groups = input_data.split("\n\n")
    count = 0
    
    for group in groups:
        persons = group.split("\n")
        common_chars = set(persons[0])
        for person in persons[1:]:
            common_chars &= set(person)
        count += len(common_chars)
    return count

def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 6, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 6, solve_part_one, solve_part_two)
