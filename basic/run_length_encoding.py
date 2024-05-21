"""
Run Length Encoding
CodeWars Link https://www.codewars.com/kata/578bf2d8daa01a4ee8000046/train/python
"""

def encode(st: str) -> str:
    count = 1
    encoded_string = ""
    for i in range(1, len(st)):
        if st[i] == st[i-1]:
            count += 1
        else:
            encoded_string += str(count) + st[i-1]
            count = 1
    encoded_string += str(count) + st[-1]
    return encoded_string

def decode(st: str) -> str:
    decoded_str = ""
    count = ""
    for char in st:
        if char.isdigit():
            count += char
        else:
            decoded_str += int(count) * char
            count = ""
    return decoded_str



print(encode("AAABBBCCCA"))
print(decode("3A3B3C1A"))
print(decode(encode("AAABBBCCCA")))