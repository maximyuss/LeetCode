# https://leetcode.com/problems/combination-sum-ii/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start:int, remaining:int, path:list[int]):
            if remaining == 0:
                res.append(path.copy())
                return
            if remaining < 0:
                return
            prev = -1
            for i in range(start, n):
                if candidates[i] == prev:
                    continue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()
                prev = candidates[i]

        candidates.sort()
        n, res = len(candidates), []
        backtrack(0, target, [])
        return res
