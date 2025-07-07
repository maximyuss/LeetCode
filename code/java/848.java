// https://leetcode.com/problems/shifting-letters/
class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        int acc = 0, n = shifts.length;
        char[] res = s.toCharArray();
        for (int i = n - 1; i > -1; i--) {
            acc = (acc + shifts[i]) % 26;
            res[i] = (char) ((res[i] + acc - 'a') % 26 + 'a');
        }
        return new String(res);
    }
}
