"""
Beginner Series #3 Sum of Numbers
CodeWars link https://www.codewars.com/kata/55f2b110f61eb01779000053/python
"""

def get_sum(a, b: int) -> int:
    result = 0
    if a < b:
        for i in range(a, b+1):
            result += i
    else:
        for i in range(a, b-1, -1):
            result += i

    return result


print(get_sum(0, 1))
print(get_sum(-10, 20))
print(get_sum(0, -1))


# Another solution

def get_sum2(a, b: int) -> int:
    return sum(range(min(a, b), max(a, b)+1))

print(get_sum2(0, 1))
print(get_sum2(-10, 20))
print(get_sum2(0, -1))