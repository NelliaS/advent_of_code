class KeyPad:
    def __init__(self, pattern, position):
        self.actual_position = position
        self.pattern = pattern
        with open("day_2.txt") as f:
            self.code_parts = f.read().splitlines()

    def should_move(self, new_pos):
        x, y = new_pos
        if x < 0 or y < 0:
            return False
        try:
            value = self.pattern[x][y]
        except IndexError:
            return False
        return bool(value)

    def move(self, instruction):
        if instruction == "U":
            new_pos = (self.actual_position[0] - 1, self.actual_position[1])
        elif instruction == "D":
            new_pos = (self.actual_position[0] + 1, self.actual_position[1])
        elif instruction == "R":
            new_pos = (self.actual_position[0], self.actual_position[1] + 1)
        else:
            new_pos = (self.actual_position[0], self.actual_position[1] - 1)

        if self.should_move(new_pos):
            self.actual_position = new_pos

    def main(self):
        code = []
        for code_part in self.code_parts:
            for instruction in code_part:
                self.move(instruction)
            x, y = self.actual_position
            code.append(self.pattern[x][y])
        return ''.join([str(number) for number in code])


keypad_simple = KeyPad(pattern=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], position=(1, 1))
keypad_advanced = KeyPad(
    pattern=[
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None],
    ],
    position=(2, 0),
)

print(f'Result of part 1: "{keypad_simple.main()}"')
print(f'Result of part 2: "{keypad_advanced.main()}"')
