from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = 2024
expected_output_part_two = None  

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
    
    while len(ops) > 0:
        
        for l, op, r, res in ops:
            if l in wires and r in wires:
                if(op == 'AND'): wires[res] = wires[l] & wires[r]
                if(op == 'OR'): wires[res] = wires[l] | wires[r]
                if(op == 'XOR'): wires[res] = wires[l] ^ wires[r]
                ops.remove((l, op, r, res))

    sorted_wires = sorted(wires.items(), key=lambda x: x[0])
    z_wires = [wire for wire in sorted_wires if wire[0].startswith('z')]
    # print(z_wires)
    return get_binary([wire[1] for wire in z_wires]), z_wires

def solve_part_one(input_data):
    wires, ops = parse_input(input_data)
    
   
    return run_instructions(wires, ops)[0]


def solve_part_two(input_data):
    wires, ops = parse_input(input_data)
    
    sorted_wires = sorted(wires.items(), key=lambda x: x[0])
    x_wires = [wire for wire in sorted_wires if wire[0].startswith('x')]
    y_wires = [wire for wire in sorted_wires if wire[0].startswith('y')]
    
    x_value = get_binary([wire[1] for wire in x_wires])
    y_value = get_binary([wire[1] for wire in y_wires])
    
    """
    SWAP 1:
    kgd OR kqf -> z10 <-
    mwq AND sqr -> kgd
    x10 AND y10 -> kqf 
    y10 XOR x10 -> sqr <-
    
    444444443333333333222222222211111111110000000000
    765432109876543210987654321098765432109876543210
    ------------------------------------------------
    000110001101110001010001100001011000001000111001
    000100000010110101010110111111000111111010101111
    001010010000100110101001011111011111110011101000
                                         ^


    
    
    """
        
    #replacements
    
    replacements = {
        'z10': 'sqr',
        'sqr': 'z10',
        }
    
    for o in ops.copy():
        l, op, r, res = o
        # print(o)
        if(res in replacements):
            res = replacements[res]
            ops.remove(o)
            o = (l, op, r, res)
            ops.append(o)
        # print(o)
        
    

    
    
    
    target_z = x_value + y_value
    res, z_wires = run_instructions(wires, ops)
    print(x_value, y_value, target_z, res)
    # print(target_z == res)
    # print("Column Numbers:")
    print("".join(f"{i//10 if i >= 10 else '0'}" for i in range(48))[::-1])
    print("".join(f"{i%10}" for i in range(48))[::-1])
    print("".join(f"-" for i in range(48)))
    
    # print(bin(x_value)[2:][::-1].zfill(48))
    # print(bin(y_value)[2:][::-1].zfill(48))
    # # print(bin(target_z)[2:].zfill(48))
    
    # print(bin(res)[2:][::-1].zfill(48))
    # return run_instructions(wires, ops
    
    # Show x, y and res value in binary form, stacked over each other
    # print("Binary Representation (LSB right, MSB left):")
    print(bin(x_value)[2:].zfill(48))
    print(bin(y_value)[2:].zfill(48))
    print(bin(res)[2:].zfill(48))
    
    
    
    
    
    
    # combos = list(it.combinations(ops, 2))
    # combo4 = it.combinations(combos, 4)
    # print(len(combos))
    # print(len(list(combo4)))
    
    
    
    return None


def run():
    # Use puzzle runner to test with example data
    test_with_example(2024, 24, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 24, solve_part_one, solve_part_two)

