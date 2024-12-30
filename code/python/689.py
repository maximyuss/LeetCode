class Solution:

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 3 * k: return [0, k, 2 * k]
        sums = [0] * (n - k + 1)
        cnt = k
        sum_window = j = 0
        
        # Calculating subarray sums
        for i in range(n):
            if cnt > 0:
                sum_window += nums[i]
                cnt -= 1
            else:
                sums[j] = sum_window
                sum_window += nums[i] - nums[j]
                j += 1
        
        # Calculating right maxima
        sums[j] = sum_window
        prefix = [-1] * (n - k)
        j = n - k
        cur_max = (j, sums[j])
        for i in range(j - k, -1, -1):
            if sums[j] >= cur_max[1]:
                cur_max = (j, sums[j])
            prefix[i] = cur_max[0]
            j -= 1
        
        # Calculating left maxima
        suffix = [-1] * (n - k)
        j = 0
        cur_max = (0, sums[0])
        for i in range(k, n - k):
            if sums[j] > cur_max[1]:
                cur_max = (j, sums[j])
            suffix[i] = cur_max[0]
            j += 1
        
        # Searching for the answer
        cur_max=(-1, -1)
        for i in range(k, n - 2 * k + 1):
            sum_ = sums[i] + sums[prefix[i]] + sums[suffix[i]]
            if sum_ > cur_max[1]:
                cur_max = (i, sum_)
        i = cur_max[0]
        return [suffix[i], i, prefix[i]]
