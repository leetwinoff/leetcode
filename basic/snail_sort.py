"""
Snail Sort
CodeWars link https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
"""


def snail_sort(array: list) -> list:
    result = []
    while array:
        result += array.pop(0)
        print(array)
        if array and array[0]:
            for row in array:
                result.append(row.pop())
        print(array)
        if array:
            result += array.pop()[::-1]
        print(array)
        if array and array[0]:
            for row in array[::-1]:
                result.append(row.pop(0))
    return result


print(snail_sort([[1,2,3],
         [4,5,6],
         [7,8,9]]))
