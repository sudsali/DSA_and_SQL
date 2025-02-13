class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #maintian a dict for count of characters
        # keep increasing count by traversing the string of the character and update the max_freq
        # when window sie - max_freq is greater than k, we decremennt character at left and shrink the window
        ht = defaultdict(int)
        res = 0
        l = 0
        max_freq = 0
        for r in range(len(s)):
            ht[s[r]]+=1
            max_freq = max(max_freq,ht[s[r]])
            while r - l + 1 - max_freq > k:
                ht[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res
