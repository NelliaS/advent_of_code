from typing import Tuple, Dict, List, Any


def parse(file_name: str) -> List[Any]:
    signals: List[Any] = []
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip().split("|")
            single_entry = []
            for el in line:
                single_entry.append(el.split())
            signals.append(single_entry)
    return signals


def count_1_4_7_8(list_of_signals: List[Any]) -> int:
    corresponding: Dict[int, int] = {1: 2, 4: 4, 7: 3, 8: 7}
    count = 0
    for line in list_of_signals:
        for el in line[1]:
            lenght = len(el)
            if lenght in corresponding.values():
                count += 1
    return count


def determine_1_4_7_8(input_signals: List[str]) -> Dict[int, str]:
    corresponding: Dict[int, str] = {}
    for el in input_signals:
        el = "".join(sorted(el))
        if len(el) == 2:
            corresponding.setdefault(1, el)
        elif len(el) == 3:
            corresponding.setdefault(7, el)
        elif len(el) == 4:
            corresponding.setdefault(4, el)
        elif len(el) == 7:
            corresponding.setdefault(8, el)
    return corresponding


def decode_signals(signals: List[Any]) -> Tuple[Any, Dict[int, str]]:
    """
    Unique_pattern:
           --0-
        _       _
        1       2
           --3-
        _       _
        4       5
           __6_

    """
    input_signals, output_signals = signals
    decoded = determine_1_4_7_8(input_signals)
    four_differs = set(decoded[4]) - set(decoded[4]).intersection(decoded[1])

    for signal in input_signals:
        signal = "".join(sorted(signal))
        # numbers 1, 4, 7, 8 already determined
        if len(signal) in (2, 3, 4, 7):
            pass
        # numbers 2, 3, 5
        if len(signal) == 5:
            # number 3 covers fully letters of 1
            if len(set(signal).intersection(decoded[1])) == 2:
                decoded.setdefault(3, signal)
            # number 5 covers fully difference in letters between 1 and 4
            elif len(set(signal).intersection(four_differs)) == 2:
                decoded.setdefault(5, signal)
            # number 2 only covers 1 letter from difference between 1 and 4
            elif len(set(signal).intersection(four_differs)) == 1:
                decoded.setdefault(2, signal)
        # number 0, 6, 9
        elif len(signal) == 6:
            # number 6 has 3 letters common with 4 and only one common with 1
            if (len(set(signal).intersection(decoded[4])) == 3) and (
                len(set(signal).intersection(decoded[1]))
            ) == 1:
                decoded.setdefault(6, signal)
            # number 9 covers fully difference in letters between 1 and 4
            elif len(set(signal).intersection(four_differs)) == 2:
                decoded.setdefault(9, signal)
            # the last is number 0
            else:
                decoded.setdefault(0, signal)

    return output_signals, decoded


def count_output(output_signals: List[str], decoded: Dict[str, int]) -> int:
    inverted_decoded = dict(zip(decoded.values(), decoded.keys()))
    total: str = ""

    for signal in output_signals:
        signal = "".join(sorted(signal))
        total += str(inverted_decoded[signal])

    return int(total)


def main(list_of_signals: List[Any]) -> int:
    total = 0
    for line in list_of_signals:
        output_signals, decoded = decode_signals(line)
        total += count_output(output_signals, decoded)
    return total


# Results
part_1 = count_1_4_7_8(parse("day_8.txt"))
print(f"Part 1: {part_1}")

part_2 = main(parse("day_8.txt"))
print(f"Part 2: {part_2}")
