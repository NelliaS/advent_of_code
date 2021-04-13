numbers = []

with open('day_1.txt') as f:
    for line in f:
        numbers.append(int(line.rstrip()))


def two_to_2020(numbers):
    '''In array of numbers find 2 numbers, which sum to number 2020. Return their product.'''
    for first_number in numbers:
        second_number = 2020 - first_number
        if second_number in numbers:
            return first_number * second_number


def three_to_2020(numbers):
    '''In array of numbers find 3 numbers, which sum to number 2020. Return their product.'''
    for i, first_number in enumerate(numbers, start=1):
        for second_number in numbers[i:]:
            sum_of_two = first_number + second_number
            third_number = 2020 - sum_of_two
            if third_number in numbers:
                return first_number * second_number * third_number


print(two_to_2020(numbers))
print(three_to_2020(numbers))