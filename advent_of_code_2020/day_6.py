with open('day_6.txt') as f:
    groups = f.read().split('\n\n')


def count_anyone_yes(groups):
    '''Identify the questions for which anyone in group answered "yes"
    Question is represented by one letter. Count all unique questions in group.'''
    count = 0
    for one_group in groups:
        people = one_group.split('\n')
        unique = []
        for person in people:
            [unique.append(x) for x in person if x not in unique]
        count += len(unique)
    return count


def count_everyone_yes(groups):
    '''Identify the questions for which everyone in group answers "yes"
    Question is represented by one letter.
    Count all questions which appears for everyone in group. '''
    count = 0
    for group in groups:
        people = group.split('\n')
        common = people[0]
        for person in people[1:]:
            common = set(common).intersection(person)     # filter off duplicates
        count += len(common)
    return count


print(count_anyone_yes(groups))     # part 1
print(count_everyone_yes(groups))   # part 2
