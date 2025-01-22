# https://leetcode.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        st = set()
        min_, max_ = float("inf"), -1
        for num in nums:
            if num > 0:
                if num < min_: min_ = num
                if num > max_: max_ = num
                st.add(num)
        if min_ > 1: return 1
        if len(st) == max_ : return max_ + 1
        for i in range(min_, max_ + 1):
            if i not in st: return i
