// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/
class Solution {
    public int longestContinuousSubstring(String s) {
        int res = 1, cnt = 1;
        char prev = s.charAt(0);
        for (int i = 1; i != s.length(); i++) {
            char code = s.charAt(i);
            if (code - prev == 1) {
                cnt += 1;
                if (cnt > res) res = cnt;
            }
            else
                cnt = 1;
            prev = code;
        }
        return res;
    }
}
