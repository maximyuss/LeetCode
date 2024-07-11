# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# This problem makes me question my software engineering career.
# The first solution is clear and obvious
class Solution:
    def reverseParentheses(self, s: str) -> str:
        de = deque()
        res = []
        i = 0
        for char in s:
            if char == "(":
                de.append(len(res))
            elif char == ")":
                j = de.pop()
                res[j:] = res[j:][::-1]
            else:
                res.append(char)
        return "".join(res)

# But the second one is very beautiful!
'''
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        parentheses = deque(maxlen=n)
        pair = [0] * n
        for i in range(n):
            if s[i] == "(":
                parentheses.append(i)
            if s[i] == ")":
                j = parentheses.pop()
                pair[i] = j
                pair[j] = i

        res = []
        i = 0
        direction = 1

        while i < n:
            if s[i] == "(" or s[i] == ")":
                i = pair[i]
                direction = -direction
            else:
                res.append(s[i])
            i += direction

        return "".join(res)
'''
