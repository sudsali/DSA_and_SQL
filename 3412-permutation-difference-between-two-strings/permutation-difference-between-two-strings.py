class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    ans = ans + abs(i-j)
        return ans