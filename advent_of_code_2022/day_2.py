with open('day_2.txt') as f:
    guide = f.read()
    for original, replacement in [('A', 'R'), ('B', 'P'), ('C', 'S'), ('X', 'R'), ('Y', 'P'), ('Z', 'S')]:
        guide = guide.replace(original, replacement)
    guide = [line.rstrip().split() for line in guide.split('\n')][:-1]


def evaluate_round(one_round):
    score_for_play = {'R': 1, 'P': 2, 'S': 3}
    opponent_play, my_play = one_round

    if opponent_play == my_play:  # draw
        return score_for_play[my_play] + 3
    elif one_round in [['S', 'R'], ['R', 'P'], ['P', 'S']]:  # win
        return score_for_play[my_play] + 6
    else:
        return score_for_play[my_play] + 0  # loss


def generate_round(one_round):
    choose_my_play = {
        'R': {'R': 'S', 'P': 'R', 'S': 'P'},
        'P': {'R': 'R', 'P': 'P', 'S': 'S'},
        'S': {'S': 'R', 'R': 'P', 'P': 'S'},
    }
    opponent_play, key_to_outcome = one_round

    return [opponent_play, choose_my_play[key_to_outcome][opponent_play]]


def results(guide, part1=True):
    total = 0
    for one_round in guide:
        total += evaluate_round(one_round) if part1 else evaluate_round(generate_round(one_round))
    return total


print(f'Result of part 1: "{results(guide)}"')
print(f'Result of part 2: "{results(guide, part1=False)}"')
