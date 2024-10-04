# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        res = 0
        total_skill = skill[0] + skill[-1]
        for i in range(0, n // 2):
            if skill[i] + skill[n - i - 1] != total_skill:
                return -1
            res += skill[i] * skill[n - i - 1]
        return res
