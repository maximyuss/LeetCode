# https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node):
            state[node] = 1
            for neighbor in graph[node]:
                if state[neighbor] == 1:
                    return False
                elif state[neighbor] == 0 and not dfs(neighbor):
                    return False
            state[node] = 2
            path.append(node)
            return True

        graph = [[] for _ in range(numCourses)]
        last_nodes = set(range(numCourses))
        for u, v in prerequisites:
            graph[u].append(v)
            if v in last_nodes:
                last_nodes.remove(v)
        path = []
        state = [0] * (numCourses)  # white, gray, black
        for node in last_nodes:
            if not dfs(node):
                return []
        if len(path) < numCourses:
            return []
        return path
