class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 0 
        maxx = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr+=1
            while curr>k:
                if nums[left] == 0:
                    curr-=1
                left+=1
            maxx = max(maxx,right-left+1)
        return maxx