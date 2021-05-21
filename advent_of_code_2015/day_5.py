import re

strings = []

with open("day_5.txt") as f:
    for line in f:
        strings.append(line.rstrip())


def nice_or_naughty_1(strings):
    '''
    Count how many strings from array of strings are nice.
    Nice string:
        1) contains at least three vowels (aeiou)
        2) contains at least one letter that appears twice in a row
        3) does NOT contain double letters - ab, cd, pq, xy
    '''
    count = 0
    vowels = '.*[aeiou].*[aeiou].*[aeiou]'      # condition 1
    double_letter = '.*([a-z])\\1'              # condition 2
    forbidden = '.*(ab|cd|pq|xy)'               # condition 3
    for string in strings:
        if re.match(vowels, string):
            if re.match(double_letter, string):
                if re.match(forbidden, string) is None:
                    count += 1
    return count


def nice_or_naughty_2(strings):
    '''
    Count how many strings from array of strings are nice.
    Nice string:
        1) contains a pair of any 2 letters that appears at least 2x in the string
        2) contains at least 1 letter which repeats with exactly 1 letter between them
    '''
    count = 0
    pair = '.*([a-z][a-z]).*\\1'                # condition 1
    repeats = '.*([a-z]).\\1'                   # condition 2
    for string in strings:
        if re.match(pair, string):
            if re.match(repeats, string):
                count += 1
    return count


print(nice_or_naughty_1(strings))   # part 1
print(nice_or_naughty_2(strings))   # part 2
