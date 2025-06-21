// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/
class Solution {
    public int minimumDeletions(String word, int k) {
        int[] freq = new int[26];
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            freq[ch - 'a']++;
        }
        int res = Integer.MAX_VALUE;
        for (int x : freq) {
            if (x == 0) continue;
            int cur = 0;
            for (int y : freq) {
                if (y == 0) continue;
                cur += (y < x) ? y : Math.max(0, y - x - k);
            }
            res = Math.min(res, cur);
        }
        return res;
    }
}
