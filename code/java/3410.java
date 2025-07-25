// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/
class Solution {
    public long maxSubarraySum(int[] nums) {
        Map<Integer, Long> map = new HashMap<>();
        map.put(0, 0L);
        long res = Long.MIN_VALUE, prefixSum = 0, lowest = 0;
        for (int num : nums) {
            prefixSum += num;
            res = Math.max(res, prefixSum - lowest);
            if (num < 0) {
                map.put(num, num + Math.min(map.getOrDefault(num, 0L), map.get(0)));
                lowest = Math.min(lowest, map.get(num));
            }
            long negativePrefixSum = map.get(0);
            map.put(0, Math.min(negativePrefixSum, prefixSum));
            lowest = Math.min(lowest, negativePrefixSum);
        }
        return res;
    }
}
