# https://leetcode.com/problems/find-all-people-with-secret/
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = [[] for _ in range(n)]
        for person1, person2, time in meetings:
            graph[person1].append((time, person2))
            graph[person2].append((time, person1))
        pq = []
        heappush(pq, (0, 0))
        heappush(pq, (0, firstPerson))
        visited = [False] * n
        while pq:
            time, person = heappop(pq)
            if visited[person]:
                continue
            visited[person] = True
            for t, next_person in graph[person]:
                if not visited[next_person] and t >= time:
                    heappush(pq, (t, next_person))
        return [i for i in range(n) if visited[i]]
