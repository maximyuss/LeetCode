# https://leetcode.com/problems/course-schedule-iv/
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(node):
            for neighbour in graph[node]:
                children[node].add(neighbour)
                if not children[neighbour]:
                    dfs(neighbour)
                children[node].update(children[neighbour])

        graph = [[] for _ in range(numCourses)]
        children = [set() for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)
        for node in range(numCourses):
            dfs(node)
        res = [False] * len(queries)
        for i, (u, v) in enumerate(queries):
            if v in children[u]:
                res[i] = True
        return res
