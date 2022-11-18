def count_code_chars():
    """
    Count all code characters - using .read() method minus new line characters
    """
    with open('day_8.txt') as f:
        chars_with_newlines = len(f.read())
    with open('day_8.txt') as f:
        number_of_lines = len(f.readlines())
    return chars_with_newlines - number_of_lines + 1


def count_string_chars():
    """
    Count string characters.
    Be aware, that below cases counts as only 1 character:
        - double backslash
        - double backslash + double quote character
        - double backslash + x + two hexadecimal characters
    """
    lines = []
    with open('day_8.txt') as f:
        for line in f:
            line = line.rstrip('\n').strip('"')
            lines.append(line)
    string_chars = 0
    string_chars_list = []
    hexadecimal_chars = '01234456789abcdef'
    for line in lines:
        while r'\\' in line:
            line = line.replace('\\\\', '1')
        while '\\"' in line:
            i = line.index('\\"')
            line = line[:i] + line[i + 1 :]  # only double quote remains
        while '\\x' in line:
            i = line.index('\\x')
            if line[i + 2] in hexadecimal_chars and line[i + 3] in hexadecimal_chars:
                line = line[:i] + '1' + line[i + 4 :]  # replace it with single character "1"
        string_chars_list.append(line)
    for el in string_chars_list:
        string_chars += len(el)
    return string_chars


def count_encoded_string():
    count = 0
    with open('day_8.txt') as f:
        for line in f:
            line = line.rstrip('\n')[1:-1]
            count += 6  # for surrounding strings
            for char in line:
                if char == '"':
                    count += 2
                elif char == '\\':
                    count += 2
                else:
                    count += 1
    return count


print(f'Result of part 1: "{count_code_chars() - count_string_chars()}"')
print(f'Result of part 2: "{count_encoded_string() - count_code_chars()}"')
