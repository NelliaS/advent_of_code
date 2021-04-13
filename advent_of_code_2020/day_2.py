import re

passwords = []

with open('day_2.txt') as f:
    for line in f:
        password_tuple = tuple(line.rstrip().split())
        passwords.append(password_tuple)


def count_valid(paswords):
    ''' Count valid passwords. Each tuple eg. ('3-4', 'j:', 'hjvj') must meet rules.
    In given example there can be 3-4 letters "j" in password "hjvj" to be counted as valid,
    return number of all valid passwords'''
    valid = 0
    for password_tuple in passwords:
        dash = password_tuple[0].index('-')     # divide by dash
        minimum = int(password_tuple[0][:dash])
        maximum = int(password_tuple[0][dash + 1:])
        letter = password_tuple[1][0]
        password = password_tuple[2]
        if password.count(letter) in range(minimum, maximum + 1):
            valid += 1
    return valid


def make_regex(first, second, l):
    '''Takes arguments of two numbers - number of allowed letters before and after specified letter "l".
    Return regEx'''
    b = '{' + str(first - 1) + '}'            # formating for regex
    a = '{' + str(second - first - 1) + '}'
    return f'(^.{b}{l}.{a}[^{l}])|(^.{b}[^{l}].{a}{l})'


def count_valid2(paswords):
    '''Count valid passwords. Each tuple eg. ('3-4', 'j:', 'hjvj') must meet rules.
    In given example there must be letter "j" either on 3rd or 4th position in password "hjvj".
    Note that letter cannot be on both positions and index starts with 1.
    Return number of all valid passwords'''
    valid = 0
    for password_tuple in passwords:
        # extract numbers for making regEx
        dash = password_tuple[0].index('-')      # divide by dash
        first = int(password_tuple[0][:dash])
        second = int(password_tuple[0][dash + 1:])
        letter = password_tuple[1][0]
        # make regex
        regex = make_regex(first, second, letter)
        # validate password
        password = password_tuple[2]
        match = re.match(regex, password)
        if match:
            valid += 1
    return valid


print(count_valid(passwords))
print(count_valid2(passwords))