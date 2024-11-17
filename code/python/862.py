# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + nums[i - 1]
        dq = deque()
        res = float("inf")
        for i in range(n + 1):
            while dq and pref[i] - pref[dq[0]] >= k:
                res = min(res, i - dq.popleft())
            while dq and pref[i] <= pref[dq[-1]]:
                dq.pop()
            dq.append(i)
        return res if res != float("inf") else -1
