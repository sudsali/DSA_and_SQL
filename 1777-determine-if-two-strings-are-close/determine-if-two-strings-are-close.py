class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = collections.Counter(word1)
        dict2 = collections.Counter(word2)
        count1 = sorted(dict1.values())
        count2 = sorted(dict2.values())
        for i in word1:
            if i not in word2:
                return False
        return count1 == count2