class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = -1
        for num in nums:
            if -num in num_set:
                ans = max(ans, abs(num))
        return ans
