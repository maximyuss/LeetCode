// https://leetcode.com/problems/merge-k-sorted-lists/
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) return NULL;

        ListNode *head = new ListNode(-1), *tail = head;
        priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, greater<pair<int, ListNode*>>> pq;
        for (auto head : lists)
            if (head != NULL) pq.push({head->val, head});
        while (pq.size()) {
            ListNode* minNode = pq.top().second;
            pq.pop();
            if (minNode->next != NULL) pq.push({minNode->next->val, minNode->next});
            tail->next = minNode;
            tail = tail->next;
        }
        return head->next;
    }
};
