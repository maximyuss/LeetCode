// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
class Solution {
    public int minDeletions(String s) {
        int[] freq = new int[26];
        for (char ch: s.toCharArray())
            freq[ch - 'a']++;
        HashSet<Integer> seen = new HashSet<>();
        int res = 0;
        for (int f: freq) {
            if (f == 0) continue;
            while (f > 0 && seen.contains(f)) {
                f--;
                res++;
            }
            seen.add(f);
        }
        return res;
    }
}
