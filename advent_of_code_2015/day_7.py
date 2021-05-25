instructions = []

with open('day_7.txt') as f:
    instructions = f.read().splitlines()


class Circuit:
    '''
    self.connections (dictionary) - contains wires and signals
        - keys: named wires (1-2 lowercase letters), eg. "gn", "ix"
        - values: integers (from 0 to 65535)
    self.instructions (list) - each instruction specify operation and involved wires
    '''
    def __init__(self, instructions):
        self.connections = {}
        self.instructions = instructions

    def return_integer(self, variable):
        '''
        Try to return given variable in type integer, possible scenarios:
            - variable is already type integer
            - variable is number in string format
            - variable is key in dictinary self.connections (-> return its value)
            - if none of the above is true, function raises ValueError
        '''
        if type(variable) == int:
            return variable
        else:
            try:
                variable = int(variable)
                return variable
            except ValueError:
                try:
                    variable = self.connections[variable]
                    return variable
                except KeyError:
                    raise ValueError

    def conduct_assign(self, instruction):
        '''
        Add a new key and a value (must be an integer) into dictionary self.connections.
        Instruction look as follow:
            - '122 -> b' (assign value 122 to key 'b')
            - 'bk -> b' (assign value of key 'bk' to key 'b')
        Return True if assign was possible, else return False
        '''
        value, _, key = instruction.split()
        try:
            value = self.return_integer(value)
            self.connections.setdefault(key, value)
            return True
        except ValueError:      # value isn't integer and cannot be made into one
            return False

    def conduct_not_operation(self, instruction):
        '''
        Follow instructions for NOT bitewise operation.
        Operation NOT is 1st' complement
            - transform 0 to 1 and 1 to 0 (in 16-bit format)
        Instructions look as follow:
            - 'NOT 123 -> ll' (assign result of NOT operation on number 123 to key 'll')
            - 'NOT bk -> ll' (first, get value of key 'bk', then do as above)
        Return True if NOT bitewise operation was possible, else return False
        '''
        _, value, _, key = instruction.split()
        try:
            value = self.return_integer(value)
        except ValueError:    # value isn't integer and cannot be made into one
            return False
        else:   # value is integer
            value_str = bin(int(value))[2:].zfill(16)      # number in 16-bit binary format
            shifted = ''
            for char in value_str:
                if char == '0':
                    shifted += '1'
                else:
                    shifted += '0'
            value = int(shifted, 2)
            self.connections.setdefault(key, value)
            return True

    def conduct_two_numbers_operation(self, instruction):
        '''
        Follow instructions for AND, OR, LSHIFT, RSHIFT bitewise operations.
        Possible two-numbers operations are in-built Bitwise operations:
            - AND: n1 & n2
            - OR: n1 | n2
            - LSHIFT: n1 << n2
            - RSHIFT: n1 >> n2
        Return True if operation was possible (n1, n2 are integers / can be made into ones),
        else return False
        '''
        n1, operation, n2, _, key = instruction.split()
        try:
            n1 = self.return_integer(n1)
            n2 = self.return_integer(n2)
        except ValueError:     # value(s) isn't / aren't integer(s) and cannot be made into one(s)
            return False
        else:
            if operation == 'AND':
                value = n1 & n2
            elif operation == 'OR':
                value = n1 | n2
            elif operation == 'LSHIFT':
                value = n1 << n2
            elif operation == 'RSHIFT':
                value = n1 >> n2
            self.connections.setdefault(key, value)
            return True

    def conduct_operations(self):
        '''
        Conduct all possible operations from list "instructions"
        append uncompleted ones to a new list "uncompleted_instructions",
        replace list "instructions" with "uncompleted_instructions"
        Repeat until all instructions are satisfied.
        '''
        while self.instructions:
            uncompleted_instructions = []
            for instruction in self.instructions:
                if instruction.split()[1] in ['AND', 'OR', 'LSHIFT', 'RSHIFT']:
                    if not self.conduct_two_numbers_operation(instruction):
                        uncompleted_instructions.append(instruction)
                elif 'NOT' in instruction:
                    if not self.conduct_not_operation(instruction):
                        uncompleted_instructions.append(instruction)
                else:
                    if not self.conduct_assign(instruction):
                        uncompleted_instructions.append(instruction)
            self.instructions = uncompleted_instructions


# part 1
circuit = Circuit(instructions)
circuit.conduct_operations()
print(circuit.connections['a'])


# part 2
def make_instructions2(instructions):
    '''
    Replace value for key 'b' with value for key 'a' from part 1
    '''
    for instruction in instructions:
        if 'b' == instruction.split()[2]:
            position = instructions.index(instruction)
    instructions2 = instructions.copy()
    instructions2[position] = f"{circuit.connections['a']} -> b"
    return instructions2


circuit2 = Circuit(make_instructions2(instructions))
circuit2.conduct_operations()
print(circuit2.connections['a'])
