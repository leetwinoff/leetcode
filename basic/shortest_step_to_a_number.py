"""
Shortest step to a number
CodeWars Link https://www.codewars.com/kata/5cd4aec6abc7260028dcd942/train/python
"""


def shortest_step_to_num(num: int) -> int:
    count = 0
    while num > 1:
        if num % 2 == 0:
            num = num // 2
            count += 1
        else:
            num -= 1
            count += 1
    return count

print(shortest_step_to_num(16)) #4
print(shortest_step_to_num(71)) #9
