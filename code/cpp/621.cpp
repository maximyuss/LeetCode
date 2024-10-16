// https://leetcode.com/problems/task-scheduler/
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int letters[26] = { 0 };
        int maxCount = 0;
        for (char task : tasks) {
            char code = task - 'A';
            letters[code]++;
            maxCount = max(maxCount, letters[code]);
        }
        int time = (maxCount - 1) * (n + 1);
        for (int f : letters)
            if (f == maxCount)
                time++;
        return max((int)tasks.size(), time);
    }
};
