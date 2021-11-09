def count_code_chars():
    '''
    Count all code characters - using .read() method minus new line characters
    '''
    with open('day_8.txt') as f:
        chars_with_newlines = len(f.read())

    with open('day_8.txt') as f:
        number_of_lines = len(f.readlines())

    code_chars = chars_with_newlines - number_of_lines + 1      # deduct newlines characters
    return code_chars


with open('day_8.txt') as f:
    raw_lines = []
    for line in f:
        line = line.rstrip('\n').strip('"')
        raw_lines.append(line)


def count_string_chars(lines):
    '''
    Count string characters.
    Be aware, that below cases counts as only 1 character:
        - double backslash
        - double backslash + double quote character
        - double backslash + x + two hexadecimal characters
    '''
    string_chars = 0
    string_chars_list = []
    hexadecimal_chars = '01234456789abcdef'
    for line in lines:
        while '\\\\' in line:
            line = line.replace('\\\\', '1')
        while '\\"' in line:
            i = line.index('\\"')
            line = line[:i] + line[i+1:]        # only double quote remains
        while '\\x' in line:
            i = line.index('\\x')
            if line[i+2] in hexadecimal_chars and line[i+3] in hexadecimal_chars:
                line = line[:i] + '1' + line[i+4:]      # replace it with single character "1"
            else:
                raise ValueError("all fucked up")
        string_chars_list.append(line)
    for el in string_chars_list:
        string_chars += len(el)
    return string_chars


# Tests
def test_x_hexadecimal():
    assert count_string_chars(['gf\\x4ep']) == 4

def test_double_quote():
    assert count_string_chars(['gf\\"te', 'ret\\"trt']) == 12

def test_double_backslash():
    assert count_string_chars(['\\ewrth', 'et\\fe']) == 11

def test_example_string():
    assert count_string_chars(['', 'abc', 'aaa\\"aaa', '\\x27']) == 11

def test_kuba_vole():
    assert count_string_chars(['\\\\\\xab\\"\\abcd']) == 8

# part 1
print(count_code_chars() - count_string_chars(raw_lines))
