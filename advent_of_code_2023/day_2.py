import math
from collections import defaultdict


def parse_games():
    with open('day_2.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
        raw_data = [(int(line.split(': ')[0].lstrip('Game ')), line.split(': ')[1].split('; ')) for line in lines]
        games = defaultdict(dict)
        for game_number, records in raw_data:
            for i, record in enumerate(records):
                games[game_number][i] = {'blue': 0, 'red': 0, 'green': 0}
                for pile in record.split(', '):
                    number, colour = pile.split(' ')
                    games[game_number][i][colour] = int(number)
        return games


def is_valid(record):
    for colour, number in record.items():
        if (colour == 'red' and number > 12) or (colour == 'green' and number > 13) or colour == 'blue' and number > 14:
            return False
    return True


def main():
    part_1 = 0
    part_2 = 0
    for game_id, game_records in parse_games().items():
        validity = []
        minimal_values = {'blue': 0, 'green': 0, 'red': 0}
        for i, record in game_records.items():
            validity.append(is_valid(record))
            for colour, value in record.items():
                minimal_values[colour] = max(minimal_values[colour], value)

        if all(validity):
            part_1 += game_id
        part_2 += math.prod(list(minimal_values.values()))

    return part_1, part_2


print(f'Result of part 1: "{main()[0]}"')
print(f'Result of part 2: "{main()[1]}"')
