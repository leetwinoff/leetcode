"""
Fibonacci sequence
Leetcode Link https://leetcode.com/problems/fibonacci-number/description/
"""


def fib(n: int) -> int:
    if n <= 1:
        return n
    f1, f2 = 0, 1

    for _ in range(2, n + 1):
        f1, f2 = f2, f1 + f2
    return f2


print(fib(4)) #3
print(fib(3)) #2

