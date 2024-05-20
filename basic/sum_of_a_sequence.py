"""
Sum of a sequence
Code Wars Link https://www.codewars.com/kata/586f6741c66d18c22800010a/python
"""


def sequence_sum(begin_number, end_number, step):
    list_numbers = []
    for i in range(begin_number, end_number+1, step):
        list_numbers.append(i)
    return sum(list_numbers)


print(sequence_sum(2, 6, 2)) #12
print(sequence_sum(1, 5, 1)) #15
print(sequence_sum(2, 24, 22)) #26
