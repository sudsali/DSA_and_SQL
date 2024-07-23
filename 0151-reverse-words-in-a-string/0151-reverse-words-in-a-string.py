class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = ""
        for i in s[::-1]:
            res+=i
            res+=' '
        return res[:-1]
