# https://leetcode.com/problems/construct-smallest-number-from-di-string/
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pattern += "I"
        n = len(pattern)
        res = ""
        len_down = 0
        for i in range(n):
            if pattern[i] == "I":
                if not len_down:
                    res += str(i + 1)
                else:
                    for j in range(len_down):
                        res += str(i - j + 1)
                        len_down -= 1
                    res += str(i -j)
            else:
                len_down += 1
        return res

  '''
    def smallestNumber(self, pattern: str) -> str:
      res, stack = [], []
      for i in range(len(pattern) + 1):
          stack.append(i + 1)
          if i == len(pattern) or pattern[i] == "I":
              while stack:
                  res.append(str(stack.pop()))
      return "".join(res)
  '''
