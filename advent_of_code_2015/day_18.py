from copy import deepcopy


class Calculator:
    def __init__(self, source):
        self.default_lights = []
        if type(source) == str:
            self.process_input(source)
        else:
            self.default_lights = source
        self.current_state = deepcopy(self.default_lights)
        self.max_x = len(self.default_lights) - 1
        self.max_y = len(self.default_lights[0]) - 1
        self.corner_lights = [(0, 0), (0, self.max_y), (self.max_x, 0), (self.max_x, self.max_x)]

    @property
    def count_shining_lights(self):
        count = 0
        for row in self.current_state:
            count += row.count('#')
        return count

    def do_steps(self, steps, special_rule=False):
        """
        Light stays on (#) when has 2-3 neighbours, which shine, too. Otherwise, turns off (.).
        Light turns on when has exactly 3 neigbours, which shine. Otherwise, stays off.
        """
        new_state = deepcopy(self.current_state)
        for i in range(steps):
            for x, row in enumerate(self.current_state):
                for y, column in enumerate(row):
                    shining_neighbours, state = self.count_on_neighours((x, y))
                    if state == '#' and shining_neighbours not in (2, 3):
                        if not special_rule or (x, y) not in self.corner_lights:
                            new_state[x][y] = '.'
                    elif state == '.' and shining_neighbours == 3:
                        new_state[x][y] = '#'
            self.current_state = deepcopy(new_state)

    def count_on_neighours(self, coordinates):
        count = 0
        x, y = coordinates
        neighbours = [
            (x - 1, y),
            (x - 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y),
            (x + 1, y - 1),
            (x + 1, y + 1),
            (x, y - 1),
            (x, y + 1),
        ]
        for neighbour in neighbours:
            test_x, test_y = neighbour
            if test_x < 0 or test_y < 0 or test_x > self.max_x or test_y > self.max_y:
                continue
            test_state = self.current_state[test_x][test_y]
            if test_state == '#':
                count += 1
        return count, self.current_state[x][y]

    def process_input(self, from_file):
        with open(from_file) as f:
            for line in f:
                line = list(line.rstrip())
                self.default_lights.append(line)

    def light_corner_lights(self):
        for x, y in self.corner_lights:
            self.current_state[x][y] = '#'

    def reset_calculator(self):
        self.current_state = deepcopy(self.default_lights)


calculator = Calculator('day_18.txt')
calculator.do_steps(100)
print(f'Result of part 1: "{calculator.count_shining_lights}"')
calculator.reset_calculator()
calculator.light_corner_lights()
calculator.do_steps(100, special_rule=True)
print(f'Result of part 2: "{calculator.count_shining_lights}"')


def test_calculator():
    calculator = Calculator([['.', '#', '.', '#', '.', '#'], ['.', '.', '.', '#', '#', '.']])
    calculator.do_steps(1)
    assert calculator.current_state == [['.', '.', '#', '#', '.', '.'], ['.', '.', '#', '#', '#', '.']]

    calculator = Calculator('day_18_test.txt')
    assert calculator.count_shining_lights == 15

    calculator.do_steps(4)
    assert calculator.count_shining_lights == 4
    assert calculator.current_state == [
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '#', '.', '.'],
        ['.', '.', '#', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
    ]
