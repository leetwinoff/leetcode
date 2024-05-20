"""
Mumbling
CodeWars Link https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/python
"""


def accum(st: str) -> str:
    new_st = []
    for i in range(0, len(st)):
        part = ((i+1) * st[i]).capitalize()
        new_st.append(part)
    return "-".join(new_st).strip("-")

print(accum("ZpglnRxqenU"))


# Another solution

def accum2(st: str) -> str:
    return "-".join([((j * (i+1)).capitalize()) for i, j in enumerate(st)])

print(accum2("ZpglnRxqenU"))