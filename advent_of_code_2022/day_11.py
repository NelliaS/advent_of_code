import math
import re
from collections import deque
from dataclasses import dataclass, field
from typing import Any


class Operator:
    def __init__(self):
        with open('day_11.txt') as f:
            self.monkeys = []
            for group in f.read().split('\n\n'):
                operation = re.findall('new = old (.+)', group)[0]
                if operation == '* old':
                    operation = '**2'
                self.monkeys.append(
                    Monkey(
                        id=int(re.findall('Monkey ([0-9]+)', group)[0]),
                        operation=operation,
                        divisor=int(re.findall('Test: divisible by ([0-9]+)', group)[0]),
                        throw_to_true=int(re.findall('If true: throw to monkey ([0-9]+)', group)[0]),
                        throw_to_false=int(re.findall('If false: throw to monkey ([0-9]+)', group)[0]),
                        items=deque([int(item) for item in re.findall('Starting items: (.+)', group)[0].split(',')]),
                    )
                )
        for monkey in self.monkeys:
            monkey.throw_to_true = self.monkeys[monkey.throw_to_true]
            monkey.throw_to_false = self.monkeys[monkey.throw_to_false]

        self.common_multiple = math.prod([monkey.divisor for monkey in self.monkeys])

    def play_rounds(self, how_many, part2=False):
        for _ in range(how_many):
            for monkey in self.monkeys:
                monkey.inspect(common_multiple=self.common_multiple if part2 else None)
        inspected_time = sorted([monkey.inspected_times for monkey in self.monkeys])
        return inspected_time[-1] * inspected_time[-2]


@dataclass
class Monkey:
    id: int
    operation: str
    divisor: int
    throw_to_true: Any
    throw_to_false: Any
    inspected_times: int = 0
    items: deque = field(default_factory=deque)

    def inspect(self, common_multiple):
        for i in range(len(self.items)):
            self.inspected_times += 1
            item = eval(str(self.items.popleft()) + self.operation)
            if common_multiple:
                item = item % common_multiple
            else:
                item = item // 3
            is_divisible = item % self.divisor == 0
            self.throw_to_true.items.append(item) if is_divisible else self.throw_to_false.items.append(item)


operator = Operator()
operator2 = Operator()
print(f'Result of part 1: "{operator.play_rounds(20)}"')
print(f'Result of part 2: "{operator2.play_rounds(10000, part2=True)}"')
