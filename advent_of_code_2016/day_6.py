from collections import defaultdict, Counter


with open('day_6.txt') as f:
    messages = [line.rstrip() for line in f.readlines()]


def main(most_common: bool) -> str:
    """Return coded message from most common or least common letters from each index of multiple words."""
    dic = defaultdict(str)
    for message in messages:
        for i, letter in enumerate(message):
            dic[i] += letter

    result = ''
    for key, value in dic.items():
        result += Counter(value).most_common()[0 if most_common else -1][0]
    return result


print(f'Result of part 1: "{main(most_common=True)}"')
print(f'Result of part 2: "{main(most_common=False)}"')


