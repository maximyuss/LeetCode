# https://leetcode.com/problems/most-profitable-path-in-a-tree/
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        def dfs_bob(node, parent, step):
            for neighbor in graph[node]:
                if neighbor == parent: continue
                if neighbor == 0 or dfs_bob(neighbor, node, step + 1):
                    bob_steps[neighbor] = step + 1
                    return True
            return False

        def dfs_alice(node, parent, step, money):
            if step < bob_steps[node]:
                money += amount[node]
            elif step == bob_steps[node]:
                money += amount[node] // 2
            if len(graph[node]) == 1:
                nonlocal max_money
                max_money = max(max_money, money)
                return
            for neighbor in graph[node]:
                if neighbor == parent: continue
                dfs_alice(neighbor, node, step + 1, money)
            return

        n = len(amount)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        bob_steps = [n] * n
        dfs_bob(bob, -1, 0)
        bob_steps[bob] = 0
        
        max_money = float('-inf')
        graph[0].append(-1) # make node 0 non-leaf
        dfs_alice(0, -1, 0, 0)
        
        return max_money
