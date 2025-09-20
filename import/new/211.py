# https://leetcode.com/problems/design-add-and-search-words-data-structure/
class WordDictionary:
    def __init__(self):
        self.by_len = defaultdict(set)
        self.cache = {}

    def addWord(self, word: str) -> None:
        self.by_len[len(word)].add(word)

    def search(self, word: str) -> bool:
        bucket = self.by_len.get(len(word))
        if not bucket:
            return False
        if '.' not in word:
            return word in bucket
        key = (word, len(bucket))
        if key in self.cache:
            return self.cache[key]
        for w in bucket:
            for p, c in zip(word, w):
                if p != '.' and p != c:
                    break
            else:
                self.cache[key] = True
                return True
        self.cache[key] = False
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
