from utils.aoc import *

# Define the expected example outputs for part one and part two
expected_output_part_one = "4,6,3,5,6,3,5,2,1,0"
expected_output_part_two = 117440

def parse_input(input_data):
    allInts = ints(input_data)
    regA = allInts[0]
    regB = allInts[1]
    regC = allInts[2]
    program = allInts[3:]
    return regA, regB, regC, program

def combop(op, regs):
    if(op==4):
        return regs[0]
    if(op==5):
        return regs[1]
    if(op==6):
        return regs[2]
    if(op==7):
        return None
    return op

def run_prog(prog, regs):
    output = []
    
    pc = 0
    # regs = [regA, regB, regC]
    while 0 <= pc < len(prog):
        oc = prog[pc]
        op = prog[pc+1]
        # print(regs, oc, op)
        
        if oc == 0:
            regs[0] = int(regs[0] / (2**combop(op, regs)))
        elif oc == 1:
            regs[1] = regs[1] ^ op
        elif oc == 2:
            regs[1] = combop(op, regs) % 8
        elif oc == 3:
            if regs[0] == 0: 
                pc += 2
                continue
            pc = op
            continue
        elif oc == 4:
            regs[1] = regs[1] ^ regs[2]
        elif oc == 5:
            output.append(combop(op, regs) % 8)
        elif oc == 6:
            regs[1] = int(regs[0] / (2**combop(op, regs)))
        elif oc == 7:
            regs[2] = int(regs[0] / (2**combop(op, regs)))
        else:
            assert False
        # print(regs)
        pc += 2
    
    # print(output)
    return ','.join(map(str, output)), output

def solve_part_one(input_data):
    regA, regB, regC, prog = parse_input(input_data)
    
    return run_prog(prog, [regA, regB, regC])[0]


def solve_part_two(input_data):
    regA, regB, regC, prog = parse_input(input_data)
    firstProg = prog.copy()
    
    reps = []
    
    # start= 35184372088832 * 1
    start = 1
    # for i in range(8**15, (8**16)-1):
    # for i in range(16):
    #     for x in range(8):
    #         A = (i*8) + x
    #         output = run_prog(prog, [A, 0, 0])[1]
    #         if output[:~i] == firstProg[:~i]: 
    #             print(A, output, firstProg)
    #             start = A

    for i in range(8):
        A = (27073025747405*8) + i # -9
        # A = (826203174*8) + i # -9
        
        output = run_prog(prog, [A, 0, 0])[1]
        print(A, output, firstProg)
        if output == firstProg: return i
    

def run():
    # Use puzzle runner to test with example data
    # test_with_example(2024, 17, solve_part_one, solve_part_two, expected_output_part_one, expected_output_part_two)

    # Use puzzle runner to submit solutions
    submit_solutions(2024, 17, solve_part_one, solve_part_two)