// https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
class Solution {
    public int maxDiff(int num) {
        String s = Integer.toString(num);
        int max = num, min = num;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch != '9') {
                max = Integer.parseInt(s.replace(ch, '9'));
                break;
            }
        }
        if (s.charAt(0) != '1')
            min = Integer.parseInt(s.replace(s.charAt(0), '1'));
        else
            for (int i = 1; i < s.length(); i++) {
                char ch = s.charAt(i);
                if (ch != '0' && ch != '1') {
                    min = Integer.parseInt(s.replace(ch, '0'));
                    break;
                }
            }
        return max - min;
    }
}
