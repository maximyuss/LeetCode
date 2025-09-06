# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero
MAX_BIT = 16
pref = [0] * MAX_BIT
for i in range(1, MAX_BIT):
    pref[i] = (((3*i - 1) << (2*i)) + 1) // 3

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for l, r in queries:
            base_l = (l.bit_length() + 1) // 2
            base_r = (r.bit_length() + 1) // 2
            if base_l == base_r:
                cur_res = (r - l + 1) * base_l
            else:
                cur_res = pref[base_r - 1] - pref[base_l] # middle part
                cur_res += (r - ((1 << (2*(base_r - 1))) - 1)) * base_r # right part
                cur_res += (((1 << (2*base_l)) - 1) - l + 1) * base_l # left part
            res += (cur_res + 1) // 2
        return res
