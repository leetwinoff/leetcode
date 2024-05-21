"""
Detect Pangram
CodeWar Link https://www.codewars.com/kata/545cedaa9943f7fe7b000048/python
"""


def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char in st.lower():
            continue
        else:
            return False
    return True


print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Cwm fjord bank glyphs vext quiz"))
print(is_pangram("This isn't a pangram!"))