with open('day_6.txt') as f:
    stream = list(f.readline().rstrip())


def main(stream, chunk_len):
    for i in range(len(stream)):
        non_repeating_chunk = set(stream[i : i + chunk_len])
        if len(non_repeating_chunk) == chunk_len:
            return i + chunk_len


print(f'Result of part 1: "{main(stream, 4)}"')
print(f'Result of part 1: "{main(stream, 14)}"')
