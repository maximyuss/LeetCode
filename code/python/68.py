# https://leetcode.com/problems/text-justification/
# Short solution
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, line, width = [], [], 0
        for word in words:
            if width + len(word) + len(line) > maxWidth:
                for i in range(maxWidth - width):
                    line[i % (len(line) - 1 or 1)] += " "
                res, line, width = res + ["".join(line)], [], 0
            line += [word]
            width += len(word)
        return res + [" ".join(line).ljust(maxWidth)]

# Long solution
'''
class Line:
    def __init__(self, maxWidth):
        self.len = 0
        self.max_len = maxWidth

    def try_insert(self, word: str) -> bool:
        len_word = len(word) + (self.len != 0)
        if self.len + len_word <= self.max_len:
            self.len += len_word
            return True
        return False

    def get_line(self, words: List[str], start: int, end: int, is_last: bool = False) -> str:
        if is_last:
            line = words[start]
            for j in range(start + 1, len(words)):
                line += ' ' + words[j]
            return line.ljust(self.max_len)
        
        cnt_spacing = end - start - 1
        if cnt_spacing == 0:
            line = words[start].ljust(self.max_len)
        else:
            line = ''
            total_spaces = self.max_len - self.len + cnt_spacing
            for i in range(start, end):
                len_space = 0 if not cnt_spacing else -(-total_spaces // cnt_spacing)
                line += words[i] + ' ' * len_space
                total_spaces -= len_space
                cnt_spacing -= 1
        self.len = 0
        return line


class Solution:
    def fullJustify3(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = Line(maxWidth)
        start = idx = 0
        while idx < len(words):
            if not line.try_insert(words[idx]):
                res.append(line.get_line(words, start, idx))
                if line.try_insert(words[idx]):
                    start = idx
                else:
                    res.append(line.get_line(words, idx, idx + 1))
                    start = idx + 1
            idx += 1
        res.append(line.get_line(words, start, idx, True))
        return res
'''
