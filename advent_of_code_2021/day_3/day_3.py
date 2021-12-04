from typing import Dict, Tuple

list_of_numbers = []

with open("day_3.txt", encoding="utf-8") as f:
    for line in f:
        list_of_numbers.append(line.rstrip())


def count_vertically_most_common_bits(numbers) -> Dict[int, Dict[str, int]]:
    """
    For each position in list of binary numbers count number 0 and number 1.
    Result save into nested dictionary.
    Eg. [11, 01] -> {0: {'0': 1, '1': 1}, 1: {'0': 0, '1': 2}}

    Args:
        numbers (list): list of numbers in binary format

    Returns:
        Dict[int, Dict[str, int]]: keys are numbered positions,
        values are dictionaries, with 2 keys ('0' and '1') and counts as values.
    """
    bits_in_lines = {}
    for digit in [*range(len(numbers[0]))]:
        bits_in_lines[digit] = {"0": 0, "1": 0}

    for number in numbers:
        for i, bit in enumerate(number):
            bits_in_lines[i][bit] += 1

    return bits_in_lines


def count_gamma_and_epsilon_rate(bits_in_lines) -> Tuple:
    """
    Gamma rate is calculated from prevailing (digit (0 or 1) in each position
    Epsilon rate is opposite number (eg. '010' was made from gamma rate '101')

    Args:
        bits_in_lines (dict): nested dictionary, counted '0' and '1' for each
                              position in list of binary numbers

    Returns:
        Tuple: gamma and epsilon rate
    """
    gamma_rate = ""
    epsilon_rate = ""
    for value in bits_in_lines.values():
        gamma_rate += "0" if value["0"] > value["1"] else "1"

    for bit in gamma_rate:
        epsilon_rate += "0" if bit == "1" else "1"

    return gamma_rate, epsilon_rate


def filter_list(numbers, bits_in_lines, criteria) -> str:
    """
    Determine 'most' or 'least' common value ('0' or '1') in the current position,
    and keep in a list only those bit numbers with that bit in that position.

    Args:
        numbers (list): list of numbers in binary format
        bits_in_lines (dict): nested dictionary, counted '0' and '1' for each
                              position in list of binary numbers
        criteria (str): criteria for comparison (values 'most' or 'least')

    Returns:
        str: resulting binary number after filtering
    """
    kept_numbers = numbers[::]
    i = 0
    while len(kept_numbers) > 1:
        new_kept_numbers = []

        number_O_count = bits_in_lines[i]["0"]
        number_1_count = bits_in_lines[i]["1"]
        number_to_keep = compare_numbers(number_O_count, number_1_count, criteria)

        for number in kept_numbers:
            if number[i] == number_to_keep:
                new_kept_numbers.append(number)

        kept_numbers = new_kept_numbers
        bits_in_lines = count_vertically_most_common_bits(kept_numbers)
        i += 1

    return kept_numbers[0]


def compare_numbers(number_0, number_1, criteria) -> str:
    """
    Compare numbers according to a criteria ('most' or 'least').
    Criteria 'most' returns the number of which count is bigger.
    Criteria 'least' returns the number of which count is lesser.
    When counts are equal, criteria 'most' returns '1', and 'least' returns '0'

    Args:
        number_0 (int): count of numbers '0'
        number_1 (int): count of numbers '1'
        criteria (str): criteria for comparison

    Returns:
        str: resulting number (values '0' or '1')
    """
    if criteria == "most":
        if number_0 == number_1:
            return "1"
        else:
            return "0" if number_0 > number_1 else "1"
    else:
        if number_0 == number_1:
            return "0"
        else:
            return "0" if number_0 < number_1 else "1"


def main() -> None:
    bits_in_lines = count_vertically_most_common_bits(list_of_numbers)
    gamma_rate, epsilon_rate = count_gamma_and_epsilon_rate(bits_in_lines)
    result1 = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(f"Part 1 result: {result1}")

    O2_rating = filter_list(numbers[::], bits_in_lines, "most")
    CO2_rating = filter_list(numbers[::], bits_in_lines, "least")
    result2 = int(O2_rating, 2) * int(CO2_rating, 2)
    print(f"Part 2 result: {result2}")


main()
