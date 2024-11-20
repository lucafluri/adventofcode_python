from utils.aoc import *

rules = {}

def parse_bag_rules(data):
    outer_bag, inner_bags = re.findall(r'(.*) bags contain (.*)', data)[0]
    inner_bags = inner_bags.split(', ')
    inner_bags = [re.findall(r'(\d+) (.*) bag', bag)[0] for bag in inner_bags] if inner_bags[0] != 'no other bags.' else []
    inner_bags = {bag[1]: int(bag[0]) for bag in inner_bags} 
    return {outer_bag: inner_bags}

def contains(bag, target, rules):
    contents = rules[bag]
    if target in contents:
        return True
    for bag, count in contents.items():
        if contains(bag, target, rules):
            return True
    return False

def num_contained(bag, rules):
    return sum(count + count * num_contained(bag, rules) for bag, count in rules[bag].items())

def solve_part_one(input_data):
    lines = input_as_lines(input_data)
    rules.clear()
    for line in lines:
        rules.update(parse_bag_rules(line))
    return quantify(contains(bag, 'shiny gold', rules) for bag in rules)


def solve_part_two(input_data):
    return num_contained('shiny gold', rules)


def run():
    # Use puzzle runner to test with example data
    test_with_example(2020, 7, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2020, 7, solve_part_one, solve_part_two)

