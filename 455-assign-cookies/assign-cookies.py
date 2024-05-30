class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        j = 0
        i = 0
        g.sort()
        s.sort()
        if len(s) == 0 or len(g) == 0:
            return j
        while i < len(s) and j< len(g):
            if j < len(g) and s[i] >= g[j]:
                j+=1
            i+=1
        return j
                