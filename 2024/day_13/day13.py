from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 480
expected_output_part_two = 875318608908  

def parse_input(input_data):
    prices = input_data.split('\n\n')
    configs = []
    for price in prices:
        lines = price.split('\n')
        a_x, a_y = ints(lines[0])
        b_x, b_y = ints(lines[1])
        t_x, t_y = ints(lines[2])
        configs.append(((a_x, a_y), (b_x, b_y), (t_x, t_y)))
    return configs

def solve(input_data, part2=False):
    configs = parse_input(input_data)
    tokens = 0
    
    for config in configs:
        a_x, a_y = config[0]
        b_x, b_y = config[1]
        t_x, t_y = config[2]
        t_x += 10000000000000 if part2 else 0
        t_y += 10000000000000 if part2 else 0
        
        # Solve equations using det(A_i)/det(A) => Cramers rule
        A = (t_x*b_y - t_y*b_x)/(a_x*b_y - a_y*b_x)
        B = (a_x*t_y - a_y*t_x)/(a_x*b_y - a_y*b_x)
        
        # A, B = solve_equations([[a_x, b_x], [a_y, b_y]], [t_x, t_y])
        C = 3*A+B
        
        # Check if A, B, C are integers, if so add to tokens
        if A % 1 == 0 and B % 1 == 0 and C % 1 == 0:
            tokens += C
    
    return int(tokens)

def solve_part_one(input_data):
    return solve(input_data, False)

def solve_part_two(input_data):
    return solve(input_data, True)
    
def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 13, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 13, solve_part_one, solve_part_two)

