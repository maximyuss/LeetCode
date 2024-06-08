#https://leetcode.com/problems/subarray-sums-divisible-by-k/
def subarraysDivByK(nums: List[int], k: int) -> int:
    sum = rem = res = 0
    mp = {0: 1}
    for num in nums:
        sum += num
        rem = (sum % k + k) % k
        if rem in mp:
            res += mp[rem]
            mp[rem] += 1
        else:
            mp[rem] = 1
    return res
