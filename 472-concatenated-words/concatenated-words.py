class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res_set = set(words)
        memo = {}

        def can_form(word):
            if word in memo:
                return memo[word]
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in res_set:
                    if suffix in res_set or can_form(suffix):
                        memo[word] = True
                        return True
                memo[word] = False
            return False

        result = []
        for word in res_set:
            res_set.remove(word)
            if can_form(word):
                result.append(word)
            res_set.add(word)    
        return result