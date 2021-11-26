import itertools


def make_dictionary_of_distances():
    """
    Load data from file 
    and make nested dictionary of distances between 2 locations

    Returns:
        dict: nested dictionary of locations, example output:
              {
                'Praha': {'Brno': 207, 'Znojmo': 203}, 
                'Brno': {'Praha': 207, 'Znojmo': 67},
                'Znojmo': {'Praha': 203, 'Brno': 67}
              }
    """
    
    distances = {}
    # load data and make empty nested dictionaries for every location
    with open('day_9.txt') as f:
        for line in f:
            location1, _, location2, _, number = line.split()
            if location1 not in distances:
                distances[location1] = {}
            distances[location1][location2] = int(number)
        if location2 not in distances:
            distances[location2] = {}

    # fill in all nested dictionaries
    for location1, nested_dictionary in distances.items():
        for location2, number in nested_dictionary.items():
            distances[location2][location1] = number

    return distances


def make_permutations():
    """
    Take locations and make a list of all permutations

    Args:
        distances (dict): nested dictionary of locations

    Returns:
        list: list of tuples, each tuple is one possible permutation
    """
    distances = make_dictionary_of_distances()
    locations = distances.keys()
    return list(itertools.permutations(locations))


def determine_shortest_distance():
    """
    Calculate distances for every permutation of locations and determine
    how long is shortest distance

    Returns:
        int: shortest distance between locations
    """
    distances = make_dictionary_of_distances()
    permutations_of_distances = make_permutations()

    for permutation in permutations_of_distances:
        permutation_distance = calculate_distance(permutation, distances)

        if "shortest_distance" not in locals():
            shortest_distance = permutation_distance

        if permutation_distance < shortest_distance:
            shortest_distance = permutation_distance

    return shortest_distance


def calculate_distance(permutation, distances):
    """
    Sum up all distances between locations for given permutation

    Args:
        permutation (tuple): locations in specific order
        distances (dict) : nested dictionary of locations

    Returns:
        int: total distance between locations
    """
    permutation_distance = 0
    for x in range(7):
        number = distances[permutation[x]][permutation[x+1]]
        permutation_distance += distances[permutation[x]][permutation[x+1]]
    
    return permutation_distance


def determine_longest_distance(): 
    """
    Calculate distances for every permutation of locations and determine
    how long is longest distance

    Returns:
        int: longest distance between locations
    """
    distances = make_dictionary_of_distances()
    permutations_of_distances = make_permutations()

    for permutation in permutations_of_distances:
        permutation_distance = calculate_distance(permutation, distances)

        if "longest_distance" not in locals():
            longest_distance = permutation_distance

        if permutation_distance > longest_distance:
            longest_distance = permutation_distance

    return longest_distance
    

print(determine_shortest_distance())    # part 1
print(determine_longest_distance())     # part 2
