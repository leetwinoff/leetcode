"""Persistent Bugger
CodeWars link https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/python
"""

def persistence(n: int) -> int:
    if n < 10:
        return 0

    count = 0
    while n >= 10:
        digits = 1
        for digit in str(n):
            digits *= int(digit)
        n = digits
        count +=1

    return count


print(persistence(39))
print(persistence(4))


