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
    while len(ops) > 0:        
        for l, op, r, res in ops:
            if l in wires and r in wires:
                if(op == 'AND'): wires[res] = wires[l] & wires[r]
                if(op == 'OR'): wires[res] = wires[l] | wires[r]
                if(op == 'XOR'): wires[res] = wires[l] ^ wires[r]
                ops.remove((l, op, r, res))
            else:
                return 0, 0

    sorted_wires = sorted(wires.items(), key=lambda x: x[0])
    z_wires = [wire for wire in sorted_wires if wire[0].startswith('z')]
    print('Simulation done.')
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
    y10 XOR x10 -> sqr 
    bmn OR cmj -> mwq
    sqr XOR mwq -> mwk <-
         
    SWAP 2:
    y18 AND x18 -> z18 <-
    x18 XOR y18 -> nqq
    nfh XOR nqq -> qgd <-
    ndb OR qqc -> nfh

    
    SWAP 3:
    jmh XOR mrs -> z24 <-
    y24 XOR x24 -> hsw <-
    sdd OR hcp -> mrs
    y24 AND x24 -> jmh
    
    SWAP 4:
    cvt AND wwp -> z33 <-
    y33 XOR x33 -> wwp
    wwp XOR cvt -> gqp <-
    rgm OR vgp -> cvt
    
    """
        
    
    replacements = {
        'z10': 'mwk',
        'mwk': 'z10',
        'z18': 'qgd',
        'qgd': 'z18',
        'jmh': 'hsw',
        'hsw': 'jmh',
        'z33': 'gqp',
        'gqp': 'z33'
    }

        
    for o in ops.copy():
        l, op, r, res = o
        if(res in replacements):
            res = replacements[res]
            ops.remove(o)
            o = (l, op, r, res)
            ops.append(o)

    all_wires = set()
    for l, op, r, res in ops:
        all_wires.update([l, r, res])
    all_wires.difference_update(replacements.keys())
    

        
    solution = ",".join(sorted(replacements.keys()))
    print(solution)
    
    target_z = x_value + y_value
    res, _ = run_instructions(wires, ops)
    
    
    if target_z == res:
        print("Solution found!")
        print(solution)
        return solution

    # print(x_value, y_value, target_z, res)
    # print()
    # print(target_z == res)
    # print("".join(f"{i//10 if i >= 10 else '0'}" for i in range(48))[::-1])
    # print("".join(f"{i%10}" for i in range(48))[::-1])
    # print("".join(f"-" for i in range(48)))
    
    # length = 48
    # print(bin(x_value)[2:].zfill(length))
    # print(bin(y_value)[2:].zfill(length))
    # print(bin(res)[2:].zfill(length))
    # print()
    # print(bin(target_z)[2:].zfill(length))
    # print(bin(target_z ^ res)[2:].zfill(length))

    
    return solution

def generate_mermaid_chart(ops):
    """
    Generates a Mermaid chart code from the list of operations as a linked tree graph.
    Shows AND, OR, XOR as gates with source and destination as nodes.
    Marks all 'z' wires in red.
    """
    mermaid_chart = ["graph TD;"]
    for l, op, r, res in ops:
        # Mark 'z' wires in red
        l_style = ":::red" if l.startswith('z') else ""
        r_style = ":::red" if r.startswith('z') else ""
        res_style = ":::red" if res.startswith('z') else ""
        # Create nodes and gates for each operation
        gate_id = f"{l}_{op}_{r}"  # Unique ID for the gate
        mermaid_chart.append(f"{l}{l_style} --> {gate_id}({op})")
        mermaid_chart.append(f"{r}{r_style} --> {gate_id}({op})")
        mermaid_chart.append(f"{gate_id} --> {res}{res_style}")
    # Define the red style
    mermaid_chart.append("classDef red fill:#f96;")
    return "\n".join(mermaid_chart)

# Example usage:
# ops = [("x1", "AND", "y1", "z1"), ("x2", "OR", "y2", "z2")]
# print(generate_mermaid_chart(ops))
