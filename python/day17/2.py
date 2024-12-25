from utils import input_blocks

# Define the extract pattern for the example input
extract_pattern = [
    "Register A: {}",
    "Register B: {}",
    "Register C: {}",
    "",
    "Program: {}"
]

class Computer:
    def __init__(self):
        a, b, c, program = tuple(i for i in tuple(input_blocks(*extract_pattern)))[0]
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.program = list(map(int, program.split(",")))
        self.instruction_pointer = 0
        self.output = []
        self.opcodes = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }

    def get_combo_operand(self, num):
        combo_operands = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.a,
            5: self.b,
            6: self.c
        }
        return combo_operands[num]

    def adv(self, num):
        self.a = self.a // (2 ** self.get_combo_operand(num))

    # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
    def bxl(self, num):
        self.b = self.b ^ num

    # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
    def bst(self, num):
        self.b = self.get_combo_operand(num) % 8
    # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
    def jnz(self, num):
        if self.a != 0:
            self.instruction_pointer = num-2
    # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
    def bxc(self, num):
        self.b = self.b ^ self.c
    # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
    def out(self, num):
        self.output.append(self.get_combo_operand(num) % 8)
    # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
    def bdv(self, num):
        self.b = self.a // (2 ** self.get_combo_operand(num))
    def cdv(self, num):
        self.c = self.a // (2 ** self.get_combo_operand(num))

    def run(self, verbose=False):
        if verbose:
            print(self.program) 
        while self.instruction_pointer < len(self.program):
            opcode, operand = self.program[self.instruction_pointer:self.instruction_pointer+2]
            if verbose:
                print(f"A: {self.a}, B: {self.b}, C: {self.c}")
                print(f"Opcode: {opcode}, Operand: {operand}")
            self.opcodes[opcode](operand)
            self.instruction_pointer += 2
            if verbose:
                print(f"Output: {self.output}")
        return self.output
    
code = Computer()
p = code.program
o = code.run()

def get_out(a):
    b = a%8
    b = b^7
    c = a // (2**b)
    b = b^7
    a = a // 8
    b = b^c
    return b % 8

print(get_out(0))

def find_a(program):
    a = {0}

    for target in reversed(program):
        possible_a = set()
        for _a in a:
            for i in range(8):
                if get_out((_a << 3) + i) == target:
                    possible_a.add((_a << 3) + i)
        
        a = possible_a

    return min(a)


print(find_a(p))