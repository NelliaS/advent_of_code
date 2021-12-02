list_of_measurements = []

with open("day_1.txt", encoding="utf-8",) as f:
    for line in f:
        list_of_measurements.append(int(line.rstrip()))


def count_number_of_sequent_increases(measurements) -> int:
    """
    Count how many sequent increases are in a list of measurements

    Args:
        measurements (List[int]): list of measurements

    Returns:
        int: number of sequent increases
    """
    if len(measurements) < 2:
        raise ValueError("List contains less than 2 values to compare")

    increase_count = 0
    previous_measurement = measurements[0]

    for measurement in measurements[1:]:
        if measurement > previous_measurement:
            increase_count += 1
        previous_measurement = measurement

    return increase_count


def count_number_of_sequent_increases_of_triplets(measurements) -> int:
    """
    Count how many sequent increases are between triplets.
    Compare a sum of each triplet to determine increase / decrease.

    Triples are made as follow:
        199  A
        200  A B
        208  A B C
        210    B C D
        200  E   C D
        207  E F   D
        240  E F G
        269    F G H
        260      G H
        263        H

    Args:
        measurements (List[int]): list of measurements

    Returns:
        int: number of sequent increases between triplets
    """
    if len(measurements) < 6:
        raise ValueError("List contains less than 6 values to compare")

    increase_count = 0

    for i in range(len(measurements) - 3):
        if i == 0:
            first = sum(measurements[i : i + 3])
        else:
            first = second
        second = sum(measurements[i + 1 : i + 4])

        if second > first:
            increase_count += 1

    return increase_count


# part 1
print(count_number_of_sequent_increases(list_of_measurements))
# part 2
print(count_number_of_sequent_increases_of_triplets(list_of_measurements))
