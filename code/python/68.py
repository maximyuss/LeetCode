# https://leetcode.com/problems/text-justification/
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        len_line = start = idx = 0
        while idx < len(words):
            len_word = len(words[idx])
            if len_line + len_word <= maxWidth:
                len_line += len_word + 1
                idx += 1
                continue
            cnt_spacing = idx - start - 1
            if cnt_spacing < 1:
                line = words[start].ljust(maxWidth)
            else:
                total_spaces = maxWidth - len_line + cnt_spacing + 1
                line = ''
                for j in range(start, idx):
                    len_space = 0 if not cnt_spacing else -(-total_spaces // cnt_spacing)
                    line += words[j] + ' ' * len_space
                    total_spaces -= len_space
                    cnt_spacing -= 1
            res.append(line)
            idx += (idx == start)
            start = idx
            len_line = 0
        line = ''
        for j in range(start, len(words)):
            line += words[j] + ' '
        if len(line) > maxWidth:
            line = line[:-1]
        res.append(line.ljust(maxWidth))
        return res
