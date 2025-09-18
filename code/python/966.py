# https://leetcode.com/problems/vowel-spellchecker/
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowel_map = str.maketrans('aeiou', '*****')
        dict0 = set(wordlist)
        dict1, dict2 = {}, {}
        for word in wordlist:
            word_lower = word.lower()
            dict1.setdefault(word_lower, word)
            dict2.setdefault(word_lower.translate(vowel_map), word)

        res = []
        for query in queries:
            if query in dict0:
                res.append(query)
                continue
            query_lower = query.lower()
            if query_lower in dict1:
                res.append(dict1[query_lower])
                continue
            query_mask = query_lower.translate(vowel_map)
            res.append(dict2.get(query_mask, ''))
        return res
