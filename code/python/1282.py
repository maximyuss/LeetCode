# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mp, res = {}, []
        for i, group in enumerate(groupSizes):
            mp[group] = mp.get(group, []) + [i]
        for key, val in mp.items():
            tmp = [val[i:i+key] for i in range(0, len(val), key)]
            res.extend(tmp)
        return res
