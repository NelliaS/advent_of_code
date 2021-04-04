from hashlib import md5

with open("day_4.txt") as f:
    key = f.read()

def find_hash1(key):
    '''We are looking for a md5 hash, which in hexadecimal format is starting with 5 leading zeros.
    Function returns a number, which must be added to given key to form above specified hash'''
    number = 0
    while True:
        test_key = key + str(number)     # extending key for number
        encoded = test_key.encode()      # encoding before hashing
        md5_hash = md5(encoded)          # md5 hash
        hexadecimal_format = md5_hash.hexdigest()        # to hexadecimal format
        if hexadecimal_format[:5] == '00000':     # five leading zeros required
            return number
        else:
            number += 1

print(find_hash1(key))
