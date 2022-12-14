class Calculator:
    cycle = 0

    def __init__(self):
        self.x = 1
        self.interesting_cycles = (20, 60, 100, 140, 180, 220)
        self.signal_strengths = []
        self.monitor = list('.' * 240)
        self.sprite = (self.x - 1, self.x, self.x + 1)

        with open('day_10.txt') as f:
            self.instructions = f.read().splitlines()

    def __setattr__(self, name, value):
        self.__dict__[name] = value

        if name == 'cycle':
            if value in self.interesting_cycles:
                self.signal_strengths.append(self.cycle * self.x)

            if (self.cycle - 1) % 40 in self.sprite:
                self.monitor[self.cycle] = '█'

        if name == 'x':
            self.sprite = (self.x - 1, self.x, self.x + 1)

    def get_results(self):
        for instruction in self.instructions:
            if instruction == 'noop':
                self.cycle += 1
            else:
                self.cycle += 1
                self.cycle += 1
                self.x += int(instruction.split()[1])

        print('Result of part 2:')
        for since, to in [(0, 40), (40, 81), (80, 121), (120, 160), (160, 200), (200, 240)]:
            print(''.join(self.monitor[since:to]))

        return sum(self.signal_strengths)


calculator = Calculator()
print(f'Result of part 1: "{calculator.get_results()}"')
