# https://leetcode.com/problems/minimum-number-of-people-to-teach/
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        dumbs = [False] * len(languages)
        languages = list(map(set, languages))
        is_dumbs = False
        for man1, man2 in friendships:
            man1 -= 1; man2 -= 1
            if languages[man1].isdisjoint(languages[man2]):
                dumbs[man1] = True
                dumbs[man2] = True
                is_dumbs = True
        if not is_dumbs: return 0
        freq = [0] * (n + 1)
        cnt_dumbs = 0
        for i, is_dumbs in enumerate(dumbs):
            if not is_dumbs: continue
            cnt_dumbs += 1
            for lang in languages[i]:
                freq[lang] += 1
        return cnt_dumbs - max(freq)
