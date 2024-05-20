"""
Square Every Digit
CodeWars Link https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
"""


def square_digit(num: int) -> int:
    result = ""
    for i in str(num):
        i = int(i)**2
        result += str(i)
    return int(result)

print(square_digit(9119)) #811181


def square_digit2(num: int) -> int:
    return int(''.join(str(int(d)**2) for d in str(num)))


print(square_digit2(9119)) #811181


