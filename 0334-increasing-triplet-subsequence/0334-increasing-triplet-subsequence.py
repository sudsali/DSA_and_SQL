class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = float('inf')
        nextsmall = float('inf')
        for i in range(len(nums)):
            if nums[i] <= small:
                small = nums[i]
            elif nums[i] <= nextsmall:
                nextsmall = nums[i]
            else:
                return True
        return False