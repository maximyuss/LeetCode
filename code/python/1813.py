# https://leetcode.com/problems/sentence-similarity-iii/
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        l1, l2 = sentence1.split(), sentence2.split()
        n1, n2 = len(l1) - 1, len(l2) - 1
        idx = 0
        while idx <= n1 and idx <= n2 and l1[idx] == l2[idx]:
            idx += 1
        while n1 >= idx and n2 >= idx and l1[n1] == l2[n2]:
            n1 -= 1
            n2 -= 1
        return (idx > n1 or idx > n2 or n1 < idx or n2 < idx)
