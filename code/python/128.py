# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0
        for num in nums:
            if num in st and (num - 1) not in st:
                cur = num
                cnt = 0
                while cur in st:
                    st.remove(cur)
                    cur += 1
                    cnt += 1
                res = max(res, cnt)
        return res
