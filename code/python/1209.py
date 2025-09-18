# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        prev_char = None
        prev_count = 0
        for char in s:
            if char == prev_char:
                prev_count+=1
                if prev_count==k:
                    if stack:
                        prev_char, prev_count = stack.pop()
                    else:
                        prev_char = None
                        prev_count = 0
            else:
                if prev_char:
                    stack.append((prev_char, prev_count))
                prev_char = char
                prev_count = 1
        if prev_char:
            stack.append((prev_char,prev_count))
        return ''.join(c * n for c, n in stack)
