class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        hash_map = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in hash_map:
                hash_map.remove(s[l])
                l+=1
            hash_map.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
