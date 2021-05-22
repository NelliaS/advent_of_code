import numpy

instructions = []
with open('day_6.txt') as f:
    for line in f:
        instructions.append(line.rstrip())


class Grid:
    '''
    Class Grid can make a grid (empty_grid()), which is nested array of zeros (1000 x 1000),
    method extract_tuple() return a tuple (operation, n1, n2), where n1 and n2 are itself tuples of coordinates (x,y)
    There are two ways of applying instructions (part 1 and part 2 of a puzzle),
        method main_simple() uses apply_instruction_simple(), lights in the grid are either 0 or 1
        method main_brightness() uses apply_instruction_brightness(), lights in the grid are >= 0
    '''

    def __init__(self):
        self.empty_grid()

    def empty_grid(self):
        '''
        Return nested array - 1000 x 1000, with values 0
        '''
        self.grid = numpy.zeros((1000, 1000))

    def extract_tuple(self, instruction):
        '''
        From instruction an operation, a tuple n1 (x,y) and a tuple n2 (x,y) are derived.
        Return them as a tuple.
        '''
        instruction = instruction.split()
        if len(instruction) == 5:               # turn off / turn on
            operation = instruction[1]
            n1 = instruction[2].split(',')
            n2 = instruction[4].split(',')
        else:                                   # toggle
            operation = instruction[0]
            n1 = instruction[1].split(',')
            n2 = instruction[3].split(',')
        n1 = (int(n1[1]), int(n1[0]))           # n1 = (x, y)
        n2 = (int(n2[1]), int(n2[0]))           # n2 = (x, y)
        return (operation, n1, n2)

    def count_grid(self):
        '''
        Count a sum of the grid.
        '''
        total = 0
        for line in self.grid:
            total += sum(line)
        return int(total)

    def apply_instruction_simple(self, operation, x, y):
        '''
        Apply instruction for turning a specific light in the grid ON (to 1) or OFF (to 0)
        '''
        light = self.grid[x][y]
        if light == 0 and (operation == 'on' or operation == 'toggle'):
            self.grid[x][y] = 1
        elif light == 1 and (operation == 'off' or operation == 'toggle'):
            self.grid[x][y] = 0
        else:           # light is already off, or on
            pass

    def apply_instruction_brightness(self, operation, x, y):
        '''
        Apply instruction for increasing / decreasing brightness.
        '''
        light = self.grid[x][y]
        if operation == 'on':
            self.grid[x][y] += 1
        elif operation == 'off' and light != 0:
            self.grid[x][y] -= 1
        elif operation == 'toggle':
            self.grid[x][y] += 2
        else:           # cannot decrese to negative values
            pass

    def main_simple(self, instructions):
        '''
        Apply instructions on a grid (nested arrays /one array for each row/, valid values = 0 or 1)
        Instruction consists of and operation, a tuple n1 (x,y) and a tuple n2 (x,y), where:
            - operation:
                - "on" (turn lights on) = change values from 0 to 1
                - "off" (turn lights off) = change values from 1 to 0
                - "toggle" (change state of lights) = a value 0 becomes 1, a value 1 becomes 0
            - tuples n1 (x, y) and n2 (x, y) represent an opposite corners of a rectangle, inclusive
        - e.g. let's have a grid 4x4 and instruction 'turn on 1,0 through 3,2',
            where variables: n1 = (0,1), n2 = (2,4), operation = 'on'
            initial grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                which represents coordinates:
                    (0,0) (0,1) (0,2) (0,3)
                    (1,0) (1,1) (1,2) (1,3)
                    (2,0) (2,1) (2,2) (2,3)
                    (3,0) (3,1) (3,2) (3,3),
            in total there are 9 lights in a rectangle (0,1) - (2,4), which become ON,
            therefore new grid = [[0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0]]
        Return total number of lights on.
        '''
        for instruction in instructions:
            operation, n1, n2 = self.extract_tuple(instruction)
            n1_x, n1_y = n1
            n2_x, n2_y = n2
            for row in range(n2_x - n1_x + 1):             # difference in rows
                for column in range(n2_y - n1_y + 1):      # difference in columns
                    self.apply_instruction_simple(operation, n1_x + row, n1_y + column)
        return self.count_grid()

    def main_brightness(self, instructions):
        '''
        Apply instructions on a grid (nested arrays /one array for each row/, valid values >= 0)
        Instruction consists of and operation, a tuple n1 (x,y) and a tuple n2 (x,y), where:
            - operation:
                - "on" (increase brightness) = +1
                - "off" (decrease brightness) = -1
                - "toggle" (increase brightness two times) = +2
            - tuples n1 (x, y) and n2 (x, y) represent an opposite corners of a rectangle, inclusive
        Return total brightness of lights.
        '''
        for instruction in instructions:
            operation, n1, n2 = self.extract_tuple(instruction)
            n1_x, n1_y = n1
            n2_x, n2_y = n2
            for row in range(n2_x - n1_x + 1):             # difference in rows
                for column in range(n2_y - n1_y + 1):      # difference in columns
                    self.apply_instruction_brightness(operation, n1_x + row, n1_y + column)
        return self.count_grid()


grid = Grid()
print(grid.main_simple(instructions))         # part 1
grid.empty_grid()
print(grid.main_brightness(instructions))     # part 2