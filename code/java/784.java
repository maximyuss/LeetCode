// https://leetcode.com/problems/letter-case-permutation/
class Solution {
    public List<String> letterCasePermutation(String s) {
        List<String> res = new ArrayList<>();
        recurse(res, 0, s.toCharArray());
        return res;
    }

    private static void recurse(List<String> res, int i, char[] s) {
        if (i == s.length)
            res.add(new String(s));
        else {
            if (Character.isDigit(s[i]))
                recurse(res, i + 1, s);
            else {
                s[i] = Character.toUpperCase(s[i]);
                recurse(res, i + 1, s);
                s[i] = Character.toLowerCase(s[i]);
                recurse(res, i + 1, s);
            }
        }
    }
}
