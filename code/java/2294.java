//https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
class Solution {
    public int partitionArray(int[] nums, int k) {
        int[] freq = new int[100001];
        int max = 0, min = Integer.MAX_VALUE;
        for (int num : nums) {
            freq[num] = 1;
            max = Math.max(max, num);
            min = Math.min(min, num);
        }
        int res = 0, range = -1;
        for (int num = min; num <= max; num++)
            if (freq[num] == 1)
                if (range < num) {
                    range = num + k;
                    res++;
            if (range >= max) break;
        }
        return res;
    }
}
