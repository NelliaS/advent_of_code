import json
from pytest import mark


class ExtractorSimple:
    def __init__(self):
        self.numbers = []

    @property
    def sum_of_numbers(self):
        return sum(self.numbers)

    def extract_numbers(self, obj):
        """
        Find all numbers in nested dictionaries or lists.
        """
        if type(obj) == list:
            for el in obj:
                self.extract_numbers(el)
        elif type(obj) == dict:
            for key, value in obj.items():
                self.extract_numbers(key)
                self.extract_numbers(value)
        elif type(obj) == int:
            self.numbers.append(obj)


class ExtractorAdvanced(ExtractorSimple):
    def extract_numbers_with_condition(self, obj):
        """
        Find all numbers in nested dictionaries or lists.
        But ignore all dictionaries (and their contents) where any key / value is word 'red'.
        """
        if type(obj) == list:
            for el in obj:
                self.extract_numbers_with_condition(el)
        elif type(obj) == dict:
            if 'red' not in obj.values() and 'red' not in obj.keys():
                for key, value in obj.items():
                    self.extract_numbers_with_condition(key)
                    self.extract_numbers_with_condition(value)
        elif type(obj) == int:
            self.numbers.append(obj)


@mark.parametrize(
    ['obj', 'result'],
    [
        ({'b': 2, 'c': 'red'}, 0),
        ({'e': [1, 2, 3, 4], 'f': 5, 'd': 'r'}, 15),
        ({'d': 'r', 'e': [1, 2, 'red', 3, 4], 'f': 5}, 15),
        ({'d': 'r', 'e': [1, 2, 'red', {'a': ['red']}, 3, 4], 'f': 5}, 15),
        ({'d': 'r', 'x': [1, 2, 'red', {'a': ['red']}, 3, 4], 'red': 5}, 0),
        ([1, {'c': 'red', 'b': 2}, 3], 4),
        ([1, 'red', 5], 6),
    ],
)
def test_advanced_extract_dict(obj, result):
    extractor = ExtractorAdvanced()
    extractor.extract_numbers_with_condition(obj)
    assert extractor.sum_of_numbers == result


# Results:
with open('day_12.txt') as f:
    content = f.read()
    json_doc = json.loads(content)

# part 1
extractor = ExtractorSimple()
extractor.extract_numbers(json_doc)
print(f'Result of part 1: "{extractor.sum_of_numbers}"')

# part 2
extractor_2 = ExtractorAdvanced()
extractor_2.extract_numbers_with_condition(json_doc)
print(f'Result of part 2: "{extractor_2.sum_of_numbers}"')
