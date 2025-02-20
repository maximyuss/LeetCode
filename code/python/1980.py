# https://leetcode.com/problems/find-unique-binary-string/
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        res = ["0"] * n
        for i in range(n):
            if nums[i][i] == "0":
                res[i] = "1"
        return "".join(res)
