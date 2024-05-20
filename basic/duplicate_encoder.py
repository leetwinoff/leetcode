"""
Duplicate encoder
Code Wars Link https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python
"""


def duplicate_encode(word: str) -> str:
    word = word.lower()
    encoded_word = ""
    for i in word:
        if word.count(i) == 1:
            encoded_word += "("
        else:
            encoded_word += ")"

    return encoded_word


print(duplicate_encode("din"))
print(duplicate_encode("recede"))


# Another solution

def duplicate_encode2(word: str) -> str:
    return "".join(["(" if word.lower().count(i) == 1 else ")" for i in word])

print(duplicate_encode2("din"))
print(duplicate_encode2("recede"))

