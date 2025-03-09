# https://leetcode.com/problems/partition-array-according-to-given-pivot/
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, greater = [], []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
        less.extend([pivot] * (len(nums) - len(less) - len(greater)))
        less.extend(greater)
        return less
