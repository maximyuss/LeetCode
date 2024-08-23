# https://leetcode.com/problems/maximum-distance-in-arrays/
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_diff = 0
        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_diff = max(max_diff, arr[-1] - min_val, max_val - arr[0])
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
        return max_diff
