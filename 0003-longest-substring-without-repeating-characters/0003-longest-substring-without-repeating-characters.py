class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #here we need to keep on removing element from l until curr element is in the hashset
        res = 0
        l = 0
        h = set()
        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l += 1
            h.add(s[r])
            res = max(res,r-l+1)    
        return res

