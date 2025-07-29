// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
class Solution {
    public int largestCombination(int[] candidates) {
        int res = 0;
        for (int i = 0; i <= 24; i++) {
            int cnt = 0;
            for (int num : candidates)
                cnt += (num >> i) & 1;
            res = Math.max(res, cnt);
        }
        return res;
    }
}
