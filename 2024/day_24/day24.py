from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 2024
expected_output_part_two = 2024

def parse_input(input_data):
    default, gates = input_data.split('\n\n')
    wires = {}
    ops = []
    
    for wire in default.split('\n'):
        n, v = wire.split(': ')
        wires[n] = int(v)
        
    for gate in gates.split('\n'):
        l, op, r, res = gate.replace('-> ', '').split(' ')
        ops.append((l, op, r, res))
    
    return wires, ops

def get_binary(listWires):
    binary = ""
    for i in range(len(listWires)):
        binary += str(listWires[~i])
    return int(binary, 2)

def run_instructions(wires, ops):
    # wires, ops = parse_input(input_data)
    o = ops.copy()
    
    while len(o) > 0:
        
        for l, op, r, res in o:
            if l in wires and r in wires:
                if(op == 'AND'): wires[res] = wires[l] & wires[r]
                if(op == 'OR'): wires[res] = wires[l] | wires[r]
                if(op == 'XOR'): wires[res] = wires[l] ^ wires[r]
                o.remove((l, op, r, res))

    sorted_wires = sorted(wires.items(), key=lambda x: x[0])
    z_wires = [wire for wire in sorted_wires if wire[0].startswith('z')]
    
    return get_binary([wire[1] for wire in z_wires])

def solve_part_one(input_data):
    wires, ops = parse_input(input_data)
    
   
    return run_instructions(wires, ops)


def solve_part_two(input_data):
    wires, ops = parse_input(input_data)
    
    sorted_wires = sorted(wires.items(), key=lambda x: x[0])
    
        # Set all wires starting with 'x' to 1
    for wire_name in wires:
        if wire_name.startswith('x'):
            wires[wire_name] = 1

    # Set all wires starting with 'y' to 1
    for wire_name in wires:
        if wire_name.startswith('y'):
            wires[wire_name] = 0
    
    
    x_wires = [wire for wire in sorted_wires if wire[0].startswith('x')]
    y_wires = [wire for wire in sorted_wires if wire[0].startswith('y')]
    
    x_value = get_binary([wire[1] for wire in x_wires])
    y_value = get_binary([wire[1] for wire in y_wires])
    


    
    target_z = x_value & y_value
    res = run_instructions(wires, ops)
    print(bin(x_value), bin(y_value), bin(target_z), bin(res))
    print(target_z == res)
    # return run_instructions(wires, ops
    
    print(bin(target_z)[2:].zfill(32))
    print(bin(res)[2:].zfill(32))
    print(bin(target_z ^ res)[2:].zfill(32))
    
    count = 0
    A = target_z
    B = res
    for i in range(32):
        # right shift both the numbers by 'i' and
        # check if the bit at the 0th position is different
        if ((( A >>  i) & 1) != (( B >>  i) & 1)): 
             count=count+1
    print(count)

    count = 0
    A = ~target_z
    B = ~res
    for i in range(32):
        # right shift both the numbers by 'i' and
        # check if the bit at the 0th position is different
        if ((( A >>  i) & 1) != (( B >>  i) & 1)): 
             count=count+1
    print(count)
    
    # combos = list(it.combinations(sorted_wires, 4)
    
    
 
    
    # for c in combos:
    #     c2 = combos.copy()
    #     # remove all gates in c from c2
    #     for g in c:
    #         c2.remove(g)
    #     print(len(c2))
    # print(len(list(combo4)))
    
    
    
    return None


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 24, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    # submit_solutions(2024, 24, solve_part_one, solve_part_two)

