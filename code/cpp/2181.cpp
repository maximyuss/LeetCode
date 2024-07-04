# https://leetcode.com/problems/merge-nodes-in-between-zeros/
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
        ListNode* res = new ListNode(-1), * curr = res;
        size_t sum = 0;
        for (ListNode* it = head->next; it != nullptr; it = it->next) {
            if (it->val != 0)
                sum += it->val;
            else {
                curr->next = new ListNode(sum);
                curr = curr->next;
                sum = 0;
            }
        }
        return res->next;
    }
};
