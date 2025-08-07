// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        int n = answerKey.length(), start_t = 0, start_f = 0, max_t = 0, max_f = 0;
        for (int i = 0; i != n; i++) {
            if (answerKey.charAt(i) == 'T')
                max_t++;
            else
                max_f++;
            if (max_t > k) {
                if (answerKey.charAt(start_t) == 'T')
                    max_t--;
                start_t++;
            }
            if (max_f > k) {
                if (answerKey.charAt(start_f) == 'F')
                    max_f--;
                start_f++;
            }
        }
        return Math.max(n - start_t, n - start_f);
    }
}
