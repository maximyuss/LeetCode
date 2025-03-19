# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt_operations = 0
        change=[False, False]
        for i in range (len(nums)-2):
            is_change = not(change[0] ^ change[1] ^ nums[i])
            cnt_operations += is_change
            change[0] = change[1]
            change[1] = is_change
        if bool(nums[-2] ^ change[0] ^ change[1] and nums[-1] ^ change[1]):
            return cnt_operations
        return -1
