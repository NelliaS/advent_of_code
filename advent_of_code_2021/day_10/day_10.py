from typing import List, Any, Tuple
from statistics import median


def parse(file_name: str) -> List[Any]:
    all_chunks = []
    with open(file_name) as f:
        for line in f:
            all_chunks.append(list(line.rstrip()))
    return all_chunks


def filter_chunks(chunks: list) -> Any:
    opposite_chunks = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = []

    for chunk in chunks:
        if chunk in opposite_chunks.values():
            stack.append(chunk)
        else:
            last_chunk = stack.pop()
            if opposite_chunks[chunk] != last_chunk:
                # invalid chunk line
                return chunk

    stack.reverse()
    return stack


def count_corrupted(all_chunks: list) -> int:
    score = 0
    syntax_points = {")": 3, "]": 57, "}": 1197, ">": 25137}

    for line in all_chunks:
        output = filter_chunks(line)
        if type(output) is str:  # one chunk returned
            score += syntax_points[output]

    return score


def count_completion(all_chunks: list) -> int:
    score = []
    syntax_points = {"(": 1, "[": 2, "{": 3, "<": 4}

    for line in all_chunks:
        output = filter_chunks(line)
        if type(output) is list:  # incomplete chunks returned
            score_of_line = 0
            for el in output:
                score_of_line = score_of_line * 5 + syntax_points[el]
            score.append(score_of_line)
    return int(median(score))


def main(file_name: str) -> Tuple[int, int]:
    all_chunks = parse(file_name)
    part_1 = count_corrupted(all_chunks)
    part_2 = count_completion(all_chunks)
    return part_1, part_2


part_1, part_2 = main("day_10.txt")
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
