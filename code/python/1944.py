# https://leetcode.com/problems/number-of-visible-people-in-a-queue/
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res, stack = [0] * n, deque()
        for i in range(n - 1, -1, -1):
            cur = heights[i]
            cnt = 0
            while stack and cur >= stack[-1]:
                stack.pop()
                cnt += 1
            res[i] = cnt + (1 if stack else 0)
            stack.append(cur)
        return res
