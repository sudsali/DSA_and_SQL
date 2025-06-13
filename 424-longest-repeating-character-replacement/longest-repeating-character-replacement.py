class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_freq={}
        max_len = 0
        res = 0
        for right in range(len(s)):
            max_freq[s[right]] = max_freq.get(s[right],0)+1
            max_len = max(max_len, max_freq[s[right]])

            while (right - left + 1) - max_len > k:
                max_freq[s[left]]-=1
                left+=1

            res = max(res,right-left+1)
        
        return res