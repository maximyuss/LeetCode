# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: ListNode, count: int) -> ListNode:
        prev = None
        curr = head
        while count:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            count -= 1
        return prev

    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 2
        res = head
        cur_node = head.next
        while cur_node:
            cur_count = 0
            while cur_node and cur_count < count:
                prev = cur_node
                cur_node = cur_node.next
                cur_count += 1
            if cur_count % 2 == 0:
                rev = self.reverse(head.next, cur_count)
                prev = head.next
                prev.next = cur_node
                head.next = rev
            head = prev
            count += 1
        return res
