class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        ans = 0
        for i in range(len(s) - k + 1):
            d = int(s[i:i+k])
            if d != 0 and num % d == 0:
                ans += 1
        return ans