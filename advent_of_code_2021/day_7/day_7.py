from typing import Optional

list_of_crabs = []

with open("day_7.txt", encoding="utf-8") as f:
    for line in f:
        list_of_crabs = list(map(int, line.rstrip().split(",")))


def calculate_fuel(crabs: list, fuel_cost_increase: Optional[bool] = None) -> int:
    crabs.sort()
    min_position, max_position = crabs[0], crabs[-1]
    min_fuel = None

    for position in range(min_position, max_position):
        used_fuel = 0
        for crab in crabs:
            if not fuel_cost_increase:
                used_fuel += abs(crab - position)
            else:
                used_fuel += int(
                    ((1 + abs(crab - position)) / 2) * abs(crab - position)
                )
        if min_fuel is None or used_fuel < min_fuel:
            min_fuel = used_fuel
        used_fuel = 0
    return min_fuel


# Tests
test_example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
assert calculate_fuel(test_example) == 37
assert calculate_fuel(test_example, fuel_cost_increase=True) == 168


# Results
part_1 = calculate_fuel(list_of_crabs)
part_2 = calculate_fuel(list_of_crabs, fuel_cost_increase=True)

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
