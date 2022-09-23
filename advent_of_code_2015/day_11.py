from pytest import mark
from string import ascii_lowercase as alphabet

with open('day_11.txt') as f:
    initial_string = f.read().strip()


class PasswordMaker:

    length = 8
    password = None

    @property
    def password_as_string(self):
        return ''.join(self.password)

    def __init__(self, initial_string):
        self.password = list(initial_string)

    def make_password(self):
        """
        Increment password until all conditions are satisfied.
        """
        self.increment()
        while not (self.condition1 and self.condition2 and self.condition3):
            self.increment()

    def increment(self):
        """
        Change a last letter of a string to a next one in alphabet.
            eg. 'ekoe' -> 'ekof'
        If letter is 'z' (changed to 'a') increment also previous letter.
            eg. 'ekoz' -> 'ekpa'
        """
        for i in range(self.length - 1, -1, -1):
            if not self.should_increment_another_letter(index=i):
                break

    def should_increment_another_letter(self, index):
        """
        Determine next letter from incrementing unicode representation.
        """
        if self.password[index] == 'z':
            incremented_letter = 'a'
        else:
            incremented_letter = chr(ord(self.password[index]) + 1)
        self.password[index] = incremented_letter
        return incremented_letter == 'a'

    @property
    def condition1(self):
        """
        Check if at least one increasing straight of at least three letters is present.
            eg. 'jkl' in 'hijklmmn'
        """
        for i in range(self.length - 2):
            substring = ''.join(self.password[i : i + 3])
            if substring in alphabet:
                return True
        return False

    @property
    def condition2(self):
        """
        Check if none of the letters 'i', 'o', 'l' is present.
        """
        if 'i' in self.password or 'o' in self.password or 'l' in self.password:
            return False
        return True

    @property
    def condition3(self):
        """
        Check if at least two different, non-overlapping pairs of letters are present.
            eg. 'aa' & 'cc' in 'ghjaabcc'
        """
        pairs = 0
        for i in range(self.length - 1):
            if self.password[i] == self.password[i + 1]:
                if self.password[i] != self.password[i - 1]:
                    pairs += 1
        return pairs >= 2


# Tests:
@mark.parametrize(
    ['tested_password', 'condition_1_result', 'condition_2_result', 'condition_3_result'],
    [
        ('hijklmmn', True, False, False),
        ('abbceffg', False, True, True),
        ('abbcegjk', False, True, False),
        ('abcdefgh', True, True, False),
        ('abcdffaa', True, True, True),
        ('ghijklmn', True, False, False),
        ('ghjaabcc', True, True, True),
    ],
)
def test_conditions(tested_password, condition_1_result, condition_2_result, condition_3_result):
    passwordmaker = PasswordMaker(tested_password)
    assert passwordmaker.condition1 is condition_1_result
    assert passwordmaker.condition2 is condition_2_result
    assert passwordmaker.condition3 is condition_3_result


@mark.parametrize(
    ['initial_string', 'password'],
    [
        ('abcdefgh', 'abcdffaa'),
        ('ghirugbj', 'ghjaabcc'),
    ],
)
def test_make_password(initial_string, password):
    passwordmaker = PasswordMaker(initial_string)
    passwordmaker.make_password()
    assert passwordmaker.password_as_string == password


# Results:

# part 1
passwordmaker = PasswordMaker(initial_string)
passwordmaker.make_password()
print(f'Result of part 1: "{passwordmaker.password_as_string}"')

# part 2
passwordmaker.make_password()
print(f'Result of part 2: "{passwordmaker.password_as_string}"')
