# https://leetcode.com/problems/meeting-rooms-iii/
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free, busy = list(range(n)), []
        heapq.heapify(free)
        meetings.sort(key=lambda x: x[0])
        freq = [0] * n
        for m_start, m_end in meetings:
            while busy and busy[0][0] <= m_start:
                heapq.heappush(free, heapq.heappop(busy)[1])
            if free:
                room = heapq.heappop(free)
            else:
                now, room = heapq.heappop(busy)
                m_end += now - m_start
            heapq.heappush(busy, (m_end, room))
            freq[room] += 1
        return max(range(n), key=lambda x: (freq[x], -x))
