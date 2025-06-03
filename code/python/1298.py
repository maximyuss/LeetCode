# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        dq = deque()
        for box in initialBoxes:
            if status[box]:
                dq.appendleft(box)
            else:
                dq.append(box)
        res = 0
        while dq:
            cur = dq.popleft()
            if status[cur]:
                res += candies[cur]
                for key in keys[cur]:
                    status[key] = 1
                for box in containedBoxes[cur]:
                    if status[box]:
                        dq.appendleft(box)
                    else:
                        dq.append(box)
        return res
