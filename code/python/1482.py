#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def countBlooms(day):
            i = count = 0
            for e in bloomDay:
                if e<= day:
                    i+=1
                    if i == k:
                        count+=1
                        if count == m: return True
                        i = 0
                else:
                    i = 0
            return False
        
        target = m * k
        if target > len(bloomDay): return -1
        l = min(bloomDay)
        r = max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if countBlooms(mid):
                r = mid
            else:
                l = mid + 1
        return int(l)
