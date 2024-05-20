"""
Get the middle character
CodeWars Link https://www.codewars.com/kata/56747fd5cb988479af000028/python
"""


def get_middle(s: str) -> str:
    if len(s) % 2 == 0:
        return s[(len(s)//2)-1:(len(s)//2)+1]
    else:
        return s[(len(s)//2)]


print(get_middle("teste"))
print(get_middle("test"))


#Another solution
def get_middle2(s: str) -> str:
    return s[(len(s)-1)//2:len(s)//2+1]

print(get_middle2("test"))
print(get_middle2("teste"))