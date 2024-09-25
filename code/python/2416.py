# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        COUNT_KEY = "_count_"
        trie = dict()
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = dict()
                node = node[ch]
                node[COUNT_KEY] = node.get(COUNT_KEY, 0) + 1
        res = []
        for word in words:
            node = trie
            total = 0
            for ch in word:
                node = node[ch]
                total += node[COUNT_KEY]
            res.append(total)
        return res
