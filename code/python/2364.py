# https://leetcode.com/problems/count-number-of-bad-pairs/
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        st, dict = set(), {}
        for i, num in enumerate(nums):
            diff = num - i
            if diff in st:
                dict[diff] = dict.get(diff, 0) + 1
            else:
                st.add(diff)
        if len(dict) == 1 and next(iter(dict.values())) == (n - 1):
            return 0
        cnt = sum([v * (v + 1) for v in dict.values()])
        return (n * (n - 1) - cnt) >> 1
