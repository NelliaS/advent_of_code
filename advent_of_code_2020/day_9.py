numbers = []

with open('day_9.txt') as f:
    for line in f:
        numbers.append(int(line.rstrip()))


def validate(preamble, numbers, tested_number):
    '''
    Return True if tested number is valid.
    Valid number is sum of two numbers from array of numbers.
    Else return False.
    '''
    for i in range(preamble):
        number_1 = numbers[i]
        number_2 = tested_number - number_1
        if number_2 in numbers:
            return True
    return False


def identify_nonvalid(numbers):
    '''
    Valid number is sum of two of the 25 numbers in list before it.
    Return first nonvalid number (after preamble).
    '''
    preamble = 25
    for i, tested_number in enumerate(numbers):
        if i > preamble:
            numbers_before = numbers[(i - preamble):i]
            valid = validate(preamble, numbers_before, tested_number)
            if valid is False:
                return tested_number


def return_weakness(list_numbers, wide, nonvalid):
    '''
    Try to identify list of numbers (in specified wide) which sum to invalid number.
    An encryption weakness is multiplication of first and last number in identified list.
    Return the encryption weakness, if found. Else return None.
    '''
    sum_numbers = 0
    tested_numbers = []
    for i in range(wide):          # initial list of tested numbers (in specified wide)
        number = list_numbers[i]
        sum_numbers += number
        tested_numbers.append(number)
    i = wide        # start index for adding from list
    while True:
        try:
            tested_numbers.append(list_numbers[i])     # add next number to tested list
            sum_numbers += tested_numbers[-1]          # add to sum next number in tested list
            sum_numbers -= tested_numbers[0]           # deduct from sum first number in tested list
            tested_numbers = tested_numbers[1:]        # remove first number in tested list
            if sum_numbers == nonvalid:
                tested_numbers.sort()      # weakness is sum of lowest and highest number in list
                encryption_weakness = tested_numbers[0] + tested_numbers[-1]
                return encryption_weakness
            i += 1  # move to next number in list
        except IndexError:
            return None


def find_weakness(numbers):
    '''
    Adjust wide of array to find an encryption weakness.
    Return found encryption weakness.
    '''
    wide = 2
    found_weakness = None
    nonvalid = identify_nonvalid(numbers)
    while found_weakness is None:
        found_weakness = return_weakness(numbers, wide, nonvalid)
        wide += 1
    return found_weakness


print(identify_nonvalid(numbers))       # part 1
print(find_weakness(numbers))           # part 2
