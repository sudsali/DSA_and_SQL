class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return len(s)
        ans = 0
        odd = False
        freq = Counter(s)
        for _,count in freq.items():
            if count % 2 == 0:
                ans+=count
            else:
                ans+=count-1
                odd = True
        if odd:
            return ans+1
        else:
            return ans

        