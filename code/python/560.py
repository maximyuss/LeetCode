#https://leetcode.com/problems/subarray-sum-equals-k/
def subarraySum(self, nums: List[int], k: int) -> int:
    sum, res = 0, 0
    mp = {0: 1}
    for num in nums:
        sum += num
        if sum - k in mp:
            res += mp[sum - k]
        mp[sum] = mp.get(sum, 0) + 1
    return res
