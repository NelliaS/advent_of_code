with open('day_15.txt') as f:
    numbers = list(map(int, f.read().rstrip().split(',')))


def memory_game(initial_numbers, searched_index):
    stats = {number: (i,) for i, number in enumerate(initial_numbers, start=1)}
    last_key = initial_numbers[-1]
    i = len(initial_numbers) + 1
    while i <= searched_index:
        try:
            last_key_value = stats[last_key]
            diff = last_key_value[1] - last_key_value[0]
            stats[diff] = (stats[diff][-1], i) if diff in stats else (i,)
        except IndexError:
            diff = 0
            stats[diff] = (stats[diff][-1], i)
        last_key = diff
        i += 1
    return last_key


print(f'Result of part 1: "{memory_game(numbers, 2020)}"')
print(f'Result of part 2: "{memory_game(numbers, 30000000)}"')
