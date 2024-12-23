# https://leetcode.com/problems/next-greater-element-ii/
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * (n)
        dq = deque()
        for i in range(2 * n - 1, -1, -1):
            j = i % n
            cur = nums[j]
            while dq and dq[0] <= cur:
                dq.popleft()
            if dq and dq[0] > cur:
                res[j] = dq[0]
            dq.appendleft(cur)
        return res
