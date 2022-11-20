with open('day_10.txt') as f:
    initial_sequence = f.read()


def parse_sequence(sequence):
    """
    Take a sequence of numbers and parse them into a list, group the same
    numbers into one element of the list

    Args:
        sequence (str): sequence of numbers

    Returns:
        list: parsed sequence, where each element of the list contains only
              one type of number (eg. '112333' == ['11', '2', '333'])
    """
    parsed_sequence = [sequence[0]]
    current_index = 0

    for i, number in enumerate(sequence[1:]):
        # number is the same as previous one, add into the element of the list
        if number in parsed_sequence[current_index]:
            new_value = (len(parsed_sequence[current_index]) + 1) * number
            parsed_sequence[current_index] = new_value
        # number isn't the same as previous one, append a new element to the list
        if number not in parsed_sequence[current_index]:
            current_index += 1
            parsed_sequence.append(number)

    return parsed_sequence


def make_new_sequence(parsed_sequence):
    """
    Apply look-and-say rule to a whole parsed_sequence

    Args:
        parsed_sequence (list): each element consists of one type of number

    Returns:
        list: parsed sequence after applying look-and-say rule
    """

    new_sequence = []

    for element in parsed_sequence:
        new_element = parse_sequence(apply_look_and_say(element))
        new_sequence.extend(new_element)

    # correct the parsing (same numbers are in one element)
    return parse_sequence(new_sequence)


def apply_look_and_say(element):
    """
    Apply look-and-say rule to an element
    New element consist of number which represents length of string
    and then one of the digits of the element

    Args:
        element (str): various number of digits of one type

    Returns:
        list: new string after applying look and say rule

    """
    lenght = len(element)
    number = element[0]
    new_element = str(lenght) + number
    return new_element


def repeat_game(number, sequence):
    """
    Apply look-and-say rule to a sequence in specified number of times

    Args:
        number (int): number of game repetitions
        sequence (str): initial sequence of numbers

    Returns:
        str: resulting string after applying the look-and-say rule number-times
    """
    parsed_sequence = parse_sequence(sequence)

    for repetition in range(number):
        parsed_sequence = make_new_sequence(parsed_sequence)

    return ''.join(parsed_sequence)


# Tests
def test_parse_sequence():
    assert parse_sequence('11233551111') == ['11', '2', '33', '55', '1111']
    assert parse_sequence('444411111122') == ['4444', '111111', '22']
    assert parse_sequence('001155555') == ['00', '11', '55555']


def test_apply_look_and_say():
    assert apply_look_and_say('1') == '11'
    assert apply_look_and_say('11') == '21'
    assert apply_look_and_say('2222') == '42'


def test_make_new_sequence():
    assert make_new_sequence(['1']) == ['11']
    assert make_new_sequence(['11']) == ['2', '1']
    assert make_new_sequence(['2', '1']) == ['1', '2', '11']
    assert make_new_sequence(['1', '2', '11']) == ['111', '22', '1']
    assert make_new_sequence(['111', '22', '1']) == ['3', '1', '22', '11']


def test_repeat_game():
    assert repeat_game(5, '1') == '312211'


# Results:

# part 1
print(len(repeat_game(40, initial_sequence)))

# part 2
print(len(repeat_game(50, initial_sequence)))
