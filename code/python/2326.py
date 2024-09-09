# https://leetcode.com/problems/spiral-matrix-iv/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]
        row, col, dir = 0, -1, 1
        m -= 1
        while head:
            for _ in range(n):
                if not head: return res
                col += dir
                res[row][col] = head.val
                head = head.next
            n -= 1
            for _ in range(m):
                if not head: return res
                row += dir
                res[row][col] = head.val
                head = head.next
            m -= 1
            dir = -dir
        return res
