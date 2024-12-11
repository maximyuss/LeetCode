# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node):
            state[node] = 1
            for neighbor in graph[node]:
                if state[neighbor] == 1:
                    return False
                elif state[neighbor] == 0 and not dfs(neighbor):
                    return False
            state[node] = 2
            return True

        graph = [[] for _ in range(numCourses)]
        state = [0] * (numCourses) # white, gray, black
        for v, u in prerequisites:
            graph[u].append(v)
        for node in range(numCourses):
            if state[node] == 0 and not dfs(node):
                return False
        return True
