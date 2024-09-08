# https://leetcode.com/problems/split-linked-list-in-parts/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None] * k
        n = 0
        curr = head
        while curr is not None:
            n += 1
            curr = curr.next
        l1 = n // k
        l2 = n % k
        curr = head
        prev = curr
        for i in range(k):
            new_part = curr
            idx = l1
            if l2 > 0:
                l2 -= 1
                idx += 1
            j = 0
            while j < idx:
                prev = curr
                if curr is not None:
                    curr = curr.next
                j += 1
            if prev is not None:
                prev.next = None
            res[i] = new_part
        return res
