# https://leetcode.com/problems/tuple-with-same-product/
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dict = {}
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                dict[product] = dict.get(product, 0) + 1
        res = 0
        for val in dict.values():
            res += 4 * val * (val - 1)
        return res
