class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            ans = ""
            if word[i] == ch:
                res = word[:i+1]
                rev = res[::-1]
                ans = rev + word[i+1:]
                return ans
        return word
