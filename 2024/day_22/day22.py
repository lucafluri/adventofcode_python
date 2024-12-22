from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 37990510 
expected_output_part_two = 23  

def parse_input(input_data):
    nums = ints(input_data)
    return nums

@cache
def next_num(n):
    m = n * 64
    n = n ^ m
    n = n % 16777216
    m = int(n/32)
    n = n ^ m
    n = n % 16777216
    m = n * 2048
    n = n ^ m
    n = n % 16777216
    
    return n

def solve_part_one(input_data):
    initial = parse_input(input_data)
    ends = []
    
    for n in initial:
        tmp = n
        for _ in range (2000):
            tmp = next_num(tmp)
        ends.append(tmp)

    return sum(ends)


def solve_part_two(input_data):
    initial = parse_input(input_data)
    prices = [([n], [n % 10], [None], [None]) for n in initial]  # initial: ([all nums], [all prices], [all changes], [last 4 changes])    

    changes_price = {}

    for i, (nums, price_list, changes, last_changes) in enumerate(prices):
        for x in range(1, 2000):
            tmp = next_num(nums[-1])
            nums.append(tmp)
            price = tmp % 10
            price_list.append(price)
            change = price - price_list[-2]
            changes.append(change)

            if x >= 4:
                last_changes.append(tuple(changes[-4:]))
                change_key = last_changes[-1]

                if change_key not in changes_price:
                    changes_price[change_key] = [0] * len(initial)

                if changes_price[change_key][i] == 0:
                    changes_price[change_key][i] = price
            else:
                last_changes.append(None)
            
    return max(sum(prices) for prices in changes_price.values())


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 22, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 22, solve_part_one, solve_part_two)

