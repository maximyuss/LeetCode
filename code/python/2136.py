#https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
      pairs = list(zip(growTime, plantTime))
      pairs.sort(reverse=True)
      totalPlantTime = -1
      totalMaxTime = 0
      for i in range(len(growTime)):
          totalPlantTime += pairs[i][1]
          totalMaxTime = max(totalMaxTime, totalPlantTime + pairs[i][0])
      return totalMaxTime + 1
