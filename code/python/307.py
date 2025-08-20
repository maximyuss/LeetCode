# https://leetcode.com/problems/range-sum-query-mutable/
class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums.copy()
        self.tree = BIT(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(right + 1) - self.tree.query(left)


class BIT:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            self.tree[i] += nums[i - 1]
            if i + (i & -i) <= self.n:
                self.tree[i + (i & -i)] += self.tree[i]

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res
