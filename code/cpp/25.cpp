# https://leetcode.com/problems/reverse-nodes-in-k-group/
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;
        ListNode tmp;
        tmp.next = head;
        ListNode* prev = &tmp;
        ListNode* curr = head;
        size_t cnt = 0;
        while (curr) {
            cnt++;
            curr = curr->next;
        }
        while (cnt >= k) {
            curr = prev->next;
            ListNode* next = curr->next;
            for (int i = 1; i < k; i++) {
                curr->next = next->next;
                next->next = prev->next;
                prev->next = next;
                next = curr->next;
            }
            prev = curr;
            cnt -= k;
        }
        return tmp.next;
    }
};
