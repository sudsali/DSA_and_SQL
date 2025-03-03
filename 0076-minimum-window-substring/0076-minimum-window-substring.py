class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #Create 2 hashmaps, create have and need variables
        #if curr char count in s is equal to curr char count in t
        #increase have
        #while have == need, update res and reslen if min found 
        # keep popping left and updating hashmap 

        if t == "":
            return ""
        countT,window = {},{}
        
        for c in t:
            countT[c] = 1 + countT.get(c,0)

        have, need = 0, len(countT)
        l = 0
        res,resLen = [-1,-1], float("infinity")
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have+=1

            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                window[s[l]]-=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
            
        l,r = res
        if resLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""