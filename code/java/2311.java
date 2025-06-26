// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/
class Solution {
    public int longestSubsequence(String s, int k) {
        int last = s.length() - 1, res = 0, num = 0;
        for (int i = 0; i <= last; i++) {
            if (s.charAt(last - i) == '1') {
                if (i < 31) {
                    num += (1 << i);
                    res += (num <= k) ? 1 : 0;
                }
            } else
                res++;
        }
        return res;
    }
}
