"""
Count and Say
LeetCode Link https://leetcode.com/problems/count-and-say/description/
"""


def count_and_say(n: int) -> str:
    def helper(s): #Creating helper function inside
        result = ""
        count = 1
        for i in range(len(s)):
            if i == len(s)-1 or s[i] != s[i+1]:
                result += str(count) + s[i]
            else:
                count += 1
        return result

    ans = "1"
    for i in range(2, n+1):
        ans = helper(ans)
    return ans

print(count_and_say(4))