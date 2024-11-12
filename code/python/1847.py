# https://leetcode.com/problems/closest-room/
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        q = deque(sorted([(size, room, i) for i, (room, size) in enumerate(queries)], key=lambda x: (-x[0], x[1], x[2])))
        rooms = deque(sorted(rooms, key=lambda x: -x[1]))
        pool = []
        while q:
            size, room, i = q.popleft()
            while rooms and rooms[0][1] >= size:
                insort(pool, rooms.popleft()[0])
            if pool:
                idx = bisect_left(pool, room)
                if idx == 0:
                    res[i] = pool[idx]
                elif idx == len(pool):
                    res[i] = pool[-1]
                else:
                    res[i] = pool[idx - 1] if room - pool[idx - 1] <= pool[idx] - room else pool[idx]
        return res
