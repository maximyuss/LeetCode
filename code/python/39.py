# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, cur: list[int], total: int):
            if total == target:
                res.append(cur.copy())
                return
            for j in range(i, n):
                if total + candidates[j] > target:
                    return
                cur.append(candidates[j])
                dfs(j, cur, total + candidates[j])
                cur.pop()
        
        n = len(candidates)
        res = []
        candidates.sort()
        dfs(0, [], 0)
        return res
