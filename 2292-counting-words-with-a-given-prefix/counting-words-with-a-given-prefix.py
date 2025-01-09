class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        l1 = len(pref)
        res = 0
        for word in words:
            if pref == word[:l1]:
                res+=1
        return res
