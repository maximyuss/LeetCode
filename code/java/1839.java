// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/
class Solution {
    public int longestBeautifulSubstring(String word) {
        char[] vowels = {'a', 'e', 'i', 'o', 'u'};
        int n = word.length(), l = word.indexOf('a'), res = 0;
        while (l != -1) {
            int r = l, cnt = 0;
            boolean isBeauty = true;
            for (char ch : vowels) {
                int cnt_ch = 0;
                while (r < n && word.charAt(r) == ch) {
                    r++;
                    cnt_ch++;
                }
                if (cnt_ch == 0) {
                    isBeauty = false;
                    break;
                }
                cnt += cnt_ch;
            }
            if (isBeauty) res = Math.max(res, cnt);
            l = word.indexOf('a', r);
        }
        return res;
    }
}
