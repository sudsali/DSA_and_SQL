class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = collections.Counter(t)
        hash_map = {}
        current_count = 0
        required = len(count_t)
        res = ""
        l = 0
        min_len = float("inf")

        for r in range(len(s)):
            hash_map[s[r]] = hash_map.get(s[r], 0) + 1
            if count_t[s[r]] == hash_map[s[r]] and s[r] in count_t:
                current_count+=1
            
            while required == current_count:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]
                
                hash_map[s[l]]-=1
                if s[l] in count_t and count_t[s[l]] > hash_map[s[l]]:
                    current_count-=1
                l+=1
        return res