from utils.aoc import *

# Define the expected outputs for part one and part two
expected_output_part_one = 161 
expected_output_part_two = 48 

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
