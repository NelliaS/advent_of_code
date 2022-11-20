class Computer:
    a: int
    b: int
    index: int

    def __init__(self):
        self.instructions = []

    def fill_instructions(self):
        with open('day_23.txt') as f:
            for line in f:
                self.instructions.append([el.rstrip(',') for el in line.rstrip().split()])

    def do_simple_operation(self, register, register_value):
        """Assign new register value and move add +1 to index (next step)."""
        setattr(self, register, register_value)
        self.index += 1

    def hlf(self, instruction):
        """Divide register value by 2."""
        register, register_value = instruction[1], getattr(self, instruction[1])
        if register_value % 2 != 0:
            raise ValueError
        self.do_simple_operation(register, register_value // 2)

    def tpl(self, instruction):
        """Multiply register value by three."""
        register, register_value = instruction[1], getattr(self, instruction[1])
        self.do_simple_operation(register, register_value * 3)

    def inc(self, instruction):
        """Add +1 to register value."""
        register, register_value = instruction[1], getattr(self, instruction[1])
        self.do_simple_operation(register, register_value + 1)

    def do_jump(self, value):
        """Jump back (-) or forth (+) in current index."""
        sign, number = value[0], int(value[1:])
        if sign == '+':
            self.index += number
        elif sign == '-':
            self.index -= number

    def jmp(self, instruction):
        """Jump unconditionally."""
        self.do_jump(value=instruction[1])

    def jie(self, instruction):
        """Jump only if register value is divisible by 2."""
        _, register, value = instruction
        if getattr(self, register) % 2 == 0:
            self.do_jump(value)
        else:
            self.index += 1

    def jio(self, instruction):
        """Jump only if register value is 1."""
        _, register, value = instruction
        if getattr(self, register) == 1:
            self.do_jump(value)
        else:
            self.index += 1

    def go_through_instructions(self, part1=True):
        if part1:
            self.a, self.b, self.index = 0, 0, 0
        else:
            self.a, self.b, self.index = 1, 0, 0
        try:
            while True:
                instruction = self.instructions[self.index]
                method = getattr(self, instruction[0])
                method(instruction)
        except IndexError:
            return self.b


computer = Computer()
computer.fill_instructions()
print(f'Result of part 1: "{computer.go_through_instructions()}"')
print(f'Result of part 2: "{computer.go_through_instructions(part1=False)}"')
