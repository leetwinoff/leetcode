"""
Moving zeros to the end
Code Wars Link https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
"""

def move_zeros(array: list) -> list:
    return sorted(array, key=lambda x: x == 0)

print(move_zeros([0, 1, 0, 3, 12])) #[1, 3, 12, 0, 0]

#Another solution

def move_zeros(array: list) -> list:
    position = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[position] = array[i]
            position += 1
    for i in range(position, len(array)):
        array[i] = 0
    return array

print(move_zeros([0, 1, 0, 3, 12])) #[1, 3, 12, 0, 0]