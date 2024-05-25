"""
Double Trouble
CodeWars Link: https://www.codewars.com/kata/57f7796697d62fc93d0001b8/train/python
"""

def trouble(x: list, y: int) -> list:
    pointer = 0
    while pointer < len(x) - 1:
        if x[pointer] + x[pointer +1] == y:
            x.pop(pointer + 1)
        else:
            pointer += 1
    return x


print(trouble([1, 3, 5, 6, 7, 4, 3],7)) #[1, 3, 5, 7, 4, 3]