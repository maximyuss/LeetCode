// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        const int MAX_N = 10e5 + 1;
        int pos[2]{ -1, -1 }, count = 1, minDist = MAX_N;
        ListNode* prev = head;
        head = head->next;
        while (head->next) {
            if ((head->val > prev->val and head->val > head->next->val) or
                (head->val < prev->val and head->val < head->next->val))
                if (pos[0] == -1) {
                    pos[0] = count;
                    pos[1] = count;
                }
                else {
                    minDist = min(minDist, count - pos[1]);
                    pos[1] = count;
                }
            count++;
            prev = head;
            head = head->next;
        }
        if (minDist < MAX_N)
            return { minDist, pos[1] - pos[0] };
        return { -1, -1 };
    }
};
