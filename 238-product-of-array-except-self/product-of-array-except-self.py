class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixSum = [1] * len(nums) 
        suffixSum = [1] * len(nums)
        suffixSum[0] = nums[0]
        prefixSum[-1] = nums[-1]
        res = []
        for i in range(1,len(nums)):
            prefixSum[i] = prefixSum[i-1] * nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            suffixSum[i] = suffixSum[i+1] * nums[i+1]

        for i in range(len(nums)):
            res.append(prefixSum[i] * suffixSum[i])

        return res