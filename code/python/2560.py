# https://leetcode.com/problems/house-robber-iv/
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(target):
            count = is_skip = 0
            for num in nums:
                if is_skip:
                    is_skip = False
                elif num <= target:
                    count += 1
                    if count == k: return True
                    is_skip = True
            return False

        items = list(sorted(set(nums)))
        l, r = 0, len(items) - 1
        while l < r:
            mid = l + (r - l) // 2
            if check(items[mid]):
                r = mid
            else:
                l = mid + 1
        return items[l]
