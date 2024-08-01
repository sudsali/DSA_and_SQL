class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr = 0
        left = 0
        maxx = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr+=1
            while curr > 1:
                if nums[left] == 0:
                    curr-=1
                left+=1
            maxx = max(maxx,right-left)
        return maxx