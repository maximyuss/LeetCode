# https://leetcode.com/problems/count-number-of-nice-subarrays/
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.append(1)
        count = [1] * (n + 1)
        res = countOdd = countOddW = 0
        for l in range(n + 1):
            if nums[l] & 1:
                countOdd += 1
                if countOddW == k:
                    res += count[countOdd - k - 1] * count[countOdd - 1]
                else:
                    countOddW += 1
            else:
                count[countOdd] += 1
        return res
