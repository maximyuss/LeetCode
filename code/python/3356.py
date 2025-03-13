# https://leetcode.com/problems/zero-array-transformation-ii/
class Solution:
  def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if all(x == 0 for x in nums): return 0
        queries.append([0, 0, 0])
        n = len(queries)
        diff_left = [0] * (len(nums) + 1)

        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2

            # Filling the difference array for the middle
            diff_mid = diff_left[:]
            for i in range(l, m + 1):
                diff_mid[queries[i][0]] += queries[i][2]
                diff_mid[queries[i][1] + 1] -= queries[i][2]

            # Calculate the current difference
            acc = 0
            check = False
            for i, num in enumerate(nums):
                acc += diff_mid[i]
                if num > acc:
                    break
            else:
                check = True

            if check:
                r = m
            else:
                l = m + 1
                diff_left = diff_mid[:]
        if l == n - 1:
            return -1
        return l + 1

'''
    # Faster but more complex solution using line sweep
    def minZeroArray3(self, nums: List[int], queries: List[List[int]]) -> int:
        k = acc = 0
        diff = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            while acc + diff[i] < nums[i]:
                k += 1
                if k > len(queries):
                    return -1
                l, r, val = queries[k - 1]
                if r >= i:
                    diff[max(l, i)] += val
                    diff[r + 1] -= val
            acc += diff[i]
        return k
'''
