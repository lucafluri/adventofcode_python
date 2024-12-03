from utils.aoc import *

def solve_part_one(input_data):
    matches = re.findall(r'mul\((\d+),(\d+)\)', input_data)
    return sum(int(a)*int(b) for a, b in matches)


def solve_part_two(input_data):
    matches = re.finditer(r'mul\((\d+),(\d+)\)|don\'t\(\)|do\(\)', input_data) #re.findall(r'mul\((\d+),(\d+)\)', input_data)
    do=True
    sum=0
    for m in matches:
        if(m.group(0)=='don\'t()'):
            do=False
        elif(m.group(0)=='do()'):
            do=True
        elif(do):
            a, b = m.groups()
            sum += int(a)*int(b)
    
    return sum

def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 3, solve_part_one, solve_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 3, solve_part_one, solve_part_two)
