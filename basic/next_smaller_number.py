"""
Next smaller Number with the same digits
Code Wars Link https://www.codewars.com/kata/5659c6d896bc135c4c00021e/python
"""

def next_maller(n: int) -> int:
    digits = list(str(n))
    length = len(digits)

    for i in range(length - 2, -1, -1):
        if digits[i] > digits[i + 1]:
            break
    else:
        return -1
    max_index = i + 1
    for j in range(i + 1, length):
        if digits[j] < digits[i] and digits[j] > digits[max_index]:
            max_index = j

    digits[i], digits[max_index] = digits[max_index], digits[i]

    digits = digits[:i + 1] + sorted(digits[i+1:], reverse=True)

    if digits[0] == "0":
        return -1

    result = int("".join(digits))

    return result


print(next_maller(21))
print(next_maller(531))
print(next_maller(907))

