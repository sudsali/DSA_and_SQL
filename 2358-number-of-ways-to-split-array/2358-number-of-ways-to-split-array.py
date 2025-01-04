class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left = nums[0]
        curr = 1
        right = 0
        for i in range(1,len(nums)):
            right += nums[i]
        if left >= right:
            res = 1
        else:
            res = 0
        for i in range(1,len(nums)-1):
            left += nums[curr]
            right -= nums[curr]
            curr+=1
            if left>= right:
                res+=1
        return res