# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pref = set()
        for num in arr1:
            while num not in pref and num:
                pref.add(num)
                num //= 10
        res = 0
        for num in arr2:
            while num:
                if num in pref:
                    break
                num //= 10
            if num:
                res = max(res, len(str(num)))
        return res
