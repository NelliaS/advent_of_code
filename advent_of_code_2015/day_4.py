from hashlib import md5

with open("day_4.txt") as f:
    key = f.read()


def decrypt_md5(encoded):
    return md5(encoded)             # decrypt hash


def to_hexadecimal(md5_hash):
    return md5_hash.hexdigest()     # to hexadecimal format


def leading_zeros(hexadecimal, number_of_zeros):
    if hexadecimal[:number_of_zeros] == number_of_zeros * '0':     # leading zeros required
        return hexadecimal


def find_hash(key, number_of_zeros):
    '''We are looking for a md5 hash, which in hexadecimal format is starting with specified number of leading 0.
    Function returns a number, which must be added to given key to form above specified hash'''
    number = 0
    while True:
        test_key = key + str(number)             # extending key for number
        encoded = test_key.encode()              # encoding before hashing
        md5_hash = decrypt_md5(encoded)          # decrypt hash
        hexadecimal = to_hexadecimal(md5_hash)   # to hexadecimal format
        if leading_zeros(hexadecimal, number_of_zeros):
            return number
        else:
            number += 1


# part 1: 5 leading zeros required
print(find_hash(key, 5))

# part 2: 6 leading zeros required
print(find_hash(key, 6))
