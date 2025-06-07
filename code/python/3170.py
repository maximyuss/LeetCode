# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/
class Solution:
    def clearStars(self, s: str) -> str:
        pq = []
        for i, ch in enumerate(s):
            if ch == '*':
                heapq.heappop(pq)
            else:
                heapq.heappush(pq, (ch, -i))
        pq.sort(key=lambda x: -x[1])
        return ''.join(x[0] for x in pq)
