"""
507. Perfect Number
Leetcode link https://leetcode.com/problems/perfect-number/description/
"""


def check_perfect_number(num: int) -> bool:
    if num <= 1:
        return False
    count = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            count += i
            if i != num // i:
                count += num // i
    return count == num

print(check_perfect_number(28)) #True
print(check_perfect_number(6)) #True
print(check_perfect_number(496)) #True
print(check_perfect_number(8128)) #True
print(check_perfect_number(2)) #False
print(check_perfect_number(1)) #False