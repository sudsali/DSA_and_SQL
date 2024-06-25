class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        ans = n * 2
        if n % 2 == 0:
            ans = n
        return ans 