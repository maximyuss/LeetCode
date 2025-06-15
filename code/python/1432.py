# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        for ch in s:
            if ch != '9':
                num_max = int(s.replace(ch, '9'))
                break
        else:
            num_max = num
        
        if s[0] != '1':
            num_min = int(s.replace(s[0], '1'))
        else:
            for ch in s[1:]:
                if ch not in ('01'):
                    num_min = int(s.replace(ch, '0'))
                    break
            else:
                num_min = num
        return num_max - num_min
