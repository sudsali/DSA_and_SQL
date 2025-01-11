class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False
        count = 0
        char_freq = collections.Counter(s)
        for c in char_freq:
            if char_freq[c] % 2 != 0:
                count+=1
        if count > k :
            return False
        return True