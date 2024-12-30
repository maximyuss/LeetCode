# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        nums = list(map(int, boxes))
        res = [0] * n
        cnt, prev = nums[0], 0
        for i in range(1, n):
            prev += cnt
            res[i] = prev
            cnt += nums[i]
        cnt, prev = nums[n - 1], 0
        for i in range(n - 2, -1, -1):
            prev += cnt
            res[i] += prev
            cnt += nums[i]
        return res
