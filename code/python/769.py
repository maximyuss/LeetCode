# https://leetcode.com/problems/max-chunks-to-make-sorted/
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = max_chunk = len_chunk = start_chunk = 0
        for i in range(len(arr)):
            if arr[i] <= i and max_chunk <= i and i - start_chunk == len_chunk:
                res += 1
                len_chunk = 0
                start_chunk = i + 1
            else:
                len_chunk += 1
            max_chunk = max(max_chunk, arr[i])
        return res
