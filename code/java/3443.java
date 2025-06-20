// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/
class Solution {
    public int maxDistance(String s, int k) {
        final int n = s.length();
        int res = 0, x = 0, y = 0;
        for (int i = 0; i < n; ++i) {
            char ch = s.charAt(i);
            switch (ch) {
                case 'E':
                    x++; break;
                case 'W':
                    x--; break;
                case 'N':
                    y++; break;
                case 'S':
                    y--; break;
            }
            res = Math.max(res, Math.min(Math.abs(x) + Math.abs(y) + 2 * k, i + 1));
        }
        return res;
    }
}
