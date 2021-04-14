import re

batch_files = []

with open('day_4.txt') as f:
    one_entry = []
    for line in f:
        if line != '\n':
            line = line.rstrip().split(' ')
            for item in line:
                one_entry.append(item)
        else:
            batch_files.append(one_entry)
            one_entry = []
    batch_files.append(one_entry)


def check_items(batch):
    '''Return True if all required items (byr, iyr, eyr, hgt, hcl, ecl, pid) are present. Else return False'''
    all_fields = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    requiered_fields = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    present_fields = []
    for entry in batch:
        item = entry[:entry.index(':')]
        present_fields.append(item)
    present_fields.sort()
    if present_fields == all_fields or present_fields == requiered_fields:
        return True
    else:
        return False


def requiered_items(batch_files):
    '''Count all passports which contain all required items.
    Required items are: byr, iyr, eyr, hgt, hcl, ecl, pid.
    Only cid can be missing.'''
    valid = 0
    for batch in batch_files:
        met_criteria = check_items(batch)
        if met_criteria:
            valid += 1
    return valid


def count_valid_passports(batch_files):
    '''Count all valid passports, validation criteria are specified in function validate_values(),
    also all required fields must be present, as is specified in function required_items()'''
    valid = 0
    for batch in batch_files:
        if not check_items(batch):
            continue
        dictionary = {}
        for item in batch:
            key = item[:item.index(':')]
            value = item[item.index(':')+1:]
            dictionary.setdefault(key, value)
        if validate_values(dictionary):
            valid += 1
    return valid


def validate_values(dict):
    '''
    Validate values in dictionary according rules:
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.
    Return False if any condition is not met. Else return True.
    '''
    byr_regex = '(19[2-9][0-9])|(200[012])'     # numbers 1920 - 2002
    iyr_regex = '(201[0-9])|(2020)'             # numbers 2010 - 2020
    eyr_regex = '(202[0-9])|(2030)'             # numbers 2020 - 2030
    hgt_regex = '(1[5-8][0-9]cm)|(19[0-3]cm)|(59in)|(6[0-9]in)|(7[0-6]in)'  # 150-193cm or 59-76in
    hcl_regex = '#[0-9a-f]{6}'                  # hash symbol + 6 characters from 0-9, a-f
    ecl_regex = '(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)'     # amb blu brn gry grn hzl oth
    pid_regex = '[0-9]{9}'                      # nine digit number
    regexes = [byr_regex, iyr_regex, eyr_regex, hgt_regex, hcl_regex, ecl_regex, pid_regex]
    values = [dict['byr'], dict['iyr'], dict['eyr'], dict['hgt'], dict['hcl'], dict['ecl'], dict['pid']]
    for i, value in enumerate(values):
        if not re.fullmatch(regexes[i], value):
            return False
    return True


print(requiered_items(batch_files))         # part 1
print(count_valid_passports(batch_files))   # part 2