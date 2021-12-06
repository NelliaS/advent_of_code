from typing import Counter
from collections import Counter


with open("day_6.txt", encoding="utf-8") as f:
    initial_fishes = []
    for line in f:
        initial_fishes = list(map(int, line.split(",")))


def create_empty_counter() -> Counter[int]:
    dictionary: Counter = Counter()
    for n in range(9):
        dictionary[n] = 0

    return dictionary


def count_fishes(initial_fishes: list, n: int) -> int:
    empty_counter: Counter = create_empty_counter()
    counter: Counter = empty_counter.copy()
    counter.update(Counter(initial_fishes))

    for _ in range(n):
        counter2: Counter = empty_counter.copy()
        for key, value in counter.items():
            if value > 0:
                if key == 0:
                    counter2[8] += value
                    counter2[6] += value
                else:
                    counter2[key - 1] += value
        counter = counter2.copy()
    return counter.total()


# Tests
assert count_fishes([3, 4, 3, 1, 2], 18) == 26
assert count_fishes([3, 4, 3, 1, 2], 80) == 5934


# Results
part_1 = count_fishes(initial_fishes, 80)
part_2 = count_fishes(initial_fishes, 256)

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
