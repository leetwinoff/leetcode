"""
Find Duplicates
CodeWars Link https://www.codewars.com/kata/5558cc216a7a231ac9000022/python
"""

def duplicates(arr: list) -> list:
    count = {}
    duplicates =[]
    for i in arr:
        if i in count:
            count[i] += 1
            if count[i] == 2:
                duplicates.append(i)
        else:
            count[i] = 1
    return duplicates

print(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, "5"])) #[4, 3, 1]
