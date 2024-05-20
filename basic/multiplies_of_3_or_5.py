"""
Multiples of 3 or 5
Code Wars Link https://www.codewars.com/kata/514b92a657cdc65150000006/python
"""


def solution(number:int) -> int:
    list_numbers = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            list_numbers.append(i)
    return sum(list_numbers)


print(solution(4)) #3
print(solution(6)) #8
print(solution(16)) #60


def solution2(number: int) -> int:
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 ==0])


print(solution2(4))
print(solution2(6))
print(solution2(16))

