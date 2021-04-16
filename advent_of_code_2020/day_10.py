numbers = []

with open('day_10.txt') as f:
    for line in f:
        line = int(line.rstrip())
        numbers.append(line)
    numbers.sort()
    numbers = [0] + numbers + [numbers[-1] + 3]


def multiplied_differences(numbers):
    '''
    Count 1-jolt and 3-jolt differences.
    Return multiplication of those two numbers.
    '''
    one_jolts = 0
    three_jolts = 0
    for i, number in enumerate(numbers[1:]):
        difference = number - numbers[i]
        if difference == 1:
            one_jolts += 1
        else:
            three_jolts += 1
    return one_jolts * three_jolts


print(multiplied_differences(numbers))
